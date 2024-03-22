import re
inputfile= input("enter the filename which contain timestamps : ")
outputfile=input("enter the filename which will contain the result : ")

f = open(inputfile,"r")
ips=f.read()
f.close()

result= re.findall(r"09:\d+ \d+/\d+/\d+",ips)

with open(outputfile,"w") as x:
    for line in result:
        x.write(line+"\n")

print("timestamps extracted successfully")
print(f"resultfile -----> {outputfile}")
