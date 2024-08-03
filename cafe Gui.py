import tkinter as tk
from tkinter import messagebox

# Menu dictionary
dict1 = {
    "coffee": 100,
    "tea": 50,
    "pasta": 150,
    "pizza": 200,
    "burger": 300
}

# Initialize main window
root = tk.Tk()
root.title("Cafe Management System")
root.configure(bg='#f4f4f4')  # Background color

# Initialize global variables
order_items = []
total_bill = 0

# Update menu in the Listbox
def update_menu():
    menu_listbox.delete(0, tk.END)
    for item, price in dict1.items():
        menu_listbox.insert(tk.END, f"{item}: {price} RS")

# Add order to the list and update total bill
def add_order():
    global total_bill
    order = order_entry.get().lower()
    try:
        quantity = int(quantity_entry.get())
        if quantity <= 0:
            messagebox.showwarning("Invalid Input", "Please enter a positive number for quantity.")
            return
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number for quantity.")
        return

    if order in dict1:
        total_price = quantity * dict1[order]
        total_bill += total_price
        order_items.append((order, quantity, total_price))
        messagebox.showinfo("Order Added", f"You ordered {order} Quantity={quantity} Price: {total_price} RS")
    else:
        messagebox.showwarning("Item Not Found", "Sorry, that item is not available on the menu.")

# Show the bill in the Text widget
def show_bill():
    bill_text.delete(1.0, tk.END)
    bill_text.insert(tk.END, "YOU ordered:\n")
    for item, quantity, price in order_items:
        bill_text.insert(tk.END, f"-- {item}: No: {quantity} Price: {price} RS\n")
    bill_text.insert(tk.END, f"Your total bill is: {total_bill} RS\n")
    bill_text.insert(tk.END, "===========================\n")
    bill_text.insert(tk.END, "THANK YOU FOR VISITING !!!!\n")

# Create and pack widgets
title_label = tk.Label(root, text="Welcome to Our Cafe", font=("Arial", 24, "bold"), bg='#f4f4f4', fg='#ff5722')
title_label.pack(pady=10)

menu_label = tk.Label(root, text="------ MENU CARD ----------", font=("Arial", 18, "bold"), bg='#f4f4f4', fg='#333')
menu_label.pack(pady=10)

menu_listbox = tk.Listbox(root, height=5, width=50, font=("Arial", 14), bg='#fff', fg='#333', selectbackground='#ff5722')
menu_listbox.pack(pady=10)
update_menu()

order_label = tk.Label(root, text="What do you want?", font=("Arial", 14), bg='#f4f4f4', fg='#333')
order_label.pack(pady=5)
order_entry = tk.Entry(root, font=("Arial", 14))
order_entry.pack(pady=5)

quantity_label = tk.Label(root, text="How many quantities do you want?", font=("Arial", 14), bg='#f4f4f4', fg='#333')
quantity_label.pack(pady=5)
quantity_entry = tk.Entry(root, font=("Arial", 14))
quantity_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Order", font=("Arial", 14), bg='#ff5722', fg='#fff', command=add_order)
add_button.pack(pady=10)

show_bill_button = tk.Button(root, text="Show Bill", font=("Arial", 14), bg='#4caf50', fg='#fff', command=show_bill)
show_bill_button.pack(pady=10)

bill_text = tk.Text(root, height=5, width=50, font=("Arial", 12), bg='#fff', fg='#333', wrap='word')
bill_text.pack(pady=10)

# Run the main loop
root.mainloop()
