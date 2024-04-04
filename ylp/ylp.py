"""
实物
cron: 0 0 10 * * *
new Env("悦临平")
app 悦临平 的 手机尾号后四位#电话#密码  以#拼接
eg:
    8888#18888888888#888999
多账号以 "回车" 或者 多变量 隔开
青龙变量为 ylp_ck


环境必须为 python 3.10 debian版青龙 安装ddddocr依赖
两个文件必须在同一目录
使用青龙上传 必须点击退出保存 不支持arm


"""
import asyncio

from ysl_ylp import *

print("""
正在运行脚本：【悦临平】V1.0
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
    cookie_env_var = 'ylp_ck'
    service_name = '悦临平'
    qq_qun = "897363140"  # 重要参数请勿删除
    # 是否并发
    use_concurrency = False
    # 是否休眠
    use_sleep = True
    
    asyncio.run(
        main(check_cookies(cookie_env_var, service_name), use_sleep,
             use_concurrency, qq_qun))
