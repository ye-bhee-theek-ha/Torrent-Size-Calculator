# Torrent Size Calculator

## Overview
This Python script calculates the total size of downloaded files from `.torrent` files within a specified directory. It also provides detailed information about individual file sizes within each torrent.

## Features
- Recursively scans a directory and its subdirectories for `.torrent` files.
- Parses `.torrent` files using the `bencodepy` library to extract file size information.
- Displays the total size of downloaded files for each torrent.
- Lists individual file sizes for multi-file torrents.
- Handles errors gracefully and provides informative error messages.

## Requirements
- Python 3.x
- `bencodepy` library (install via `pip install bencode.py`)

## Usage
1. Clone the repository or download the script file (`calculate_torrent_size.py`).
2. Install the required `bencodepy` library if not already installed:
3. Open a terminal or command prompt.
4. Navigate to the directory containing `calculate_torrent_size.py`.
5. Run the script with the following command:
6. 6. The script will prompt you to enter the path to the directory containing your `.torrent` files.
7. It will then display the total size of downloaded files and individual file sizes for each torrent found.

## Example
Suppose you have a directory `~/Downloads/Torrents/` containing various `.torrent` files. Running the script will provide output similar to:
Torrent file: /path/to/your/torrent/file.torrent
Total size of downloaded files: 1234.56 bytes

Individual file sizes:
file1.txt: 567.89 bytes
file2.jpg: 666.77 bytes
Total size of downloaded files in directory: 1234.56 bytes


## Notes
- Ensure that the `.torrent` files in your directory adhere to the BitTorrent specification for accurate parsing.
- Adjust the script or handle exceptions as needed for specific edge cases or non-standard torrent files.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
