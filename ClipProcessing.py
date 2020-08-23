import os
from datetime import date

inputDir = ".\\clips\\new\\"
scaledDir = ".\\clips\\scaled\\"

def getClipPaths(clipDir):
  ret = []
  for clip in os.listdir(clipDir):
    ret.append(clip)
  return ret

def scaleVideo(clips):
  for clip in clips:
    os.system(f"ffmpeg -i {inputDir}{clip} -vcodec libx264 -s 1920x1080 -r 60" +
              f" -strict experimental ./clips/scaled/{clip}")

def exportVideo(clips):
  outputPath = "./videos/" + date.today().strftime("%d-%m-%Y") + ".mp4"
  inputFiles = ""
  filterComplex = ""

  for i, clip in enumerate(clips):
    inputFiles += f"-i {scaledDir}{clip} "
    filterComplex += f"[{i}:v:0][{i}:a:0]"

  command = f'ffmpeg {inputFiles}-filter_complex "{filterComplex}concat=n='
  command += f'{len(clips)}:v=1:a=1[outv][outa]" -map "[outv]" -map "[outa]" {outputPath}'

  os.system(command)

def deleteClips(pathList):
  for clip in pathList:
    os.remove(clip)

def processClips():
  clips = getClipPaths(inputDir)
  scaleVideo(clips)
  clips = getClipPaths(scaledDir)
  exportVideo(clips)
