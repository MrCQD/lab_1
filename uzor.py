CSI = '\x1b['
RED = f'{CSI}41m'
GREEN = f'{CSI}42m'
YELLOW = f'{CSI}43m'
BLACK = f'{CSI}40m'
WHITE = f'{CSI}47m'
RESET = f'{CSI}0m'

diametr = 6
radius = diametr // 2

def draw(k, n):
    for i in range(n):
        print(f'{WHITE}{'  '* 27}'*k)
        # верх
        print((f"{WHITE}{'   '*(radius-1)}{BLACK}{'   '*4}{WHITE}{'   '*(radius-1)}"
               f"{WHITE}{'   '*(radius-2)}{BLACK}{'   '*4}{WHITE}{'   '*(radius-1)}{RESET}") * k)

        #  чуть ниже
        print((f"{WHITE}{'   '*(radius-2)}{BLACK}{'   '*6}{WHITE}{'   '*1}"
               f"{BLACK}{'   '*6}{WHITE}{'   '*(radius-2)}{RESET}") * k)

        # середина
        print((f"{WHITE}{'   '*1}{BLACK}{'   '*7}"
               f"{BLACK}{'   '*6}{WHITE}{'   '*1}{RESET}") * k)


        # чуть ниже
        print((f"{WHITE}{'   '*(radius-2)}{BLACK}{'   '*6}{WHITE}{'   '*1}"
               f"{BLACK}{'   '*6}{WHITE}{'   '*(radius-2)}{RESET}") * k)

        # низ
        print((f"{WHITE}{'   '*(radius-1)}{BLACK}{'   '*4}{WHITE}{'   '*(radius-1)}"
               f"{WHITE}{'   '*(radius-2)}{BLACK}{'   '*4}{WHITE}{'   '*(radius-1)}{RESET}") * k)
        print(f'{WHITE}{'  ' * 27}' * k)
        print()

if __name__ == "__main__":
    draw(5, 1)