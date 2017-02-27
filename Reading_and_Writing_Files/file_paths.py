import os

# Backslash on Windows and Forward Slash on OSX and Linux
# myFiles = ["accounts.txt", "details.csv", "invite.docx"]
# for filename in myFiles:
#   print(os.path.join("/Users/Kunal/", filename))

# The Current Working Directory
print(os.getcwd())
os.chdir("/Users/Kunal/Development/Automating_Tasks")
print(os.getcwd())

# Creating New Folders with os.makedirs()
os.makedirs('/Users/Kunal/Development/Automating_Tasks/Reading_and_Writing_Files/New_Folder')