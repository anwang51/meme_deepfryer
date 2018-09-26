import sys
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter

SIGMA = 10
NUM_STEPS = 5

def matrix_add(r, g, b):
	h = len(r)
	w = len(r[0])
	output = np.zeros((h, w, 3), 'uint8')
	for i in range(h):
		for j in range(w):
			temp = np.concatenate((r[i][j], g[i][j], b[i][j]))
			output[i][j] = temp
	return output

def deepfryer():
	image_name = sys.argv[1]
	original = np.array(Image.open(image_name))
	im_array = np.array(Image.open(image_name).convert('RGB'))
	h = len(im_array)
	w = len(im_array[0])
	r, g, b = np.split(im_array, 3, axis=2)
	r_filtered = gaussian_filter(r, SIGMA)
	b_filtered = gaussian_filter(b, SIGMA)
	g_filtered = gaussian_filter(g, SIGMA)
	gaussian_negative = matrix_add(r_filtered, g_filtered, b_filtered)
	processed = 3*original - 3*gaussian_negative
	final = Image.fromarray(processed)
	final.save("deep_fried_" + image_name)

deepfryer()