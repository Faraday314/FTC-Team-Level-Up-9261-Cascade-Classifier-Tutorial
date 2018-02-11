import sys
import os
import fileinput
import math
import random

if len(sys.argv) < 2:
    print("You must supply a positives .txt file, a negatives .txt file, an output name for the .vec filename, a width value, a height value, and the number of samples you want")
    print("to avoid problems, try to use absolute file paths")
    print("Usage: createsamples.exe <positives file name> <negatives file name> <output file name (without .vec ending)> <width> <height> <total number of samples>")
    sys.exit(2)
else:
    positives = sys.argv[1]
    negatives = sys.argv[2]
    output = sys.argv[3]
    width = int(sys.argv[4])
    height = int(sys.argv[5])
    num = int(sys.argv[6])

    images = []
    with open(positives) as data:
        for line in data:
            images.append(line.split()[0])
    data.close()
    div = math.ceil(num/len(images))
    nums = [div]
    while num > div:
        if num - div > div:
            nums.append(div)
        else:
            nums.append(num-div)
        num -= div
    for i in range(0,len(images)):
        rng = random.randint(1,99999)
        os.system("opencv_createsamples -info "+positives+" -img "+images[i]+" -vec "+output+str(i)+".vec"+" -bg "+negatives+" -num "+str(nums[i])+" -bgcolor 0 -bgthresh 0 -maxidev 40 -maxxangle 1.1 -maxyangle 1.1 -maxzangle 0.5 -w "+str(width)+" -h "+str(height)+" -maxscale -1 -rngseed "+str(rng))
