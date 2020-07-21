import configparser
import requests 
import urllib3

config = configparser.ConfigParser()
config.read("config.ini")
twitch = config["Twitch"]

slug = ""

clip_info = requests.get("https://api.twitch.tv/helix/clips?id=WittyDirtyRaccoonFeelsBadMan").json()

print(clip_info)
#thumb_url = clip_info['data'][0]['thumbnail_url']
#mp4_url = thumb_url.split("-preview",1)[0] + ".mp4"
#out_filename = slug + ".mp4"

#print(mp4_url)