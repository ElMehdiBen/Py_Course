file = open("text.txt", "r")

lines = file.readlines()

lines_clean = []

for line in lines:
    if line != "\n":
        line = line.replace(".\n", "")
        line = line.replace("\n", "")
        lines_clean.append(line.split('.')[1])

f = open("text_complet.txt", "w")
f.write(" ".join(lines_clean))
f.close()