import asyncio

from ysl_yhzc import *

"""
实物
cron: 0 0 10 * * *
new Env("一嗨租车")
抓取微信小程序 一嗨租车 的 备注, userid, token  以#拼接
eg:
    https://appmini.1hai.cn/Wechat/User/Base/CacheInfo?%2F%2FW7FhThpifw%2FS22t55d3Y%24z22AyX22xiOCV5j8t0g*
    userid == %2F%2FW7FhThpifw%2FS22t55d3Y%24z22AyX22xiOCV5j8t0g*
    token == 请求头的token

    备注#userid#token
多账号以 "回车" 或者 多变量 隔开
青龙变量为 yczc_ck
"""

print("""
正在运行脚本：【一嗨租车】V1.0

警告: 本脚本限制环境为 python版本为3.10 并且不支持arm环境. 
网络问题请自行解决 需能访问 raw.githubusercontent.com

📢 请认真阅读以下声明
 【免责声明】   
📌 脚本文件仅用于测试和学习研究   
📌 脚本文件任何人不得用于商业以及非法用途   
📌 禁止任何公众号、自媒体进行任何形式的转发   
📌 脚本文件请在下载试用后24小时内自行删除   
📌 因使用脚本造成软件平台的一切损失皆由使用者承担   
📌 脚本文件如有不慎被破解或修改由破解或修改者承担   
📌 如不接受此条款请立即删除脚本文件
""")

if __name__ == '__main__':
    # 脚本配置区
    cookie_env_var = 'yhzc_ck'
    service_name = '一嗨租车'
    qq_qun = "897363140"  # qq交流群, 重要参数请勿删除
    # 是否并发
    use_concurrency = False
    # 是否休眠
    use_sleep = True
    asyncio.run(
        main(check_cookies(cookie_env_var, service_name), use_sleep, use_concurrency, qq_qun))
