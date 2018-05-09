from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("./modules") if isfile(join("./modules", f))]

with open("input.py") as f: c = f.read()

for fileName in onlyfiles:
    with open("./modules/" + fileName) as f:
        exec(f.read())
        c = obfuscate(c)

print(c)