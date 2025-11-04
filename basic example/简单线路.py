from pyqpanda3.core import QProg, measure, draw_qprog, CPUQVM, H, CNOT

prog = QProg()
prog << H(0)
for i in range(1, 5):
    prog << CNOT(i - 1, i)
for i in range(5):
    prog << measure(i, i)

print(draw_qprog(prog))

qvm = CPUQVM()
qvm.run(prog, 1024)
print(qvm.result().get_prob_dict())
