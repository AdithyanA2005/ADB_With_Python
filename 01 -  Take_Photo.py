import time
from ppadb.client import Client as AdbClient


def connect():
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037
    devices = client.devices()

    if len(devices) == 0:
        print('No devices Found')
        quit()

    device = devices[0]
    print(f'Connected to {device}')
    return device, client

if __name__ == '__main__':
    device, client = connect()
    device.shell('input keyevent 27')  # open up camera app
    time.sleep(5)  # wait 5 seconds
    device.shell('input keyevent 24')  # take a photo with volume up
    print('Taken a photo!')
