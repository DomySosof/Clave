import qrcode

def mostrar_codigo_qr(clave):
    qr = qrcode.QRCode(version=1, box_size=30, border=1)
    qr.add_data(clave)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.show()



claves = [
        ("Binance"," hola mundo"), #1

        ]


while True:
    #primera inteacion para que el usuario seleccione la clave que desea ver
    a = input(
        "\n 1 = binance \t \t \t" 
        #input del usuarios
        " \n Seleccione una opción: \t")

    # ...
    if a.isdigit() and int(a) <= len(claves):
        clave = claves[int(a) - 1]
        (f"\nLa clave es: {clave[1]}\n")
        mostrar_codigo_qr(clave[1])

    else:
        print("\n Opción inválida\n")


    b = input("¿Desea consultar otra clave?\n\nSi\nNo\n")

    if b.lower() == "no":
        print("¡Que tengas un lindo día!")
        break
    elif b.lower() != "si":
        print("\nOpción inválida\n")
        continue


print(" \n \n \t \t  Presione Enter para salir")
input()
