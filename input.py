#coding:utf-8
import sys
from Tkinter import *

class app(Frame):
	a=0
	b=0
	output = ''
	sudoku = [[0 for col in range(9)] for row in range(9)]
	def __init__(self,scr):
		Frame.__init__(self,scr)
		#初始化label和button
		self.label1=Label(scr,text="机智的数独游戏")
		self.label1.pack()
		self.button1=Button(scr,text="检查是否有解")
		self.button1.pack(side='top')
		self.button1.bind('<Button-1>',self.out)
		#初始化canvas，画一组矩形
		self.cv=Canvas(scr,bg="gray",width=290,height=290)
		self.cv.pack()
		self.rt=self.cv.create_rectangle(10,10,280,280,
									fill="gray",
									tag="rt",
									outline="blue")
		for i in range(9):
			for j in range(9):
				self.rt=self.cv.create_rectangle(10+(30*i),10+(30*j),40+(30*i),40+(30*j),
																	outline="red",tags="rt")
				self.cv.tag_bind('rt',"<Button-1>",lambda click:self.mouse(click))
		#画蓝色直线，分区
		for i in range(10):
			if i%3==0:
				self.cv.create_line(10+30*i,10,10+30*i,280,fill="blue")
				self.cv.create_line(10,10+30*i,280,10+30*i,fill="blue")
	def mouse(self,event):
		#鼠标点击选中矩形
		for i in range(9):
			for j in range(9):
				self.rt=self.cv.create_rectangle(10+(30*i),10+(30*j),40+(30*i),40+(30*j),
																	outline="red",tags="rt")
		for i in range(10):
			if i%3==0:
				self.cv.create_line(10+30*i,10,10+30*i,280,fill="blue")
				self.cv.create_line(10,10+30*i,280,10+30*i,fill="blue")
		#根据鼠标坐标计算方格坐标
		self.a=(event.x-10)/30
		self.b=(event.y-10)/30
		self.cv.create_rectangle(10+(30*self.a),10+(30*self.b),40+(30*self.a),40+(30*self.b),outline="yellow",tags="rt")
	def key(self,event):
		#按下键盘，修改当前方格内数字，并写入数独数组sudoku[][]
		self.tag='n%d%d' % (self.b,self.a)
		self.sudoku[self.b][self.a]=event.char
		self.cv.itemconfig(self.tag,text=event.char,)
		self.cv.create_text(25+30*self.a,25+30*self.b,text=event.char,tags=self.tag)
	def out(self,event):
		#将sudoku当中的数字串成字符串输出交给核心算法处理
		for i in xrange(0,9):
			for j in xrange(0,9):
				if self.sudoku[i][j]==0:
					self.output='%s%s' % (self.output,'.')
				else:
					self.output='%s%s' % (self.output,self.sudoku[i][j])
		print self.output
		exit()

def main():
	root = Tk()
	root.geometry("400x420")
	root.resizable(0,0)
	test=app(root)
	root.bind('<KeyPress>',test.key)
	test.mainloop()

main()