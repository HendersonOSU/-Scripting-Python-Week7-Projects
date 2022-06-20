fileName = input("Enter the file name: ")

f = open(fileName, "r")
fileList = list()

for line in f:
    line = line.strip('\n')
    fileList.append(line)

content = True
while content:
    print("File has: ", len(fileList), "lines.")
    noLine = int(input("Enter a number of the line: " ))
    if noLine == 0:
        content = False
    else:
        print(str(noLine)+ ' : ' +fileList[noLine-1] + '\n')
fin.close()


                
