import tkinter as tk
from tkinter import Entry, Label, Button

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window properties
        self.title("Login")
        self.geometry("400x250")
        self.configure(bg="black")  # Black background

        # Username label
        self.username_label = Label(self, text="USERNAME :", font=("Arial", 14, "bold"), fg="cyan", bg="black")
        self.username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        # Username entry field
        self.username_entry = Entry(self, font=("Arial", 12), fg="black", bg="white", width=20)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        # Password label
        self.password_label = Label(self, text="PASSWORD:", font=("Arial", 14, "bold"), fg="cyan", bg="black")
        self.password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        # Password entry field
        self.password_entry = Entry(self, font=("Arial", 12), fg="black", bg="white", width=20, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        # Login button
        self.login_button = Button(self, text="LOGIN", font=("Arial", 12, "bold"), fg="red", bg="#222", width=10, borderwidth=0, command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=20)

    def login(self):
        # Dummy function for login logic (can be extended)
        print(f"Username: {self.username_entry.get()}")
        print(f"Password: {self.password_entry.get()}")

if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()