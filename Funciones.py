def mensaje2():
  i = 1
  iterracion = 0 

  mensaje = input("**¿Cual es el mensaje que desea transmitir?**")

  iterracion = input("**¿Cuales son las veces que desea transmitirlo?**")
  iterracion = int(iterracion)
  
  while i<=iterracion:
    print(mensaje)
    i += 1
    print(i)






mensaje2()



def my_print(text):
  print(text * 2)

my_print('Este es my texto')
my_print('Hola')

a = 10
b = 90

c = a + b

def suma(a, b):
  my_print(a + b)

suma(1 ,5) # 6
suma(10, 4) # 14
  