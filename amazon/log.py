import sqlite3
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# Set mobile-like window size
Window.size = (360, 640)

# Database setup
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT NOT NULL)''')
conn.commit()

# Login Screen
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)

        layout.add_widget(Label(text='Login', font_size=32))

        self.username = TextInput(hint_text='Username', multiline=False)
        layout.add_widget(self.username)

        self.password = TextInput(hint_text='Password', multiline=False, password=True)
        layout.add_widget(self.password)

        login_btn = Button(text='Login', size_hint=(1, 0.2))
        login_btn.bind(on_press=self.login)
        layout.add_widget(login_btn)

        signup_btn = Button(text='Sign Up', size_hint=(1, 0.2))
        signup_btn.bind(on_press=self.go_to_signup)
        layout.add_widget(signup_btn)

        self.message = Label(text='')
        layout.add_widget(self.message)

        self.add_widget(layout)

    def login(self, instance):
        user = self.username.text
        pwd = self.password.text
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (user, pwd))
        result = cursor.fetchone()
        if result:
            self.message.text = "✅ Login successful!"
        else:
            self.message.text = "❌ Invalid credentials"

    def go_to_signup(self, instance):
        self.manager.current = 'signup'

# Sign-Up Screen
class SignupScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)

        layout.add_widget(Label(text='Sign Up', font_size=32))

        self.new_username = TextInput(hint_text='New Username', multiline=False)
        layout.add_widget(self.new_username)

        self.new_password = TextInput(hint_text='New Password', multiline=False, password=True)
        layout.add_widget(self.new_password)

        signup_btn = Button(text='Create Account', size_hint=(1, 0.2))
        signup_btn.bind(on_press=self.create_account)
        layout.add_widget(signup_btn)

        back_btn = Button(text='Back to Login', size_hint=(1, 0.2))
        back_btn.bind(on_press=self.go_to_login)
        layout.add_widget(back_btn)

        self.message = Label(text='')
        layout.add_widget(self.message)

        self.add_widget(layout)

    def create_account(self, instance):
        user = self.new_username.text
        pwd = self.new_password.text
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user, pwd))
            conn.commit()
            self.message.text = "✅ Account created!"
        except sqlite3.IntegrityError:
            self.message.text = "⚠️ Username already exists"

    def go_to_login(self, instance):
        self.manager.current = 'login'

# App Manager
class AuthApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SignupScreen(name='signup'))
        return sm

if __name__ == '__main__':
    AuthApp().run()
class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        layout.add_widget(Label(text='🎉 Welcome to your Dashboard!', font_size=28))
        logout_btn = Button(text='Logout', size_hint=(1, 0.2))
        logout_btn.bind(on_press=self.logout)
        layout.add_widget(logout_btn)
        self.add_widget(layout)

    def logout(self, instance):
        self.manager.current = 'login'