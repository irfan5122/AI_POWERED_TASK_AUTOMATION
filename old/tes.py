import psutil

app_name = "whatsapp.exe"

for proc in psutil.process_iter(attrs=['pid', 'name']):
    try:
        if proc.info['name'].lower() == app_name:
            print(f"{app_name} is running with PID: {proc.info['pid']}")
            
            # Terminate the process
            psutil.Process(proc.info['pid']).terminate()
            print(f"{app_name} has been terminated.")

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        continue
