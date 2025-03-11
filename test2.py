import customtkinter as ctk

def on_send(event=None):  # Add event parameter for key binding
    message = task_entry.get()
    if message == "":
        print("No message")
    else:
        print(message)

# Create window
app = ctk.CTk()
app.geometry("800x500")
app.title("AI Task Automation")
app.configure(fg_color="black")

# Circle Voice Mode Button
voice_button = ctk.CTkButton(app, text="VOICE MODE", width=200, height=200, corner_radius=100, fg_color="red", text_color="black", font=("Arial", 30))
voice_button.place(relx=0.5, rely=0.4, anchor="center")

# Task Entry Box
task_entry = ctk.CTkEntry(app, placeholder_text="Enter the task here", width=500, height=50, corner_radius=25, fg_color="black", text_color="cyan", border_color="red", border_width=2)
task_entry.place(relx=0.5, rely=0.8, anchor="center")

# Bind the Enter key to the entry box
task_entry.bind("<Return>", on_send)

# Send Button
send_button = ctk.CTkButton(app, text="➤", width=50, height=50, corner_radius=25, fg_color="grey", text_color="cyan", command=on_send)
send_button.place(relx=0.75, rely=0.8, anchor="center")

app.mainloop()
