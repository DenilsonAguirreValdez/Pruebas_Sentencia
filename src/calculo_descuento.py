# src/calculo_descuento.py

#PARA ACTIVAR EL ENTORNO VIRTUAL: .\env\Scripts\Activate.ps1
#EJECUTAR LAS PRUEBAS: coverage run --source=src -m unittest discover -s tests
#GENERAR EL INFORME DE COBERTURA: coverage report
#GENERAR UN INFORME HTML: coverage html

def calcular_descuento(precio, es_vip):
    if es_vip:
        precio_final = precio * 0.8
    else:
        precio_final = precio * 0.9
    return precio_final

#def calcular_descuento(precio, es_vip):
#    if es_vip:
#        precio_final = precio * 0.8
#        # Agregamos una línea que nunca se ejecutará en las pruebas
#        print("Descuento VIP aplicado")
#    else:
#        precio_final = precio * 0.9
#    return precio_final
