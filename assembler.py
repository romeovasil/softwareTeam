from lexer import Lexer, Token
from binary import Binariser
import sys
import os.path
from opcodes import opcodes

def read(assembly_file):
    with open(assembly_file) as file:
        return file.read()

def print_instructions(instructions_tokenized):
    for instruction in instructions_tokenized:
        print(", ".join([str(token) for token in instruction]))

if __name__ == '__main__':
    arg_count = len(sys.argv)
    if arg_count != 2:
        print("Script expects file path as argument")
        exit()

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f'{file_path} doesn\'t exist')
        exit()

    output_path = '.'.join(file_path.split('.')[:-1] + ['bin'])
    assembly_code = read(file_path)

    lexer = Lexer(assembly_code)

    instructions_tokenized = lexer.tokenize()

    binariser = Binariser(instructions_tokenized)
    binary_instructions = binariser.binarise()

    with open(output_path, "w+") as output_file:
        output_file.write(binary_instructions)

    print_instructions(instructions_tokenized)
