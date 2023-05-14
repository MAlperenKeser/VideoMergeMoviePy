from moviepy.editor import *
import os

# list of videos
print("enter file count")
size = input()
sizeint = int(size)

print("enter file names in order you want to merge")
strs = [input() for i in range(sizeint)]

# Create a new video
def color_clip(size, duration, fps=60, color=(0,0,0), output='color.mp4'):
    ColorClip(size, color, duration=duration).write_videofile(output, fps=fps)


x = int(0)
y = int(1)
# write file names in black screen with white font
while(x<sizeint):

    size = (1920, 1080)
    duration = 1
    color_clip(size, duration)

    c=VideoFileClip("color.mp4")
    c.ipython_display()

    text = TextClip(strs[x],fontsize=40,color="white").set_position(("center")).set_duration(1)
    finalcomp = CompositeVideoClip([c,text])
    finalcomp.ipython_display()
    clip1 = VideoFileClip("__temp__.mp4")
    clip2 = VideoFileClip(strs[x])
    temp = concatenate_videoclips([clip1,clip2])
    y = str(y)
    temp.write_videofile("temp" + y + ".mp4")
    y = int(y)
    x = x + 1
    if(x<sizeint):
        y = y + 1


clips = [0] * sizeint
j = int(1)

#Concatenate to the new video
for i in range(len(strs)):
    j = str(j)
    clipout = VideoFileClip("temp"+ j +".mp4")
    clips[i] = clipout
    j = int(j)
    j = j + 1

out = concatenate_videoclips(clips)
out.write_videofile("output.mp4")

#remove temporary mp4 files
while(y>0):
    y = str(y)
    os.remove("temp"+ y + ".mp4")
    y = int(y)
    y = y - 1
os.remove("__temp__.mp4")
os.remove("color.mp4")



print("do you want to change the start time(y/n)")
answer = input()
if(answer == "y"):
    print("from what second you want to play mp4 file")
    start_time = input()
    start_time = int(start_time)
    clipduration = VideoFileClip("output.mp4")

    clipsubclip = VideoFileClip("output.mp4")
    clipsubclip = clipsubclip.subclip(start_time,clipduration.duration)
    clipsubclip.ipython_display()

    os.rename("__temp__.mp4", "SubclippedOutput.mp4")

