start: MOV X, #12 // comentariu
MOV Y, X -> 001010 1 0 00000000
ADD X, #1
ADD X, X
SUB Y, #1
JMP proc1
proc1: SUB Y, X
LSR X, #3
LSR X, X
LSL Y, #3
LSL Y, Y
RSR X, #1
RSR X, X
RSL Y, #1
RSL Y, Y
MUL X, #2
MUL X, X
DIV Y, #2
DIV Y, Y
MOD X, #255
MOD X, X
AND X, #2
AND X, Y
ORR Y, #6
ORR Y, X
XOR X, #12
XOR X, Y
NOT X
INC X
DEC Y
CMP X, Y
BRZ label1
TST X, Y
BRN label2
CMP X, #10
BRC label3
TST Y, #20
BRO label4
BRA label5
label1: ADD X, #1
label2: ADD X, #2
label3: ADD X, #3
label4: ADD X, #4
label5: PSH X
PSH Y
RET
