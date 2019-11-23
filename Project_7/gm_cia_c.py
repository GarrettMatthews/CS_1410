# Garrett Matthews
# Project 7 part C

# I declare that the following source code was written solely by me. I understand that copying any source code,
# in whole or in part, constitutes cheating, and that I will receive a zero on this project if I am found in violation
# of this policy. #

import requests
import os
import time
from concurrent.futures import ThreadPoolExecutor

class CIA_C(object):
    def __init__(self):
        self.flags = []
        self.file_names = []
    def flag(self):
        with open("flags.txt",'r') as flgs:
            for line in flgs:
                self.flags.append(line)

        self.flags = [x.replace('\n','') for x in self.flags]
        #print(flags)
        return self.flags

    def filepath(self):
        file_path = "-lgflag.gif"
        for i in self.flags:
            file = i + file_path
            self.file_names.append(file)
        #print(file_names)
        return self.file_names

    def download(self):
        url = "https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/"
        for i in self.file_names:
            r = requests.get(url + i)
            with open(i, 'wb') as f:
                f.write(r.content)
    def run(self):
        start = time.perf_counter()
        executor = ThreadPoolExecutor(max_workers=1)
        task1 = executor.submit(self.flag())
        task2 = executor.submit(self.filepath())
        task3 = executor.submit(self.download())
        byte = 0
        for i in self.file_names:
            byte += os.path.getsize(i)
        end = time.perf_counter()
        with open("cia_c.txt", 'w') as f:
            b = ("{}{}".format(byte, " bytes downloaded"))
            t = ("{}{}{}".format("Elapsed time: ", end - start, '\n'))
            f.write(t + b)

def main():
    c = CIA_C()
    c.run()


main()


