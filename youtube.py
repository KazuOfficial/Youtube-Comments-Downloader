import sys
import requests
import argparse
import json

from bs4 import BeautifulSoup as bs

def main(argv):

    parser = argparse.ArgumentParser(add_help=False, description=('Youtube Comments Downloader made by Kazu'))
    parser.add_argument('--help', '-h', action='help', help='Show help message')
    parser.add_argument('--limit', '-l', type=int, default=5, help='Limit number of comments (default: 5)')
    parser.add_argument('--filetype', '-f', default="txt", help='Choose output file type: txt or json (default: txt)')
    args = parser.parse_args(argv)

    isTxt=False
    isJson=False
    limit = args.limit
    filetype = args.filetype

    if not (filetype=="txt" or filetype=="json"):
        print("Invalid file type! Must be txt or json.")
        quit()
    elif filetype=="txt":
        isTxt=True
    elif filetype=="json":
        isJson=True
        

    try:
        print("Welcome!")
        print("You can limit number of comments by using flag -l LIMIT (default: 5)")
        print("You can choose an output file type by using flag -f FILETYPE (txt/json) (default: txt)")
        print("If you want to exit the script type 'e' or 'exit'")
        print("Youtube video id example: in https://www.youtube.com/watch?v=dQw4w9WgXcQ id is dQw4w9WgXcQ")
        youtubelink = input("Insert a youtube video id: ")

        if(youtubelink=="e" or youtubelink=="exit"):
            quit()

        r = requests.get(url = "https://www.googleapis.com/youtube/v3/commentThreads?key=API_KEY&textFormat=plainText&part=snippet&videoId="+youtubelink+"&maxResults="+str(limit))
        print("Link is valid, processing...")
        print("Souping...")
        soup = bs(r.text,"lxml")
        print("Splitting...") 
        allLines = soup.text.split('\n')
        print("Writing out...")
        with open('output.' + filetype, 'w') as outfile:
            print("Dumping...")
            for line in allLines:
                json.dump(line, outfile)
                outfile.write("\n")
                if line.startswith('"') and line.endswith('"'):
                    line = line[1:-1]
        print("Successfully dumped to output." + filetype + "!")

    except ValueError:
        print("Insert a valid youtube link!")

if __name__ == "__main__":
    main(sys.argv[1:])