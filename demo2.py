from dosplay import Screen
# designed to work only with cmd console

# initializing Screen with xsize=80 and ysize=25
scr = Screen(80, 25)
# setup console window size to scr size
scr.setup_size()

for i in range(scr.ysize):
    scr.vin('|', 0, i)

for i in range(scr.ysize):
    scr.vin('|', scr.xsize-1, i)

text = 'hello world' # center of screen
scr.vin(text, scr.xsize//2-len(text)//2, scr.ysize//2)

scr.render()

# whaiting for any input
input()
scr.clear_vram()

# some animation
c=0
c2=0 
while True:
    c+=1
    scr.clear_vram() # deletes previous frame 
    scr.vin('WOOOOOW', c, 0)
    scr.render() 
    if c-len('WOOOOOW') > scr.vram_length: 
        c = 0 
        c2+=1
        if c2==5: break

# whaiting for any input
input()
