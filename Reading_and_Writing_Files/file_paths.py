import os

# Backslash on Windows and Forward Slash on OSX and Linux
# myFiles = ["accounts.txt", "details.csv", "invite.docx"]
# for filename in myFiles:
#   print(os.path.join("/Users/Kunal/", filename))

# The Current Working Directory
print(os.getcwd())
os.chdir("/Users/Kunal/Development/Automating_Tasks")
print(os.getcwd())