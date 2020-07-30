import RedditParser
import Downloader

posts = RedditParser.getDailyTopPosts(30)
print([x.url for x in posts])
clipCount = 0
for post in posts:
  print(post.url)
  post = post.url.split("/")[3].split("?")[0]
  
  if Downloader.downloadClip(post):
    clipCount += 1
  if clipCount == 20:
    break


  
  


