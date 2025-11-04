# 导入QCircuit类
from pyqpanda3.core import QCircuit, H, CNOT

# Create a quantum circuit with 2 qubits
circuit = QCircuit(2)

# 插入门操作
circuit << H(0)  # 将H门作用至第0个量子比特
circuit << CNOT(0, 1)  # 在量子比特0,1上作用CNOT门

# 打印线路属性
print("Circuit Size:", circuit.size())
print("Qubits:", circuit.qubits())
print("Operations:", circuit.count_ops(False))
print("Circuit Depth:", circuit.depth(False))
