#coding:utf-8
import sys
from Tkinter import *

class app(Frame):
	a=0
	b=0
	m=0
	n=0
	output=''
	def __init__(self,scr,input):
		Frame.__init__(self,scr)
		#print input
		self.label1=Label(scr,text="机智的数独游戏")
		self.label1.pack()
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
				#self.cv.tag_bind('rt',"<Button-1>",lambda click:self.mouse(click))
		for i in range(10):
			if i%3==0:
				self.cv.create_line(10+30*i,10,10+30*i,280,fill="blue")
				self.cv.create_line(10,10+30*i,280,10+30*i,fill="blue")
		for i in range(9):
			for j in range(9):
				if input[i*9+j]!='.':
					self.cv.create_text(25+30*j,25+30*i,text=input[i*9+j])
def main():
	root = Tk()
	root.geometry("400x420")
	root.resizable(0,0)
	test=app(root,sys.argv[1])
	test.mainloop()

main()