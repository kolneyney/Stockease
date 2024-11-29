import tkinter as tk
from tkinter import messagebox
import calldatabase


class SplashScreen:
    def __init__(self, root, on_splash_complete):
        self.root = root
        self.on_splash_complete = on_splash_complete
        self.setup_ui()

    def setup_ui(self):
        # Configure the splash screen
        self.root.title("StockEase")
        self.root.geometry("700x500")
        self.root.configure(bg='light blue')

        frame = tk.Frame(self.root, bg='white', padx=50, pady=50, bd=10, relief="ridge")
        frame.pack(padx=100, pady=100)
        tk.Label(frame, text="StockEase", font=("Verdana", 35, 'italic bold underline'), bg='white', fg="#4682b4").pack(expand=True)

        
        self.root.after(3000, self.on_splash_complete)


class LoginWindow:
    def __init__(self, root, on_login_success):
        self.root = root
        self.on_login_success = on_login_success  # Callback for successful login
        self.login_ui()

    def login_ui(self):
        # Configure the login UI
        self.root.title("Login")
        self.root.geometry("700x500")
        self.root.configure(bg='light blue')

        tk.Label(self.root, text="Login Page", font=("Verdana", 16, 'bold'), bg='light blue').pack(pady=30)
        tk.Label(self.root, text="Username", font=("Verdana", 14), bg='light blue').pack(pady=10)
        self.username_entry = tk.Entry(self.root, font=("Verdana", 14), width=20)
        self.username_entry.pack()

        tk.Label(self.root, text="Password", font=("Verdana", 14), bg='light blue').pack(pady=10)
        self.password_entry = tk.Entry(self.root, font=("Verdana", 14), show='*', width=20)
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.login_action, font=("Verdana", 14), bg='bisque', width=20).pack(pady=40)

        self.status_label = tk.Label(self.root, text="", font=("Verdana", 12), fg="red", bg='light blue')
        self.status_label.pack(pady=10)

    def login_action(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            result = True
            if result == calldatabase.authenticate_user(username, password):
                messagebox.showinfo("Success", "Login successful!")
                self.on_login_success()
            else:
                self.status_label.config(text="Error: Invalid username or password.")
        else:
            self.status_label.config(text="Please enter both username and password!")



