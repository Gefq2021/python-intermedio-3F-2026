from tarea.CuentaBancaria import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, cbu, saldo_inicial, limite_descubierto = 500):
        super().__init__(titular, cbu, saldo_inicial)
        self.limite_descubierto = limite_descubierto

    @CuentaBancaria.saldo.setter
    def saldo(self, valor):
        if valor < -self.limite_descubierto:
            raise ValueError("El saldo no puede ser menor que el límite de descubierto.")
        self._saldo = valor

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto a extraer debe ser mayor que cero.")
        if monto > self.saldo + self.limite_descubierto:
            raise ValueError("Fondos insuficientes para realizar la extracción.")
        self.saldo -= monto
