'''
是一个简单的绘图工具

使用时需要导入turtle库
import turtle
移动命令：
forward(d)     向前移动d长度
backward(d)    向后移动d长度
right(d)       向右转动d度
left(d)        向左转动d度
goto(x,y)      移动到坐标位置
speed()        笔画绘制的速度

笔画控制命令:
up()   将笔抬起，移动时不会绘图
down()  将笔落下，移动会绘图
setheading（）  改变箭头的朝向
pensize()      笔画的宽度
pencolor()     不花的颜色
reset()    回复所有设置，重置turtle状态
clear（）  清空窗口，不会重置turtle状态
circle（r,e）  绘制一个圆形，r为半径，e为画出一个圆的次数
begin_fill()
fillcolor()
end_fill()



'''
import turtle
turtle.forward(152)
turtle.circle(50,steps=4)
turtle.done()

'''
其他命令:
turtle.done()  使得程序不结束
undo(0  撤销上一次动作
hideturtle（）  隐藏海龟
showturtle（）  显示海龟
screensize（）  



'''
