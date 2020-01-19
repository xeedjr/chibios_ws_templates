import os

path = '..\\src'
project_dir = '..\\..\\..\\src'

files = []
files_fromproj = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.h' in file:
            files.append(os.path.join(r, file))


for f in files:
    new_f = '"' + project_dir + f[len(path):f.rfind('\\')] + '"\n';

    if not(new_f in files_fromproj):
        files_fromproj.append(new_f);

file1 = open("includes.txt","w+") 
file1.writelines(files_fromproj);
file1.close()

for f in files_fromproj:
    print(f)