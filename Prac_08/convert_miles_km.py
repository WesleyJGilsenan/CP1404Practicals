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
        miles = self.convert_to_number(text)
        self.handle_update(miles)

    def handle_increment(self, text, change):
        miles = self.convert_to_number(text) + change
        self.root.ids.user_distance_input.text = str(miles)

    def handle_update(self, miles):
        self.km_output = str(miles * MILES_TO_KM)

    @staticmethod
    def convert_to_number(text):
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesToKmApp().run()
