import wx
import wx.xrc
import ast
import MySQLdb

rec_r = 0
datas = []
 
with open('mariadb.txt','r') as figu:
    aa = figu.read()
    config = ast.literal_eval(aa)
    
class MyFrame3 (wx.Frame):
    
    def __init__(self, parent):
        wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(410, 201), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        
        # self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))
        
        bSizer11 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel9 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText14 = wx.StaticText(self.m_panel9, wx.ID_ANY, u"코드:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)
        bSizer12.Add(self.m_staticText14, 0, wx.ALL, 5)
        
        self.txtCode = wx.TextCtrl(self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.txtCode, 0, wx.ALL, 5)
        
        self.m_staticText16 = wx.StaticText(self.m_panel9, wx.ID_ANY, u"상품:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)
        bSizer12.Add(self.m_staticText16, 0, wx.ALL, 5)
        
        self.txtSang = wx.TextCtrl(self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.txtSang, 0, wx.ALL, 5)
        
        self.m_panel9.SetSizer(bSizer12)
        self.m_panel9.Layout()
        bSizer12.Fit(self.m_panel9)
        bSizer11.Add(self.m_panel9, 0, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel10 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText17 = wx.StaticText(self.m_panel10, wx.ID_ANY, u"수량:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)
        bSizer13.Add(self.m_staticText17, 0, wx.ALL, 5)
        
        self.txtSu = wx.TextCtrl(self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer13.Add(self.txtSu, 0, wx.ALL, 5)
        
        self.m_staticText18 = wx.StaticText(self.m_panel10, wx.ID_ANY, u"단가:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText18.Wrap(-1)
        bSizer13.Add(self.m_staticText18, 0, wx.ALL, 5)
        
        self.txtDan = wx.TextCtrl(self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer13.Add(self.txtDan, 0, wx.ALL, 5)
        
        self.m_panel10.SetSizer(bSizer13)
        self.m_panel10.Layout()
        bSizer13.Fit(self.m_panel10)
        bSizer11.Add(self.m_panel10, 0, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel11 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer14 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText19 = wx.StaticText(self.m_panel11, wx.ID_ANY, u"금액:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText19.Wrap(-1)
        bSizer14.Add(self.m_staticText19, 0, wx.ALL, 5)
        
        self.staKum = wx.StaticText(self.m_panel11, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staKum.Wrap(-1)
        bSizer14.Add(self.staKum, 0, wx.ALL, 5)
        
        self.m_panel11.SetSizer(bSizer14)
        self.m_panel11.Layout()
        bSizer14.Fit(self.m_panel11)
        bSizer11.Add(self.m_panel11, 0, wx.ALL | wx.EXPAND, 5)
        
        self.m_panel12 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer15 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.btn1 = wx.Button(self.m_panel12, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer15.Add(self.btn1, 0, wx.ALL, 5)
        
        self.btn2 = wx.Button(self.m_panel12, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer15.Add(self.btn2, 0, wx.ALL, 5)
        
        self.btn3 = wx.Button(self.m_panel12, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer15.Add(self.btn3, 0, wx.ALL, 5)
        
        self.btn4 = wx.Button(self.m_panel12, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer15.Add(self.btn4, 0, wx.ALL, 5)
        
        self.m_panel12.SetSizer(bSizer15)
        self.m_panel12.Layout()
        bSizer15.Fit(self.m_panel12)
        bSizer11.Add(self.m_panel12, 0, wx.ALL, 5)
        
        self.SetSizer(bSizer11)
        self.Layout()
        
        self.Centre(wx.BOTH)
        
        # Connect Events
        self.btn1.Bind(wx.EVT_BUTTON, self.Onclick)
        self.btn2.Bind(wx.EVT_BUTTON, self.Onclick)
        self.btn3.Bind(wx.EVT_BUTTON, self.Onclick)
        self.btn4.Bind(wx.EVT_BUTTON, self.Onclick)
        
        self.btn1.id = 1
        self.btn2.id = 2
        self.btn3.id = 3
        self.btn4.id = 4
        
        self.DbLoad()
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def Onclick(self, event):
        id = event.GetEventObject().id
        # print(id)
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
            sql = 'select * from sangdata'
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
        self.txtCode.SetLabelText(str(datas[r][0]))
        self.txtSang.SetLabelText(datas[r][1])
        self.txtSu.SetLabelText(str(datas[r][2]))
        self.txtDan.SetLabelText(str(datas[r][3]))
        self.staKum.SetLabelText(str(datas[r][2] * datas[r][3]))        
if __name__ == '__main__':
    # 앱 생성자 콜
    app = wx.App()
    MyFrame3(None).Show()
    app.MainLoop()    