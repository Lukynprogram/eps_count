import requests, time
import os
import subprocess

os.chdir("/var/log/collected")

previous_total_lines = 0

def run_command(command):
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    return result.stdout

while True:
    try:
        output = run_command("wc -lc *")
        total_lines = sum(int(line.split()[0]) for line in output.strip().split('\n') if 'total' not in line)
        eps = total_lines - previous_total_lines
        previous_total_lines = total_lines
        url = 'http://10.0.0.9:8000/'
        data = {
            'uid': 'customer4keystring',
            'value': f'{eps}'
        }
        # send data every second 
        response = requests.post(url=url, json=data)
        print("Status Code:", response.status_code)
        print("Server responded:", response.text)
        time.sleep(1)
        
    except:
        time.sleep(1)
        output = run_command("wc -lc *")
        total_lines = sum(int(line.split()[0]) for line in output.strip().split('\n') if 'total' not in line)
        eps = total_lines - previous_total_lines
        previous_total_lines = total_lines
        url = 'http://10.0.0.9:8000/'
        data = {
            'uid': 'customer4keystring',
            'value': f'{eps}'
        }
        # send data every second 
        response = requests.post(url=url, json=data)
        print("Status Code:", response.status_code)
        print("Server responded:", response.text)
        time.sleep(1)
