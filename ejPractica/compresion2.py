vocales = ['A', 'E', 'I', 'O', 'U']
Nombres = ['Juan', 'Pedro', 'Alberto', 'Adrian', 'Isabela', 'Ulises', 'Irene', 'Sofia', 'Andrea', 'Nerea', 'Maria']

chicos, chicas = [], []

[chicas.append(nombre) if nombre.endswith('a') or nombre.endswith('e') else chicos.append(nombre) for nombre in Nombres]