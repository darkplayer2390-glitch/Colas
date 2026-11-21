from colas import Cola


def menu():
    cola = Cola()

    while True:
        print("\nMENÚ DE OPCIONES DE LA COLA")
        print("1. Insertar")
        print("2. Extraer")
        print("3. Mostrar")
        print("4. Buscar")
        print("5. Mostrar el primero")
        print("6. Mostrar el último")
        print("7. Cantidad")
        print("8. Vacía")
        print("9. Vaciar")
        print("10. Sumar")
        print("11. Salir")

        opcion = input("Selecciona una opción del menú: ")

        match opcion:
            case "1":
                try:
                    valor = int(input("Ingresa un número entero: "))
                    cola.insertar(valor)
                    print(f"-> Elemento {valor} insertado con éxito.")
                except ValueError:
                    print("Error: Debes ingresar un número entero válido.")

            case "2":
                resultado = cola.extraer()
                if resultado == "Cola Vacía":
                    print("-> Error: Cola Vacía, no se puede extraer.")
                else:
                    print(f"-> Elemento extraído: {resultado}")

            case "3":
                if cola.vacia():
                    print("-> Cola Vacía.")
                else:
                    cola.imprimir()

            case "4":
                try:
                    valor_buscado = int(input("Ingresa el número a buscar: "))
                    if cola.buscar(valor_buscado):
                        print(
                            f"-> El elemento {valor_buscado} sí se encuentra en la cola."
                        )
                    else:
                        print(
                            f"-> El elemento {valor_buscado} no se encuentra en la cola."
                        )
                except ValueError:
                    print("Error: Debes ingresar un número entero válido.")

            case "5":
                primero = cola.mostrar_primero()
                if primero == "Cola Vacía":
                    print("-> Error: Cola Vacía.")
                else:
                    print(f"-> El primer elemento es: {primero}")

            case "6":
                ultimo = cola.mostrar_ultimo()
                if ultimo == "Cola Vacía":
                    print("-> Error: Cola Vacía.")
                else:
                    print(f"-> El último elemento es: {ultimo}")

            case "7":
                print(f"-> Cantidad de elementos en la cola: {cola.cantidad()}.")

            case "8":
                if cola.vacia():
                    print("-> La cola está VACÍA.")
                else:
                    print("-> La cola NO está vacía.")

            case "9":
                cola.vaciar()
                print("-> La cola ha sido vaciada.")

            case "10":
                if cola.vacia():
                    print("-> Cola Vacía, no hay elementos para sumar.")
                else:
                    suma = cola.sumar()
                    print(f"-> La suma de los elementos en la cola es: {suma}")

            case "11":
                print("Adiós! Gracias por usar el programa.")
                break

            case _:
                print("Opción inválida. Inténtalo de nuevo.")


if __name__ == "__main__":
    menu()