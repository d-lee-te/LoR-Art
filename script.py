import os
import shutil

cd = os.getcwd()
fPath = os.path.join(cd, 'LoR Sets')

#Creating "target" folder to store full arts
target = "aggregate"

if not os.path.exists(target):
    os.makedirs(target)
    print("%s folder created" % target)
else:
    print("%s folder already exists" % target)

tPath = os.path.join(cd, target)


os.chdir(fPath)

root = os.getcwd()
for filename in os.listdir():
    #Entering a set
    cd = os.path.join(root, filename)
    os.chdir(cd)
    print("Working on %s" % filename)

    #LoR set img folder
    cd = os.path.join(cd, 'en_us', 'img', 'cards')
    os.chdir(cd)
    
    #Copying all files with full in filename to target directory
    for file in os.listdir():
        #Check to see if it's a full art and not an alt file
        if 'full' in file and 'alt' not in file:
            pic = os.path.join(os.getcwd(), file)
            #Checking to see if it's a full background and not an icon
            if os.path.getsize(pic) > 1000000:
                shutil.copy(pic, os.path.join(tPath, file))
    

    #Back to main folder
    os.chdir(fPath)