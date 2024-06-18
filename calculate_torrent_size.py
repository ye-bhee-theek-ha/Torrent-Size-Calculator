import os
import bencodepy

def calculate_total_size(torrent_file):
    with open(torrent_file, 'rb') as f:
        metadata = bencodepy.decode(f.read())

    if b'info' in metadata:
        info = metadata[b'info']

        if b'files' in info:
            # Multi-file torrent
            total_size = 0
            files_info = []
            for file in info[b'files']:
                file_size = file[b'length']
                files_info.append((file[b'path'], file_size))
                total_size += file_size
        else:
            # Single file torrent
            total_size = info[b'length']
            files_info = [(info[b'name'], total_size)]

        return total_size, files_info
    else:
        raise ValueError('Invalid .torrent file format.')

def process_torrent_directory(directory):
    total_directory_size = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.torrent'):
                torrent_file = os.path.join(root, file)
                try:
                    total_size, files_info = calculate_total_size(torrent_file)
                    print(f"Torrent file: {torrent_file}")
                    print(f"Total size of downloaded files: {total_size} bytes")

                    if files_info:
                        print("Individual file sizes:")
                        for filename, size in files_info:
                            print(f"{filename.decode('utf-8')}: {round(size/1024**3 , 2)} bytes")
                    
                    total_directory_size += total_size
                    print("\n")
                    print("-" * 40)
                    print("\n")
                except Exception as e:
                    print(f"Error processing {torrent_file}: {e}")
                    print("-" * 40)
    
    print(f"Total size of downloaded files in directory: {round(total_directory_size/1024**3 , 2)} gb")

def main():
    directory = './../'
    process_torrent_directory(directory)

if __name__ == "__main__":
    main()
