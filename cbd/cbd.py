"""
实物
cron: 30 59 19 * * *
new Env("茶百道")
抓取微信小程序 茶百道 的 手机号, csession 以#拼接
多账号以 "回车" 或者 多变量 隔开
青龙变量为 cbd_ck

eg:
    18888888888#csession
"""

import asyncio
from ysl_cbd import *

print("""
正在运行脚本：【茶百道】V1.0
📢 请认真阅读以下声明
 【免责声明】   
📌 脚本文件仅用于测试和学习研究   
📌 脚本文件任何人不得用于商业以及非法用途   
📌 禁止任何公众号、自媒体进行任何形式的转发   
📌 脚本文件请在下载试用后24小时内自行删除   
📌 因使用脚本造成软件平台的一切损失皆由使用者承担   
📌 脚本文件如有不慎被破解或修改由破解或修改者承担   
📌 如不接受此条款请立即删除脚本文件


警告: 本脚本限制环境为 python版本为3.10 并且不支持arm环境. 
网络问题请自行解决 需能访问 raw.githubusercontent.com

""")

if __name__ == '__main__':
    # 脚本配置区
    cookie_env_var = 'cbd_ck'
    service_name = '茶百道'
    qq_qun = "897363140"  #重要参数请勿删除
    # 是否并发
    use_concurrency = True
    # 是否休眠
    use_sleep = False
    asyncio.run(
        main(Cookies=check_cookies(cookie_env_var, service_name), qun=qq_qun, use_sleep=use_sleep,
             use_concurrency=use_concurrency))
