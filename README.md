# A python script to prepare files for time-laps video. 
The input image (.jpg, .png,..) files must be in a format year-month-day_hour-minut-second (YYYY-MM-DD_hh-mm-ss). The output files have <new_name><count>.<jpg> format.

# Usage : python jpegSequence.py <path> <new_name.extension>

This script copies files present in the directory given by <path> and places the renamed files in a directory called "pic_folder" that will be created within <path>. The renamed files are ordered sequentially with a counter.
