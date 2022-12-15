
dual_mode_instructions = ["ADD", "SUB", "LSR", "LSL", "RSR", "RSL", "MOV", "MUL", "DIV",
                          "MOD", "AND", "ORR", "XOR", "CMP", "TST",
                          ]
opcodes = {
    # BRZ LABEL ; jump to label if Z flag is set
    "BRZ": "000000",
    # BRN LABEL ; jump to label if N flag is set
    "BRN": "000001",
    # BRC LABEL ; jump to label if C flag is set
    "BRC": "000010",
    # BRO LABEL ; jump to label if O flag is set
    "BRO": "000011",
    # BRA LABEL ; jump to label
    "BRA": "000100",
    # JMP LABEL ; push PC to stack and jump to label
    "JMP": "000101",
    # ADD R0, #immediate ; R0 = R0 + #immediate
    # ADD R0, R1 ; R0 = R0 + R1
    'ADD': "000110",
    # SUB R0, #immediate ; R0 = R0 - #immediate
    # SUB R0, R1 ; R0 = R0 - R1
    'SUB': "000111",
    # LSR R0, #immediate ; right shift RO #immediate times where #immediate < 16, fill void with zeros
    # LSR R0, R1 ; right shift R0 R1 times where value of R1 < 16
    'LSR': "001000",
    # LSL R0, #immediate ; left shift RO #immediate times where #immediate < 16, fill void with zeros
    # LSL R0, R1 ; left shift R0 R1 times where value of R1 < 16
    'LSL': "001001",
    # RSR R0, #immediate ; right shift RO #immediate times where #immediate < 16, fill void with right most bit
    # RSR R0, R1 ; right shift R0 R1 times where value of R1 < 16
    'RSR': "001010",
    # RSL R0, #immediate ; left shift RO #immediate times where #immediate < 16, fill void with left most bit
    # RSL R0, R1 ; left shift R0 R1 times where value of R1 < 16
    'RSL': "001011",
    # MOV R0, #immediate ; R0 = #immediate
    # MOV R0, R1 ; R0 = R1
    'MOV': "001100",
    # MUL R0, #immediate ; RO = RO * #immediate
    # MUL R0, R1 ; R0 = R0 * R1
    'MUL': "001101",
    # DIV R0, #immediate ; R0 = quotient of R0 / #immediate
    # DIV R0, R1 ; R0 = quotient of R0 / R1
    'DIV': "001110",
    # MOD R0, #immediate ; R0 = R0 % #immediate
    # MOD R0, R1 ; R0 = R0 % R1
    'MOD': "001111",
    # AND R0, #immediate ; R0 = R0 AND #immediate
    # AND R0, R1 ; R0 = R0 AND R1
    'AND': "010000",
    # ORR R0, #immediate ; R0 = R0 OR #immediate
    # ORR R0, R1 ; R0 = R0 OR R1
    'ORR': "010001",
    # XOR R0, #immediate ; R0 = R0 XOR #immediate
    # XOR R0, R1 ; R0 = R0 XOR R1
    'XOR': "010010",
    # CMP R0, #immediate ; compute R0 - #immediate, if 0 set the Z flag, if <0 set the N flag
    # CMP R0, R1 ; compute R0 - R1
    'CMP': "010011",
    # TST R0, #immediate; compute RO and #immediate, setting flags
    'TST': "010100",
    # NOT R0 ; negates all bits in R0
    'NOT': "010101",
    # INC R0 ; increments R0
    'INC': "010110",
    # DEC R0 ; decrements R0
    'DEC': "010111",
    # LDR R0, R1 ; R0 = memory[R1]
    # LDR R0, #immediate ; R0 = memory[#immediate]
    'LDR': "011000",
    # STR R0, R1 ; memory[R1] = R0
    # STR R0, #immediate ; memory[#immediate] = R0
    'STR': "011001",
    # PSH R0 ; pushes R0 into stack
    "PSH": "011010",
    # POP R0 ; pops R0 from stack
    "POP": "011011",
    # HLT ; stops execution
    'HLT': "011100",
    # RET ; pop PC from stack
    'RET': "011101",
    # OUT R1 ; prints registers R1 in binary and decimal
    'OUT': "011110",
    # INP R1 ; reads decimal value and stores it in R1
    'INP': "011111"
}
