f = open("inputFile.txt", "r")
print("The following students are passed the exam: ")
for line in f:
    line_split = line.split()
    if line_split[2] == "P":
        print(line)

f.close()