# Backslash on Windows and Forward Slash on OSX and Linux
import os

myFiles = ["accounts.txt", "details.csv", "invite.docx"]
for filename in myFiles:
  print(os.path.join("/Users/Kunal/", filename))
