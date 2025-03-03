# WPA File Uploader

## Overview
This script allows users to upload WPA handshake files to [WPA-sec](https://wpa-sec.stanev.org) for analysis. It takes an API key and a file path as arguments and uploads the specified file to the service.

## Requirements
- Python 3.x
- `requests` library (install with `pip install requests` if not already installed)

## Installation
Clone the repository or download the script:
```sh
 git clone https://github.com/your-repo/wpa-uploader.git
 cd wpa-uploader
```

## Usage
Run the script with the following command:
```sh
python uploader.py <api_key> <file_path>
```

### Arguments:
- `<api_key>`: Your API key for WPA-sec.
- `<file_path>`: Path to the WPA handshake file you want to upload.

### Example:
```sh
python uploader.py myapikey /path/to/handshake.cap
```

## Features
- Validates the file path before uploading.
- Uses a lock mechanism for thread safety.
- Handles request timeouts and errors gracefully.

## Error Handling
- If the file does not exist, the script will exit with an error message.
- If the upload request fails, it will print the error details and exit.

## License
This project is released under the MIT License.
