import argparse
import requests


def download_file(url , fn):
    local_filename = fn
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename



parser=argparse.ArgumentParser()



parser.add_argument("url", help="Enter url of file to download")
parser.add_argument("file_name", help="Enter Name of file")



args=parser.parse_args()
download_file(args.url , args.file_name)