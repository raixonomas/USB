import usb.core
import usb.util

device = usb.core.find(idVendor=0x0079, idProduct=0x0006)
endpoint = device[0].interfaces()[0].endpoints()[0]
interface = device[0].interfaces()[0].bInterfaceNumber

print(endpoint)
print(interface)

#device.set_configuration()
endpaddr = endpoint.bEndpointAddress

if device.is_kernel_driver_active(interface):
    device.detach_kernel_driver(interface)


list_len = 8

while True:
    joy_data_1_from_usb = []

    joy1_axes = [0, 0, 0, 0]
    joy1_buttons = [0]

    read = device.read(endpaddr, 8)

    for i in range(list_len):
        joy_data_1_from_usb.append(read[i])

    joy_data_1_from_usb = joy_data_1_from_usb[1:7]

    read = device.read(endpaddr, 8)
    #print(joy_data_1_from_usb)
    print(joy_data_1_from_usb)

    if joy_data_1_from_usb[0] == 127:
        #print("center")
        1
    elif joy_data_1_from_usb[0] < 127:
        #print("up")
        1
    elif joy_data_1_from_usb[0] > 127:
        #print("down")
        1


    if joy_data_1_from_usb[4] == 31:  # UP
        #print("clicked")
        1
    elif joy_data_1_from_usb[4] == 4:  # DOWN
        #print("not clicked")
        1

