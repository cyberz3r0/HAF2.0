from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import DictProperty
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import ScreenManager, Screen

class ReceiptCapture(Screen):
    result = DictProperty({})
    def selected(self, filename):
        self.ids.image_viewer.source = filename[0]
    def analyze_receipt(self, filename):
        from helper import analyze_photo
        self.result = analyze_photo(filename[0])
        return self.result   

class ValidationForm(Screen):
    pass

# class MainWidget(GridLayout):
    # result = DictProperty({})
    # def selected(self, filename):
    #     self.ids.image_viewer.source = filename[0]
    # def analyze_receipt(self, filename):
    #     from helper import analyze_photo
    #     self.result = analyze_photo(filename[0])
    #     return self.result    
class HafApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ReceiptCapture())
        sm.add_widget(ValidationForm())
        return sm

HafApp().run()