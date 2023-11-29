import moviepy.editor as moviepy
#import neccesary libraries

video = "Enter your orignal video file path"
#get the path of the original .mov file

clip = moviepy.VideoFileClip(video)
clip.write_videofile('new_vid.mp4')
#process the original video to a new .mp4 file
