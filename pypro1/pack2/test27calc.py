
import wx
import wx.xrc
from pack1.mymod3 import Gop


# 계산기
class MyFrame1 (wx.Frame):
    
    def __init__(self, parent):
        wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        
        # self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"숫자1 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer2.Add(self.m_staticText1, 0, wx.ALL, 5)
        
        self.txtNum1 = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.txtNum1, 0, wx.ALL, 5)
        
        self.m_panel1.SetSizer(bSizer2)
        self.m_panel1.Layout()
        bSizer2.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText2 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"숫자2 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        bSizer3.Add(self.m_staticText2, 0, wx.ALL, 5)
        
        self.txtNum2 = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.txtNum2, 0, wx.ALL, 5)
        
        self.m_panel2.SetSizer(bSizer3)
        self.m_panel2.Layout()
        bSizer3.Fit(self.m_panel2)
        bSizer1.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)
        
        rdoOpChoices = [ u"+", u"-", u"*", u"/" ]
        self.rdoOp = wx.RadioBox(self.m_panel3, wx.ID_ANY, u"연산자 선택", wx.DefaultPosition, wx.DefaultSize, rdoOpChoices, 1, wx.RA_SPECIFY_ROWS)
        self.rdoOp.SetSelection(0)
        bSizer4.Add(self.rdoOp, 1, wx.ALL, 5)
        
        self.m_panel3.SetSizer(bSizer4)
        self.m_panel3.Layout()
        bSizer4.Fit(self.m_panel3)
        bSizer1.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText3 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"결과 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        bSizer5.Add(self.m_staticText3, 0, wx.ALL, 5)
        
        self.staResult = wx.StaticText(self.m_panel4, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staResult.Wrap(-1)
        bSizer5.Add(self.staResult, 0, wx.ALL, 5)
        
        self.m_panel4.SetSizer(bSizer5)
        self.m_panel4.Layout()
        bSizer5.Fit(self.m_panel4)
        bSizer1.Add(self.m_panel4, 1, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel5 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.btnCalc = wx.Button(self.m_panel5, wx.ID_ANY, u"계산", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.btnCalc, 0, wx.ALL, 5)
        
        self.btnClear = wx.Button(self.m_panel5, wx.ID_ANY, u"초기화", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.btnClear, 0, wx.ALL, 5)
        
        self.btnExit = wx.Button(self.m_panel5, wx.ID_ANY, u"종료", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.btnExit, 0, wx.ALL, 5)
        
        self.m_panel5.SetSizer(bSizer6)
        self.m_panel5.Layout()
        bSizer6.Fit(self.m_panel5)
        bSizer1.Add(self.m_panel5, 1, wx.EXPAND | wx.ALL, 5)
        
        self.SetSizer(bSizer1)
        self.Layout()
        
        self.Centre(wx.BOTH)
        
        # Connect Events
        self.btnCalc.id = 1
        self.btnClear.id = 2
        self.btnExit.id = 3
        
        self.btnCalc.Bind(wx.EVT_BUTTON, self.OnProcess)
        self.btnClear.Bind(wx.EVT_BUTTON, self.OnProcess)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnProcess)
    
    # Virtual event handlers, overide them in your derived class
    def OnProcess(self, event):
        num1 = self.txtNum1.GetValue()
        num2 = self.txtNum2.GetValue()
       
        bid = event.GetEventObject().id   
        
        if bid == 1:
                
            if self.rdoOp.GetStringSelection() == '+' :
                aa = int(num1) + int(num2)
                self.staResult.SetLabel('결과:' + str(aa))

            elif self.rdoOp.GetStringSelection() == '-' :
                aa = int(num1) - int(num2)
                self.staResult.SetLabel('결과:' + str(aa))
        
            elif self.rdoOp.GetStringSelection() == '*' :
                aa = float(num1) * float(num2)
                self.staResult.SetLabel('결과:' + str(aa))
            
            elif self.rdoOp.GetStringSelection() == '/' :
                aa = float(num1) / float(num2)
                self.staResult.SetLabel('결과:' + str(aa))
    
        elif bid == 2:
            self.txtNum1.Clear()
            self.txtNum2.Clear()
       
        elif bid == 3:
            self.Close()


if __name__ == '__main__':
    app = wx.App()
    MyFrame1(None).Show()
    app.MainLoop()
