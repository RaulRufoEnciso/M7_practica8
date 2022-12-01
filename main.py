import delete
import update
import insertar
import select

pregunta = input("Que quiere hacer? ")

if (pregunta == "eliminar"):
    delete.delete()
elif(pregunta == "modifica"):
    update.update()
elif(pregunta == "añadir"):
    insertar.insert()
elif(pregunta == "mostrar"):
    select.select()
else:
    print("Las opciones para ejecutar son: "
          "eliminar"
          "modifica"
          "añadir"
          "mostrar")

print(pregunta)


