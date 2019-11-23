# Garrett Matthews
# Project 7 part A

# I declare that the following source code was written solely by me. I understand that copying any source code,
# in whole or in part, constitutes cheating, and that I will receive a zero on this project if I am found in violation
# of this policy. #

import requests
import os
import time
start = time.perf_counter()
flags = []
with open("flags.txt",'r') as flgs:
    for line in flgs:
        flags.append(line)

flags = [x.replace('\n','') for x in flags]
#print(flags)

file_path = "-lgflag.gif"
file_names = []
for i in flags:
    file = i + file_path
    file_names.append(file)

#print(file_names)

url = "https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/"

byte = 0

for i in file_names:
    r = requests.get(url + i)
    with open(i,'wb') as f:
        f.write(r.content)
    byte += os.path.getsize(i)

end = time.perf_counter()

with open("cia_a.txt",'w') as f:
    b = ("{}{}".format(byte," bytes downloaded"))
    t = ("{}{}{}".format("Elapsed time: ",end - start,'\n'))
    f.write(t + b)

