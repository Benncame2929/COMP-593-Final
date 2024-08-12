
"""
Library of useful functions for working with images.
"""

import requests
import ctypes

def download_image(image_url):
    """
    Downloads an image from a specified URL.

    DOES NOT SAVE THE IMAGE FILE TO DISK.

    Args:
        image_url (str): URL of image

    Returns:
        bytes: Binary image data, if successful. None, if unsuccessful.
    """
    print(f'Downloading image from {image_url}...', end=' ')
    resp_msg = requests.get(image_url)

    if resp_msg.status_code == requests.codes.ok:
        print('Success.')
        return resp_msg.content
    else:
        print('Fail.')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')
        return None

def save_image_file(image_data, image_path):
    """
    Saves image data as a file on disk.

    DOES NOT DOWNLOAD THE IMAGE.

    Args:
        image_data (bytes): Binary image data
        image_path (str): Path to save image file

    Returns:
        bool: True, if successful. False, if unsuccessful
    """
    try:
        print(f"Saving image file as {image_path}...", end=' ')
        with open(image_path, 'wb') as file:
            file.write(image_data)
        print("Success.")
        return True
    except Exception as e:
        print("Fail.")
        return False

def set_desktop_background_image(image_path):
    """
    Sets the desktop background image to a specific image.

    Args:
        image_path (str): Path of image file

    Returns:
        bool: True, if successful. False, if unsuccessful
    """
    print(f"Setting desktop to {image_path}...", end=' ')
    SPI_SETDESKWALLPAPER = 20
    result = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
    
    if result:
        print("Success.")
        return True
    else:
        print("Fail.")
        return False

def main():
    image_data = download_image('https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg')
    if image_data:
        save_image_file(image_data, r'C:\temp\kitty.jpg')

if __name__ == '__main__':
    main()
