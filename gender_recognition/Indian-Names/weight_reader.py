import h5py as h5
import numpy as np

f = h5.File('weights_saved.h5', 'r')
weights = [n for n in f.keys()]

for n in weights:
	for m in n:
		print(m)
