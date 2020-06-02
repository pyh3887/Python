import wx
import wx.xrc
import MySQLdb
import sys
import locale

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}


class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"직원 관리 고객", pos = wx.DefaultPosition, size = wx.Size( 850,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.staMsg = wx.StaticText( self.m_panel2, wx.ID_ANY, u"작성자 : 박윤호", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staMsg.Wrap( -1 )
        bSizer3.Add( self.staMsg, 0, wx.ALL, 5 )
        
        
        self.m_panel2.SetSizer( bSizer3 )
        self.m_panel2.Layout()
        bSizer3.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"상품명 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.txtSang = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtSang, 0, wx.ALL, 5 )
        
        self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"수량 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        self.txtSu = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtSu, 0, wx.ALL, 5 )
        
        self.m_staticText6 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"단가:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )
        
        self.txtDan = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtDan, 0, wx.ALL, 5 )
        
        self.btnOk = wx.Button( self.m_panel1, wx.ID_ANY, u"등록", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.btnOk, 0, wx.ALL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
        self.lstGogek = wx.ListCtrl( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer4.Add( self.lstGogek, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel3.SetSizer( bSizer4 )
        self.m_panel3.Layout()
        bSizer4.Fit( self.m_panel3 )
        bSizer1.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.staCount = wx.StaticText( self.m_panel4, wx.ID_ANY, u"건 수 : 0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staCount.Wrap( -1 )
        bSizer5.Add( self.staCount, 0, wx.ALL, 5 )
        
        
        self.m_panel4.SetSizer( bSizer5 )
        self.m_panel4.Layout()
        bSizer5.Fit( self.m_panel4 )
        bSizer1.Add( self.m_panel4, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # lstGogek 객체에 제목
        self.lstGogek.InsertColumn(0, '코드', width=100)
        self.lstGogek.InsertColumn(1, '상품명', width=150)
        self.lstGogek.InsertColumn(2, '수량', width=150)
        self.lstGogek.InsertColumn(3, '단가', width=200)
        self.lstGogek.InsertColumn(4, '금액', width=200)
        
        # Connect Events
        self.btnOk.Bind( wx.EVT_BUTTON, self.OnInsert )
    
    def __del__( self ):
        pass
    
    def OnInsert(self,event):
        if self.txtSang.GetValue() == '':
            wx.MessageBox('상품을 입력하시오' , '알림' , wx.OK)
            self.txtNo.SetFocus()
            return
        if self.txtSu.GetValue() == '':
            wx.MessageBox('수량을 입력하시오' , '알림' , wx.OK)
            self.txtSu.SetFocus()
            return
        if self.txtDan.GetValue() == '':
            wx.MessageBox('단가를 입력하시오' , '알림' , wx.OK)
            self.txtDan.SetFocus()
            return
        
        
        self.maxData()
       
    def maxData(self):
        try:
            conn = MySQLdb.connect(**config)            
            cursor = conn.cursor()  # SQL 문 수행을 위한 커서 객체 생성
            
            sang = self.txtSang.GetValue()
            su = self.txtSu.GetValue()
            dan = self.txtDan.GetValue()
                        
            sql = "insert into sangdata(code,sang,su,dan) values((select max(code)+1 as a from sangdata  ALIAS_FOR_SUBQUERY),%s,%s,%s)"
                        
            cursor.execute(sql,(sang,su,dan))
            conn.commit()
            
        
            sql = '''
                  select * from sangdata
                  '''
                  
            cursor.execute(sql)
            
            sql = '''
                select code,sang,su,dan,(su*dan) from sangdata
                '''
            #print(sql)
            
            cursor.execute(sql)
            datas = cursor.fetchall()
            
            
            
            for d in datas:
                i = self.lstGogek.InsertItem(1000,0) 
                self.lstGogek.SetItem(i,0,str(d[0]))
                self.lstGogek.SetItem(i,1,str(d[1])) 
                self.lstGogek.SetItem(i,2,str(d[2])) 
                self.lstGogek.SetItem(i,3,str(d[3])) 
                self.lstGogek.SetItem(i,4,locale.format_string('%d', d[4], 1)) 
                
            self.staCount.SetLabelText('건수' + str(len(datas)))
        
        
        
        
                  
        except Exception as e :
            print('Logcheck err:' + e)

        finally:
            cursor.close()
            conn.close()  
      
        
if __name__ == '__main__':
    app = wx.App()
    MyFrame1(None).Show()
    app.MainLoop()
