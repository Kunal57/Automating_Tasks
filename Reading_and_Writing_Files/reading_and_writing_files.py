# Opening Files with the open() Function
helloFile = open("hello.txt")
print(helloFile)

# Reading the Contents of Files
helloContent = helloFile.read()
print(helloContent)
helloFile.close()

sonnetFile = open("sonnet29.txt")
print(sonnetFile.readlines())
sonnetFile.close()

# Writing to Files
appleFile = open('apple.txt', "w")
appleFile.write("Hello, World!\n")
appleFile.close()

appleFile = open('apple.txt', "a")
appleFile.write("Apples are amazing!")
appleFile.close()

appleFile = open("apple.txt")
content = appleFile.read()
appleFile.close()
print(content)