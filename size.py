import os

def folder_size(path1='.', path2='.'):
    missing = []
    for entry in os.scandir(path1):
        if entry.is_file():
            total += entry.stat().st_size
        elif entry.is_dir():
            total += folder_size(entry.path)
    return total

print(folder_size('.'))