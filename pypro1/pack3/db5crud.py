

import wx
import wx.xrc
import ast
import MySQLdb
from _pylief import NONE

rec_r = 0
datas = []
 
with open('mariadb.txt', 'r') as figu:
    aa = figu.read()
    config = ast.literal_eval(aa)


class MyFrame4 (wx.Frame):
    
    def __init__(self, parent):
        wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(401, 395), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        
        # self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
        
        bSizer15 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel13 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer16 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText22 = wx.StaticText(self.m_panel13, wx.ID_ANY, u"번호 :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        bSizer16.Add(self.m_staticText22, 0, wx.ALL, 5)
        
        self.txtNo = wx.TextCtrl(self.m_panel13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer16.Add(self.txtNo, 0, wx.ALL, 5)
        
        self.btnInsert = wx.Button(self.m_panel13, wx.ID_ANY, u"등록", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer16.Add(self.btnInsert, 0, wx.ALL, 5)
        
        self.m_panel13.SetSizer(bSizer16)
        self.m_panel13.Layout()
        bSizer16.Fit(self.m_panel13)
        bSizer15.Add(self.m_panel13, 0, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel14 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer17 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText23 = wx.StaticText(self.m_panel14, wx.ID_ANY, u"이름 :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText23.Wrap(-1)
        bSizer17.Add(self.m_staticText23, 0, wx.ALL, 5)
        
        self.txtName = wx.TextCtrl(self.m_panel14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer17.Add(self.txtName, 0, wx.ALL, 5)
        
        self.btnUpdate = wx.Button(self.m_panel14, wx.ID_ANY, u"수정", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer17.Add(self.btnUpdate, 0, wx.ALL, 5)
        
        self.btnConfirm = wx.Button(self.m_panel14, wx.ID_ANY, u"확인", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer17.Add(self.btnConfirm, 0, wx.ALL, 5)
        
        self.m_panel14.SetSizer(bSizer17)
        self.m_panel14.Layout()
        bSizer17.Fit(self.m_panel14)
        bSizer15.Add(self.m_panel14, 0, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel15 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer18 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText25 = wx.StaticText(self.m_panel15, wx.ID_ANY, u"전화 :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText25.Wrap(-1)
        bSizer18.Add(self.m_staticText25, 0, wx.ALL, 5)
        
        self.txtTel = wx.TextCtrl(self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer18.Add(self.txtTel, 0, wx.ALL, 5)
        
        self.btnDel = wx.Button(self.m_panel15, wx.ID_ANY, u"삭제", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer18.Add(self.btnDel, 0, wx.ALL, 5)
        
        self.m_panel15.SetSizer(bSizer18)
        self.m_panel15.Layout()
        bSizer18.Fit(self.m_panel15)
        bSizer15.Add(self.m_panel15, 0, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel16 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer19 = wx.BoxSizer(wx.VERTICAL)
        
        self.lstMem = wx.ListCtrl(self.m_panel16, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        bSizer19.Add(self.lstMem, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_panel16.SetSizer(bSizer19)
        self.m_panel16.Layout()
        bSizer19.Fit(self.m_panel16)
        bSizer15.Add(self.m_panel16, 1, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel17 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer20 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText26 = wx.StaticText(self.m_panel17, wx.ID_ANY, u"인원수 :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText26.Wrap(-1)
        bSizer20.Add(self.m_staticText26, 0, wx.ALL, 5)
        
        self.staCount = wx.StaticText(self.m_panel17, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staCount.Wrap(-1)
        bSizer20.Add(self.staCount, 0, wx.ALL, 5)
        
        self.m_panel17.SetSizer(bSizer20)
        self.m_panel17.Layout()
        bSizer20.Fit(self.m_panel17)
        bSizer15.Add(self.m_panel17, 1, wx.EXPAND | wx.ALL, 5)
        
        self.SetSizer(bSizer15)
        self.Layout()
        
        self.Centre(wx.BOTH)
        
        # Connect Events
        self.btnInsert.Bind(wx.EVT_BUTTON, self.OnBtnClick)
        self.btnUpdate.Bind(wx.EVT_BUTTON, self.OnBtnClick)
        self.btnConfirm.Bind(wx.EVT_BUTTON, self.OnBtnClick)
        self.btnDel.Bind(wx.EVT_BUTTON, self.OnBtnClick)
        
        self.btnInsert.id = 1
        self.btnUpdate.id = 2
        self.btnConfirm.id = 3
        self.btnDel.id = 4
        
        self.lstMem.InsertColumn(0, '번호' , width=50)
        self.lstMem.InsertColumn(1, '이름' , width=100)
        self.lstMem.InsertColumn(2, '전화' , width=150)
        
        self.btnConfirm.Enable(enable=False)
        
        self.viewListData()
        
    def __del__(self):
        pass

    def viewListData(self):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            sql = 'select * from pymem';
            cursor.execute(sql)

            self.lstMem.DeleteAllItems()
            count = 0
            for data in cursor :
                i = self.lstMem.InsertItem(65535, 0)  # 동적인 행 확보
                self.lstMem.SetItem(i, 0 , str(data[0]))
                self.lstMem.SetItem(i, 1 , data[1])
                self.lstMem.SetItem(i, 2 , data[2])
                count += 1 
    
                self.staCount.SetLabelText(str(count))
        
        except Exception as e:
            print('디비디비딥 에러', e)
            
        finally:
            cursor.close()
            conn.close()
        
    # Virtual event handlers, overide them in your derived class
    def OnBtnClick(self, event):
        id = event.GetEventObject().id
        # print(id)
        
        if id == 1:
            self.MemInsert()  # 등록
        
        elif id == 2:
            self.MemUpdate()  # 수정 준비
            
        elif id == 3:
            self.MemUpdateOk()  # 수정 처리
            
        elif id == 4:
            self.MemDelete()  # 삭제
        
        elif id == 5:
            self.MemUpdateCancel()  # 수정 취소
    
    def MemInsert(self):
        no = self.txtNo.GetValue()
        name = self.txtName.GetValue()
        tel = self.txtTel.GetValue()
        
        if no == '' or name == '' or tel == '':
            wx.MessageBox('자료를 입릭하시오', '입력', wx.OK)
            return   
                       
        try : 
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            data = self.SelectData(no) #추가용 번호의 등록 가능여부 확인
            
            if data != None:
                wx.MessageBox('이미  사용중인 번호 입니다','알림',wx.OK)
                self.txtNo.SetFocus()
                return
            # 추가계속
            sql = 'insert into pymem values(%s,%s,%s)';
            
            cursor.execute(sql,(no,name,tel))              
            conn.commit()
            
            self.viewListData() # 추가 후 자료 보기
            self.txtNo.SetValue('') #입력 자료 초기화\
            self.txtName.SetValue('') #입력 자료 초기화
            self.txtTel.SetValue('') #입력 자료 초기화
               
            
            
          
        except Exception as e:
            print('디비디비딥 에러', e)
            
        finally:
            cursor.close()
            conn.close()
    
    def MemUpdate(self):
        dig = wx.TextEntryDialog(None,'수정할 번호 입력','수정')
        if dig.ShowModal() == wx.ID_OK:
            if dig.GetValue == '':
                return 
            upno = dig.GetValue()
            #print(upno)
            
            data = self.SelectData(upno) 
            if data == None:    # SelectData 에 입력한 값이 없는 경우
                wx.MessageBox(upno + '번은 등록된 자료가 아닙니다', '알림' , wx.OK) 
                return
                        
            #수정 준비 계속
            self.txtNo.SetValue(str(data[0])) # 수정할 자료 화면에 표시
            self.txtName.SetValue(str(data[1])) # 수정할 자료 화면에 표시
            self.txtTel.SetValue(str(data[2])) # 수정할 자료 화면에 표시
            
            self.txtNo.SetEditable(False)  # 수정 버튼 입력시 txtNo값은 수정불가
            self.btnConfirm.Enable(True)  # 확인버튼 활성화
            self.btnUpdate.SetLabel("취소") # 수정버튼 취소로 바뀜 
            self.btnUpdate.id = 5 # btnupdate id가 5가되고 취소 버튼 은 취소버튼을 누를시 btnupdate 는 MemUpdateCancel를 실행시킬것임.
        else : 
            return 
        
        dig.Destroy()
        
        
        

    def MemUpdateOk(self):
        no = self.txtNo.GetValue()
        name = self.txtName.GetValue()
        tel = self.txtTel.GetValue()
        
        if name == '' or tel == '':
            wx.MessageBox('자료를 입릭하시오', '입력', wx.OK)
            return   
                       
        try : 
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = 'update pymem set irum = %s,junhwa=%s where bun = %s'
            cursor.execute(sql,(name,tel,no))
            
            conn.commit() #자료 수정 
            
            self.viewListData() # 수정하 자료보기
            self.txtTel.SetValue('')
            self.txtNo.SetValue('')
            self.txtName.SetValue('')
            self.txtNo.SetEditable(True)  # 수정 버튼 입력시 txtNo값 다시 수정가능하게 바꿈
            self.btnConfirm.Enable(False)  # 확인버튼 다시비화렁화
            self.btnUpdate.SetLabel("수정") # 취소버튼을 다시 수정으로 바꿈
            self.btnUpdate.id = 2 # btnupdate id가 2가되고 수정 메소드로 가게끔함.
            
            
            
        except Exception as e:
            print('디비디비딥 에러', e)
            
        finally:
            cursor.close()
            conn.close()
            
            
    def MemDelete(self):
        
        dig = wx.TextEntryDialog(None,'삭제번호 입력','삭제')
        if dig.ShowModal() == wx.ID_OK:
            if dig.GetValue == '':
                return 
            delno = dig.GetValue()
            #print(upno)
            
            data = self.SelectData(delno) 
            if data == None:    # SelectData 에 입력한 값이 없는 경우
                wx.MessageBox(delno + '번은 등록된 자료가 아닙니다', '알림' , wx.OK) 
                return
            #삭제 준비 계속 
        try : 
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = 'delete from pymem where bun = {}'.format(delno)
            cursor.execute(sql)
            
            conn.commit() #자료 수정 
            
            self.viewListData()
        except Exception as e:
            print('디비디비딥 에러', e)
            
        finally:
            cursor.close()
            conn.close()    
    
    def MemUpdateCancel(self):
        pass
    
    
    def SelectData(self, no): # 해당 번호의 자료 읽기  (i,u,d)
                       
        try : 
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
                    
            sql = 'select * from pymem where bun = {0};'.format(no)
            cursor.execute(sql)
            
            data = cursor.fetchone() # 하나의 자료 추출
            return data
            
        except Exception as e:
            print('디비디비딥 에러', e)
            
        finally:
            cursor.close()
            conn.close()

    
    
    
    
    

if __name__ == '__main__':
    # 앱 생성자 콜
    app = wx.App()
    MyFrame4(None).Show()
    app.MainLoop()      
