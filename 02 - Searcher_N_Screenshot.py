import time

from ppadb.client import Client as AdbClient

def connect():
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037
    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]
    print(f'Connected to {device}')
    return device, client

if __name__ == '__main__':
    device, client = connect()
    search_bar = '450 150 '  # Location of search_bar(x, y)
    query = input('What word do you want to search for: ')

    device.shell('input keyevent 64')  # Open Browser
    time.sleep(3)  # Wait for browser to load
    device.shell(f"input tap {search_bar}")  # Click on the Searchbar
    device.shell(f"input text '{query}'")  # Put the text in the bar
    device.shell('input keyevent 66')  # Click enter button to search
    time.sleep(3) # wait for results to load


    screenshot = device.screencap()  # Taking screenshot

    with open('result.png', 'wb') as f: # save the screenshot as result.png
        f.write(screenshot)
        print('Saved screenshot!')
