import cv2

import os

import sys
import numpy as np
#from skimage import io
import glob

input_path = sys.argv [1]
output_path = sys.argv[2]

size = 100,60

print "hello to test"
def process(input_path,output_path):
    print os.path.join(input_path)
    for f in glob.glob(os.path.join(input_path)):
        print "hello"
        print ("process files : {}".format(f))
        img = cv2.imread(f)
    files = [f for f in os.listdir(input_path) if  f.endswith(".png") or f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".BMP") or f.endswith("*.bmp")]
    #print files
    i =0
    for f in files:
        i = i+1
        outfile = os.path.join(output_path,os.path.splitext(f)[0]) +str(i)+ ".jpg"
        inputfile =  os.path.join(input_path,f)
        print outfile
        img = cv2.imread(inputfile)
        #img = img.thumbnail(size, Image.ANTIALIAS)
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        resized_image = cv2.resize(gray_image, (120,100  )) 
        cv2.imwrite(outfile,resized_image)
        
        line  = outfile +"\n"
        with open("negetives.dat", "a") as f:
            f.write(line)



if  __name__ == "__main__":
    process(sys.argv[1] , sys.argv[2])
