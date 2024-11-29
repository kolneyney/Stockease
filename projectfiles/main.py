import tkinter as tk
from tkinter import messagebox
from loginpage import LoginWindow
from grocery_product import GroceryApp
from loginpage import SplashScreen  

def show_grocery_app(root):
    
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("700x500")
    GroceryApp(root)

def main():
    def show_login():
        
        splash_root.destroy()
        login_root = tk.Tk()
        LoginWindow(login_root, on_login_success=lambda: show_grocery_app(login_root))
        login_root.mainloop()

    # Display splash screen
    splash_root = tk.Tk()
    SplashScreen(splash_root, on_splash_complete=show_login)
    splash_root.mainloop()

if __name__ == "__main__":
    main()
