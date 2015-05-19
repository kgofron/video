# A python script to prepare files for time-laps video. The input image (.jpg, .png,..) files must be in a format year-month-day_hour-minut-second (YYYY-MM-DD_hh-mm-ss). The output files have <new_name><count>.<jpg> format.

# Usage : python rename.py <path> <new_name.extension>

# This script copies files present in the directory given by <path> and places the renamed files in a directory called "pic_folder" that will be created within <path>. The renamed files are ordered sequentially with a counter.

# Example : Python rename.py /home/haris/pictures/tour/ tour.jpg
# Output : tour1.jpg, tour2.jpg, etc.
# FIXME
# -----

# K. Gofron, BNL, NSLS2 control group.
# 2014-2-5

import shutil
import os
import sys

#Checking whether path and filename are given.
if len(sys.argv) != 3:
    print "Usage : python rename.py <path> <new_name.extension>"
    sys.exit()

#Splitting name and extension.
name = sys.argv[2].split('.')
if len(name) < 2:
    name.append('')
else:
    name[1] = ".%s" %name[1]

#To name starting from 1 to number_of_files.
count = 1
    
#Creating a new folder in which the renamed files will be stored.
s = "%s/pic_folder" % sys.argv[1]
try:
    os.mkdir(s)
except OSError:
    #If pic_folder is already present, use it.
    pass

try:
    for fName in sorted(os.listdir(sys.argv[1])):
#        if fName.endswith(".jpg") and (count < 1180):
        if fName.endswith(".jpg"):
#        if fName.endswith(".jpg") or fName.endswith(".png"):
#            print fName, fName[0],fName[1],fName[2],fName[3],fName[4],fName[5],fName[6],fName[7],count 
            img_name, img_ext = fName.split('.')
            img_date, img_time = img_name.split('_')
            img_day = img_date.split('-')
            img_sec = img_time.split('-')
#            print img_day[0], img_day[1], img_day[2],img_sec[0],img_sec[1],img_sec[2]
# Select images from the day between 9:00am and 8:00pm            
            if ((int(img_sec[0]) > 6) and (int(img_sec[0]) < 19)):
                src_img = "%s/%s"  %(sys.argv[1], fName)
                countStr = "%06d" % count
#               print countStr
                dest_img = "%s/%s%s%s" %(s, name[0], countStr, name[1])
#               print fName, s, count, src_img, dest_img
                shutil.copyfile(src_img,dest_img)
                count = count + 1
except OSError:
    pass

try:
#    Create video
#    avconv -r 1 -i img%d.jpg -r 24 -s 704x480 -vsync cfr video.mpg
#    avconv -r 10 -i img%d.jpg -b:v 1000k test.mp4 
#    mkVideo= r"avconv -r 30 -i hxn-cam1/pic_folder/img%d.jpg -r 30 -s 704x480 -vsync cfr video.mp4"
 
    str1= "avconv -r 30 -i %s/" %(s)
    str2= r"img%06d.jpg -r 30 -s 704x480 -vsync cfr video.mp4"
    mkVideo = str1 + str2
    print mkVideo
    os.system(mkVideo)
##    os.system("avconv -r 30 -i hxn-cam1/pic_folder/img%d.jpg -r 30 -s 704x480 -vsync cfr video.mp4")
except OSError:
    #If video.mp4 is already present, overwrite it.
    pass
