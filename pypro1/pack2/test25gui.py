# 레이아웃 매니저 중 BOXSIZER()


import wx

class MyFrame(wx.Frame):
    
    def __init__(self, parent, title):
        super(MyFrame,self).__init__(parent,title=title,size=(400,300))
        
        
        panel1 = wx.Panel(self,-1,style = wx.SUNKEN_BORDER) #오목한 테두리
        panel2 = wx.Panel(self,-1,style = wx.SUNKEN_BORDER) #오목한 테두리
        
        panel1.SetBackgroundColour('BLUE')
        panel2.SetBackgroundColour('RED')
        
        box = wx.BoxSizer(wx.HORIZONTAL) #VERTICAL
        box.Add(panel1,1,wx.EXPAND) # 1/3 영역
        box.Add(panel2,2,wx.EXPAND) # 2/3 영역
        
        
        self.SetSizer(box)
        self.Center()
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    MyFrame(None, title='연습')
    app.MainLoop()
