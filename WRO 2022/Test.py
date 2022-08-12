from huskylib import HuskyLensLibrary
from time import sleep

hl= HuskyLensLibrary("I2C","",address=0x32)

class Arrow:
    def __init__(self, xTail, yTail , xHead , yHead, ID):
        self.xTail=xTail
        self.yTail=yTail
        self.xHead=xHead
        self.yHead=yHead
        self.ID=ID
        self.learned= True if ID > 0 else False
        self.type="ARROW"


class Block:
    def __init__(self, x, y , width , height, ID):
        self.x = x
        self.y=y
        self.width=width
        self.height=height
        self.ID=ID
        self.learned= True if ID > 0 else False
        self.type="BLOCK"
        
while True:
    check = hl.count()
    if check == 0:
        print('Error')
    else:
        Block = hl.blocks()
        x = Block.x
        y = Block.y
        print(f'X:{x} Y:{y}')
    sleep(1)