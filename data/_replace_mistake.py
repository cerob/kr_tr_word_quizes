'''
replaces a single line string with another one just once
intended to correct a word mistake in simple files
not works such as: pdf, docx, odf etc.

if the string to be changed;
    -has more than one occurences,
    -has no occurences
then this program raises ValueError

run from command line as follows:
python _replace_mistake.py input_file replacement_info_file

replacement_info_file must consist of two lines:
    -the first is the string to be changed
    -the second is the string to be changed to
'''
import sys


def replace_mistake():
    '''main function'''

    data = ''
    with open(sys.argv[1], 'r', encoding='utf-8', errors='ignore') as inp:
        for line in inp:
            data += line

    with open(sys.argv[2], 'r', encoding='utf-8', errors='ignore') as repl_file:
        str_from = repl_file.readline().replace('\n', '')
        str_to = repl_file.readline().replace('\n', '')

    if data.find(str_from) == -1:
        raise ValueError('there are no occurences, no changes has been made')

    data = data.replace(str_from, str_to, 1)

    if data.find(str_from) != -1:
        raise ValueError('there are more than one occurences, no changes has been made')

    with open(sys.argv[1], 'w', encoding='utf-8', errors='ignore') as out:
        out.write(data)

        

if __name__ == '__main__':
    replace_mistake()
