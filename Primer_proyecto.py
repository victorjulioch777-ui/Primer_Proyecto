import devspace as d
from utils import pintar as p, colorear_codigo, es_codigo, escribir_lento
import utils as c
import time as t
import os
import subprocess

def limpiar_consola():
    """Limpia la consola del sistema operativo actual.
    
    Detecta el sistema operativo mediante "os.name" y ejecuta el comando
    limpiar la pantalla en terminal.
    
    Utiliza "subprocess.run()" para ejecutar el comando.
    
    Args:
        None
    
    Returns:
        None
    """
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)

def crear_usuario():
    """
    Gestiona la creación de un usuario solicitando datos por consola.

    Solicita al usuario su nombre de usuario, correo electrónico y contraseña,
    y utiliza la función create_user para intentar registrarlo. Repite el proceso
    hasta que el usuario sea creado exitosamente.

    Args:
        None
    
    Returns:
        None
    """
    while True:
        print("===== Creación de usuario =====", c.AZUL)
        username = input(p("Usuario: ", c.AZUL)).strip()
        email = input(p("Email: ", c.AZUL)).strip()
        password = input(p("Contraseña: ", c.AZUL)).strip()

        success,data = d.create_user(username, email, password)

        if success:
            limpiar_consola()
            print(p("\nUsuario creado exitosamente", c.VERDE))
            t.sleep(0.2)
            break
        else:
            limpiar_consola() 
            print(p(f"\n{data}", c.ROJO))
            print(p("Vuelve a intentarlo.", c.ROJO))
            t.sleep(0.2)

def iniciar_sesion():
    """
    Gestiona el inicio de sesión de un usuario mediante consola.

    Solicita al usuario su nombre de usuario y contraseña, y utiliza la función
    login para validar las credenciales. Si el acceso es correcto, retorna el
    nombre de usuario. Si falla, permite reintentar.

    Args:
        None
    
    Returns:
        str: Nombre de usuario si el inicio de sesión es exitoso.
    """
    while True:
        limpiar_consola()  
        print(p("\n===== INICIO DE SESIÓN =====", c.AZUL))
        username = input(p("Usuario: ", c.AZUL)).strip()
        password = input(p("Contraseña: ", c.AZUL)).strip()

        success, data = d.login(username, password)

        if success:
            limpiar_consola() 
            print(p("\nLogin exitoso", c.VERDE_BRIGHT))
            print(p(f"\nBienvenido, {username}", c.VERDE_BRIGHT))
            t.sleep(0.2)
            return username
        else:
            limpiar_consola() 
            print(p("\nUsuario o contraseña incorrectos", c.ROJO))
            print(p("Vuelve a intentarlo.", c.ROJO))
            t.sleep(0.2)

def mostrar_menu():
    """
    Muestra el menú principal de opciones al usuario.
    
    Presenta en consola las diferentes opciones disponibles del sistema,
    como consultas de usuarios, spaces, seguidores y cierre de sesión.

    Args:
        None

    Returns:
        None
    """
    print(p("\n===== MENÚ PRINCIPAL =====", c.AZUL_BRIGHT, c.NEGRITA))
    print(p("1.", c.AMARILLO ) +p(" Consulta de usuarios", c.AZUL))
    print(p("2.", c.AMARILLO ) +p(" Consultar space de un usuario", c.AZUL))
    print(p("3.", c.AMARILLO ) +p(" Crear un space", c.AZUL))
    print(p("4.", c.AMARILLO ) +p(" Crear post", c.AZUL))
    print(p("5.", c.AMARILLO ) +p(" Seguir un space", c.AZUL))
    print(p("6.", c.AMARILLO ) +p(" Gestionar solicitudes", c.AZUL))
    print(p("7.", c.AMARILLO ) +p(" Consulta de space seguidos", c.AZUL))
    print(p("8.", c.AMARILLO ) +p(" Consulta de seguidores de mis spaces", c.AZUL))
    print(p("9.", c.AMARILLO ) +p(" Consulta de seguidores", c.AZUL))
    print(p("10.", c.AMARILLO ) +p(" Consulta de post por space", c.AZUL))
    print(p("11.", c.AMARILLO ) +p(" Cerrar sesión", c.AZUL))

def ver_users():
    """
    Obtiene y muestra la lista de usuarios registrados.

    Llama a la función get_users para recuperar los usuarios. Si la operación
    es exitosa, muestra la lista numerada en consola. Si no hay usuarios o ocurre
    un error, informa al usuario.

    Args:
        None

    Returns:
        None
    """
    success, data = d.get_users()
    
    if success:
        if len(data) == 0:
            print(p("No existe ningun usuario.", c.ROJO))
            t.sleep(0.2)
        else:
            print("\n===== LISTA DE USUARIOS =====")
            for i, user in enumerate(data, start=1):
                print(f"{i}. {user}")
                t.sleep(0.2)
    else:
        print(p(f"\n{data}", c.ROJO))
        t.sleep(0.2)

def ver_spaces_por_usuario():
    """
    Obtiene y muestra los spaces asociados a un usuario.

    Solicita el nombre de usuario por consola y utiliza la función
    get_spaces_by_user para recuperar los spaces vinculados. Si la operación
    es exitosa, muestra la lista numerada. Si no hay spaces o ocurre un error,
    informa al usuario.

    Args:
        None

    Returns:
        None
    """
    print(p("\n===== VER SPACE POR USUARIO =====", c.NEGRITA, c.AZUL))
    username =  input(p("\nIngresa el usuario del space: ", c.VERDE)).strip()   

    success, data = d.get_spaces_by_user(username)
    
    if success:
        if len(data) == 0:
            print(p("No existe ningun space.", c.ROJO))
            t.sleep(0.2)
        else:
            print(p(f"\n===== LISTA DE SPACES DEL USUARIO {username.upper()} =====", c.NEGRITA, c.AZUL))
            for i, space in enumerate(data, start=1):
                print(f"{i}. {space}")
                t.sleep(0.2)
    else:
        print(p(f"\n{data}", c.ROJO))
        t.sleep(0.2)

def crear_space(usuario):
    """
    Esta funcion se encarga de solicitar al usuario, nombre y descripción 
    y luego intenta crear un space.

    Args:
        usuario (str): Nombre del dueño del space.

    Returns:
        None
    """
    print(p("\n ===Crear un space===", c.NEGRITA, c.AZUL))
    username = input(p("Ingresa tu usuario: ", c.AZUL)).strip()
    name = input(p("Ingresa el nombre del nuevo espacio: ", c.AZUL)).strip()
    description = input(p("Ingresa la descripcion del nuevo espacio: ", c.AZUL)).strip()
    visibility = input(p("Ingresa la visibilidad del nuevo espacio(public): ", c.AZUL)).strip()
    
    success, data = d.create_space(usuario, name, description)

    if success:
        print("\nSpace creado exitosamente.")
        t.sleep(0.2)
    else:
        print(p(f"\n{data}", c.ROJO))
        print(p("Vuelve a intetarlo", c.AMARILLO))  
        t.sleep(0.2)

def crear_post():
    """
    Esta funcion se encarga de crear un nuevo post dentro de un space.

    Le solicita al usario el ID del space,titulo,contenido y tipo de post
    y luego intenta crear el post.

    Args:
        None

    Returns:
        None
    """
    print(p("\n===== Crear un post =====", c.NEGRITA, c.AZUL))
    space_id = int(input(p("Ingresa el space ID al que pertenecerá el nuevo post: ", c.AZUL)))
    title = input(p("Ingresa el Titulo del nuevo post: ", c.AZUL))
    content = input(p("Ingresa el Contenido del nuevo post: ", c.AZUL))
    post_type = input(p("Ingresa el Tipo de post (post): ", c.AZUL))

    success, data = d.create_post(space_id, title, content, post_type)

    if success:
        print(p("\nPost creado exitosamente", c.VERDE))
        print(data)
        t.sleep(0.2)
    else:
        print(p(f"\n{data}", c.ROJO))
        print(p("Vuelve a intentarlo", c.AMARILLO))
        t.sleep(0.2)

def seguir_space(usuario):
    """
    Permite a un usuario seguir un space.

    Solicita el nombre de usuario y el ID del space por consola, y utiliza la
    función follow_space para registrar la acción. Informa si la operación fue
    exitosa o si ocurrió un error.

    Args:
        None

    Returns:
        None
    """
    print(p("\n===== Seguir un space =====\n", c.AZUL, c.NEGRITA))
    user_space = input(p("Ingrese el nombre del usuario que quieres seguir:", c.AZUL))
    success, data = d.get_spaces_by_user(user_space)

    if success:
        print(p("El usuario: ", c.AZUL) + user_space, p(" tiene los siguiente Spaces", c.AZUL))
        print(p("===== SPACES =====", c.NEGRITA, c.AZUL))
        for space in data:
            id_espacio, nombre, descripcion = space
            print(p("ID: ", c.AZUL) + f"{id_espacio}")
            print(p("Nombre: ", c.AZUL) + f"{nombre}")
            print(p("Descripción: ", c.AZUL) + f"{descripcion}\n")
            t.sleep(0.2)
    else:
        print(p("El", c.ROJO) + f"{user_space}" + p("que ingreso no tiene Spaces", c.ROJO))
        t.sleep(0.2)

    space_id = input(p("Ingresa el space id que deseas seguir: ", c.AZUL)).strip()

    success, data = d.follow_space(usuario, space_id)

    if success:
        print(p("\nSpace seguido exitosamente", c.VERDE))
        t.sleep(0.2)
    else:
        print(p(f"\n{data}", c.ROJO))
        print(p("Vuelve a intentarlo.", c.ROJO))
        t.sleep(0.2)

def gestion_solicitudes(usuario):
    """Se encarga de gestionar las solicitudes de seguimiento 
    entre los usuarios de un space.
    
    Esta función muestra un menú en consola para que el usuario
    actual procese la solicitud de seguimiento sobre un space determinado.

    Args:
        usuario (_type_): Nombre del usuario que está procesando la solicitud.
        
    Returns:
        None
    """
    ciclo = True
    while ciclo == True:
        print(p("GESTION DE SOLICITUDES DE SEGUIMIENTO", c.AZUL, c.NEGRITA))
        print(p("Ingrese el ID SPACE que desea seguir", c.AMARILLO))
        space_id = int(input(p("ID del space: ", c.VERDE)))

        print(p("Nombre de usuario propietario del space", c.AMARILLO))
        user_que_solicita = input(p("Nombre: ", c.VERDE))

        print(p(usuario, c.MAGENTA_BRIGHT) + p(" ID del space = ", c.MAGENTA_BRIGHT) + p(space_id, c.CYAN_BRIGHT) + p(": PROCESA A: ", c.MAGENTA_BRIGHT) + p(user_que_solicita, c.CYAN_BRIGHT))
        print(p("1. Aceptar", c.VERDE))
        print(p("2. Rechazar", c.ROJO))
        print("3. Salir")

        opcion = int(input(p("opcion: ", c.VERDE)))
        if opcion == 1:
            estado = True
            ciclo = False
        elif opcion == 2:
            estado = False
            ciclo = False
        else:
            print("No existe esa opcion", c.ROJO)
    
    success, data = d.handle_follower(usuario, space_id, user_que_solicita, estado)

    if success == True:
        print(p("Se realizo correctamente la solicitud a", c.VERDE), p(user_que_solicita, c.CYAN_BRIGHT))
        t.sleep(0.2)
    else:
        print(p("Algo falló, no se pudo realizar la solicitud a:", c.ROJO), p(user_que_solicita, c.CYAN_BRIGHT))
        t.sleep(0.2)

def ver_spaces_seguidos(usuario):
    """
    Obtiene y muestra los spaces que sigue un usuario.

    Recibe el nombre de usuario como parámetro y utiliza la función
    get_following_spaces para recuperar los spaces que sigue. Si la operación
    es exitosa, muestra la lista numerada. Si no sigue ningún space o ocurre
    un error, informa al usuario.

    Args:
        usuario (str): Nombre de usuario.

    Returns:
        None
    """
    success, data = d.get_following_spaces(usuario)

    if success:
        if len(data) == 0:
            print("No sigues ningún space.")
            t.sleep(0.2)
        else:
            print(p("\n===== SPACES QUE SIGO =====", c.NEGRITA, c.AZUL))
            for i, space in enumerate(data, start=1):
                print(f"{i}. {space}")
                t.sleep(0.2)
    else:
        print(p(f"\n{data}", c.ROJO))
        t.sleep(0.2)

def ver_seguidores_de_mis_spaces(usuario):
    """
    Muestra las solicitudes/seguidores de los spaces del usuario actual.

    Args:
        usuario (str): Nombre de usuario.

    Returns:
        None
    """
    success, data = d.get_followers(usuario)

    print(p("\n===== SEGUIDORES DE MIS SPACES =====", c.NEGRITA, c.AZUL))

    if success:
        if len(data) == 0:
            print("No hay seguidores para mostrar.")
            t.sleep(0.2)
        else:
            if len(data) > 0 and not isinstance(data[0], list):
                data = [data]

            for i, follower in enumerate(data, start=1):
                username_seguidor = follower
                id_space = follower
                nombre_space = follower
                estado = follower

                if estado == True:
                    estado_texto = "Aceptado"
                else:
                    estado_texto = "Pendiente/Rechazado"

                print(f"{i}. Seguidor: {username_seguidor}")
                print(f"   ID Space: {id_space}")
                print(f"   Space: {nombre_space}")
                print(f"   Estado: {estado_texto}")
                print("-" * 40)
                t.sleep(0.2)
    else:
        print(p(f"\n{data}", c.ROJO))
        t.sleep(0.2)

def ver_seguidores(usuario):
    """
    Obtiene y muestra los seguidores de un usuario.

    Recibe el nombre de usuario como parámetro y utiliza la función
    get_followers para recuperar la lista de seguidores. Si la operación
    es exitosa, muestra los seguidores numerados. Si no hay seguidores o
    ocurre un error, informa al usuario.

    Args:
        usuario (str): Nombre de usuario.

    Returns:
        None
    """
    success, data = d.get_followers(usuario)
    
    if success:
        if len(data) == 0:
            print("No hay seguidores para mostrar.")
            t.sleep(0.2)
        else:
            print(p("\n===== SEGUIDORES =====", c.NEGRITA, c.AZUL))
            for i, follower in enumerate(data, start=1):
                print(f"{i}. {follower}")
            t.sleep(0.2)
    else:
        print(p(f"\n{data}", c.ROJO))
        t.sleep(0.2)

def ver_posts_por_space():
    """
    Obtiene y muestra los posts de un space para un usuario específico.

    Solicita el ID del space y el nombre de usuario por consola, y utiliza la
    función get_posts para recuperar los posts asociados. Si la operación es
    exitosa, muestra los posts numerados. Si no hay posts o ocurre un error,
    informa al usuario.

    Args:
        None

    Returns:
        None
    """
    print(p("\n===== Post por Space =====", c.NEGRITA, c.AZUL))

    user_space = input(p("Ingrese el nombre dueño del Space: ", c.AZUL))
    success, data = d.get_spaces_by_user(user_space)

    if success:
        print(p("\n===== Spaces =====", c.AZUL, c.NEGRITA))
        print(p("El usuario: ", c.AZUL) + user_space + p(" tiene los siguientes Spaces\n", c.AZUL))

        for space in data:
            id_espacio, nombre, descripcion = space
            print(p("ID: ", c.AZUL) + f"{id_espacio}")
            print(p("Nombre: ", c.AZUL) + f"{nombre}")
            print(p("Descripción: ", c.AZUL) + f"{descripcion}\n")
            t.sleep(0.2)
    else:
        print(p("El usuario ", c.ROJO) + f"{user_space} " + p("no tiene Spaces", c.ROJO))
        return

    try:
        space_id = int(input(p("Ingrese el space ID del que desea obtener los posts: ", c.AZUL)))
    except ValueError:
        print(p("\n===== Post por Space =====", c.NEGRITA, c.AZUL))
        print(p("Debe ingresar un número válido para el Space ID.", c.ROJO))
        t.sleep(0.2)
        return

    success2, data2 = d.get_posts(space_id, user_space)

    if success2:
        posts = data2[1] if isinstance(data2, (list, tuple)) and len(data2) > 1 else data2

        if not posts or len(posts) == 0:
            print(p("\n===== Post por Space =====", c.NEGRITA, c.AZUL))
            print(p("No hay posts para mostrar.", c.VERDE))
            t.sleep(0.2)
        else:
            i = 0

            while True:
                post = posts[i]
                id_post = post[0]
                titulo = post[1]
                contenido = post[2]
                tipo = post[3]

                if es_codigo(contenido):
                    contenido_mostrar = colorear_codigo(contenido)
                else:
                    contenido_mostrar = contenido

                print(p("\n===== Post del Space =====", c.NEGRITA, c.AZUL))
                print(f"Post {i + 1} de {len(posts)}")
                print(f"Tipo de POST: [{tipo}]")
                print(f"Título: {titulo}")
                print(f"Post ID: {id_post}")
                print("Contenido:\n")
                escribir_lento(contenido_mostrar)

                print()
                print(
                    p("1) Ver post anterior   ", c.AMARILLO) +
                    p("2) Ver siguiente post   ", c.VERDE) +
                    p("3) Salir", c.AZUL)
                )

                opcion = input(p("> ", c.VERDE))

                if opcion == "1":
                    if i > 0:
                        i -= 1
                elif opcion == "2":
                    if i < len(posts) - 1:
                        i += 1
                elif opcion == "3":
                    break
                else:
                    print(p("Opción no válida", c.ROJO))
                    t.sleep(0.2)
    else:
        print(p(f"\n{data}", c.ROJO))
        t.sleep(0.2)

def menu_principal(usuario):
    """
    Controla el flujo del menú principal del sistema para un usuario autenticado.

    Recibe el nombre de usuario y muestra el menú de opciones de forma continua.
    Según la opción seleccionada, ejecuta diferentes funcionalidades como ver usuarios,
    consultar spaces, seguir spaces, ver seguidores o cerrar sesión.

    Args:
        usuario (str): Nombre de usuario autenticado.

    Returns:
        None
    """ 
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            limpiar_consola()
            ver_users()

        elif opcion == "2":
            limpiar_consola()
            ver_spaces_por_usuario()

        elif opcion == "3":
            limpiar_consola()
            crear_space(usuario)

        elif opcion == "4":
            limpiar_consola()
            crear_post()

        elif opcion == "5":
            limpiar_consola()
            seguir_space(usuario)

        elif opcion == "6":
            limpiar_consola() 
            gestion_solicitudes(usuario)
        
        elif opcion == "7":
            limpiar_consola()
            ver_spaces_seguidos(usuario)

        elif opcion == "8":
            limpiar_consola() 
            ver_seguidores_de_mis_spaces(usuario)
        
        elif opcion == "9":
            limpiar_consola() 
            ver_seguidores(usuario)
        
        elif opcion == "10":
            limpiar_consola() 
            ver_posts_por_space()

        elif opcion == "11":
            print(p("\nSesión cerrada.", c.VERDE))
            break

        else:
            print(p(" Opción inválida. Intente de nuevo.", c.ROJO))
            t.sleep(0.2)

def main():
    """
    Controla el flujo principal de la aplicación.

    Muestra el menú de bienvenida y permite al usuario iniciar sesión,
    registrarse o salir del sistema.

    Args:
        None

    Returns:
        None
    """
    while True:
        limpiar_consola()
        print(p("\n===== BIENVENIDO A DevSpace =====", c.NEGRITA, c.VERDE, c.FONDO_BLANCO))
        print(p("1. ", c.AMARILLO) + p("Iniciar Sesion", c.AZUL))
        print(p("2. ", c.AMARILLO) + p("Registrarse", c.AZUL))
        print(p("3. ", c.AMARILLO) + p("Salir", c.AZUL))
        login = input(p("Opcion: ", c.VERDE))
        if login == "1": 
            limpiar_consola() 
            usuario = iniciar_sesion()
            menu_principal(usuario)
        elif login == "2":
            limpiar_consola()  
            print(crear_usuario())
        elif login == "3":
            limpiar_consola()  
            print(p("Salió del sistema", c.ROJO))
            exit()
        else:
                limpiar_consola() 
                print(p("\nSucedio un error", c.ROJO))
                print(p("Vuelve a intentarlo.", c.ROJO))
                input(p("Presione enter para Volver a intentar ", c.VERDE))
                t.sleep(0.2)

if __name__ == "__main__":
    main()
