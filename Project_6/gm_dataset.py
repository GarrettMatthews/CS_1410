import numpy
import matplotlib.pyplot as plt
import glob

def analyze(file_name):
    rough_array = numpy.loadtxt(file_name)
    smooth_array = smooth(rough_array)
    print("{}{}{}".format(rough_array,'\n',smooth_array))
    graph_volt(rough_array,smooth_array,file_name)


def smooth(array):
    smooth_array = numpy.empty_like (array)
    smooth_array[0:4] = array[0:4]
    # Figure out how to access elements of the array [4:-4] rather than just using the len(array)
    for i in range(int(len(array))):
        if i <= (int(len(array)) - 8):
            avg = (array[i] + (2 * array[i+2]) + (3 * array[i + 3]) + (3 * array[i + 4]) + (3 * array[i + 5]) +
               (2 * array[i + 6]) + array[i + 7]) // 15
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
    plt.show()


def main():
    for fname in glob.glob('*.dat'):
        print(analyze(fname))


main()