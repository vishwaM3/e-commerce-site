import sqlite3
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.toast import toast


# ---------- Database Setup ----------
conn = sqlite3.connect("users.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")
conn.commit()


# ---------- Screens ----------
class LoginScreen(Screen):
    def do_login(self):
        username = self.ids.username.text.strip()
        password = self.ids.password.text.strip()

        cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cur.fetchone()

        if user:
            toast("✅ Login successful!")
        else:
            toast("❌ Invalid username or password")


class SignupScreen(Screen):
    def do_signup(self):
        username = self.ids.username.text.strip()
        password = self.ids.password.text.strip()

        if not username or not password:
            toast("⚠ Please fill all fields")
            return

        try:
            cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            toast("✅ Account created! You can login now")

            # clear fields
            self.ids.username.text = ""
            self.ids.password.text = ""

            self.manager.current = "login"
        except sqlite3.IntegrityError:
            toast("⚠ Username already exists")

# ---------- Screen Manager ----------
class WindowManager(ScreenManager):
    pass


# ---------- Main App ----------
class LoginApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        return Builder.load_file("log3.kv")


if __name__ == "__main__":
    LoginApp().run()