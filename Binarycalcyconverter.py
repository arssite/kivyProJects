#ARSSITE_MINI_PROJECT
#DESIGN+ALGORITHM_BY_ARS
from kivy.resources import resource_add_path, resource_find
import os, sys
from re import T
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size=(300,390)
Window.borderless=True
class MainApp(MDApp):
    def add(self):
            prior=self.root.ids.inp.text
            self.root.ids.inp.text=f'{prior}+'
    def button_press(self,button):
        try:
            prior=self.root.ids.inp.text 
            if prior=='0':
                self.root.ids.inp.text=''
                self.root.ids.inp.text=f'{button}'
            else:
                self.root.ids.inp.text=f'{prior}{button}'
        except:
            pass
                
    def clr(self):
            self.root.ids.inp.text=''
            
    def equ(self):
             
            try:
                inp=self.root.ids.inp.text
                lt=[]
                ltign=[]
                ltv=[]
                v=['+','-','*','/','&','|','^','<','>','~']
                for i in v:
                            for j in inp:
                                            if i==j:
                                                        while True:
                                                                        try:
                                                                                    b=i
                                                                                    x=inp.index(b)
                                                                                    lt.append(x)
                                                                                    vl=inp[0:x]
                                                                                    inp=inp[x+1:]
                                                                                    ltign.append(b)
                                                                                    ltv.append(vl)
                                                                        
                                                                        except:
                                                                                    break
                                            
                ltv.append(inp)
                j=0
                for i in range(len(ltv)):
                            for j in ltign:
                                            if j=='+':
                                                        try:
                                                                        sum=bin(int(ltv[0],2)+int(ltv[1],2))
                                                                        #print(sum)
                                                                        v=sum[:]
                                                                        if len(ltv)>1:
                                                                                    del ltv[1]
                                                                                    del ltv[0]
                                                                        ltv.insert(0,str(v))
                                                        except:
                                                                        break
                                            elif j=='-':
                                                        try:
                                                                        sum=bin(int(ltv[0],2)-int(ltv[1],2))
                                                                        #print(sum)
                                                                        v=sum[:]
                                                                        if len(ltv)>1:
                                                                                    del ltv[1]
                                                                                    del ltv[0]
                                                                        ltv.insert(0,str(v))
                                                        
                                                        except:
                                                                        break
                                            elif j=='*':
                                                        try:
                                                                        sum=bin(int(ltv[0],2)*int(ltv[1],2))
                                                                        #print(sum)
                                                                        v=sum[:]
                                                                        if len(ltv)>1:
                                                                                    del ltv[1]
                                                                                    del ltv[0]
                                                                        ltv.insert(0,str(v))
                                                        
                                                        except:
                                                                        break
                                            elif j=='/':
                                                        try:
                                                                        sum=int(ltv[0],2)/int(ltv[1],2)
                                                                        #print(sum)
                                                                        M=int(sum)
                                                                        v=bin(M)
                                                                        if len(ltv)>1:
                                                                                    del ltv[1]
                                                                                    del ltv[0]
                                                                        ltv.insert(0,str(v))
                                                        
                                                        except:
                                                                        break
                                            elif j=='&':
                                                        try:
                                                                        sum=int(ltv[0],2) and int(ltv[1],2)
                                                                        #print(sum)
                                                                        M=int(sum)
                                                                        v=bin(M)
                                                                        if len(ltv)>1:
                                                                                    del ltv[1]
                                                                                    del ltv[0]
                                                                        ltv.insert(0,str(v))
                                                        
                                                        except:
                                                                        break
                                            elif j=='|':
                                                        try:
                                                                        sum=int(ltv[0],2) or int(ltv[1],2)
                                                                        #print(sum)
                                                                        M=int(sum)
                                                                        v=bin(M)
                                                                        if len(ltv)>1:
                                                                                    del ltv[1]
                                                                                    del ltv[0]
                                                                        ltv.insert(0,str(v))
                                                        
                                                        except:
                                                                        break
                                            elif j=='^':
                                                        try:
                                                                        sum=int(ltv[0],2) ^ int(ltv[1],2)
                                                                        #print(sum)
                                                                        M=int(sum)
                                                                        v=bin(M)
                                                                        if len(ltv)>1:
                                                                                    del ltv[1]
                                                                                    del ltv[0]
                                                                        ltv.insert(0,str(v))
                                                        
                                                        except:
                                                                        break
                                            elif j=='~':
                                                        try:
                                                                        sum= ~ int(ltv[1],2)
                                                                        #print(sum)
                                                                        M=int(sum)
                                                                        v=bin(M)
                                                                        if len(ltv)>1:
                                                                                    del ltv[1]
                                                                                    del ltv[0]
                                                                        ltv.insert(0,str(v))
                                                        
                                                        except:
                                                                        break
                                            elif j=='>':
                                                        try:
                                                                        sum= int(ltv[0],2)
                                                                        print(sum,'1')
                                                                        pnm=  sum >> 1
                                                                        print(pnm,'2')
                                                                        #M=int(sum)
                                                                        v=bin(pnm)
                                                                        ltv=v
                                                        
                                                        except:
                                                                        break
                                            elif j=='<':
                                                        
                                                                        vb=ltv[0]
                                                                        sum= int(vb,2)
                                                                        print(sum,'1')
                                                                        pnm=  sum << 1
                                                                        print(pnm,'2')
                                                                        #M=int(sum)
                                                                        v=bin(pnm)
                                                                        ltv=v
                                                    
                                                    
                                                    
                                                    
            
               
                c=ltv[0]
                
                ind=0
                if 'b' in c:
                            for i in c:
                                            if i=='b':
                                                        self.root.ids.inp.text=c[ind+1:]
                                            ind+=1
                            print("ARSSITE MINI PROJECTS")

                else:
                                
                    if c[0]!='-':
                        
                                self.root.ids.inp.text=c[0]
                            
                                
                    else:
                        
                                self.root.ids.inp.text='-'+c[0]
            except:
                pass 
                    
                                        
    def bck(self):
            prior=self.root.ids.inp.text
            self.root.ids.inp.text=prior[:-1]
    def sub(self):
            prior=self.root.ids.inp.text
            self.root.ids.inp.text=f'{prior}-'
    def nd(self):
            prior=self.root.ids.inp.text
            self.root.ids.inp.text=f'{prior}&'
    def ro(self):
            prior=self.root.ids.inp.text
            self.root.ids.inp.text=f'{prior}|'
    def nor(self):
            prior=self.root.ids.inp.text
            self.root.ids.inp.text=f'{prior}^'
    def inv(self):
            prior=self.root.ids.inp.text
            self.root.ids.inp.text=f'{prior}~'
    def lhift(self):
            prior=self.root.ids.inp.text
            self.root.ids.inp.text=f'{prior}>'
    def rhift(self):
            prior=self.root.ids.inp.text
            self.root.ids.inp.text=f'{prior}<'
            
    def mul(self):
            prior=self.root.ids.inp.text
            self.root.ids.inp.text=f'{prior}*'
    #ARSSITE_MINI_PROJECT
    #DESIGN+ALGORITHM_BY_ARS        
    def divv(self):
            prior=self.root.ids.inp.text
            self.root.ids.inp.text=f'{prior}/'
    def addt(self):
            prior=self.root.ids.urr.text
            self.root.ids.urr.text=f'{prior}'
    def button_presst(self,button):
        try:
            prior=self.root.ids.urr.text 
            if prior=='0':
                self.root.ids.urr.text=''
                self.root.ids.urr.text=f'{button}'
            else:
                self.root.ids.urr.text=f'{prior}{button}'
        except:
            pass
                
    def clrt(self):
            self.root.ids.urr.text=''           
    
                    
                                        
    def bckt(self):
            prior=self.root.ids.urr.text
            self.root.ids.urr.text=prior[:-1]
    def hen(self):
        try:
            prior=self.root.ids.urr.text
            gui=hex(int(prior))
            self.root.ids.urr.text=gui[2:]
            print("ARSSITE MINI PROJECTS")
        except:
           pass
            
            
    def decc(self):
        print("ARSSITE MINI PROJECTS")
        exit()
    def octt(self):
        try:
              prior=self.root.ids.urr.text
              gui=oct(int(prior))
              self.root.ids.urr.text=gui[2:]
              print("ARSSITE MINI PROJECTS")
        except:
              pass

    def bin(self):
           
        try:
            prior=self.root.ids.urr.text
            gui=bin(int(prior))
            self.root.ids.urr.text=gui[2:]
            print("ARSSITE MINI PROJECTS")
        except:
           pass
    def build(self):
        self.theme_cls.theme_style='Dark'
        self.theme_cls.primary_palette='Orange'
        return Builder.load_string('''
BoxLayout:
    orientation:'vertical'
    
    MDBottomNavigation:
        panel_color:rgba('000000')
        MDBottomNavigationItem:
            name:'g1'
            text:'bcalcy'
            icon:'calculator'
            text_color: 1, 0, 1, 1
            BoxLayout:
                orientation:'vertical'
                size: root.width ,root.height
                padding:0.5
                spacing:2
                halign:'center'
                Widget:
                    height:8
                    size_hint_y:None
            
                MDTextField:
                    id:inp
                    md_bg_color: 1,1,1,1
                    pos_hint: {"center_y": 0.8,"center_x":0.501}
                    hint_text: "bcalcy"
                    #line_color_focus: 1, 1, 1, 1
                    #color_mode: 'custom'
                    text_color_focus: 1, 1, 1, 1#tetcolor
                    

                    theme_text_color: "Custom"
                    text_color:app.theme_cls.primary_color    
                    mode: "round"
                    size:(2,5)
                    size_hint_y:None
                    size_hint_x:.985
                    height:8
                    font_size:20
                BoxLayout:
                    orientation:'horizontal'
                    padding:20
                    spacing:20
                    BoxLayout:
                        orientation:'horizontal'
                        size: .5 ,.5
                        padding:1,1
                        spacing:1,1
                        size_hint_x:.5
                        GridLayout:
                            cols:2
                            rows:4
                            #['lr-tb', 'tb-lr', 'rl-tb', 'tb-rl', 'lr-bt', 'bt-lr', 'rl-bt', 'bt-rl']
                            orientation:'tb-lr'
                            padding:.8,.8
                            spacing:5.5,7.5
                            
                            MDRectangleFlatButton:
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                size:(5,5)
                                font_size:20
                                
                                md_bg_color: app.theme_cls.primary_color
                                text:'+'
                                on_press:app.add()
                            MDRectangleFlatButton:
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                size:(5,5)
                                font_size:20
                                
                                md_bg_color: app.theme_cls.primary_color
                                text:'-'
                
                                on_press:app.sub()

                            

                            MDRectangleFlatButton:
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                size:(5,5)
                                font_size:20
                                md_bg_color: app.theme_cls.primary_color
                                text:'*'
                                
                                background_color: (117/255,1,1,1)
                                on_press:app.mul()
                            
                            MDRectangleFlatButton:
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                size:(5,5)
                                font_size:20
                                
                                md_bg_color: app.theme_cls.primary_color
                                text:'/'
                                background_color: (117/255,1,1,1)
                                on_press:app.divv()
                            


                            MDRectangleFlatButton:
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                size:(5,5)
                                font_size:20
                                md_bg_color: app.theme_cls.primary_color
                                text:'|'
                                background_color: (117/255,1,1,1)
                                on_press:app.ro()

                            

                            MDRectangleFlatButton:
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                size:(5,5)
                                font_size:20
                                md_bg_color: app.theme_cls.primary_color
                                text:'^'
                                background_color: (117/255,1,1,1)
                                on_press:app.nor()
                            
                            MDRectangleFlatButton:
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                size:(5,5)
                                font_size:20
                                md_bg_color: app.theme_cls.primary_color
                                text:'&'
                                background_color: (117/255,1,1,1)
                                on_press:app.nd()
                            
                            MDRectangleFlatButton:
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                size:(5,5)
                                font_size:20
                                md_bg_color: app.theme_cls.primary_color
                                text:'~'
                                background_color: (117/255,1,1,1)
                                on_press:app.inv()
                                
                    
                        
                        
                            

                    #ARSSITE_MINI_PROJECT
                    #DESIGN+ALGORITHM_BY_ARS
                    BoxLayout:
                        orientation:'horizontal'
                        size: .5 ,.5
                        padding:1,1
                        spacing:1,1
                        size_hint_x:.5
                        GridLayout:
                            cols:1
                            rows:4
                            #['lr-tb', 'tb-lr', 'rl-tb', 'tb-rl', 'lr-bt', 'bt-lr', 'rl-bt', 'bt-rl']
                            orientation:'lr-tb'
                            padding:0,0
                            spacing:0,0


                            MDIconButton:
                                icon: "equal-box"
                                theme_icon_color: "Custom"
                                icon_color: app.theme_cls.primary_color
                                icon_size: "44sp"
                                background_color: (117/255,1,1,1)
                                on_press:app.equ()
                                

                    
                            MDIconButton:
                                icon: "alpha-c-box-outline"
                                theme_icon_color: "Custom"
                                icon_color: app.theme_cls.primary_color
                                icon_size: "44sp"
                                background_color: (117/255,1,1,1)
                                on_press:app.clr()
                        
                            MDIconButton:
                                icon: "arrow-left-bold-box-outline"
                                theme_icon_color: "Custom"
                                icon_color: app.theme_cls.primary_color
                                icon_size: "44sp"
                                background_color: (117/255,1,1,1)
                                on_press:app.bck()
                        GridLayout:
                            cols:1
                            rows:3
                            #['lr-tb', 'tb-lr', 'rl-tb', 'tb-rl', 'lr-bt', 'bt-lr', 'rl-bt', 'bt-rl']
                            orientation:'lr-tb'
                            padding:.5,.5
                            spacing:2.5,2.5


                            MDIconButton:
                                icon: "numeric-1-circle"
                                theme_icon_color: "Custom"
                                icon_color: app.theme_cls.primary_color
                                icon_size: "60sp"
                                background_color: (117/255,1,1,1)
                                on_press:app.button_press(1)
                                

                    
                            MDIconButton:
                                icon: "numeric-0-circle"
                                theme_icon_color: "Custom"
                                icon_color: app.theme_cls.primary_color
                                icon_size: "60sp"
                                background_color: (117/255,1,1,1)
                                on_press:app.button_press(0)
                        
                            MDIconButton:
                                theme_icon_color: "Custom"
                                icon_color: 13, 13, 13,1
                                icon_size: "54sp"
                                on_press:exit()
                                icon: "exit-run"
                                md_bg_color: 0,0,0,0


                

                            
                

                            
            
        
        
    
        MDBottomNavigationItem:
            name:'g2'
            text:'converter'
            icon:'abacus'
            text_color: 1, 0, 1, 1
            BoxLayout:
                orientation:'vertical'
                size: root.width ,root.height
                padding:0.5
                spacing:2
                halign:'center'
                Widget:
                    height:8
                    size_hint_y:None
                #ARSSITE_MINI_PROJECT
                #DESIGN+ALGORITHM_BY_ARS
                MDTextField:
                    id:urr
                    md_bg_color: 1,1,1,1
                    pos_hint: {"center_y": 0.8,"center_x":0.501}
                    hint_text: "converter"
                    #line_color_focus: 1, 1, 1, 1
                    #color_mode: 'custom'
                    text_color_focus: 1, 1, 1, 1#tetcolor
                    

                    theme_text_color: "Custom"
                    text_color:app.theme_cls.primary_color    
                    mode: "round"
                    size:(2,5)
                    size_hint_y:None
                    size_hint_x:.985
                    height:8
                    font_size:20
                BoxLayout:
                    orientation:'horizontal'
                    padding:20
                    spacing:10
                    
            
                    BoxLayout:
                        orientation:'horizontal'
                        size: .5 ,.5
                        padding:1,1
                        spacing:1,1
                        size_hint_x:.5

                        GridLayout:
                            cols:4
                            rows:4
                            #['lr-tb', 'tb-lr', 'rl-tb', 'tb-rl', 'lr-bt', 'bt-lr', 'rl-bt', 'bt-rl']
                            orientation:'lr-tb'
                            padding:.21,.21
                            spacing:4.5,3.5
                            
                            
                            MDRectangleFlatButton:
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                size:(5,5)
                                font_size:18
                                
                                md_bg_color: app.theme_cls.primary_color
                                text:'BIN'
                                on_press:app.bin()
                            

                            

                            MDRectangleFlatButton:
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                size:(5,5)
                                font_size:18
                                md_bg_color: app.theme_cls.primary_color
                                text:'OCT'
                                
                                background_color: (117/255,1,1,1)
                                on_press:app.octt()
                            
                            MDRectangleFlatButton:
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                size:(5,5)
                                font_size:18
                                
                                md_bg_color: app.theme_cls.primary_color
                                text:'HEX'
                                background_color: (117/255,1,1,1)
                                on_press:app.hen()
                            MDRectangleFlatButton:
                                
                                text_color: 0, 0, 1, 0
                                size:(5,5)
                                font_size:18
                                
                                md_bg_color: app.theme_cls.primary_color
                                text:'x'
                                background_color: (117/255,1,1,1)
                                on_press:app.decc()
                            
                        

                            

                            

                            
                                
                   


                            MDIconButton:
                                icon: "numeric-1-circle"
                                theme_icon_color: "Custom"
                                icon_color: app.theme_cls.primary_color
                                icon_size: "40sp"
                                background_color: (117/255,1,1,1)
                                on_press:app.button_presst(1)
                                

                    
                            MDIconButton:
                                icon: "numeric-4-circle"
                                theme_icon_color: "Custom"
                                icon_color: app.theme_cls.primary_color
                                icon_size: "40sp"
                                background_color: (117/255,1,1,1)
                                on_press:app.button_presst(4)
                        
                            MDIconButton:
                                icon: "numeric-7-circle"
                                theme_icon_color: "Custom"
                                icon_color: app.theme_cls.primary_color
                                icon_size: "40sp"
                                background_color: (117/255,1,1,1)
                                on_press:app.button_presst(7)
                            MDIconButton:
                                icon: "arrow-left-bold-box-outline"
                                theme_icon_color: "Custom"
                                icon_color: app.theme_cls.primary_color
                                icon_size: "40sp"
                                background_color: (117/255,1,1,1)
                                on_press:app.bckt()
                            
                            MDIconButton:
                                icon: "numeric-2-circle"
                                theme_icon_color: "Custom"
                                icon_color: app.theme_cls.primary_color
                                icon_size: "40sp"
                                background_color: (117/255,1,1,1)
                                on_press:app.button_presst(2)
                            MDIconButton:
                                icon: "numeric-5-circle"
                                theme_icon_color: "Custom"
                                icon_color: app.theme_cls.primary_color
                                icon_size: "40sp"
                                background_color: (117/255,1,1,1)
                                on_press:app.button_presst(5)
                            MDIconButton:
                                icon: "numeric-8-circle"
                                theme_icon_color: "Custom"
                                icon_color: app.theme_cls.primary_color
                                icon_size: "40sp"
                                background_color: (117/255,1,1,1)
                                on_press:app.button_presst(8)
                            MDIconButton:
                                icon: "numeric-0-circle"
                                theme_icon_color: "Custom"
                                icon_color: app.theme_cls.primary_color
                                icon_size: "40sp"
                                background_color: (117/255,1,1,1)
                                on_press:app.button_presst(0)
                            
                            MDIconButton:
                                icon: "numeric-3-circle"
                                theme_icon_color: "Custom"
                                icon_color: app.theme_cls.primary_color
                                icon_size: "40sp"
                                background_color: (117/255,1,1,1)
                                on_press:app.button_presst(3)
                            MDIconButton:
                                icon: "numeric-6-circle"
                                theme_icon_color: "Custom"
                                icon_color: app.theme_cls.primary_color
                                icon_size: "40sp"
                                background_color: (117/255,1,1,1)
                                on_press:app.button_presst(6)
                            MDIconButton:
                                icon: "numeric-9-circle"
                                theme_icon_color: "Custom"
                                icon_color: app.theme_cls.primary_color
                                icon_size: "40sp"
                                background_color: (117/255,1,1,1)
                                on_press:app.button_presst(9)
                            MDIconButton:
                                icon: "alpha-c-box-outline"
                                theme_icon_color: "Custom"
                                icon_color: app.theme_cls.primary_color
                                icon_size: "40sp"
                                background_color: (117/255,1,1,1)
                                on_press:app.clrt()                                   
                                   
                                   
                                   
                                   ''')
    
if __name__ == '__main__':
    try:
        if hasattr(sys, '_MEIPASS'):
            resource_add_path(os.path.join(sys._MEIPASS))
        app = MainApp()
        app.run()
    except Exception as e:
        print(e)
        input("Press enter.")    
#MainApp().run()
#ARSSITE_MINI_PROJECT
#DESIGN+ALGORITHM_BY_ARS
