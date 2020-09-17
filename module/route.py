from module import json,request,app,get_access_token
from module.text_content import post_text_content
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