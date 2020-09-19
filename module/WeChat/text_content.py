from module.WeChat import get_access_token
from module import json,reqparse, Resource,requests
class WeiXin_Post_Text(Resource):
    # 接收请求参数
    def __init__(self):
        self.parser_put = reqparse.RequestParser()
        self.parser_put.add_argument("corpid", type=str, required=True, help="need corpid data")
        self.parser_put.add_argument("corpsecret", type=str, required=True, help="need corpsecret data")
        self.parser_put.add_argument("agentid", type=str, required=True, help="need agentid data")
        self.parser_put.add_argument("text", type=str, required=True, help="need text data")    
    
    # 发送请求
    def post_text_content(self,access_token,agentid,content):
        data = {
                    "touser" : "@all",
                    "toparty" : "@all",
                    "totag" : "@all",
                    "msgtype" : "text",
                    "agentid" : agentid,
                    "text" : {
                        "content" :content
                    },
                    "safe":0,
                    "enable_id_trans": 0,
                    "enable_duplicate_check": 0,
                    "duplicate_check_interval": 1800
                }
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={ACCESS_TOKEN}'.format(ACCESS_TOKEN=access_token),data=json.dumps(data)).json()
        return r
    # 获取access_token并提交请求参数
    def except_data(self):
        args = self.parser_put.parse_args()
        # 请求access_token
        access_token_code = get_access_token(args['corpid'],args['corpsecret'])
        # 处理请求的access_token返回值
        if access_token_code['errcode'] == 0:
            access_token = access_token_code['access_token']
        else:
            return access_token_code
        post_text = self.post_text_content(access_token,args['agentid'],args['text'])
        return post_text
    # 添加作者信息
    def json_data(self,json):
        json['author'] = {
                    'name':'HTMAPI',
                    'desc':'本api由HTMAPI免费提供服务，官方文档：www.htm.fun'
            }
        return json

    # 挂载get和post方法
    def get(self):
        r = self.except_data()
        r = self.json_data(r)
        return r

    def post(self):
        r = self.except_data()
        r = self.json_data(r)
        return r