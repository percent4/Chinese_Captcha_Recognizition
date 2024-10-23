# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: server.py
# @time: 2024/9/29 19:53
import datetime
import random
import os.path
import shutil
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

file_path_content_dict = {}
with open('lexicon.txt', 'r') as f:
    content = [_.strip() for _ in f.readlines()]
    for line in content:
        file_path_content_dict[line.split('\t')[0]] = line.split('\t')[1]
content_file_path_dict = {v: k for k, v in file_path_content_dict.items()}


def save_tagged_content(old_file_name, old_file_path, new_file_name):
    with open('tagged_content.txt', 'a') as f:
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"{now_time}\t{old_file_path}\t{old_file_name}\t{new_file_name}\n")


# 定义端口为9100
define("port", default=9100, help="run on the given port", type=int)


def get_image(image_dir):
    files = os.listdir(image_dir)
    file = random.choice(files)
    file_tag = file_path_content_dict[file]
    return file, file_tag


class ImageHandler(tornado.web.RequestHandler):
    image_dir = './static/resized_images'
    new_image_dir = 'static/tagged_images'

    # get函数
    def get(self):
        image_src, img_name = get_image(self.image_dir)
        self.render('index.html', img_src=image_src, img_name=img_name, new_img_name=img_name)

    # post函数
    def post(self):
        old_file_name = self.get_argument('img_name')
        old_file_path = content_file_path_dict[old_file_name]
        new_file_name = self.get_argument('new_img_name')
        save_tagged_content(old_file_name=old_file_name,
                            old_file_path=old_file_path,
                            new_file_name=new_file_name)
        print(f"old_file_name: {old_file_name}, new_file_name: {new_file_name}")
        old_image_file_path = os.path.join(self.image_dir, old_file_path)
        new_image_file_path = os.path.join(self.new_image_dir, old_file_path)
        if os.path.exists(old_image_file_path):
            shutil.move(old_image_file_path, new_image_file_path)
        print(f"还有 {len(os.listdir(self.image_dir))} 张图片尚未检查！")

        image_src, img_name = get_image(self.image_dir)
        self.render('index.html', img_src=image_src, img_name=img_name, new_img_name=img_name)


# 主函数
def main():

    # 开启tornado服务
    tornado.options.parse_command_line()
    # 定义app
    app = tornado.web.Application(
            handlers=[(r'/index', ImageHandler)
                      ],    # 网页路径控制
            template_path=os.path.join(os.path.dirname(__file__), "templates"), # 模板路径
            static_path=os.path.join(os.path.dirname(__file__), "static"),  # 配置静态文件路径
          )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


main()
