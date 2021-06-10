

KV = """
<MyLabel@MDLabel>:
    color:1,1,1,1
<MyBoxLayout@MDBoxLayout>:
    orientation:'vertical'
    size_hint:.7,.04
    md_bg_color:
    
    
    

MDScreen:
    md_bg_color:0,0,0,.85
    #top color
    MDFloatLayout:
        size_hint_y:.3
        md_bg_color:1,0,0,1
        pos_hint:{'center_y':.85}
        radius:0,0,20,20
    #     
    MDStackLayout:
        orientation:'lr-tb'
        MDIconButton:
            icon:'arrow-left'
            size_hint:.2,.1
        MDLabel:
            text:'Pokedex'
            size_hint:.6,.1
            outline_color:0,0,0,1
            outline_width:2
            color:1,1,1,1
        MDLabel:
            text:'#006'
            size_hint:.2,.1
            color:1,1,1,1
            outline_color:0,0,0,1
            outline_width:2
    #
    MDFloatLayout:
        MDLabel:
            text:'Charizard'
            color:1,1,1,1
            font_style:'H5'
            halign:'center'
            bold:True
            italic:True
            pos_hint:{'center_y':.65}
        MDBoxLayout:
            orientation:'vertical'
            size_hint:.4,.05
            md_bg_color:1,0,0,1
            radius:20,20,20,20
            pos_hint:{'center_y':.57,'center_x':.25}
            MDLabel:
                text:'Fire'
                halign:'center'
                color:1,1,1,1
        MDBoxLayout:
            orientation:'vertical'
            size_hint:.4,.05
            md_bg_color:.1,0,1,1
            radius:20,20,20,20
            pos_hint:{'center_y':.57,'center_x':.75}
            MDLabel:
                text:'Flying'
                halign:'center'
                color:1,1,1,1
        
        MDBoxLayout:
            orientation:'horizontal'
            padding:
            spacing:
            MDLabel:
                text:'Weight'
                halign:'center'
                color:1,1,1,.7
                pos_hint:{'center_y':.4,'center_x':.75}
            
            MDLabel:
                text:'Height'
                color:1,1,1,.7
                halign:'center'
                pos_hint:{'center_y':.4,'center_x':.75}
        MDBoxLayout:
            orientation:'horizontal'
            padding:
            spacing:
            MDLabel:
                text:'90 KG'
                halign:'center'
                color:1,1,1,1
                font_size:"29dp"
                pos_hint:{'center_y':.47,'center_x':.75}
            
            MDLabel:
                text:'1.7 M'
                color:1,1,1,1
                halign:'center'
                font_size:"29dp"
                pos_hint:{'center_y':.47,'center_x':.75}
    MDFloatLayout:
        MDLabel:
            text:'Base Stats'
            halign:'center'
            color:1,1,1,1
            pos_hint:{'center_y':.35}
    MDBoxLayout:
        spacing:1
        
        pos_hint:{'center_y':.2,'center_x':.5}
        orientation:'vertical'
        size_hint:.9,.2
        md_bg_color:
        MyLabel:
            text:'HP '
        MyLabel:
            text:'ATK'
        MyLabel:
            text:'DEF'
        MyLabel:
            text:'SPD'
        MyLabel:
            text:'EXP'
    MyBoxLayout:
        padding:15
        pos_hint:{'center_y':.28,'center_x':.5}
        MDProgressBar:
            max:300
            value:168
    MyBoxLayout:
        padding:15
        pos_hint:{'center_y':.24,'center_x':.5}
        MDProgressBar:
            max:300
            value:208
            color:1,0,0,1
    MyBoxLayout:
        padding:15
        pos_hint:{'center_y':.2,'center_x':.5}
        MDProgressBar:
            max:300
            value:64
            color:0,1,1,.7
    MyBoxLayout:
        padding:15
        pos_hint:{'center_y':.16,'center_x':.5}
        MDProgressBar:
            max:300
            value:204
            color:0,1,0,1
    MyBoxLayout:
        padding:15
        pos_hint:{'center_y':.12,'center_x':.5}
        MDProgressBar:
            max:1000
            value:295
            color:1,1,0,1
"""

from kivymd.app import MDApp
from kivy.lang import Builder




class DemoApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

DemoApp().run()