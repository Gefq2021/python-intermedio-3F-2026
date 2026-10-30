import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, cbu, saldo, limite_descubierto = 500):
        super().__init__(titular, cbu, saldo)
        self.limite_descubierto = limite_descubierto

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto a extraer debe ser mayor que cero.")
        if monto > self.saldo + self.limite_descubierto:
            raise ValueError("Fondos insuficientes para realizar la extracción.")
        self.saldo -= monto
