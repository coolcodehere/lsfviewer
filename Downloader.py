import configparser
import requests 
import urllib.request

config = configparser.ConfigParser()
config.read("config.ini")
twitch = config["Twitch"]
authResponse = requests.post(f"https://id.twitch.tv/oauth2/token?client_id={twitch['clientID']}&client_secret={twitch['clientSecret']}&grant_type=client_credentials").json()
token = authResponse["access_token"]
outputFolderPath = "E:\\projects\\video-automation\\clips\\new"

def downloadClip(slug):
  outputFile = outputFolderPath + "\\" + slug + ".mp4"
  clip_info = requests.get("https://api.twitch.tv/helix/clips?id=" + slug, headers={"Client-ID": twitch['clientID'], "Authorization": f"Bearer {token}"}).json()

  try:
    thumb_url = clip_info['data'][0]['thumbnail_url']
    mp4_url = thumb_url.split("-preview",1)[0] + ".mp4"
    urllib.request.urlretrieve(mp4_url, outputFile)
    return True
  except:
    print("Bad URL")  
    return False