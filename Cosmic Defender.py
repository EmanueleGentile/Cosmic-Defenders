from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import subprocess
import webbrowser
import os

class MainApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical", padding=20, spacing=20)
        
        # Layout orizzontale per i 3 pulsanti grandi
        top_buttons = BoxLayout(orientation="horizontal", spacing=10, size_hint=(1, 0.7))
        
        facile_btn = Button(text="FACILE", font_size=32, on_press=self.run_facile)
        medio_btn = Button(text="MEDIO", font_size=32, on_press=self.run_medio)
        difficile_btn = Button(text="DIFFICILE", font_size=32, on_press=self.run_difficile)
        
        top_buttons.add_widget(facile_btn)
        top_buttons.add_widget(medio_btn)
        top_buttons.add_widget(difficile_btn)
        
        # Layout verticale per i 2 pulsanti più piccoli
        bottom_buttons = BoxLayout(orientation="horizontal", spacing=10, size_hint=(1, 0.3))
        
        github_btn = Button(text="GitHub", font_size=24, on_press=self.open_github)
        readme_btn = Button(text="README", font_size=24, on_press=self.open_readme)
        
        bottom_buttons.add_widget(github_btn)
        bottom_buttons.add_widget(readme_btn)
        
        # Aggiungiamo tutto al layout principale
        main_layout.add_widget(top_buttons)
        main_layout.add_widget(bottom_buttons)
        
        return main_layout

    def run_facile(self, instance):
        subprocess.run(["python", "FACILE.py"])

    def run_medio(self, instance):
        subprocess.run(["python", "MEDIO.py"])

    def run_difficile(self, instance):
        subprocess.run(["python", "DIFFICILE.py"])

    def open_github(self, instance):
        webbrowser.open("https://github.com/EmanueleGentile")

    def open_readme(self, instance):
        if os.path.exists("README.md"):
            os.startfile("README.md")
        else:
            print("README.md non trovato.")

if __name__ == "__main__":
    MainApp().run()
