from pyvqnet.qnn.vqc  import *

qm = QMachine(4)

X1(wires=[1], q_machine=qm)
MeasureAll(obs={"X1:2"})


