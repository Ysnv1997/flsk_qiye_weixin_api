from flask import Flask,request,Response
import json
import requests

# flask app注册
app = Flask(__name__)
# 全局通用函数 获取access_token
def get_access_token(corpid,corpsecret):
    params={
        'corpid':corpid,
        'corpsecret':corpsecret
    }
    r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',params=params).content
    r = json.loads(r)
    access_token_content = r['access_token']
    print(access_token_content)
    return access_token_content
# 引入路由模块
from module import route