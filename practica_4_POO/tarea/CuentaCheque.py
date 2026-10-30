import CuentaBancaria

class CuentaCheque(CuentaBancaria):
    def __init__(self, titular, cbu, saldo, costo_emision = 50):
        super().__init__(titular, cbu, saldo)
        self.costo_emision = costo_emision

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto a extraer debe ser mayor que cero.")

        total_a_descontar = monto + self.costo_emision

        if total_a_descontar > self.saldo:
            raise ValueError("Fondos insuficientes para realizar la extracción.")
        self.saldo -= total_a_descontar
