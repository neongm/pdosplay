from dosplay import Screen

# designed to work only with cmd console

# initializing Screen with xsize=80 and ysize=25
scr = Screen(80, 25)
# setup console window size to scr size
scr.setup_size()

# print text 'hello world' at coordinates x, y
scr.vin('hello world', 8, 4)

# scr.xsize return width of scr
# scr.ysize returns height of scr
# lines and cols are numbered from 0
scr.vin('right-top', scr.xsize-len('right-top'), 0)
scr.vin('right-bottom', scr.xsize-len('right-bottom'), scr.ysize-1)
scr.vin('left-bottom', 0, scr.ysize-1)
scr.vin('left-top', 0, 0)
# render all
scr.render()

# whaiting for any input
input()
