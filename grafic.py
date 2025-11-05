CSI = '\x1b['
RED = f'{CSI}41m'
GREEN = f'{CSI}42m'
YELLOW = f'{CSI}43m'
BLACK = f'{CSI}40m'
WHITE = f'{CSI}47m'
RESET = f'{CSI}0m'


def draw_gr():
    height = 10

    for x in range(height, 0, -1):
        if x % 2 != 0:
            y = x//2 + 0.5
        else:
            y = x//2
        print(f'{float(y)}\t{'|'}{GREEN}{'  '*(x-1)}{BLACK}{"  "}{GREEN}{'  '* ((height-1) - (x-1))}{RESET}')
    for x in range(height+1):
        if x == 0:
            print('0.0','|', end = '')
        else: print(str(x), end = ' ')


if __name__ == "__main__":
    draw_gr()