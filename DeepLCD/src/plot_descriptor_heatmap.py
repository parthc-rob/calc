import matplotlib.pyplot as plt
import numpy as np

# fls = ["000000.png_descriptor.txt", "001000.png_descriptor.txt", "002000.png_descriptor.txt"]

fls = ["live_college.jpg_descriptor.txt", "memory_college.jpg_descriptor.txt"]
fl_dir = '../build/images/descriptors/'

total_px = 1064
ratio = 160/120

n_rows = 28 #int(np.sqrt(1064/ratio))

n_cols = 38 #total_px/n_rows
print "ROWS: " + str(n_rows) + " COLS : " + str(n_cols);

fig_count = 0

for fl in fls:
    lines = [line.rstrip('\n') for line in open(fl_dir + fl)]
    descr_vector = np.asarray(lines)
    print "\ndescriptor size :" + str(descr_vector.size) + "\n DESCR Vector\n"

    descr_vector_floats = np.asarray([float(component) for component in descr_vector])
    print descr_vector_floats
    # reshape then plot as heatmap
    descr_heatmap = descr_vector_floats.reshape((n_rows, n_cols))
  
    print "DESCR shape \n"
    print descr_heatmap.shape
    plt.figure(fig_count)
    fig_count = fig_count + 1

    plt.imshow(descr_heatmap, cmap='hsv', interpolation='nearest')
    plt.show()

# a = np.random.random((16, 16))
# plt.imshow(a, cmap='hot', interpolation='nearest')
# plt.show()
