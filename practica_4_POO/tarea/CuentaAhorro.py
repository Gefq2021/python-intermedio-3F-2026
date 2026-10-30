import CuentaBancaria

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, cbu, saldo):
        super().__init__(titular, cbu, saldo)

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto a extraer debe ser mayor que cero.")
        if monto > self.saldo:
            raise ValueError("Fondos insuficientes para realizar la extracción.")
        self.saldo -= monto

    def aplicar_interes(self):
        interes = self.saldo * 0.001  # 0,1% de interés
        self.saldo += interes
