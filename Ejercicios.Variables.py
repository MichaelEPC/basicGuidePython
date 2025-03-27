def message_creator(text):
  if text == "computadora":
     return"Con mi computadora puedo programar usando Python"

  if text == "celular":
      return "En mi celular puedo aprender usando la app de Platzi"

  if text == "cable":
      return "¡Hay un cable en mi bota!"
    
  else:
      return "Artículo no encontrado"
         
  

text = 'computadora'
response = message_creator(text)
print(response)

text = 'celular'
response = message_creator(text)
print(response)

text = 'cable'
response = message_creator(text)
print(response)

text = 'xd'
response = message_creator(text)
print(response)

