import numpy as np
import pylab as pl
f = open('/home/diego/Dropbox/Seville/Googlehash/logo.in','r')
img =  np.zeros(map(int, f.readline().split(' ')))
print img.shape
i = 0
for line in f:
    j = 0
    for ch in line:
        if ch == '.':
            img[i,j] = 0
            j += 1
        elif ch == '#':
            img[i,j] = 1
            j += 1       
    i += 1

pl.imshow(img)
pl.show()