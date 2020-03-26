import os
from chardet import detect


def search_dir(dirname):
    result_list = []
    filenames = os.listdir(dirname)

    for filename in filenames:
        full_path = os.path.join(dirname, filename)
        print(full_path)
        if os.path.isdir(full_path):
            result_list.extend(search_dir(full_path))
        else:
            result_list.append(full_path)
    return result_list

def get_encoding_type(filepath):
    with open(filepath, "rb") as f:
        rawdata = f.read()

    codec = detect(rawdata)


INCLUDE_EXT_LIST = [".txt", ".smi"]
path = "c:\\test"
filelists = search_dir(path)

# c:||test||aaa.txt
for file in filelists:
    filename, ext = os.path.splitext(file)
    if ext.lower() in INCLUDE_EXT_LIST:
