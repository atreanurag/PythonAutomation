#! python
#Take inputs 
import sys
import shutil
import os
import subprocess

#subprocess.run()

print('Copyting requied installer media')

#Total arguments
n = len(sys.argv)
print("Total number of arguments - "+ str(n))

source_dir=sys.argv[1]
dest_dir=sys.argv[2]

print("source_dir - " + sys.argv[1])
print("dest_dir - " + sys.argv[2])

isExistsSrc=os.path.exists(source_dir)
print("source folder exists? - "+ str(isExistsSrc))

isExistsDest=os.path.exists(dest_dir)
print("destination folder exists? - "+ str(isExistsDest))

if isExistsSrc==False:
    print("Source folder doesn't exists")

if isExistsDest==False:
    print("Destination folder doesn't exists")

if isExistsSrc and isExistsDest:
    shutil.copytree(source_dir,dest_dir)

shutil.copytree()