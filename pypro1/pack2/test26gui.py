# wxFormBuilder 디자인 툴 사용


import wx
import wx.xrc



class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"연습", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"이름 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer4.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.txtName = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.txtName, 0, wx.ALL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer4 )
        self.m_panel1.Layout()
        bSizer4.Fit( self.m_panel1 )
        bSizer3.Add( self.m_panel1, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"나이", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer5.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        self.txtAge = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer5.Add( self.txtAge, 0, wx.ALL, 5 )
        
        self.btnOk = wx.Button( self.m_panel2, wx.ID_ANY, u"확인", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.btnOk, 0, wx.ALL, 5 )
        
        
        self.m_panel2.SetSizer( bSizer5 )
        self.m_panel2.Layout()
        bSizer5.Fit( self.m_panel2 )
        bSizer3.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"결과:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer6.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        self.staResult = wx.StaticText( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staResult.Wrap( -1 )
        bSizer6.Add( self.staResult, 0, wx.ALL, 5 )
        
        
        self.m_panel3.SetSizer( bSizer6 )
        self.m_panel3.Layout()
        bSizer6.Fit( self.m_panel3 )
        bSizer3.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer3 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btnOk.Bind( wx.EVT_BUTTON, self.EvtKbs )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def EvtKbs( self, event ):
        name = self.txtName.GetValue()
        if name == '':
            wx.MessageBox('이름 입력','알림',wx.OK)  #나이 입력검사
            return
        
        age = self.txtAge.GetValue()
        
        #wx.MessageBox(name + ' ' + age, '결과' , wx.OK)  #나이 입력검사
        
        self.staResult.SetLabel(name + ' ' + age)
        
        


if __name__ == '__main__':
    app = wx.App()
    MyFrame1(None).Show()
    app.MainLoop()


