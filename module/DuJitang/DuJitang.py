import os,sys,linecache,random
from os import path
from module import Resource

class DuJitang(Resource):

    def random_text(self):
        # 获取文件路径
        d = path.dirname(__file__)
        this_path = d + '/api_data.txt'
        # 获取当前一共多少行
        text_file = open(this_path,"r",encoding="utf-8",errors="ignore")
        number = len(text_file.readlines())
        text_file.close()
        # 随机读取一行
        num = random.randint(0,number)
        text=linecache.getline(this_path,num).replace('\n','')
        data_json = {
                        "code": 200,
                        "msg": "success",
                        "data": {
                            "content":text
                        },
                        "author": {
                            "name": "HTMAPI",
                            "desc": "由HTMAPI提供的免费API 服务，官方文档：www.htm.fun"
                        }
                    }
        return data_json

    def get(self):
        return self.random_text()

    def post(self):
        return self.random_text()