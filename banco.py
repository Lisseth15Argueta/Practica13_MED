class Banco:
    def __init__(self):
        self.cola = []

    def atender_cliente(self):
        if len(self.cola) > 0:
            cliente = self.cola.pop(0)
            print("Atendiendo al cliente:", cliente)
        else:
            print("No hay clientes en espera.")

    def agregar_cliente(self, cliente):
        self.cola.append(cliente)
        print("Cliente", cliente, "agregado a la cola.")

    def mostrar_estado(self):
        if len(self.cola) > 0:
            print("Clientes en espera:", self.cola)
        else:
            print("No hay clientes en espera.")
banco = Banco()

banco.agregar_cliente("Cliente 1")
banco.agregar_cliente("Cliente 2")
banco.agregar_cliente("Cliente 3")

banco.mostrar_estado()

banco.atender_cliente()
banco.atender_cliente()
banco.atender_cliente()

banco.mostrar_estado()
