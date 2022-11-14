"""
CP1404 Practical 8 - Convert Miles to Km
Wesley Gilsenan

"""


from kivy.app import App
from kivy.lang import Builder


class MilesToKmApp(App):

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


MilesToKmApp().run()
