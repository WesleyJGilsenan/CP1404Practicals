"""
CP1404 Practical 8 - Convert Miles to Km
Wesley Gilsenan

"""


from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesToKmApp(App):
    km_output = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def label_calculation(self, text):
        miles = text

    #def handle_update(self, miles):
        #self.km_output = miles * MILES_TO_KM


MilesToKmApp().run()
