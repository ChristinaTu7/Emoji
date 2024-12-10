#!/usr/bin/python
# modifies the color of the halo from blue to green

from PIL import Image
import sys

if len(sys.argv) != 3:
    print("Usage:", sys.argv[0], "source", "target")
    sys.exit(0)

source = sys.argv[1]
target = sys.argv[2]
img = Image.open(source)
pixels = img.load()
w,h = img.size

# let's look at 100 pixels in the center
# comment this for loop out before submission
'''
for i in range(w//2-5,w//2+5):
    for j in range(w//2-5,w//2+5):
        print(pixels[i,j])
'''

# your solution goes here, you have to conditionally modify the pixels

for i in range (w):
    for j in range (h):
        r,g,b,a = pixels[i,j]
        if b > 100 and not (r > 175 and g > 175):
            pixels[i,j] = (r,255,0,a)
            #print(pixels[i,j])

# using a nested for loop

img.show()
img.save(target)
