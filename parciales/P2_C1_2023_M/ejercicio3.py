import sys
from ejercicio2 import read_file, generate_password_alpha, generate_password_alphanum, save_file

def get_passwords(path, new_path, length):
    """
    Utilizo funciones del módulo (ejercicio2) para
    generar contraseñas para cada persona del dataset.
    """

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

if __name__ == '__main__':
    if len(sys.argv) == 3:
        path = sys.argv[1]
        length = int(sys.argv[2])
        new_path = 'Personas_nuevo_consola.csv'
        get_passwords(path=path, new_path=new_path, length=length)
    else:
        raise SystemError('Comando inválido')