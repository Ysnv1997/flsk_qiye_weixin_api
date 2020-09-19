from flask import Flask,request,make_response
from flask_restful import reqparse, Api, Resource
import json
import requests
import os,sys

# flask app注册
app = Flask(__name__)
api = Api(app)
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
# 引入路由模块
from module import route