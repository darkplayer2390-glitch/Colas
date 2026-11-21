class Cola:

    class _Nodo:

        def __init__(self, info: int):
            self.info = info
            self.sig = None

    def __init__(self):
        self.raiz = None
        self.fondo = None

    def vacia(self) -> bool:
        return self.raiz is None

    def insertar(self, info: int) -> None:
        nuevo = self._Nodo(info)
        if self.vacia():
            self.raiz = nuevo
            self.fondo = nuevo
        else:
            self.fondo.sig = nuevo
            self.fondo = nuevo

    def extraer(self) -> int | str:
        if not self.vacia():
            informacion = self.raiz.info
            if self.raiz == self.fondo:
                self.raiz = None
                self.fondo = None
            else:
                self.raiz = self.raiz.sig
                return informacion
        else:
            return "Cola Vacía"

    def imprimir(self) -> None:
        reco = self.raiz
        print("Listado de todos los elementos de la cola")
        while reco is not None:
            print(f"{reco.info}-", end="")
            reco = reco.sig
        print()

    def buscar(self, info: int) -> bool:
        reco = self.raiz
        while reco is not None:
            if reco.info == info:
                return True
            reco = reco.sig
        return False

    def mostrar_primero(self) -> int | str:
        if not self.vacia():
            return self.raiz.info
        return "Cola Vacía"

    def mostrar_ultimo(self) -> int | str:
        if not self.vacia():
            return self.fondo.info
        return "Cola Vacía"

    def cantidad(self) -> int:
        contador = 0
        reco = self.raiz
        while reco is not None:
            contador += 1
            reco = reco.sig
        return contador

    def vaciar(self) -> None:
        self.raiz = None
        self.fondo = None

    def sumar(self) -> int:
        suma = 0
        reco = self.raiz
        while reco is not None:
            suma += reco.info
            reco = reco.sig
        return suma