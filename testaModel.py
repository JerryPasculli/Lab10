from model.model import Model

modello = Model()
modello.creaGrafo(1980)
output = modello.output()
print(output)
stringa = modello.statiRaggiungibili1("900")
print(stringa)