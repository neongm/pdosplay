import os
import colorama


class Screen():
    def __init__(self, xsize, ysize):
        self.colors = {'reset':'\33[39m', 'red':'\033[31m', 'green':'\033[32m',
        'yellow':'\033[33m', 'blue':'\033[34m', 'magnetta':'\033[35m', 'cyan':'\033[36m'}
        self.background_colors = {'reset':'\33[49m', 'red':'\033[41m', 'green':'\033[42m',
        'yellow':'\033[43m', 'blue':'\033[44m', 'magnetta':'\033[45m', 'cyan':'\033[46m'}
        colorama.init()
        self.xsize = xsize
        self.ysize = ysize
        self.vram = [' ' for i in range(xsize*ysize+1)]
        self.vram_length = len(self.vram)-1

    def setup_size(self): os.system("mode con cols={} lines={}".format(self.xsize, self.ysize+2))

    def vin(self, string, x, y, color='reset', background='reset'):
        index = y*self.xsize+x
        colors = self.colors
        bc = self.background_colors
        strl = len(string)
        
        if background!='reset' or color!='reset':
            for i in range(1,strl):
                ind = index + i
                if ind < self.vram_length:
                        self.vram[ind] = string[i]
            self.vram[index+strl-1] = string[-1]+bc['reset']+colors['reset']
            self.vram[index] = bc[background]+colors[color]+string[0]
        else:
            for i in range(strl):
                ind = index + i
                if ind < self.vram_length:
                        self.vram[ind] = string[i]

    def clear_vram(self): self.vram = [' ' for i in range(self.xsize*self.ysize+1)]

    def render(self): print(''.join(self.vram))
