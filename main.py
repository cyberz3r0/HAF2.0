from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import DictProperty
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput

class ReceiptCapture(Screen):
    result = DictProperty({})
    def selected(self, filename):
        self.ids.image_viewer.source = filename[0]
    def analyze_receipt(self, filename):
        from helper import analyze_photo
        result = analyze_photo(filename[0])
        ValidationForm.make_form(self, result)
        self.result = result   
        self.manager.current = 'validation_form'
        # Call make_form method of ValidationForm screen
        self.manager.get_screen('validation_form').make_form(result)
class ValidationForm(Screen):
    def make_form(self, result):
            
        
        # Create a GridLayout to organize the widgets
        layout = GridLayout(cols=3, spacing=10, padding=10)
        # layout.bind(minimum_height=layout.setter('height'))
        # root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        # root.add_widget(layout) 
        # total_net_label = Label(text=result['total_net']['value'], font_size=30)
        taxes_label = Label(text=str(result['taxes'][0]['value']), font_size=30, size_hint=(None, None), size=(200, 50))
        total_amount_label = Label(text=str(result['total_amount']['value']), font_size=30, size_hint=(None, None), size=(200, 50))
        # tip_label = Label(text=result['tip']['value'], font_size=30)
        
        # Iterate over line_items and create labels and buttons dynamically
        for item in result['line_items']:
            label = Label(text=item['description'], font_size=30)
            if item['quantity']!= None:
                qty_label = Label(text=str(item['quantity']), font_size=30)
            else:
                qty_label = Label(text="1", font_size=30)
            text_input = TextInput(text=str(format(item['total_amount'], '.2f')), size_hint=(None, None), size=(150, 50), font_size=30, pos_hint=(1,1))
            
            # Add labels and buttons to the GridLayout
            layout.add_widget(label)
            layout.add_widget(qty_label)
            layout.add_widget(text_input)
        # layout.add_widget(total_net_label)
        layout.add_widget(taxes_label)
        layout.add_widget(total_amount_label)
        # layout.add_widget(tip_label)
        
            

        # Add the GridLayout to the screen
        self.add_widget(layout)

class HafApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ReceiptCapture(name='receipt_capture'))
        sm.add_widget(ValidationForm(name='validation_form'))
        return sm

HafApp().run()