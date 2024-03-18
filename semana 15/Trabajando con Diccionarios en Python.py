# crear el dicionario inicial con informacion _ personal fistica

informacion_personal= {
"nombre": "Carmen",
"edad": 30,
"ciudad":"Shsuhufindi"}

#Accede al valor asociado con la clave "ciudad" y modifícalo.
informacion_personal ["ciudad"]="Shsuhufindi"

#Agrega una nueva clave-valor al diccionario que represente la "profesion" de la persona
informacion_personal ["profesion"]="tecnologias de la informacion"

#Verifica si la clave "telefono" existe en el diccionario. Si no existe, agrégala con un número de teléfono ficticio.
informacion_personal ["telefono"]="9876543210" # numero de telefono fisticio

# Elimina la clave "edad" del diccionario, ya que esa información no es necesaria.
informacion_personal ["edad"]

# Imprime el diccionario resultante después de realizar todas las operaciones.
print (informacion_personal)
