
from model.model import Model

modello = Model()
modello.creaGrafo(1980)
output = modello.output()
print(output)
stringa = modello.statiRaggiungibili1("20")
stringa1 = modello.statiRaggiungibili1("20")
print(stringa)
print(stringa1)
print(stringa == stringa1)