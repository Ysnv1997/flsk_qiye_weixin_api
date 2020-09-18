import requests,json

def post_textcard_content(access_token,agentid,title,description,url):
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
    return json.dumps(r)