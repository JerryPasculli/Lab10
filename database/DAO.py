from turtledemo.sorting_animate import start_qsort

from database.DB_connect import DBConnect
from model.stato import Stato


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getNodi(anno):
        connessione = DBConnect.get_connection()
        cursor = connessione.cursor(dictionary=True)
        query = """SELECT * FROM country WHERE CCode in (SELECT state1no 
         from contiguity c where year<=%s)"""
        cursor.execute(query, [anno])
        lista = []
        for element in cursor:
            stato = Stato(**element)
            lista.append(stato)
        cursor.close()
        connessione.close()
        return lista


    @staticmethod
    def getArchi(anno):
        connessione = DBConnect.get_connection()
        cursor = connessione.cursor()
        query = """select state1no, state2no
from contiguity c 
where conttype = 1 and year<=%s and state1no>state2no"""
        cursor.execute(query, [anno])
        lista = []
        for element in cursor:
            lista.append(element)
        cursor.close()
        connessione.close()
        return lista

