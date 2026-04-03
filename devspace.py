from urllib import response

import requests

BASE_URL = "http://leoviquez.com/devspaces"


def to_list(data:dict)->list:
    """Convierte cualquier estructura JSON a listas puras:
    - dict  → lista de valores (recursivo)
    - list  → procesa cada elemento
    - otros → se dejan igual

    args:
        data: cualquier estructura JSON (dict, list, o valor simple)
    returns:
        lista pura (sin claves de dict)
    """
    if isinstance(data, dict):
        return [to_list(v) for v in data.values()]
    elif isinstance(data, list):
        return [to_list(v) for v in data]
    else:
        return data


def _handle_response(response: requests.Response) -> tuple:
    """Maneja la respuesta de la API, intentando extraer un mensaje de éxito y los datos relevantes.

    Args:
        response (requests.Response): La respuesta de la API.

    Returns:
        tuple: Una tupla con un booleano indicando el éxito de la operación y una lista con los datos relevantes.
    """
    try:
        json_data = response.json()
    except:
        return False, [["Respuesta no es JSON", response.text]]

    # boolean directo (login)
    if isinstance(json_data, bool):
        return json_data, [json_data]

    success = response.status_code == 200 and json_data.get("success", False)

    # priorizar data
    if isinstance(json_data, dict) and "data" in json_data:
        data = json_data["data"]
    else:
        data = json_data

    return success, to_list(data)


# ---------------- USERS ----------------

def create_user(username: str, email: str, password: str) -> tuple:
    """Crea un nuevo usuario en el sistema de DevSpace utilizando una solicitud POST a la API correspondiente.

    Args:
        username (str): Nombre de usuario del nuevo usuario.
        email (str): Correo electrónico del nuevo usuario (No permite repeticiones).
        password (str): Contraseña del nuevo usuario.

    Returns:
        tuple: Una tupla con un booleano indicando el éxito de la operación y una lista con los datos relevantes (por ejemplo, mensaje de error o información del usuario creado).
    """
    url = f"{BASE_URL}/create_user.php"

    try:
        response = requests.post(url, json={
            "username": username,
            "email": email,
            "password": password
        })
        return _handle_response(response)
    except Exception as e:
        return False, [[str(e)]]


def get_users() -> tuple:
    """Obtiene la lista de usuarios registrados en el sistema de DevSpace.

    Returns:
        tuple: Una tupla con un booleano indicando el éxito de la operación y una lista con los datos relevantes (por ejemplo, información de los usuarios en formato: [<nombre de usuario>,<correo del usuario>]).
    """

    url = f"{BASE_URL}/get_users.php"

    try:
        response = requests.get(url)
        return _handle_response(response)
    except Exception as e:
        return False, [[str(e)]]


# ---------------- SPACES ----------------

def get_spaces_by_user(username: str) -> tuple:
    """Obtiene los spaces asociados a un usuario específico en el sistema de DevSpace utilizando una solicitud POST a la API correspondiente.

    Args:
        username (str): Nombre de usuario del cual se desean obtener los spaces asociados.

    Returns:
        tuple: Una tupla con un booleano indicando el éxito de la operación y una lista con los datos relevantes (por ejemplo, información de los spaces asociados al usuario en formato: [<id del espacio>, <nombre del espacio>, <descripción del espacio>]).
    """
    url = f"{BASE_URL}/get_spaces_by_user.php"

    try:
        response = requests.post(url, json={"username": username})
        return _handle_response(response)
    except Exception as e:
        return False, [[str(e)]]


def create_space(username: str, name: str, description: str = "", visibility: str = "public") -> tuple:
    """Crea un nuevo espacio en el sistema de DevSpace utilizando una solicitud POST a la API correspondiente.

    Args:
        username (str): Nombre de usuario del cual se desean obtener los spaces asociados.
        name (str): Nombre del nuevo espacio.
        description (str, optional): Descripción del nuevo espacio. Defaults to "".
        visibility (str, optional): Visibilidad del nuevo espacio. Defaults to "public".

    Returns:
        tuple: Una tupla con un booleano indicando el éxito de la operación y una lista con los datos relevantes (por ejemplo, mensaje de error o información del espacio creado).
    """

    url = f"{BASE_URL}/create_space.php"

    try:
        response = requests.post(url, json={
            "username": username,
            "name": name,
            "description": description,
            "visibility": visibility
        })
        return _handle_response(response)
    except Exception as e:
        return False, [[str(e)]]


# ---------------- POSTS ----------------

def create_post(space_id: int, title: str, content: str, post_type: str) -> tuple:
    """Crea un nuevo post en el sistema de DevSpace utilizando una solicitud POST a la API correspondiente.

    Args:
        space_id (int): ID del espacio al que pertenece el nuevo post.
        title (str): Título del nuevo post.
        content (str): Contenido del nuevo post.
        post_type (str): Tipo del nuevo post.

    Returns:
        tuple: Una tupla con un booleano indicando el éxito de la operación y una lista con los datos relevantes (por ejemplo, mensaje de error o información del post creado, el formato del post es [<Estado de creación booleana]>,<id del post>,<tipo del post>]).
    """

    url = f"{BASE_URL}/create_post.php"

    try:
        response = requests.post(url, json={
            "space_id": space_id,
            "title": title,
            "content": content,
            "type": post_type
        })
        return _handle_response(response)
    except Exception as e:
        return False, [[str(e)]]


def get_posts(space_id: int, username: str) -> tuple:
    """Obtiene la lista de posts asociados a un espacio específico en el sistema de DevSpace utilizando una solicitud POST a la API correspondiente.        
    
    args:
        space_id (int): ID del espacio del cual se desean obtener los posts asociados.
        username (str): Nombre de usuario del cual se desean obtener los posts asociados.
    returns:
        tuple: Una tupla con un booleano indicando el éxito de la operación y una lista con los datos relevantes (por ejemplo, información de los posts asociados al espacio en formato: [<id del post>, <título del post>, <contenido del post>, <tipo del post>]).
    """
    url = f"{BASE_URL}/get_posts_by_space.php"

    try:
        response = requests.post(url, json={
            "space_id": space_id,
            "username": username
        })
        return _handle_response(response)
    except Exception as e:
        return False, [[str(e)]]


# ---------------- FOLLOWERS ----------------

def follow_space(username: str, space_id: int) -> tuple:
    """Sigue un espacio específico en el sistema de DevSpace utilizando una solicitud POST a la API correspondiente.

    Args:
        username (str): Nombre de usuario que desea seguir el espacio.
        space_id (int): ID del espacio que se desea seguir.

    Returns:
        tuple: Una tupla con un booleano indicando el éxito de la operación y una lista con los datos relevantes (por ejemplo, mensaje de error o información sobre el seguimiento del espacio, La lista de respuesta tiene el formato [<Estado de creación booleana]>,<estado actual de aceptación booleana]>,<Mesaje de estado>]).
    """

    url = f"{BASE_URL}/follow_space.php"

    try:
        response = requests.post(url, json={
            "username": username,
            "space_id": space_id
        })
        return _handle_response(response)
    except Exception as e:
        return False, [[str(e)]]


def get_followers(username: str) -> tuple:
    """Obtiene la lista de seguidores asociados a un espacio específico en el sistema de DevSpace utilizando una solicitud POST a la API correspondiente.
    
    args:
        username (str): Nombre de usuario del cual se desean obtener los seguidores asociados.

    returns:
        tuple: Una tupla con un booleano indicando el éxito de la operación y una lista con los datos relevantes (por ejemplo, información de los seguidores asociados al espacio en formato: [<nombre de usuario>, <id del sapace>, <nombre del espacio>, <estado de aceptación>]).
    """

    url = f"{BASE_URL}/get_followers_by_owner.php"

    try:
        response = requests.post(url, json={"username": username})
        return _handle_response(response)
    except Exception as e:
        return False, [[str(e)]]

def get_following_spaces(username: str) -> tuple:
    """Obtiene la lista de espacios que un usuario específico está siguiendo en el sistema de DevSpace utilizando una solicitud POST a la API correspondiente.

    args:
        username (str): Nombre de usuario del cual se desean obtener los espacios seguidos.

    returns:
        tuple: Una tupla con un booleano indicando el éxito de la operación y una lista con los datos relevantes (por ejemplo, información de los espacios seguidos en formato: [<id del espacio>, <nombre del espacio>]).
    """

    url = f"{BASE_URL}/get_following_spaces.php"

    try:
        response = requests.post(url, json={
            "username": username
        })
        return _handle_response(response)
    except Exception as e:
        return False, [[str(e)]]
# ---------------- AUTH ----------------

def login(username: str, password: str) -> tuple:
    """Realiza el proceso de inicio de sesión para un usuario específico en el sistema de DevSpace utilizando una solicitud POST a la API correspondiente.
    Args:
        username (str): Nombre de usuario del usuario que desea iniciar sesión.
        password (str): Contraseña del usuario que desea iniciar sesión.
    Returns:
        tuple: Una tupla con un booleano indicando el éxito de la operación y una lista con los datos relevantes (por ejemplo, mensaje de error o información de inicio de sesión).
    """

    url = f"{BASE_URL}/login_validate.php"

    try:
        response = requests.post(url, json={
            "username": username,
            "password": password
        })
        return _handle_response(response)
    except Exception as e:
        return False, [[str(e)]]
    
def handle_follower(username: str, space_id: int, follower_username: str, accepted: bool):
    """
    Gestiona una solicitud de seguimiento (aceptar o rechazar).

    Parámetros:
        username (str): Usuario propietario del space
        space_id (int): ID del space
        follower_username (str): Usuario que solicita seguir
        accepted (bool): True para aceptar, False para rechazar

    Retorna:
        list: [True] si la operación fue exitosa
              [False] si ocurrió un error
    """
    try:
        response = requests.post(
            f"{BASE_URL}/handle_follower_request.php",
            json={
                "username": username,
                "space_id": space_id,
                "follower_username": follower_username,
                "accepted": accepted
            }
        )
        return _handle_response(response)    
    except Exception as e:
        return False, [[str(e)]]