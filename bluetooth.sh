#!/bin/bash

bluetooth_disconnect() {
   # MAC address of the Bluetooth device to disconnect
   DEVICE_MAC="AC:3E:B1:9B:54:47"

   # Start bluetoothctl, then disconnect the device, and finally quit
   echo -e "disconnect $DEVICE_MAC\nquit" | bluetoothctl

   echo "Device $DEVICE_MAC disconnected."
}

bluetooth_connect() {
   # MAC address of the Bluetooth device to disconnect
   DEVICE_MAC="AC:3E:B1:9B:54:47"

   # Start bluetoothctl, then disconnect the device, and finally quit
   echo -e "connect $DEVICE_MAC\nquit" | bluetoothctl

   echo "Device $DEVICE_MAC connected."
}

# works
# bluetooth_disconnect
bluetooth_connect
