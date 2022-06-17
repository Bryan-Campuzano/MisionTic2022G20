#Implemente una clase llamada operaciones, en la cual se cargan dos numeros
#decimales en el método __init__ y debe tener 4 métodos para realizar 
#suma, resta, multiplicación y división

class Operaciones:
    def __init__(self,x:float,y:float):
        self.x = x  
        self.y = y
    def sum(self):
        print(f'La suma es: {self.x + self.y}')
    def sub(self):
        print(f'La resta es: {self.x - self.y}')
    def mul(self):
        print(f'La multiplicación es: {self.x * self.y}')
    def div(self):
        try:
            print(f'La división es: {self.x / self.y}')
        except:
            print(f'División no válida')
            
x = Operaciones(55.40,35.9)     
x.sum()
x.sub()
x.mul()
x.div()   