import os
import re
import time
import sys

selected = ("DP-4" if len(sys.argv) <=1 else sys.argv[1])

xinput_list = "xinput_calibrator --list"

pattern = r'Pen+ (id)'

connected_devices = os.popen('xinput_calibrator --list')



connected_devices_text = connected_devices.read()

connected_devices.close()


print()

print("\033[0;36mstarting calibration process...")
print()
print("\033[0m")

text = ""


for t in range(20):
    for el in range(t):
        sys.stdout.write("\033[D")
    sys.stdout.write("\033[K")
    print(text, end="")
    text += "#"
    sys.stdout.flush()
    time.sleep(0.2)

print("\n"*2)



connected_devices_text = connected_devices_text.strip().split("\n")


for el in connected_devices_text:

    if re.search(r"Pen*", el):
        connected_devices_text = el
        break

#pen found
id_number = re.search(r'id=(\d+)', connected_devices_text).groups()[0]



if not id_number:
    print('\033[0;91no id found, aborting...')
    print("\033[0m")
    raise Exception("id number not found")

print('\033[0;92mid number found at '+id_number)
print("Starting formation...")
print("\033[0m")

os.system("xinput map-to-output "+id_number+ " " + selected)

print("Calibration succeeded")
