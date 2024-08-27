usuarios_registrados = []
reservas = []

def registrar_usuario():
    """Permite a un nuevo usuario registrarse en el sistema."""
    print("Registro de Usuario")
    nombre_usuario = input("Ingrese el nombre de usuario: ").strip()

    if nombre_usuario in usuarios_registrados:
        print("El nombre de usuario ya está registrado.")
    else:
        usuarios_registrados.append(nombre_usuario)
        print(f"Usuario '{nombre_usuario}' registrado exitosamente.")

def reservar_viaje():
    """Permite a un usuario registrado reservar un viaje."""
    print("Reserva de Viaje")
    nombre_usuario = input("Ingrese su nombre de usuario: ").strip()

    if nombre_usuario not in usuarios_registrados:
        print("Usuario no registrado. Por favor, regístrese primero.")
        if input("¿Desea registrarse ahora? (s/n): ").strip().lower() == 's':
            registrar_usuario()
        else:
            return
    
    destino = input("Ingrese el destino del viaje: ").strip()
    fecha = input("Ingrese la fecha del viaje (dd/mm/yyyy): ").strip()

    reservas.append({
        'usuario': nombre_usuario,
        'destino': destino,
        'fecha': fecha
    })

    print("Reserva realizada exitosamente.")

def ver_reservas():
    """Permite a un usuario ver todas sus reservas."""
    print("Ver Reservas")
    nombre_usuario = input("Ingrese su nombre de usuario: ").strip()

    if nombre_usuario not in usuarios_registrados:
        print("Usuario no registrado. No se pueden mostrar reservas.")
        return

    reservas_usuario = [r for r in reservas if r['usuario'] == nombre_usuario]
    if not reservas_usuario:
        print("No tiene reservas.")
    else:
        for i, reserva in enumerate(reservas_usuario):
            print(f"{i + 1}. Destino: {reserva['destino']}, Fecha: {reserva['fecha']}")

def cancelar_reserva():
    """Permite a un usuario cancelar una de sus reservas."""
    print("\nCancelar Reserva")
    nombre_usuario = input("Ingrese su nombre de usuario: ").strip()

    if nombre_usuario not in usuarios_registrados:
        print("Usuario no registrado. No se pueden cancelar reservas.")
        return

    reservas_usuario = [r for r in reservas if r['usuario'] == nombre_usuario]
    if not reservas_usuario:
        print("No tiene reservas para cancelar.")
        return

    ver_reservas()
    try:
        indice = int(input("Ingrese el número de la reserva que desea cancelar: ")) - 1
        if 0 <= indice < len(reservas_usuario):
            reserva_a_cancelar = reservas_usuario[indice]
            reservas.remove(reserva_a_cancelar)
            print("Reserva cancelada exitosamente.")
        else:
            print("Número de reserva inválido.")
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número.")

def menu_principal():
    """Muestra el menú principal y gestiona las opciones seleccionadas por el usuario."""
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar Usuario")
        print("2. Reservar Viaje")
        print("3. Ver Reservas")
        print("4. Cancelar Reserva")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            reservar_viaje()
        elif opcion == '3':
            ver_reservas()
        elif opcion == '4':
            cancelar_reserva()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 5.")

if __name__ == "__main__":
    menu_principal()