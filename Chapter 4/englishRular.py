def main():
    draw_ruler(1,5)


def draw_ruler(inchLength, major_tick):
    '''Draw English ruler with given number of inches, major tick length.'''
    drawLine(major_tick,'0')
    for i in range(1,1+inchLength):
        drawInterval(major_tick - 1)
        drawLine(major_tick,str(i))


def drawLine(tick,label=''):
    line = '-'* tick
    if label != '':
        line += ' ' + label
    print(line)

def drawInterval(tick):
    if tick > 0:
        drawInterval(tick-1)
        drawLine(tick)
        drawInterval(tick-1)

if __name__ == '__main__':
    main()
