import numpy as np
f = open('/home/diego/Dropbox/Seville/Googlehash/logo.in','r')
img =  np.zeros(map(int, f.readline().split(' ')))
print img.shape
i = 0
for line in f:
    j = 0
    for ch in line:
        if ch == '.':
            img[i,j] = 0
        else:
            img[i,j] = 1
        j += 1
    i += 1