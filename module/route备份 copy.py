from module import json,request,app,make_response
from module.WeChat import get_access_token
from module.WeChat.text_content import post_text_content
from module.WeChat.textcard_content import post_textcard_content
from module.DuJitang.DuJitang import random_text
# 微信及时沟通api
# 发送文本来类型的post请求
@app.route('/api/WeChat/text/',methods=['GET','POST'])
def post_text():
    if request.method == 'POST':
        corpid = request.form.get('corpid')
        corpsecret = request.form.get('corpsecret')
        agentid = request.form.get('agentid')
        text = request.form.get('text')
    else:
        corpid = request.args.get('corpid')
        corpsecret = request.args.get('corpsecret')
        agentid = request.args.get('agentid')
        text = request.args.get('text')
    # 请求access_token
    access_token_code = get_access_token(corpid,corpsecret)
    # 处理请求的access_token返回值
    if access_token_code['errcode'] == 0:
        access_token = access_token_code['access_token']
    else:
        return access_token_code
    post_text = post_text_content(access_token,agentid,text)
    return post_text



# 发送卡片消息类型的post请求
@app.route('/api/WeChat/textcard/',methods=['GET','POST'])
def post_textcard():
    if request.method == 'POST':
        corpid = request.form.get('corpid')
        corpsecret = request.form.get('corpsecret')
        agentid = request.form.get('agentid')
        title = request.form.get('title')
        description = request.form.get('description')
        url = request.form.get('url')
    else:
        corpid = request.args.get('corpid')
        corpsecret = request.args.get('corpsecret')
        agentid = request.args.get('agentid')
        title = request.args.get('title')
        description = request.args.get('description')
        url = request.args.get('url')

    # 请求access_token
    access_token_code = get_access_token(corpid,corpsecret)
    # 处理请求的access_token返回值
    if access_token_code['errcode'] == 0:
        access_token = access_token_code['access_token']
    else:
        return access_token_code
    post_text = post_textcard_content(access_token,agentid,title,description,url)
    return post_text


# 毒鸡汤api
@app.route('/api/dujitang/')
def dujitang():
    s = random_text()
    return json.dumps(s, ensure_ascii = False)