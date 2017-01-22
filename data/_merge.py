import sys


def merger():
    input1 = open(sys.argv[1], 'r', encoding='utf-8', errors='ignore')
    input2 = open(sys.argv[2], 'r', encoding='utf-8', errors='ignore')
    output = open(sys.argv[3], 'w', encoding='utf-8', errors='ignore')
    
    table1 = []
    table2 = []
    
    for line in input1:
        table1.append(line.replace('\n', ''))    
    
    for line in input2:
        table2.append(line.replace('\n', ''))
    
    print(len(table1))
    print(len(table2))
    
    for i in range(0, min(len(table1), len(table2))):
        output.write(table1[i] + ',' + table2[i] + '\n')


if __name__ == '__main__':
    merger()
#python _merger.py 7k.txt 7t.txt 7.txt