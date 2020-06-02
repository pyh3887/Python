# Gui 프로그래밍 - wxPython 라이브러리를 사용

import wx

# app = wx.App(False)
# frame = wx.Frame(None,wx.ID_ANY, "Hello World")
# frame.Show(True)
# app.MainLoop()


class Ex(wx.Frame):

    def __init__(self, parent, title):
        super(Ex, self).__init__(parent, title=title, size=(400, 300))
        
        # TextBox 추가
        # self.txtA = wx.TextCtrl(self) # text box
        # self.CreateStatusBar() # 상태 표시줄
        
        # Menu 추가
        
        menuBar = wx.MenuBar() 
        mnuFile = wx.Menu()
        mnuNew = mnuFile.Append(wx.ID_NEW, 'New', '새글')
        mnuOpen = mnuFile.Append(wx.ID_NEW, 'open', '열기')
        mnuFile.AppendSeparator()
        mnuExit = mnuFile.Append(wx.ID_NEW, 'close', '닫기')
        
        menuBar.Append(mnuFile, 'File')
        
        self.SetMenuBar(menuBar)
        
        # 메뉴에 이벤트 장착
        self.Bind(wx.EVT_MENU, self.OnEvent1 , mnuNew)  # 클릭시 이벤트 1
        self.Bind(wx.EVT_MENU, self.OnEvent2 , mnuExit)  # 클릭시 이벤트 2
        
        # 라벨과 텍스트 박스
        panel = wx.Panel(self)
        wx.StaticText(panel, label='i d :' , pos=(5, 5))  # pos= (x, y)
        wx.StaticText(panel, label='p w d :' , pos=(5, 40))  # pos= (x, y)
        self.txtA = wx.TextCtrl(panel, pos=(50, 5))  # pos = 위치 
        self.txtB = wx.TextCtrl(panel, pos=(50, 40), size=(200, -1))
        
        # 버튼 
        btn1 = wx.Button(panel, label='일반버튼', pos=(5, 100))
        btn2 = wx.ToggleButton(panel, label='토글버튼', pos=(100, 100))
        btn3 = wx.Button(panel, label='종료', pos=(200, 100), size=(50, -1))
        
        # 이벤트 처리방법1
        # btn1.Bind(wx.EVT_BUTTON, self.OnClick1)
        # btn2.Bind(wx.EVT_TOGGLEBUTTON, self.OnClick2)
        # btn3.Bind(wx.EVT_BUTTON, self.OnClick3)
         
        # 이벤트 처리방법2 (1개의 이벤트 핸들러 호출) - id 사용
        btn1.id = 1
        btn2.id = 2
        btn3.id = 3
        
        btn1.Bind(wx.EVT_BUTTON, self.OnClickABC)
        btn2.Bind(wx.EVT_TOGGLEBUTTON, self.OnClickABC)
        btn3.Bind(wx.EVT_BUTTON, self.OnClickABC)
              
        self.Center()
        self.Show()
    
    def OnEvent1(self, event):    
        self.txtA.SetLabelText('새글 메뉴 누름')

    def OnEvent2(self, event):
        self.Close(True)
    
    def OnClick1(self, event):   
        # 대화상자 호출
        msgDial = wx.MessageDialog(self, '메세지', '제목', wx.OK)
        msgDial.ShowModal()
        msgDial.Destroy()
        
        self.SetTitle('버튼1 클릭')
        
    def OnClick2(self, event):    
        # print(event.GetEventObject().GetValue())
        if event.GetEventObject().GetValue():
            self.txtA.SetLabelText('mbc')
            self.txtB.SetLabelText('11')
        else:
            self.txtA.SetLabelText('')
            self.txtB.SetLabelText('')
        
    def OnClick3(self, event):    
        pass    
    
    def OnClickABC(self, event):
        # print(event.GetEventObject().id) # id 로 구분하기
        
        bid = event.GetEventObject().id      
        
        if  bid == 1:
            self.SetTitle("버튼1")        
        elif bid == 2:
            self.SetTitle("버튼2")         
        else:
            self.Close()
            
            
if __name__ == '__main__':
    app = wx.App()
    Ex(None, title='연습')
    app.MainLoop()
