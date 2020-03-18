import sys
import requests
import argparse

def main(argv):
    parser = argparse.ArgumentParser(add_help=False, description=('Youtube Comments Downloader made by Kazu'))
    parser.add_argument('--help', '-h', action='help', help='Show help message')
    parser.add_argument('--limit', '-l', type=int, default=100, help='Limit number of comments')
    args = parser.parse_args(argv)

    limit = args.limit

    try:
        print("Welcome!")
        youtubelink = input("Insert a youtube link to the video: ")
        #CTRL-X = exit
        #iflimitisstring - error message
        print("Link is valid, processing...")
        r = requests.get(url = youtubelink) 
        data = print(r.text)
    except ValueError:
        print("Insert a valid youtube link!")

if __name__ == "__main__":
    main(sys.argv[1:])