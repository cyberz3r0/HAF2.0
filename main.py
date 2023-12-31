from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.utils import get_color_from_hex



class MainWidget(GridLayout):
    def selected(self, filename):
        self.ids.image_viewer.source = filename[0]
    def analyze_receipt(self, filename):
        from helper import analyze_photo
        analyze_photo(filename[0])
        
class HafApp(App):
    def build(self):
        return MainWidget()

HafApp().run()