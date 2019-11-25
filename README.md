# recolour-image

Recolours an image with a palette of a given number of colours using the k-means clustering algorithm.

(The kmeans directory just contains a huge mess of code that's probably worth ignoring until I get 
around to cleaning it up)

## Usage
```
./recolour_img.py INFILE OUTFILE K
```
INFILE and OUTFILE are the input and output image file names respectively, and K is the number of colours to be used in the palette.

The algorithm is not perfect at the moment so there is an OVERRIDE variable in the code set to 2 but this will hopefully be removed when I get a chance to fix it.
