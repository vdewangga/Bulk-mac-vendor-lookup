import urllib.request
import json
import sys

ar = sys.argv
line = []
v = {}
file = open(ar[1]).read().split()
for m in range(len(file)):
	j = json.load(urllib.request.urlopen('https://macvendors.co/api/'+file[m]))
	v[file[m]] = j['result']['company']

line.append(max(len(x) for x in v))
line.append(max(len(v[x]) for x in v))

lineA = "_" * (line[0]+5)
lineB = "_" * (line[1]+2)

print(lineA.strip() + lineB.strip() + "__".strip())
print("|MAC Address         :" + "  vendor" + " " * (len(lineB) - len("vendor")) + "|")
print("|" + lineA.strip() + lineB.strip() + "_".strip() + "|")

for k, v in v.items():
	spc = " " * (int(len(lineB)) - int(len(v)) - 2)
	print("|", k, " : ", v, spc, "|")

print("|" + lineA.strip() + lineB.strip() + "_".strip() + "|")
