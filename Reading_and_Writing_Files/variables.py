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

# Saving Variables with the pprint.pformat() Function
import pprint

dogs = [{"name": "Thor", "desc": "Golden Retriever"}, {"name": "Loki", "desc": "Husky"}]
pprint.pformat(dogs)

fileObj = open("myDogs.py", "w")
fileObj.write('dogs = ' + pprint.pformat(dogs) + "\n")
fileObj.close()

import myDogs
print(myDogs.dogs)
print(myDogs.dogs[0])
print(myDogs.dogs[0]["name"])