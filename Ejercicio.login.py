def register():
  while True:
    password = (str(input("** Digite porfavor la contraseña **")))
    user = (str(input("** Digite porfavor el user **")))
    password = password.lower()
    user = user.lower()
  
    
    if user==password:
      print(" Tu contrasñesa no puede ser igual a tu usuario")
      continue
    else:
      return password, user
    
  
password, user = register()


def login(password, user):
  while True:
    
    passwordverification = (str(input("** Digite porfavor la contraseña **")))
    userverification = (str(input("** Digite porfavor el user **")))

    if password == passwordverification and userverification == user:
      print("**Bienvenido al sistema**")
      break
     
    else:
      print(" Algo ha sucedido mal")
      continue
    

    


login (password, user)