from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import TwoLineListItem

KV = """
MDScreen:
    id:sc1
    name:'sc1'
    ScrollView:
        MDList:
            id:lst
    MDRaisedButton:
        text:'go fetch data'
        on_release: app.fetch_data()





"""


class Example(MDApp):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(Builder.load_string(KV))
        return self.sm

    def fetch_data(self):
        ## retrives a dict of names we will say ok
        ## So i want thren to be able to dynamicallly create however many
        ## widgets there are for names but on_release of these widgets should
        # have a MDDialog box pop open with the attritibutes associated with the data
        self.names = ["lolo", "jim", "carrey"]
        for _ in self.names:
            self.sm.get_screen("sc1").ids.lst.add_widget(
                TwoLineListItem(text="tap to view!", on_release=self.dialog)
            )

    def dialog(self, *args):
        for data in self.names:
            MDDialog(text=str(data)).open()


Example().run()
