CSI = '\x1b['
RESET = f'{CSI}0m'
WHITE = f'{CSI}48;5;15m'
BLUE = f'{CSI}48;5;19m'

def draw_flag():
    height = 11
    width = 30
    for y in range(height):
        if 4 <= y <= 5:
            print(f'{BLUE}{' ' * (width*2-1)} {RESET}')
        else:
            print(f'{WHITE}{'  ' * (width//4)}{BLUE}{'  ' * (width//10)}{WHITE}{"  " * (width-10)}{RESET}')
if __name__ == "__main__":
    draw_flag()