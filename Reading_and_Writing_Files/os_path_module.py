import os

# Handling Absolute and Relative Paths
print(os.path.abspath("."))
print(os.path.abspath("os_path_module.py"))
print(os.path.isabs("."))
print(os.path.isabs(os.path.abspath(".")))

print(os.path.relpath("/Development", "/"))
print(os.path.relpath("/Development", "/Reading_and_Writing_Files"))
print(os.getcwd())

path = '/Users/Kunal/Development/Automating_Tasks/Reading_and_Writing_Files'
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.split(path))
pathName = os.path.dirname(path), os.path.basename(path)
print(pathName)

print(path.split(os.path.sep))

# Finding File Sizes and Folder Contents
path = '/Users/Kunal/Development/Automating_Tasks/Reading_and_Writing_Files/os_path_module.py'
print(os.path.getsize(path))
print(os.listdir("/Users/Kunal/Development/Automating_Tasks"))

totalSize = 0
for filename in os.listdir("/Users/Kunal/Development/Automating_Tasks"):
  totalSize += os.path.getsize(os.path.join("/Users/Kunal/Development/Automating_Tasks", filename))

print(totalSize)