import sys
import easygui as g

# import easygui #如果用这种导入方式的话，那么在使用easygui的函数时候，必须在函数的前面加上前缀easygui
# easygui.msgbox("Dc zhanglei")

# from easygui import *   #这样使得我们更容易调用Easygui的函数，可以直接这样编写代码
# msgbox("Dc zhanglei")

# g.msgbox(msg="我一定要学会编程！",title="标题部分",ok_button="加油") #msg title ok_button可以不写，是默认的

# ccbox()ccbox() 提供一个选择：Continue 或者 Cancel，并相应的返回 1（选中Continue）或者 0（选中Cancel）。
#                注意 ccbox() 是返回整型的 1 或 0，不是布尔类型的 True 或 False。但你仍然可以这么写
if g.ccbox(msg='还继续吗',title='提示',choices=('还要继续！','算了吧！')):
	g.msgbox('还是不玩了，快睡觉吧！','继续吗','睡觉吧')
else:
	sys.exit(0)

