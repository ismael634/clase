lista_invitados=['bad', 'auron', 'pepe']
print(f"solo puedo invitar a dos personas a cenar")
ultimo_valor=lista_invitados.pop()
print(f" {ultimo_valor.title()} al final no puedes venir")
print(f"{lista_invitados[0]} tu sigues invitado")
print(f"{lista_invitados[1]} tu sigues invitado")
del lista_invitados[1]
del lista_invitados[0]
print(lista_invitados)
