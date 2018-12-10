import os

path = "D:/xrvision/5_noelcodes/temp/dataset"
os.chdir(path)

s = 0
f = 0
for subdirs, dirs, files in os.walk(path):
    for file in files:
        img_path = subdirs + "/" + file
        folder_name = subdirs[len(path)+1:]
        new = (path + '/subject_' + str(s) + '/' + folder_name + '-' + str(f) + '.jpg')
        print(img_path)
        print(new)
        os.renames(img_path, new)
        f += 1
    s+=1