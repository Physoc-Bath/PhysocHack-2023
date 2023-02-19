from qiskit import *
from qiskit.visualization import plot_histogram

simulator = Aer.get_backend('qasm_simulator')

qr = QuantumRegister(2)
cr = ClassicalRegister(2)

circuit = QuantumCircuit(qr, cr)
circuit.draw()

result = execute(circuit, backend=simulator).result()

plot_histogram(result.get_counts(circuit))
