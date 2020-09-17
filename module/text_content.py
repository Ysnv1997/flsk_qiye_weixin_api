import requests,json

def post_text_content(access_token,agentid,content):
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
    return json.dumps(r)