import copy

import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._G = None
        self._nodi = []
        self._Dnodi = {}
        self._visitati = []


    def creaGrafo(self, anno):
        self._nodi = []
        self._Dnodi = {}
        self._G = nx.Graph()
        self._nodi = DAO.getNodi(anno)
        self._G.add_nodes_from(self._nodi)
        for nodi in self._nodi:
            self._Dnodi[nodi.CCode] = nodi
        archi = DAO.getArchi(anno)
        for element in archi:
            nodo1 = self._Dnodi[element[0]]
            nodo2 = self._Dnodi[element[1]]
            self._G.add_edge(nodo1, nodo2)

    def numeroNodi(self):
        return self._G.number_of_nodes()

    def numeroArchi(self):
        return self._G.number_of_edges()

    def gradoNodo(self, nodo):
        return self._G.degree(nodo)

    def output(self):
        stringa = "Grafo correttamente creato"
        numeroComponentiConnesse = nx.number_connected_components(self._G)
        stringa = stringa + "\n" + f"Il grafo ha {numeroComponentiConnesse} componenti connesse" + "\n" +"Di seguito il dettaglio sui nodi:"
        self._nodi.sort()
        for element in self._nodi:
            stringa = stringa + "\n" + f"{element.StateNme} -- {self.gradoNodo(element)} vicini"
        return stringa

    def getPossibili(self):
        return self._nodi

    def statiRaggiungibili1(self, inizio):
        inizio = self._Dnodi.get(int(inizio))
        daVisitare = list(nx.bfs_edges(self._G, inizio))
        daReturnare = [inizio]
        for element in daVisitare:
            daReturnare.append(element[1])
        stringa = f"Elenco di nodi raggiungibili a partire da {inizio.StateNme}"
        for element in daReturnare:
            stringa = stringa + "\n" + f"{element.StateNme}"
        return stringa

    def statiRaggiungibili2(self, inizio):
        inizio = self._Dnodi.get(int(inizio))
        daVisitare = list(self._G.neighbors(inizio))
        self._visitati = [inizio]
        self.itera(daVisitare)
        stringa = f"Elenco di nodi raggiungibili a partire da {inizio.StateNme}"
        for element in self._visitati:
            stringa = stringa + "\n" + f"{element.StateNme}"
        return stringa

    def itera(self, daVisitare):
            for element in daVisitare:
                if element not in self._visitati:
                    self._visitati.append(element)
                    daVisitare2 = self._G.neighbors(element)
                    self.itera(daVisitare2)






