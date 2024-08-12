
"""
Script to interact with NASA's Astronomy Picture of the Day (APOD) API.
"""

import requests
import sys

KEY = 'aeKMT7dn7xRECWTcSO6M0LSyK8M7NOAAuQNHyK78'
NASA_URL = 'https://api.nasa.gov/planetary/apod?api_key=' + KEY

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

def main():
    apod_info = get_apod_info(apod_date='2022-01-25')
    if apod_info:
        apod_image_url = get_apod_image_url(apod_info)
        print(f"APOD Image URL: {apod_image_url}")

if __name__ == '__main__':
    main()
