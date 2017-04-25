import sys


def splitter():
    input = open(sys.argv[1], 'r', encoding='utf-8', errors='ignore')
    output = open(sys.argv[2], 'w', encoding='utf-8', errors='ignore')
    i = int(sys.argv[3])
    
    for line in input:
        output.write(line.replace('\n', '').split(',')[i] + '\n')


if __name__ == '__main__':
    splitter()
#python _split.py 7.txt 7k.txt 0