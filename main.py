import argparse
import urlscan, VThashscan
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def ArgParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='checks urlscan for URL')
    parser.add_argument('--hash', help='checks VT hash')
    args = parser.parse_args()
    
    if args.hash:
        VThashscan.checkHash(args.hash, os.getenv('VTapiKey'))
    elif args.url:
        urlscan.checkURL(args.url, os.getenv('URLapikey'))

def main():
    configure()
    ArgParser()

if __name__ == '__main__':
    main()
    pass