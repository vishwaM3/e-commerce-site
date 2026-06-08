from kivymd.app import MDApp
from kivy.lang import Builder

class LoginApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"   # blue theme
        self.theme_cls.theme_style = "Light"      # light background
        return Builder.load_file("login.kv")

if __name__ == "__main__":
    LoginApp().run()