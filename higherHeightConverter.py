#! /usr/bin/env python

import wx	#引入wx库

class Frame(wx.Frame): 	#声明Frame类

	def __init__(self, parent):	#构造函数
		
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Higher level Height Converter")	#使用wx库的Frame构造函数, 传入各种参数
		self.panel = wx.Panel(self)	#生成panel
		self.promptInch = wx.StaticText(self.panel, label = "inch", pos = (22, 31)) 	#以下均为各种文字, 输入框, 按钮的生成与定义
		self.promptFoot = wx.StaticText(self.panel, label = "foot", pos = (22, 11))
		
		self.footBox = wx.TextCtrl(self.panel, pos = (80, 11))
		self.inchBox = wx.TextCtrl(self.panel, pos = (80, 33))		
		self.btnEnter = wx.Button(self.panel, label = "Enter", pos = (88, 88))
		self.btnEnter.Bind(wx.EVT_BUTTON, self.OnEnter)	#绑定按钮btnEnter的触发处理函数为OnEnter
		self.Show()	#显示窗体
		
	def OnEnter(self, e):	#定义OnEnter函数
		feet = self.footBox.GetValue()	#获取footBox的值
		inches = self.inchBox.GetValue()	#获取inchBox的值
		
		try:
			feet = int(feet)	#尝试讲feet转化为整形, 如果无法完成则报错"你没有输入一个正确的数字, 所以程序按照0 feet来计算"
		except:
			wx.MessageBox("You didn't enter a number, so I consider you as 0 foot tall.", "Information", wx.OK | wx.CANCEL)
			self.footBox.SetValue(str(0))
			feet = 0
			
		try:
			inches = int(inches)	#上述的操作应用于inches
		except:
			wx.MessageBox("You didn't enter a number, so I consider you as o inch tall.", "Information", wx.OK | wx.CANCEL)	
			self.inchBox.SetValue(str(0))
			inches = 0
			
		
		if inches > 12:	#如果inces大于12, 则调整输入的数值, 就像"我身高0米165厘米"自动改成"我升高1米65厘米"一样, 没个球用
			wx.MessageBox("12 inches = 1 foot, I will change it to feet.", "Information", wx.OK | wx.CANCEL)
			extraFoot = inches/12
			self.inchBox.SetValue(str(inches - extraFeet * 12))
			inches -= extraFeet * 12 #inches = inches - extraFeet*12
			self.footBox.SetValue(str(feet + extraFoot))
			feet += extraFeet #feet = feet + extraFeet
			
		centimeters = 30.48 * feet + 2.54 * inches	#这是最核心的一步计算
		#self.response.SetLabel("Your height is {} cm.".format(str(round(centimeters, 1)))
		
#-------------------------------Main Program Below---------------------------------------------------------------------------

app = wx.App(False)
frame = Frame(None)
app.MainLoop()
		
		
		