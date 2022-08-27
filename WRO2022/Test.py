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
        
def compare(x1,y1,x2,y2):
    area1 = x1*x2
    area2 = x2*x2
    if area1 > area2:
        return block1
    if area1 < area2:
        return block2
    return tie
        
while True:
    check = hl.count()
    if check == 0:
        print('Error')
    elif check >= 2:
        Block1 = hl.getBlocksByID(1)
        Block2 = hl.getBlocksByID(2)
        x1 = Block1.x
        y1 = Block1.y
        x2 = Block2.x
        y2 = Block2.y
        print(f'(X:{x1} Y:{y1}) , (X:{x2} Y: {y2})')
    sleep(1)
    print (check)