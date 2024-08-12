
"""
NASA APOD Desktop - Fetches APOD info, downloads the image, and sets it as the desktop background.
"""

import requests
import ctypes

NASA_URL = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'

def get_apod_info(apod_date):
    """
    Gets information from the NASA API for the Astronomy Picture of the Day (APOD) from a specified date.

    Args:
        apod_date (str): APOD date formatted as YYYY-MM-DD

    Returns:
        dict: Dictionary of APOD info, if successful. None if unsuccessful
    """
    params = {
        'date': apod_date,
        'thumbs': True,
    }

    resp_msg = requests.get(NASA_URL, params=params)

    if resp_msg.ok:
        print('Success.')
        return resp_msg.json()
    else:
        print('Fail.')
        print(f'Status code: {resp_msg.status_code} ({resp_msg.reason})')
        return None

def get_apod_image_url(apod_info_dict):
    """
    Gets the URL of the APOD image from the dictionary of APOD information.

    Args:
        apod_info_dict (dict): Dictionary of APOD info from API

    Returns:
        str: APOD image URL
    """
    if apod_info_dict.get('media_type') == 'image':
        return apod_info_dict.get('hdurl')
    elif apod_info_dict.get('media_type') == 'video':
        return apod_info_dict.get('thumbnail_url')
    return None

def download_image(image_url):
    """
    Downloads an image from a specified URL.

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
    apod_info = get_apod_info(apod_date='2022-01-25')
    if apod_info:
        apod_image_url = get_apod_image_url(apod_info)
        if apod_image_url:
            image_data = download_image(apod_image_url)
            if image_data:
                image_path = r'C:\temp\apod.jpg'
                if save_image_file(image_data, image_path):
                    set_desktop_background_image(image_path)

if __name__ == '__main__':
    main()
