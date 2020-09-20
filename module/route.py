from module import api
from module.WeChat.text_content import WeiXin_Post_Text
from module.WeChat.textcard_content import WeiXin_Text_Card
from module.DuJitang.DuJitang import DuJitang
from module.Index.Index import Index



api.add_resource(Index, "/")
api.add_resource(WeiXin_Post_Text, "/api/Wechat/text/")
api.add_resource(WeiXin_Text_Card, "/api/Wechat/text_card/")
api.add_resource(DuJitang, "/api/dujitang/")

