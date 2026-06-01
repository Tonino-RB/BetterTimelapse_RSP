import os
import time

# Consumer control HID report for Volume Up
VOLUME_UP = bytes([0x00, 0xE9])
RELEASE = bytes([0x00, 0x00])

hid = "/dev/hidg0"

if not os.path.exists(hid):
    print("Missing /dev/hidg0")
    print("HID gadget not configured")
    exit(1)

with open(hid, "wb") as fd:
    print("Sending Volume Up")

    fd.write(VOLUME_UP)
    time.sleep(0.1)

    fd.write(RELEASE)

print("Done")
