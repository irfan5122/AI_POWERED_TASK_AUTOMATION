#@Author : AHMED IRFAN N
import sys
import spacy,cryptography,PyQt6,pyautogui,pip
from importlib.metadata import version

#versions
pyqt_ver_o =  '6.8.1' 
spacy_ver_o = '3.8.4'
crypt_ver_o = '44.0.2'
pyauto_ver_o= '0.9.54'

python_ver_o = '3.11.4'
pip_ver_o = '24.0'
check = 0

python_ver = sys.version.split()[0]
pyqt_ver =  version("PyQt6")
spacy_ver = spacy.__version__
crypt_ver = cryptography.__version__
pyauto_ver = pyautogui.__version__
pip_ver = pip.__version__

if python_ver_o == python_ver:

	if pip_ver_o == pip_ver:
		print("PIP Version (Verified)")
		check+=1
	else:
		print(f"PIP incorrect version detected version : {pip_ver} , downgrade to {pip_ver_o}")	

	if pyqt_ver_o == pyqt_ver:
		print("PyQt6 Version (Verified)")
		check+=1
	else:
		print(f"PyQt6 incorrect version detected version : {pyqt_ver} , downgrade to {pyqt_ver_o}")


	if spacy_ver_o == spacy_ver:
		print("spacy Version (Verified)")
		check+=1
	else:
		print(f"spacy incorrect version detected version : {spacy_ver} , downgrade to {spacy_ver_o}")


	if crypt_ver_o == crypt_ver:
		check+=1
		print("cryptography Version (Verified)")
	else:
		print(f"cryptography incorrect version detected version : {crypt_ver} , downgrade to {crypt_ver_o}")


	if pyqt_ver_o == pyqt_ver:
		check+=1
		print("pyautogui Version (Verified)")
	else:
		print(f"pyautogui incorrect version detected version : {pyqt_ver} , downgrade to {pyqt_ver_o}")

else:
	print(f"Incorrect Python Version detected , version {python_ver} , install {python_ver_o}")


if check == 0:
	print("Fix Python Version")

elif check == 5:
	print("All packages checked succefully , you are ready to go")


else:
	print("Install correct package versions, to avoid bugs")