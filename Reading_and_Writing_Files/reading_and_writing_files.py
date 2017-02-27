# Opening Files with the open() Function
helloFile = open("hello.txt")
print(helloFile)

# Reading the Contents of Files
helloContent = helloFile.read()
print(helloContent)

sonnetFile = open("sonnet29.txt")
print(sonnetFile.readlines())