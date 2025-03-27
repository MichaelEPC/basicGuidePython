iterracion = 0 

mensaje = input("**¿Cual es el mensaje que desea transmitir?**")

iterracion = input("**¿Cuales son las veces que desea transmitirlo?**")
iterracion = int(iterracion)


def mensaje2(mensaje, iterracion):
  i = 1
  while i<=iterracion:
    print(mensaje)
    i += 1
    print(i)




mensaje2()