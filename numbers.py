CSI = '\x1b['
RED = f'{CSI}41m'
GREEN = f'{CSI}42m'
YELLOW = f'{CSI}43m'
BLACK = f'{CSI}40m'
WHITE = f'{CSI}47m'
RESET = f'{CSI}0m'

def numbers():
    f = open('C:/Users/Gleb/Downloads/sequence.txt')
    nums = [float(x) for x in f]
    f.close()

    positive = [n for n in nums if 5 <= n <= 10]
    negative = [n for n in nums if -10 <= n <= -5]

    total = len(positive) + len(negative)

    p_pos = len(positive) / total * 100
    p_neg = len(negative) / total * 100

    print(f'{GREEN}{"  "}{BLACK}{" От -5 до -10 | кол-во: "}{len(negative)}{" | процентное соотношение: "}{round(p_neg, 1)}{" %"}{RESET}')
    print(f'{RED}{"  "}{BLACK}{" От 5 до 10 | кол-во: "}{len(positive)}{" | процентное соотношение: "}{round(p_pos, 1)}{" %"}{RESET}')
    print(f'{round(p_neg, 1)}{" % "}{GREEN}{"  " * int(p_neg // 5) }{RED}{"  " * int(p_pos // 5)}{BLACK}{" "}{round(p_pos, 1)}{" %"}{RESET}')

if __name__ == "__main__":
    numbers()