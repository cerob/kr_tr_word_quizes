'''
simple job file to unify files
no user input for files to be processed, please edit the code

example command:
python _unify.py 1
python _unify.py 0
'''

import sys


def unify():
    filename_prefix = ''
    filename_postfix = '.txt'

    count_begin = 1
    count_end = 7

    if sys.argv[1] == '1':
        raw = True
    else:
        raw = False

    data = ''

    for i in range(count_begin, count_end + 1):
        if raw is not True:
            data += str(i) + '\n'

        filename = filename_prefix + str(i) + filename_postfix
        with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                data += line

        data += '\n\n'
    
    if raw and data.find('\n\n') != -1:
        data = data.replace('\n\n', '\n')

    with open('output.txt', 'w', encoding='utf-8', errors='ignore') as ofile:
        ofile.write(data)


if __name__ == '__main__':
    unify()
