import sys

def soma(a,b,c):
    return int(a)+int(b)+int(c)

if __name__ == '__main__':
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    print(soma(a,b,c))