from tkinter import Toplevel
import tkinter as tk
from tkinter import ttk
import calldatabase  

class GroceryApp:

    def __init__(self, root):
        self.root = root
        self.main_window()

    def main_window(self):
        self.root.title("Grocery Store Management")
        self.root.geometry("700x500")
        self.root.configure(bg='light blue')

        frame = tk.Frame(self.root, bg='light grey', padx=20, pady=20, bd=5, relief="ridge")
        frame.pack(padx=20, pady=20)

        tk.Label(frame, text="Grocery Stock Management", font=("Verdana", 18,'italic'), bg='light grey').pack(pady=35)
        tk.Button(self.root, text="Products instock", command=self.open_products_window, font=("Verdana", 12), bg='peachpuff', width= 20).pack(pady=14)
        tk.Button(self.root, text="Add New Product", command=self.open_add_product_window, font=("Verdana", 12), bg='light yellow',width= 20).pack(pady=14)
        tk.Button(self.root, text="Delete Product", command=self.open_delete_product_window, font=("Verdana", 12), bg='light pink', width= 20).pack(pady=14)

    def open_products_window(self):
        self.root.withdraw()

        window = Toplevel(self.root)
        window.title("Product instock")
        window.geometry("700x500")
        window.configure(bg='light blue')

        # Category filter
        tk.Label(window, text="Filter by Category:", font=("Verdana", 11, 'bold'), bg='light blue').pack(pady=5)
        self.category_var = tk.StringVar()
        categories = calldatabase.all_categories()  # Assume backend.get_categories() returns a list of categories
        category_menu = ttk.Combobox(window, textvariable=self.category_var, values=["All"] + categories)
        category_menu.set("All")
        category_menu.pack(pady=5)

        # Product table
        columns = ("Product ID", "Product Name", "Category", "Price per Unit", "Unit Name","Quantity in stock" )
        self.product_table = ttk.Treeview(window, columns=columns, show="headings")

        for col in columns:
            self.product_table.heading(col, text=col)
            self.product_table.column(col, width=80)

        self.product_table.pack(fill="both", expand=True, padx=10, pady=10)


        tk.Button(window, text="Refresh Products", command=lambda: self.display_products(window),font=("Verdana", 10), bg='peachpuff', width= 20).pack(pady=10)
        tk.Button(window, text="Go Back", command=lambda: self.go_back(window),font=("Verdana", 10), bg='peachpuff', width= 20).pack(pady=10)

        self.update_button = tk.Button(window, text="Update Stock", state=tk.DISABLED, command=self.update_stock_button_action, font=("Verdana", 10), bg='peachpuff', width= 20)
        self.update_button.pack(pady=10)

        
        self.product_table.bind('<<TreeviewSelect>>', lambda event: self.enable_update_button(event, window))

        category_menu.bind("<<ComboboxSelected>>", lambda _: self.display_products(window))
        self.display_products(window)

    def display_products(self, window):
        selected_category = self.category_var.get()
        if selected_category == "All":
            products = calldatabase.instock_product()  # Fetch all products
        else:
            products = calldatabase.products_by_category(selected_category)  # Fetch products by category

        for item in self.product_table.get_children():
            self.product_table.delete(item)

        for product in products:
            self.product_table.insert("", "end", values=product)

        window.update()

    def enable_update_button(self, event, window):
        selected_item = self.product_table.selection()
        if selected_item:
            self.update_button.config(state=tk.NORMAL)
        else:
            self.update_button.config(state=tk.DISABLED)

    def update_stock_button_action(self):
        selected_item = self.product_table.selection()
        if selected_item:
            product_id = self.product_table.item(selected_item[0])["values"][0]
            self.update_stock_window(product_id)

    def update_stock_window(self, product_id):
    
        update_window = Toplevel(self.root)
        update_window.title("Update Stock")
        update_window.geometry("400x300")
        update_window.configure(bg='light blue')

        tk.Label(update_window, text="Enter New Stock Quantity:", font=("Verdana", 10,'italic'), bg='light blue').pack(pady=10)
        quantity_entry = tk.Entry(update_window,font=("Verdana", 10), width= 30)
        quantity_entry.pack(pady=10)

        status_label = tk.Label(update_window, text="", font=("Verdana", 10,'italic'), bg='light blue')
        status_label.pack(pady=10)

        def update_stock_action():
            new_quantity = quantity_entry.get()
            if new_quantity.isdigit():
                result = calldatabase.update_stock(new_quantity, product_id)
                status_label.config(text="Stock updated successfully!" if result == True else f"Error: {result}", font=("Verdana", 10,'italic'), bg='light blue')
            else:
                status_label.config(text="Please enter a valid quantity", font=("Verdana", 10,'italic'), bg='light blue')

        tk.Button(update_window, text="Update Stock", command=update_stock_action,font=("Verdana", 10), bg='peachpuff', width= 20).pack(pady=10)
        tk.Button(update_window, text="Cancel", command=update_window.destroy,font=("Verdana", 10), bg='peachpuff', width= 20).pack(pady=10)
        tk.Button(update_window, text="Done", command=update_window.destroy,font=("Verdana", 10), bg='peachpuff', width= 20).pack(pady=10)
        

    def open_add_product_window(self):
        self.root.withdraw()

        window = Toplevel(self.root)
        window.title("Add Product")
        window.geometry("700x500")
        window.configure(bg='light blue')

        tk.Label(window, text="Product Name", font=("Verdana", 11), bg='light blue', width= 20).pack(pady=10)
        name_entry = tk.Entry(window, font=("Verdana", 11), width= 20)
        name_entry.pack()

        tk.Label(window, text="Unit Name", font=("Verdana", 11), bg='light blue', width= 20).pack()
        unit_entry = tk.Entry(window, font=("Verdana", 11), width= 20)
        unit_entry.pack()

        tk.Label(window, text="Category ID",font=("Verdana", 11), bg='light blue', width= 20).pack()
        category_entry = tk.Entry(window,font=("Verdana", 11),width= 20)
        category_entry.pack()

        tk.Label(window, text="Price per Unit", font=("Verdana", 11), bg='light blue', width= 20).pack()
        price_entry = tk.Entry(window,font=("Verdana", 11),width= 20)
        price_entry.pack()

        tk.Label(window, text="Quantity add to stock", font=("Verdana", 11), bg='light blue', width= 20).pack()
        quantity_entry = tk.Entry(window, font=("Verdana", 11), width= 20)
        quantity_entry.pack()

        status_label = tk.Label(window, text="", font=("Verdana", 11,'italic'), bg='light blue')
        status_label.pack(pady=10)

        tk.Button(window, text="Add Product", command=lambda: self.add_product(name_entry, unit_entry, category_entry, price_entry, quantity_entry, status_label),
                  font=("Verdana", 10), bg='light yellow', width= 20).pack(pady=10)
        tk.Button(window, text="Go Back", command=lambda: self.go_back(window), font=("Verdana", 10), bg='light yellow', width= 20).pack(pady=10)

    def add_product(self, name_entry, unit_entry, category_entry, price_entry, quantity_entry, status_label):
        product_name = name_entry.get()
        unit_id = unit_entry.get()
        category_id = category_entry.get()
        price_per_unit = price_entry.get()
        quantity = quantity_entry.get()

        if product_name and unit_id and category_id and price_per_unit and quantity:
            result = calldatabase.insert_new_product(product_name, unit_id, category_id, price_per_unit, quantity)
            if result == True:
                status_label.config(text="Product added successfully!")
                name_entry.delete(0, tk.END)
                unit_entry.delete(0, tk.END)
                category_entry.delete(0, tk.END)
                price_entry.delete(0, tk.END)
                quantity_entry.delete(0, tk.END)
            else:
                status_label.config(text=result)
                name_entry.delete(0, tk.END)
                unit_entry.delete(0, tk.END)
                category_entry.delete(0, tk.END)
                price_entry.delete(0, tk.END)
                quantity_entry.delete(0, tk.END)
        else:
            status_label.config(text="Please fill in all fields")

    def open_delete_product_window(self):
        self.root.withdraw()

        window = Toplevel(self.root)
        window.title("Delete Product")
        window.geometry("400x300")
        window.configure(bg='light blue')

        tk.Label(window, text="Product ID to Delete", font=("Verdana", 11), bg='light blue', width= 20).pack(pady=10)
        id_entry = tk.Entry(window, font=("Verdana", 11),width= 20)
        id_entry.pack(pady=10)

        status_label = tk.Label(window, text="", font=("Verdana", 11, 'italic'), bg='light blue')
        status_label.pack(pady=10)

        tk.Button(window, text="Delete Product", command=lambda: self.delete_product(id_entry, status_label), font=("Verdana", 10), bg='light pink', width= 20).pack(pady=10)
        tk.Button(window, text="Go Back", command=lambda: self.go_back(window), font=("Verdana", 10), bg='light pink', width= 20).pack(pady=10)

    def delete_product(self, id_entry, status_label):
        product_id = id_entry.get()
        if product_id:
            result = calldatabase.delete_product(product_id)
            if result == True:
                status_label.config(text="Product deleted successfully!")
            else:
                status_label.config(text=result)
        else:
            status_label.config(text="Please enter a Product ID")

    def go_back(self, current_window):
        current_window.destroy()
        self.root.deiconify()



# root = tk.Tk()
# app = GroceryApp(root)
# root.mainloop()