import tkinter as tk
from tkinter import messagebox

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    if name and phone:
        contacts[name] = phone
        listbox.insert(tk.END, name)
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)

def view_contact():
    name = listbox.get(listbox.curselection()[0])
    phone = contacts[name]
    messagebox.showinfo(title="Contact", message=f"Name: {name}\nPhone: {phone}")

def delete_contact():
    name = listbox.get(listbox.curselection()[0])
    if messagebox.askyesno(title="Delete", message=f"Are you sure you want to delete {name}?"):
        listbox.delete(listbox.curselection()[0])
        del contacts[name]

root = tk.Tk()
root.title("Contact Book By Div..")

contacts = {}

frame_list = tk.Frame(root)
listbox = tk.Listbox(frame_list)
listbox.pack(side=tk.LEFT, fill=tk.Y)
scrollbar = tk.Scrollbar(frame_list, command=listbox.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
frame_list.pack(side=tk.LEFT, fill=tk.Y)

frame_entries = tk.Frame(root)
label_name = tk.Label(frame_entries, text="Name:")
label_name.grid(row=0, column=0, sticky="W")
entry_name = tk.Entry(frame_entries)
entry_name.grid(row=0, column=1)
label_phone = tk.Label(frame_entries, text="Phone:")
label_phone.grid(row=1, column=0, sticky="W")
entry_phone = tk.Entry(frame_entries)
entry_phone.grid(row=1, column=1)
frame_entries.pack(side=tk.LEFT, padx=10)

frame_buttons = tk.Frame(root)
button_add = tk.Button(frame_buttons, text="Add", command=add_contact)
button_add.pack(fill=tk.X)
button_view = tk.Button(frame_buttons, text="View", command=view_contact)
button_view.pack(fill=tk.X)
button_delete = tk.Button(frame_buttons, text="Delete", command=delete_contact)
button_delete.pack(fill=tk.X)
frame_buttons.pack(side=tk.LEFT, padx=10)

root.mainloop()