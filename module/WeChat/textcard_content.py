from module.WeChat import get_access_token
from module import json,reqparse, Resource,requests

class WeiXin_Text_Card(Resource):
    def __init__(self):
        self.parser_put = reqparse.RequestParser()
        self.parser_put.add_argument("corpid", type=str, required=True, help="need corpid data")
        self.parser_put.add_argument("corpsecret", type=str, required=True, help="need corpsecret data")
        self.parser_put.add_argument("agentid", type=str, required=True, help="need agentid data")
        self.parser_put.add_argument("title", type=str, required=True, help="need title data")
        self.parser_put.add_argument("description", type=str, required=True, help="need description data")
        self.parser_put.add_argument("url", type=str, required=True, help="need url data")

    def post_textcard_content(self,access_token,agentid,title,description,url):
        data = {
                "touser" : "@all",
                "toparty" : "@all",
                "totag" : "@all",
                "msgtype" : "textcard",
                "agentid" : agentid,
                "textcard" : {
                            "title" : title,
                            "description" : description,
                            "url" : url,
                            "btntxt":"更多"
                },
                "enable_id_trans": 0,
                "enable_duplicate_check": 0,
                "duplicate_check_interval": 1800
                }
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={ACCESS_TOKEN}'.format(ACCESS_TOKEN=access_token),data=json.dumps(data)).json()
        return r

    def except_data(self):
        args = self.parser_put.parse_args()

        # 请求access_token
        access_token_code = get_access_token(args['corpid'],args['corpsecret'])
        # 处理请求的access_token返回值
        if access_token_code['errcode'] == 0:
            access_token = access_token_code['access_token']
        else:
            return access_token_code
        post_text = self.post_textcard_content(access_token,args['agentid'],args['title'],args['description'],args['url'])
        return post_text
        
    def json_data(self,json):
        json['author'] = {
                    'name':'HTMAPI',
                    'desc':'本api由HTMAPI免费提供服务，官方文档：www.htm.fun'
            }
        return json
    def get(self):
        r = self.except_data()
        r = self.json_data(r)
        return r

    def post(self):
        r = self.except_data()
        r = self.json_data(r)
        return r