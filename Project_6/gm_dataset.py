import numpy
import matplotlib.pyplot as plt
import glob
import os

def analyze(file_name):
    rough_array = numpy.loadtxt(file_name)
    smooth_array = smooth(rough_array)
    graph_volt(rough_array,smooth_array,file_name)
    pulse_area(rough_array,smooth_array,file_name)


def smooth(array):
    smooth_array = numpy.empty(0)
    smooth_array = numpy.append(smooth_array, array[0:4])
    for i in range(len(array)):
        if i >= 4:
            if i <= (int(len(array)) - 4):
                avg = (array[i-3] + (2 * array[i - 2]) + (3 * array[i - 1]) + (3 * array[i]) + (3 * array[i + 1]) +
               (2 * array[i + 2]) + array[i + 3]) // 15
                smooth_array = numpy.append(smooth_array , avg)
    smooth_array = numpy.append(smooth_array, array[-3:])
    return smooth_array

def graph_volt(rough,smooth,file_name):
    fig = plt.figure(figsize=(8,6))
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    x1 = numpy.array(range(len(rough)))
    y1 = rough
    ax1.plot(x1,y1)
    ax1.set(title = file_name,ylabel = "Raw",xticks = [])
    x2 = numpy.array(range(len(smooth)))
    y2 = smooth
    ax2.plot(x2,y2)
    ax2.set_ylabel("Smooth")
    fname = file_name.replace(file_name[-4:],".pdf")
    fig.savefig(fname)

def pulse_area(raw,smooth,file_name):
    val = []
    height = []
    start = []
    area = []
    for i in range(len(smooth)):
        if (i + 2) < len(smooth):
            pulse = (smooth[i + 2] - smooth[i])
            if pulse >= 100:
                val.append(i)
                height.append(pulse)
    start.append(val[0])
    for i in range(len(height)):
        if (i + 2) < len(height):
            if height[i+1] < height[i]:
                if height[i + 2] > height[i+1]:
                    start.append(val[i+2])
    for i in range(len(start)):
        if (i + 1) < len(start):
            if (start[i] + 50) < (start[i + 1]):
                rea = 0
                for q in range(50):
                    z = start[i] + q
                    rea += raw[z]
                area.append(rea)
            else:
                r = (start[i + 1] - start[i])
                rea = 0
                for q in range(r):
                    z = start[i] + q
                    rea += raw[z]
                area.append(rea)
        else:
            rea = 0
            for q in range(50):
                z = start[i] + q
                rea += raw[z]
            area.append(rea)
    fname = file_name.replace(file_name[-4:], ".out")
    with open (fname, 'w') as out:
        out.write("{}{}{}".format(fname,":",'\n'))
        for i in range(len(start)):
            ar = ("{0:.0f}".format(area[i]))
            out.write("{}{}{}{}{}{}{}{}".format("Pulse ",(i + 1), ": ",start[i], " (",ar,")",'\n'))



def main():
    for fname in glob.glob('*.dat'):
        print(analyze(fname))


main()