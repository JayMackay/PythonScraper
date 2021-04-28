import csv
import json
import argparse

#Set formatting terminal commands input & output
parser = argparse.ArgumentParser(description = "Clean TikTok raw data")
parser.add_argument("-i", "--inputFile", help = "Input name of file.csv", required = True, default = "tiktokdata.csv")
parser.add_argument("-o", "--outputFile", help = "Output name of file.csv", required = True, default = "cleanedtiktokdata.csv")
args = parser.parse_args()

#Set header titles
header = ["Username",
        "Video Title",
        "Followers",
        "Total Number of Videos",
        "Video Music Artist",
        "Video URL",
        "Share Count",
        "Play Count",
        "Hashtags"]

#Create parsed data file and write new headers
with open(args.outputFile, "a", encoding = "UTF-8", newline = "") as b:
    cleanData = csv.writer(b)
    cleanData.writerow(header)

#Open and return raw data file
with open(args.inputFile, encoding = "UTF-8") as a:
    rawData = csv.reader(a)
    next(rawData)

#Declare column raw data being parsed 
    for i in rawData:
        username = i[6]
        videoTitle = i[2]
        followerCount = i[12]
        totalVideoCount = i[14]
        videoMusicArtist = i[18]
        videoURL = i[29]
        shareCount = i[37]
        playCount = i[38]
        rawHashtags = str(i[42])
        hashtags = ""

#Format hashtags
        try:
            tags = json.loads(rawHashtags)

            for n in tags:
                try:
                    hashtags += "#" + n["name"] + " "
                except:
                    pass
        except:
            pass
        
#Write raw data to parsed data
        with open(args.outputFile, "a", encoding = "UTF-8", newline = "") as b:
            writer = csv.writer(b)
            writer.writerow([username, videoTitle, followerCount, totalVideoCount, videoMusicArtist, videoURL, shareCount, playCount, hashtags])
