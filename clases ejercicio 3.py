#ejercico 3:
class calculadora:
  def _init_(self):
    self.valor1 = int(input('digite un valor'))
    self.valor2 = int(input('digite otro valor'))
  def mostrar(self):
    print('su valor 1 es:', self.valor1,
    
          'su valor 2 es:', self.valor2 )
    print('la suma es:', self.valor1+self.valor2 )
    print('la resta es:', self.valor1-self.valor2)
    print('la multiplicacion es:', self.valor1*self.valor2)
    print('la division es: ', self.valor1/self.valor2)

calculadora1=calculadora()
calculadora1.mostrar()
