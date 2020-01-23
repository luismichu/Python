import json

cadena = """{"Fruteria":
 [
  {"Fruta":
   [
    {"Nombre":"Manzana","Cantidad":10},
    {"Nombre":"Pera","Cantidad":20},
    {"Nombre":"Naranja","Cantidad":30}
   ]
  },
  {"Verdura":
   [
    {"Nombre":"Lechuga","Cantidad":80},
    {"Nombre":"Tomate","Cantidad":15},
    {"Nombre":"Pepino","Cantidad":50}
   ]
  }
 ]
}"""

with open("archivo.json", "w") as fic:
	json.dump(cadena, fic)