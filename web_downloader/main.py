import yt_dlp
import sys
try:
    import ctools
except:
    print("it returbsn an error")

def main():
    yt_dlp_options = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": "%(title)s.%(ext)s",
            }
    url = "https://www.youtube.com/watch?v=Vrn7Nb6SYwE"
    yt_dlp.YoutubeDL(yt_dlp_options).download(url)
    print("Success")

if __name__ == "__main__":
    try:
        if sys.argv[1]:
           pass 
    except:
        main()

