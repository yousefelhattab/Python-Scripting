import requests
import os

def download_file(url, destination):
    response = requests.get(url)
    file_name = os.path.join(destination, url.split('/')[-1])
    with open(file_name, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded: {file_name}")


#download_file('https://file.kutubypdf.com/s/Sm7jodXd7GEya9i/download/SDFG5RD6GR6GERG56ERG.pdf', 'D:\\organized_files')
