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


def search(name):
	import pyautogui as gui
	gui.press('win')
	gui.write(f"{name}")