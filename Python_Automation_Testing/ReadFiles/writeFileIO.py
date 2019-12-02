f = open("inputFile.txt", "r")
pass_file = open("passFile.txt", "w")
fail_file = open("failFile.txt", "w")

for line in f:
    line_split = line.split()
    if line_split[2] == "P":
        pass_file.write(line)
    else:
        fail_file.write(line)

print("The", pass_file.name, "are successfully created!")
print("The", fail_file.name, "are successfully created!")

f.close()
pass_file.close()
fail_file.close()