#Ejercicio 2:
class alumno:
  def _init_(self):
    self.nombre=input("Ingrese el nombre: ")
    self.nota=input("Ingrese su nota: ")
  def definitiva(self):
    print('hola', self.nombre)
    print('su nota es:', self.nota.isnumeric())
class resultado(alumno):
  def _init_(self):
    super()._init_()
  def final(self):
      if self.nota.isnumeric() >= 3:
        print('felicidades, usted aprobo!!')
      else:
        print('usted no aprobo!!')
        
p1=alumno()
p1.definitiva()
resultado1= resultado()
resultado1.final()
