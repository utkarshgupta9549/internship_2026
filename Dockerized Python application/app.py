import sys
from datetime import datetime

print("=" * 50)
print("Dockerized Python Application")
print("=" * 50)

print(f"Python Version : {sys.version}")
print(f"Current Date   : {datetime.now().strftime('%d-%m-%Y')}")
print(f"Current Time   : {datetime.now().strftime('%H:%M:%S')}")

print("=" * 50)