

import wx
import wx.xrc
import ast
import MySQLdb

rec_r = 0
datas = []
 
with open('mariadb.txt','r') as figu:
    aa = figu.read()
    config = ast.literal_eval(aa)
    
class MyFrame3 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"고객자료", pos = wx.DefaultPosition, size = wx.Size( 700,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
       #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        
        bSizer11 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText14 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"번호 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )
        bSizer13.Add( self.m_staticText14, 0, wx.ALL, 5 )
        
        self.txtGogekNo = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.txtGogekNo, 0, wx.ALL, 5 )
        
        self.m_staticText15 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"고객명 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )
        bSizer13.Add( self.m_staticText15, 0, wx.ALL, 5 )
        
        self.txtGogekName = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.txtGogekName, 0, wx.ALL, 5 )
        
        self.m_staticText16 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"성별 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )
        bSizer13.Add( self.m_staticText16, 0, wx.ALL, 5 )
        
        self.txtGogeGen = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.txtGogeGen, 0, wx.ALL, 5 )
        
        
        self.m_panel9.SetSizer( bSizer13 )
        self.m_panel9.Layout()
        bSizer13.Fit( self.m_panel9 )
        bSizer11.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.btn1 = wx.Button( self.m_panel11, wx.ID_ANY, u"||<<", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.btn1, 0, wx.ALL, 5 )
        
        self.btn2 = wx.Button( self.m_panel11, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.btn2, 0, wx.ALL, 5 )
        
        self.btn3 = wx.Button( self.m_panel11, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.btn3, 0, wx.ALL, 5 )
        
        self.btn4 = wx.Button( self.m_panel11, wx.ID_ANY, u">>||", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.btn4, 0, wx.ALL, 5 )
        
        
        self.m_panel11.SetSizer( bSizer12 )
        self.m_panel11.Layout()
        bSizer12.Fit( self.m_panel11 )
        bSizer11.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel12 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText17 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"직원명", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )
        bSizer14.Add( self.m_staticText17, 0, wx.ALL, 5 )
        
        self.txtJikName = wx.TextCtrl( self.m_panel12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.txtJikName, 0, wx.ALL, 5 )
        
        self.m_staticText18 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"부서명", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )
        bSizer14.Add( self.m_staticText18, 0, wx.ALL, 5 )
        
        self.txtJikBuser = wx.TextCtrl( self.m_panel12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.txtJikBuser, 0, wx.ALL, 5 )
        
        self.m_staticText19 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"전화", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )
        bSizer14.Add( self.m_staticText19, 0, wx.ALL, 5 )
        
        self.txtJikTel = wx.TextCtrl( self.m_panel12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.txtJikTel, 0, wx.ALL, 5 )
        
        self.m_staticText20 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"직급", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )
        bSizer14.Add( self.m_staticText20, 0, wx.ALL, 5 )
        
        self.txtJikJik = wx.TextCtrl( self.m_panel12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.txtJikJik, 0, wx.ALL, 5 )
        
        
        self.m_panel12.SetSizer( bSizer14 )
        self.m_panel12.Layout()
        bSizer14.Fit( self.m_panel12 )
        bSizer11.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer11 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
            # Connect Events
        self.btn1.Bind( wx.EVT_BUTTON, self.Onclick )
        self.btn2.Bind( wx.EVT_BUTTON, self.Onclick )
        self.btn3.Bind( wx.EVT_BUTTON, self.Onclick )
        self.btn4.Bind( wx.EVT_BUTTON, self.Onclick )
        
        self.btn1.id = 1
        self.btn2.id = 2
        self.btn3.id = 3
        self.btn4.id = 4
        
        self.DbLoad()
        
    def __del__( self ):
        pass

    def Onclick(self, event):
        id = event.GetEventObject().id
        
        global rec_r
      
        if id == 1: #처음
            rec_r = 0
            
        elif id == 2: #이전
            rec_r = rec_r - 1
            if rec_r < 0 : rec_r = 0
            
        elif id == 3: #다음
            rec_r = rec_r + 1
            if rec_r > (len(datas) - 1) : rec_r = (len(datas) - 1)
            
        elif id == 4: #마지막
            rec_r = len(datas) - 1
        
        self.ShowData(rec_r)
    
    def DbLoad(self):
        
        try:
            conn = MySQLdb.connect(**config)    
            cursor = conn.cursor() 
            sql = 'select gogek_no,gogek_name,gogek_jumin,jikwon_name,buser_name,buser_tel,jikwon_jik from jikwon join gogek on gogek_damsano = jikwon_no join buser on buser_num = buser_no ;'
            cursor.execute(sql)
            global datas
            datas = cursor.fetchall()
            self.ShowData(rec_r)
            
            print(datas)
            
            
        except Exception as e:
            print('디비디비딥 에러',e)
            
        finally:
            cursor.close()
            conn.close()
            
            
    def ShowData(self,r):
        self.txtGogekNo.SetLabelText(str(datas[r][0]))
        self.txtGogekName.SetLabelText(datas[r][1])
        self.txtGogeGen.SetLabelText(str(datas[r][2]))
        self.txtJikName.SetLabelText(str(datas[r][3]))
        self.txtJikBuser.SetLabelText(str(datas[r][4]))
        self.txtJikTel.SetLabelText(str(datas[r][5]))
        self.txtJikJik.SetLabelText(str(datas[r][6]))

if __name__ == '__main__':
    # 앱 생성자 콜
    app = wx.App()
    MyFrame3(None).Show()
    app.MainLoop()      

