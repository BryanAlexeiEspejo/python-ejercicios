class Casa:
    def __init__(self, muebles, cocina, deposito):
        self.muebles = muebles
        self.cocina = cocina
        self.deposito = deposito
        
    def llama(self):
        print(f'La casa tiene: {self.muebles}')
        
    def cortar(self):
        print(f'La casa tiene: {self.muebles}')

casa1 = Casa("mesa", "gas", "pequeño")
casa2 = Casa("vitrina", "lavaplatos", "grande")

casa2.llama()