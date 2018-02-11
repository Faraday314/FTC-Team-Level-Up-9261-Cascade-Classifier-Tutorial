import sys
import os
import fileinput

if len(sys.argv) < 3:
    print("You must supply a file name and a prefix as an argument when running this program.")
    sys.exit(2)

prefix = sys.argv[2]

for line in fileinput.input(sys.argv[1], inplace=True):
    sys.stdout.write(prefix+'/{l}'.format(l=line))
