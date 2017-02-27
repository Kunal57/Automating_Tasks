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