import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import re

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name}, {self.phone}, {self.email}, {self.address}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def get_all_contacts(self):
        return self.contacts

    def search_contact(self, search_term):
        results = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, original_name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name == original_name:
                self.contacts[i] = new_contact
                return True
        return False

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                return True
        return False

class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.center_window(self.root, 600, 600)
        self.manager = ContactManager()
        
        self.country_codes = {
            "Canada (+1)": "+1",
            "Morocco (+212)": "+212",
            "France (+33)": "+33",
            "UK (+44)": "+44",
            "India (+91)": "+91"
        }
        
        self.create_widgets()

    def create_widgets(self):
        
        self.add_frame = tk.Frame(self.root)
        self.add_frame.pack(pady=10)

        tk.Label(self.add_frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.add_frame, width=40)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.add_frame, text="Phone").grid(row=1, column=0, padx=5, pady=5)
        self.phone_combo = ttk.Combobox(self.add_frame, values=list(self.country_codes.keys()), width=37)
        self.phone_combo.grid(row=1, column=1, padx=5, pady=5)
        self.phone_combo.current(0)
        self.phone_entry = tk.Entry(self.add_frame, width=40)
        self.phone_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.add_frame, text="Email").grid(row=3, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.add_frame, width=40)
        self.email_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.add_frame, text="Address").grid(row=4, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.add_frame, width=40)
        self.address_entry.grid(row=4, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.add_frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=5, columnspan=2, pady=10)

        
        self.view_button = tk.Button(self.root, text="View All Contacts", command=self.view_contacts)
        self.view_button.pack(pady=5)

       
        self.search_frame = tk.Frame(self.root)
        self.search_frame.pack(pady=10)

        tk.Label(self.search_frame, text="Search").grid(row=0, column=0, padx=5, pady=5)
        self.search_entry = tk.Entry(self.search_frame, width=40)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5)

        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_contact)
        self.search_button.grid(row=0, column=2, padx=5, pady=5)

        
        self.results_listbox = tk.Listbox(self.root)
        self.results_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        
        self.update_button = tk.Button(self.root, text="Update Selected Contact", command=self.update_contact_window)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Selected Contact", command=self.delete_contact)
        self.delete_button.pack(pady=5)

    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def validate_phone(self, phone):
        return phone.isdigit() and 7 <= len(phone) <= 15

    def add_contact(self):
        name = self.name_entry.get()
        country = self.phone_combo.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        country_code = self.country_codes.get(country, "")

        if name and phone and email and address:
            if not self.validate_email(email):
                messagebox.showerror("Error", "Invalid email format!")
                return
            if not self.validate_phone(phone):
                messagebox.showerror("Error", "Invalid phone number!")
                return

            full_phone = country_code + phone
            contact = Contact(name, full_phone, email, address)
            self.manager.add_contact(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "All fields are required!")

    def view_contacts(self):
        self.results_listbox.delete(0, tk.END)
        for contact in self.manager.get_all_contacts():
            self.results_listbox.insert(tk.END, str(contact))

    def search_contact(self):
        search_term = self.search_entry.get()
        self.results_listbox.delete(0, tk.END)
        results = self.manager.search_contact(search_term)
        for contact in results:
            self.results_listbox.insert(tk.END, str(contact))

    def update_contact_window(self):
        selected = self.results_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No contact selected!")
            return

        original_name = self.results_listbox.get(selected[0]).split(",")[0]
        for contact in self.manager.contacts:
            if contact.name == original_name:
                name, phone, email, address = contact.name, contact.phone, contact.email, contact.address
                break

        update_window = tk.Toplevel(self.root)
        update_window.title("Update Contact")
        self.center_window(update_window, 350, 200)

        tk.Label(update_window, text="Name").grid(row=0, column=0, padx=5, pady=5)
        name_entry = tk.Entry(update_window, width=40)
        name_entry.grid(row=0, column=1, padx=5, pady=5)
        name_entry.insert(0, name)

        tk.Label(update_window, text="Phone").grid(row=1, column=0, padx=5, pady=5)
        phone_combo = ttk.Combobox(update_window, values=list(self.country_codes.keys()), width=37)
        phone_combo.grid(row=1, column=1, padx=5, pady=5)

        selected_country = None
        for country, code in self.country_codes.items():
            if phone.startswith(code):
                selected_country = country
                break

        if selected_country:
            phone_combo.set(selected_country)
            phone_number = phone[len(self.country_codes[selected_country]):]
        else:
            phone_combo.current(0)
            phone_number = phone

        phone_entry = tk.Entry(update_window, width=40)
        phone_entry.grid(row=2, column=1, padx=5, pady=5)
        phone_entry.insert(0, phone_number)

        tk.Label(update_window, text="Email").grid(row=3, column=0, padx=5, pady=5)
        email_entry = tk.Entry(update_window, width=40)
        email_entry.grid(row=3, column=1, padx=5, pady=5)
        email_entry.insert(0, email)

        tk.Label(update_window, text="Address").grid(row=4, column=0, padx=5, pady=5)
        address_entry = tk.Entry(update_window, width=40)
        address_entry.grid(row=4, column=1, padx=5, pady=5)
        address_entry.insert(0, address)

        def save_updates():
            new_name = name_entry.get()
            new_phone = phone_entry.get()
            new_email = email_entry.get()
            new_address = address_entry.get()
            new_country_code = self.country_codes.get(phone_combo.get(), "")

            if new_name and new_phone and new_email and new_address:
                if not self.validate_email(new_email):
                    messagebox.showerror("Error", "Invalid email format!")
                    return
                if not self.validate_phone(new_phone):
                    messagebox.showerror("Error", "Invalid phone number!")
                    return

                full_phone = new_country_code + new_phone
                new_contact = Contact(new_name, full_phone, new_email, new_address)
                if self.manager.update_contact(original_name, new_contact):
                    messagebox.showinfo("Success", "Contact updated successfully!")
                    self.view_contacts()
                    update_window.destroy()
                else:
                    messagebox.showerror("Error", "Failed to update contact.")
            else:
                messagebox.showerror("Error", "All fields are required!")

        save_button = tk.Button(update_window, text="Save", command=save_updates)
        save_button.grid(row=5, columnspan=2, pady=10)


    def delete_contact(self):
        selected = self.results_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No contact selected!")
            return

        name = self.results_listbox.get(selected[0]).split(",")[0]
        if self.manager.delete_contact(name):
            messagebox.showinfo("Success", "Contact deleted successfully!")
            self.view_contacts()
        else:
            messagebox.showerror("Error", "Failed to delete contact.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.phone_combo.current(0)

    def center_window(self, window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f'{width}x{height}+{x}+{y}')

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()
