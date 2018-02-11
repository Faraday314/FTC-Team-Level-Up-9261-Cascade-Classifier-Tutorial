import sys
import os
import fileinput

if len(sys.argv) < 2:   
    os.system("cls")
    print("You must supply a file name as an argument when running this program.")
    sys.exit(2)

for line in fileinput.input(sys.argv[1], inplace=True):
    sys.stdout.write('positive_images/{l}'.format(l=line))
