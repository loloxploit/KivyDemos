from sys import argv
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.clock import Clock, mainthread
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from os.path import dirname,basename,join
from kivymd.uix.card import MDCard
from kivy.uix.button import Button
from kivy_gradient import Gradient
from kivy.utils import get_color_from_hex


Window.size = 370,675

if len(argv) != 2:
    print('usage: %s filename.kv' % argv[0])
    exit(1)

PATH= dirname(argv[1])
TARGET= basename(argv[1])


            

class KvHandler(FileSystemEventHandler):
    def __init__(self,callback,target,**kwargs):
        super(KvHandler, self).__init__(**kwargs)
        self.callback = callback
        self.target = target
    
    def on_any_event(self, event):
        if basename(event.src_path) == self.target:
            self.callback()


class KvViewerApp(MDApp):
    def build(self):
        observer = Observer()
        observer.schedule(KvHandler(self.update, TARGET),PATH)
        observer.start()
        Clock.schedule_once(self.update, 1)
        return super(KvViewerApp, self).build()

    @mainthread
    def update(self, *args):
        Builder.unload_file(join(PATH,TARGET))
        for w in Window.children:
            Window.remove_widget(w)
        try:
            Window.add_widget(Builder.load_file(join(PATH,TARGET)))
        except Exception as e:
            Window.add_widget(MDLabel(text=(e.message if getattr(e, r'message', None) else str(e))))



if __name__== '__main__':
    KvViewerApp().run()


