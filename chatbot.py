# coding: utf-8 	
from wxpy import *

#创建一个bot机器人，从wxpy包引入的
bot = Bot(cache_path=True)

tuling = Tuling(api_key='7faa2fe104b549beaa08fba4de7d39c9')



jy = bot.groups().search(u'咱们仨')
print(jy)
jy = jy[0]
print("找到：%s"%jy)

from threading import current_thread
thread = current_thread()
print thread.getName()

@bot.register(jy,run_async=False)
def print_message(msg):
	print "-------------"
	xxxxx
	print(msg.text)
	tuling.do_reply(msg)

# 进入Python命令行，让程序保持运行
embed(shell='python')