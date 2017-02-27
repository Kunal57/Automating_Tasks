# Saving Variables with the shelve Module
import shelve

shelfFile = shelve.open('mydata')
dogs = ["Thor", "Loki", "Space"]
shelfFile['dogs'] = dogs
shelfFile.close()

shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile["dogs"])
shelfFile.close()

shelfFile =shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close