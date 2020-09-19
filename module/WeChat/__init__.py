import requests,json
# 全局通用函数 获取access_token
def get_access_token(corpid,corpsecret):
    params={
        'corpid':corpid,
        'corpsecret':corpsecret
    }
    r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',params=params).content
    r = json.loads(r)
    if r['errcode'] == 0:
        access_token_content = r['access_token']
        return {'errcode':0,'access_token':access_token_content}
    else:
        return {'errcode':r['errcode'],'errmsg':r['errmsg']}
