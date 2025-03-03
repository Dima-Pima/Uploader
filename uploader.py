import os
import sys
import requests
from threading import Lock

class WPAFileUploader:
    def __init__(self, api_key, file_path):
        self.api_key = api_key
        self.file_path = file_path
        self.lock = Lock()

    def upload_file(self, url="https://wpa-sec.stanev.org", timeout=30):
        if not os.path.exists(self.file_path):
            print(f"File not found: {self.file_path}")
            sys.exit(1)

        with open(self.file_path, 'rb') as file_to_upload:
            cookies = {'key': self.api_key}
            files = {'file': file_to_upload}

            try:
                response = requests.post(url, cookies=cookies, files=files, timeout=timeout)
                print(response.text)
            except requests.exceptions.RequestException as e:
                print(f"Error uploading file: {e}")
                sys.exit(1)

if name == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python uploader.py <api_key> <file_path>")
        sys.exit(1)

    api_key = sys.argv[1]
    file_path = sys.argv[2]
    uploader = WPAFileUploader(api_key, file_path)
    uploader.upload_file()
