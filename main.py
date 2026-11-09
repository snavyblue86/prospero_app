from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.video import Video
from kivy.uix.button import Button
from kivy.uix.label import Label
class ProsperoApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.video = Video(source='boot.mp4', state='play', options={'eos': 'loop'})
        self.btn = Button(text='ENTER PROSPERO', size_hint_y=0.2, background_color=(0,1,0,1))
        self.btn.bind(on_press=self.enter)
        self.layout.add_widget(self.video)
        self.layout.add_widget(self.btn)
        return self.layout
    def enter(self, *a):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text='PROSPERO - COMPLETE ARCHITECTURE\n\nBOOT VIDEO - DONE\nARCHITECTURE - DONE\nREADY FOR REAL CORE', font_size=24))
        b = Button(text='BACK', size_hint_y=0.2)
        b.bind(on_press=lambda x: self.build())
        self.layout.add_widget(b)
ProsperoApp().run()
