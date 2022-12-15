from lexer import NUMBER_TOKEN, INSTRUCTION_NAME, LABEL_NAME, JUMP_NAME, EOF, REGISTER_TOKEN, EOFL
from opcodes import opcodes, dual_mode_instructions
import re
BRANCH_BIT_COUNT= 10
IMMEDIATE_BIT_COUNT = 9
INSTRUCTION_SIZE = 16


class Binariser(object):
    def __init__(self, instructions_tokenized):
        self.instructions_tokenized = instructions_tokenized
        self.labels_to_lines()

    def binarise(self):
        binary_instructions = []
        for instruction in self.instructions_tokenized:
            binary_instructions.append(self.binarise_instruction(instruction))
        return '\n'.join(binary_instructions)

    def labels_to_lines(self):
        labels_lines = dict()
        for line, instruction in enumerate(self.instructions_tokenized):
            for token in instruction:
                if token.type is LABEL_NAME:
                    if labels_lines.get(token.value) is not None:
                        print(f'Label {token.value} is already used')
                    else:
                        labels_lines[token.value] = line
        self.labels_lines = labels_lines

    def binarise_instruction(self, instruction):
        binary_instruction = []
        instruction_length = 0
        for token in instruction:
            binarised_token = self.visit(token, instruction)
            if binarised_token is not None:
                instruction_length += len(binarised_token)
                binary_instruction.append(binarised_token)

        binarised_instruction = ' '.join(binary_instruction)

        padding = ''
        if INSTRUCTION_SIZE != instruction_length:
            padding = ' ' + '0'*(INSTRUCTION_SIZE - instruction_length)

        return binarised_instruction + padding

    def visit(self, token, instruction):
        method = getattr(self, "binarise" + token.type)
        return method(token, instruction)

    # transforms positive(>=0) decimals to binary
    # returns binary values between [-2^(bitCount - 1), 2^(bitCount - 1))
    def decimal_to_binary(self, decimal, bitCount): 
        minimum = -2**(bitCount - 1)
        maximum = 2**(bitCount - 1) - 1
        interval_size = 2**bitCount
        decimal = decimal % interval_size
        if decimal > maximum:
            decimal = decimal - interval_size
        binary_string = bin(decimal)
        bits_only = re.findall(r'\d+', binary_string)
        bits_only = ''.join(bits_only)
        bit_count = len(bits_only)
        padding_bit = '1' if decimal < 0 else '0'
        padding = ''.join([padding_bit] * (bitCount - bit_count))
        return padding + bits_only

    def binariseLABEL_NAME(self, token, instruction):
        return None

    def binariseINSTRUCTION_NAME(self, token, instruction):
        instruction_name = token.value
        opcode = opcodes[instruction_name]
        if instruction_name in dual_mode_instructions:
            # register - register
            if instruction[-1].type is REGISTER_TOKEN:
                opcode = '1' + opcode[1:]
        return opcode

    def binariseREGISTER_TOKEN(self, token, instruction):
        return '0' if token.value == 'X' else '1'

    def binariseNUMBER_TOKEN(self, token, instruction):
        if token.value > 255:
            raise Exception("Immediate value can't be more than 255")
        return self.decimal_to_binary(token.value, IMMEDIATE_BIT_COUNT)

    def binariseJUMP_NAME(self, token, instruction):
        line = self.labels_lines[token.value]
        return self.decimal_to_binary(line, BRANCH_BIT_COUNT)
    