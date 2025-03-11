import tkinter as tk
from tkinter import ttk

def on_voice_mode():
    print("Voice mode activated")

def on_send():
    task = entry.get()
    print(f"Task entered: {task}")

# Create main window
root = tk.Tk()
root.title("Voice Mode UI")
root.geometry("600x400")
root.configure(bg="white")

# Create border frame
border_frame = tk.Frame(root, bg="red", bd=2)
border_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Inside frame for content
content_frame = tk.Frame(border_frame, bg="white")
content_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Voice mode button
voice_button = tk.Button(content_frame, text="VOICE\nMODE", font=("Arial", 16, "bold"), fg="red", bg="white", bd=2, relief="solid", command=on_voice_mode)
voice_button.place(relx=0.5, rely=0.4, anchor="center", width=120, height=120)

# Entry field
entry_frame = tk.Frame(content_frame, bg="red", bd=2)
entry_frame.place(relx=0.5, rely=0.8, anchor="center", width=400, height=40)

entry = tk.Entry(entry_frame, font=("Arial", 12), fg="red", bg="white", bd=0)
entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(5, 0))
entry.insert(0, "Enter the task here")

def clear_placeholder(event):
    if entry.get() == "Enter the task here":
        entry.delete(0, tk.END)

def restore_placeholder(event):
    if not entry.get():
        entry.insert(0, "Enter the task here")

entry.bind("<FocusIn>", clear_placeholder)
entry.bind("<FocusOut>", restore_placeholder)

# Send button
send_button = tk.Button(entry_frame, text="➡", font=("Arial", 12, "bold"), fg="red", bg="white", bd=0, command=on_send)
send_button.pack(side=tk.RIGHT, padx=5)

root.mainloop()
