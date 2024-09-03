from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar
from datetime import datetime

class MyApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical')
        self.born_date_input = self.root.ids.born_date_input
        self.result_label = self.root.ids.result_label
        self.progress_bar = self.root.ids.progress_bar
        return self.root
    
    def calculate_weeks(self):
        born_date = self.born_date_input.text
        try:
            d1 = datetime.strptime(born_date, "%d-%m-%Y")
            d2 = datetime.today()
            weeks_lived = abs((d2 - d1).days // 7)
            
            weeks_left_100 = 5200 - weeks_lived
            weeks_left_80 = 4211 - weeks_lived
            percentage_lived = (weeks_lived * 100) // 4211
            
            # Mostra i risultati
            result_text = (
                f"You have lived for {weeks_lived} weeks.\n"
                f"Weeks left if you reach 100 years: {weeks_left_100}\n"
                f"Weeks left if you reach 80 years (UK average): {weeks_left_80}\n"
                f"You have lived {percentage_lived}% of a typical 80-year life."
            )
            
            self.result_label.text = result_text
            self.progress_bar.value = percentage_lived
            
        except ValueError:
            self.result_label.text = "Invalid date format. Please use d-m-Y."

if __name__ == "__main__":
    MyApp().run()
