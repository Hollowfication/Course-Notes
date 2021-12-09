import glob, os, shutil

path = os.getcwd()
print ("The current working directory is %s" % path)

for file_path in glob.glob(os.path.join(path,"*.tex")):
    new_dir = file_path.rsplit('.', 1)[0]
    os.mkdir(os.path.join(path, new_dir))
    shutil.move(file_path, os.path.join(new_dir, os.path.basename(file_path)))
    print(new_dir,"was created")
