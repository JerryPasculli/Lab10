import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e, anno):
        self._view._txt_result.controls.clear()
        try:
            int(anno)
        except ValueError:
            stringa = f"Non hai inserito un valore numerico"
            self._view._txt_result.controls.append(ft.Text(f"{stringa}", color="red"))
            self._view.update_page()
            return
        anno = int(anno)
        if anno >2016 or anno <1816:
            stringa = f"Non hai inserito un valore numerico numerico compreso nel range 1816-2016"
            self._view._txt_result.controls.append(ft.Text(f"{stringa}", color="red"))
            self._view.update_page()
            return
        self._model.creaGrafo(anno)
        output = self._model.output()
        self._view._txt_result.controls.append(ft.Text(f"{output}"))
        self.popolaPaesi()
        self._view.update_page()

    def popolaPaesi(self):
        lista = self._model.getPossibili()
        for element in lista:
            op = ft.dropdown.Option(text=f"{element.StateNme}", key = f"{element.CCode}")
            self._view._ddPaesi.options.append(op)

    def handleRaggiungibili(self, e, codice):
        self._view._txt_result.controls.clear()
        output = self._model.statiRaggiungibili1(codice)
        self._view._txt_result.controls.append(ft.Text(f"{output}"))
        self._view.update_page()



