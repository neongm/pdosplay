# pdosplay
simple python display for cmd console
helps make simple visualizations or text interfaces
module contains only one class - Screen
aviable only for windows cmd console

Screen class methods:
.clear_vram() - clears vram

.vin(<string>, <x>, <y>) - inserts string at x/y coordinates, the offset is calculated 
    by the formula: y*xsise+x, this means that if <string> goes beyond the screen, the 
    characters will be transferred to the next line
    
.xsize - returns width of screen

.ysize - returns height if screen

.vram_length - returns vram length

.vram - returns vram
