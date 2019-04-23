import cv2
from testNet import view_forward_pass

# fls = ["live_college.jpg_descriptor.txt", "memory_college.jpg_descriptor.txt"]

fls = ["live_college.jpg", "memory_college.jpg"]
fl_dir = '../DeepLCD/build/images/memory/'

im1_fl = fl_dir + fls[0]
im2_fl = fl_dir + fls[1]

# if cv2.imread(im1_fl) == None:
#     raise Exception("could not load image1 !")

# if cv2.imread(im2_fl) == None:
#     raise Exception("could not load image2 !")

net_def_path = "../DeepLCD/build/calc_model/deploy.prototxt"
net_model_path = "../DeepLCD/build/calc_model/calc.caffemodel"

view_forward_pass(im1_fl, im2_fl, net_def_path, net_model_path)
