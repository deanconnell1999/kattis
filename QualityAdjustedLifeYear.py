no_inputs = int(input())
QALY = 0

for i in range(no_inputs):
    x = (input().split())
    QALYi = float(x[0])*float(x[1])
    QALY += QALYi
print(QALY)