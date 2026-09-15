import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def handle_creaGrafo(self, e):
        try:
            num_voli=int(self._view.txtNumVoliMinimo.value)
        except Exception as e:
            self._view.show_alert(f"\tATTENZIONE\n {e}")
            return
        if num_voli <= 0:
            self._view.show_alert(f"mettere valore valido (> 0)")
            return
        self._model.get_states_min_voli(num_voli)


    def handle_statiRaggiungibili(self, e):
       pass #h

