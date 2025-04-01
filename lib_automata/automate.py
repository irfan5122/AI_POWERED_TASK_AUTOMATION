import os
import re
def create_file(text):
	pattern = r'\b\w+\.\w+\b'
	filename_list = re.findall(pattern, text)
	filename = filename_list[0] if filename_list else None 
	
	if filename:
		os.system(f"nul > {filename}")  
		
	else:
		print("⚠ No filename found in text!")
    

def open_app(app_name):
	import pyautogui as gui
	gui.press('win')
	gui.write(f"{app_name}")
	gui.press("Enter")

def delete_file(text):
	pattern = r'\b\w+\.\w+\b'
	filename_list = re.findall(pattern, text)
	filename = filename_list[0] if filename_list else None 
	
	if filename:
		os.remove(filename)
		
	else:
		print("⚠ No filename found in text!")


def search(name,data):
	import pyautogui as gui
	import time
	gui.FAILSAFE = False
	index = data.find("search")
	if index != -1:
		search_text = data[index + len("search"):].strip()  
  
	time.sleep(1)
	gui.press("tab")
	gui.press("Enter")
	gui.write(f"{search_text}")
	gui.press("Enter")




def close_app(app_name):
    import psutil  
    app_aliases = {
        "taskmanager": "taskmgr.exe",
        "edge": "msedge.exe",
        "explorer": "explorer.exe",
        "filemanager":"explorer.exe",
        "fileexplorer":"explorer.exe",
        "word": "winword.exe",
        "excel": "excel.exe",
        "powerpoint": "powerpnt.exe",
    }

    try:
        # Read allowed app names from file
        with open("exe_names.txt", "r", encoding="utf-8") as file:
            app_names = {line.strip().lower() for line in file if line.strip()}  # Set for fast lookup
    except FileNotFoundError:
        print("❌ Error: exe_names.txt not found!")
        return  # Exit if file is missing

    app_name = app_name.lower()  # Normalize input

    # Convert alias name to the actual process name if available
    if app_name in app_aliases:
        app_name = app_aliases[app_name]

    # Append `.exe` if not in list but with `.exe` version in the file
    if app_name not in app_names:
        app_name_with_exe = app_name + ".exe"
        if app_name_with_exe in app_names:
            app_name = app_name_with_exe
        else:
            print(f"⚠️ Warning: {app_name} is not in exe_names.txt!")
            return  # Exit if app is not in the allowed list

    # Iterate through running processes
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        try:
            if proc.info['name'].lower() == app_name:
                print(f"✅ {app_name} is running with PID: {proc.info['pid']}")

                # Terminate the process
                psutil.Process(proc.info['pid']).terminate()
                print(f"❌ {app_name} has been terminated.")

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue  # Skip inaccessible or terminated processes
        
def shutdown_system():
    from tkinter import messagebox,Tk
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)  # Ensures the message box appears on top

    response = messagebox.askyesno("Shutdown Confirmation", "Are you sure you want to shut down?")
    
    if response:
        os.system("shutdown /s /t 0")
