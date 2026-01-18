
import subprocess
import sys


result = subprocess.run(['echo', "Hello world"], capture_output=True,
                        text=True)
print(f"{result.stdout}")

# Method 2: Run Python script in subprocess
code = """
import time
print("Subprocess starting")
time.sleep(2)
print("Subprocess finished")
"""

result = subprocess.run([sys.executable, '-c', code], capture_output=True,
                        text=True)
print(f"Subprocess output: {result.stdout}")

# Method 3: Using Popen for more control
process = subprocess.Popen(['ping', '-c', '4', 'google.com'], 
                          stdout=subprocess.PIPE, 
                          stderr=subprocess.PIPE,
                          text=True)

# Get output
stdout, stderr = process.communicate()
print(f"Return code: {process.returncode}")
print(f"Output: {stdout}")