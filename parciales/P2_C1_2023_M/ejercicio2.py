import pandas as pd
from random import sample

def read_file(path):
    """
    Leo archivo .csv y retorno un DataFrame
    """
    return pd.read_csv(path, encoding='latin1')


def get_random_password(first_name, last_name, chars, length):
    """
    Genero contraseña aleatoria dados
    Pre:
        - first_name: string, nombre de la persona
        - last_name: string, apellido de la persona
        - chars: string, caracteres para generar contraseña
        - length: largo de contraseña a generar
    Post:
        - Retorno string con contraseña generada (sin validar)
    """
    password = [first_name[0], last_name[0]]
    chars_sample = sample(chars, k=length - 2)
    password += chars_sample
    password = ''.join(sample(password, k=length))
    return password


def generate_password_alpha(first_name, last_name, length):
    """
    Genero contraseña alfabética
    Pre:
        - first_name: string, nombre de la persona
        - last_name: string, apellido de la persona
        - length: largo de contraseña a generar
    Post:
        - Retorno string con contraseña generada (válida)
    """

    chars = 'abcedfghijklmnopqrstuvwxyz'
    chars += chars.upper()

    password = get_random_password(
        first_name=first_name,
        last_name=last_name,
        chars=chars,
        length=length
    )
    is_valid = validate_password_alpha(
        password=password,
        first_name=first_name,
        last_name=last_name
    )

    while not is_valid:
        password = get_random_password(
            first_name=first_name,
            last_name=last_name,
            chars=chars,
            length=length
        )
        is_valid = validate_password_alpha(
            password=password,
            first_name=first_name,
            last_name=last_name
        )

    return password


def validate_password_alpha(password, first_name, last_name):
    """
    Valido contraseña alfabética generada
    Pre:
        - password: string, contraseña a validar
        - first_name: string, nombre de la persona
        - last_name: string, apellido de la persona
    Post:
        - Retorno un boolean que indica si es válida o no (True o False)
    """
    minus = 'abcedfghijklmnopqrstuvwxyz'
    mayus = minus.upper()

    has_minus = any([p in minus for p in password])
    has_mayus = any([p in mayus for p in password])
    has_initial_first = first_name[0] in password
    has_initial_last = last_name[0] in password

    return has_minus and has_mayus and has_initial_first and has_initial_last


def generate_password_alphanum(first_name, last_name, length):
    """
    Genero contraseña alfanumérica
    Pre:
        - first_name: string, nombre de la persona
        - last_name: string, apellido de la persona
        - length: largo de contraseña a generar
    Post:
        - Retorno string con contraseña generada (válida)
    """
    chars = 'abcedfghijklmnopqrstuvwxyz'
    chars += chars.upper()
    chars += '0123456789'

    password = get_random_password(
        first_name=first_name, 
        last_name=last_name, 
        chars=chars, 
        length=length
    )
    is_valid = validate_password_alphanum(
        password=password, 
        first_name=first_name, 
        last_name=last_name
    )

    while not is_valid:
        password = get_random_password(
            first_name=first_name, 
            last_name=last_name, 
            chars=chars, 
            length=length
        )
        is_valid = validate_password_alphanum(
            password=password, 
            first_name=first_name, 
            last_name=last_name
        )

    return password


def validate_password_alphanum(password: str, first_name: str, last_name: str):
    """
    Valido contraseña alfanumérica generada
    Pre:
        - password: string, contraseña a validar
        - first_name: string, nombre de la persona
        - last_name: string, apellido de la persona
    Post:
        - Retorno un boolean que indica si es válida o no (True o False)
    """
    has_minus_mayus_initials = validate_password_alpha(
        password=password,
        first_name=first_name,
        last_name=last_name
    )
    has_numbers = any([p.isdigit() for p in password])

    return has_minus_mayus_initials and has_numbers


def save_file(df, file_name):
    """
    Guardo DataFrame en formato .csv con el nombre dado
    """
    df.to_csv(file_name, index=False)


if __name__ == '__main__':
    path = './Personas.csv'
    new_path = './Personas_nuevo.csv'
    length = 12

    df_personas = read_file(path=path)

    for n_persona in range(len(df_personas)):
        persona = df_personas.loc[n_persona]

        password1 = generate_password_alpha(
            first_name=persona.Nombre,
            last_name=persona.Apellido,
            length=length
        )
        password2 = generate_password_alphanum(
            first_name=persona.Nombre,
            last_name=persona.Apellido,
            length=length
        )
        
        df_personas.loc[n_persona, 'contrasena1'] = password1
        df_personas.loc[n_persona, 'contrasena2'] = password2

    save_file(df=df_personas, file_name=new_path)