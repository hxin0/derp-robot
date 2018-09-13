# ch2Pinyin.py
# Rename filename from Chinese characters to capitalized pinyin using the
# mapping file and taking out the tone numbers.  
 
import os
import re
 
def processDirectory(args, dirname, filenames):
    print dirname
    os.chdir(dirname)   # Rename all files in sub folder %dirname
    myulist = os.listdir(u'.')  # Read all file names in unicode mode
 
    for x in myulist:   # Each file name
        filenamePY = ''
        for y in x:     # Each character
            if 0x4e00 <= ord(y) <= 0x9fff:  # Chinese Character Unicode range
                # Strip leading '0x' and change the rest to uppercase:
                hexCH = (hex(ord(y))[2:]).upper()
                # Define the match pattern:
                p = re.compile(hexCH+'\t([a-z]+)[\d]*')
                mp = p.search(wf)
                # Get the pinyin without tone number and capitalize it.  
                filenamePY+=mp.group(1).title() # Adding a space between each word: add "+ ''"
            else:
                filenamePY+=y
        print " " * 4 + x
        Nfilename = filenamePY
        print " " * 6 + Nfilename
        os.rename(x, Nfilename)
 
# File Uni2Pinyin is a mapping from hex to Pinyin with a tone number.  
f = open('Uni2Pinyin')
wf = f.read()   # Read the whole mapping file
 
base_dir = 'D:\\Chinese to PinYin\\Chinese to Pinyin Song\\'
os.path.walk(base_dir, processDirectory, None)
