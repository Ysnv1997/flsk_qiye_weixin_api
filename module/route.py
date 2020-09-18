from module import json,request,app,get_access_token,make_response
from module.text_content import post_text_content
from module.textcard_content import post_textcard_content
# 发送文本来类型的post请求
@app.route('/api/text/',methods=['GET','POST'])
def post_text():
    if request.method =='POST':
        corpid = request.form.get('corpid')
        corpsecret = request.form.get('corpsecret')
        agentid = request.form.get('agentid')
        text = request.form.get('text')
    else:
        corpid = request.args.get('corpid')
        corpsecret = request.args.get('corpsecret')
        agentid = request.args.get('agentid')
        text = request.args.get('text')

    access_token = get_access_token(corpid,corpsecret)
    post_text = post_text_content(access_token,agentid,text)
    return post_text



# 发送卡片消息类型的post请求
@app.route('/api/textcard/',methods=['GET','POST'])
def post_textcard():
    if request.method =='POST':
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

    access_token = get_access_token(corpid,corpsecret)
    post_text = post_textcard_content(access_token,agentid,title,description,url)
    return post_text
