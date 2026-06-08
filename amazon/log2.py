from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel

class LoginApp(MDApp):
    def build(self):
        # App theme
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"

        screen = Screen()

        # Title
        title = MDLabel(
            text="Connect with Your MLA",
            halign="center",
            theme_text_color="Primary",
            font_style="H5",
            pos_hint={"center_x": 0.5, "center_y": 0.9},
        )

        # Contact Information field
        contact_input = MDTextField(
            hint_text="Contact Information",
            size_hint_x=0.8,
            pos_hint={"center_x": 0.5, "center_y": 0.75},
            mode="rectangle",
        )

        # Password field
        password_input = MDTextField(
            hint_text="Password",
            password=True,
            size_hint_x=0.8,
            pos_hint={"center_x": 0.5, "center_y": 0.65},
            mode="rectangle",
        )

        # Forgot Password link
        forgot_password = MDLabel(
            text="[u]Forgot Password?[/u]",
            markup=True,
            halign="left",
            theme_text_color="Custom",
            text_color=(0, 0, 1, 1),  # Blue color
            pos_hint={"center_x": 0.3, "center_y": 0.58},
        )

        # Login Button
        login_btn = MDRaisedButton(
            text="Login",
            size_hint_x=0.8,
            pos_hint={"center_x": 0.5, "center_y": 0.48},
        )

        # Add widgets
        screen.add_widget(title)
        screen.add_widget(contact_input)
        screen.add_widget(password_input)
        screen.add_widget(forgot_password)
        screen.add_widget(login_btn)

        return screen


LoginApp().run()