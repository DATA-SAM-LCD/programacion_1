import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def leer_archivo(nombre_archivo):
    df = pd.read_csv(nombre_archivo)
    df.drop_duplicates(
        keep='last',
        inplace=True,
        subset=['nombre', 'apellido', 'materia']
    )
    return df.reset_index(drop=True)

def imprimir_registros_materia_promedio(df, materia):
    df_materia = df[df['materia'] == materia][['nombre', 'apellido', 'nota_final']]
    df_materia = df_materia.rename(columns={
        'nombre': 'Nombre', 
        'apellido': 'Apellido', 
        'nota_final': 'Nota'
    })
    promedio = df_materia['Nota'].mean()
    print(df_materia)
    print('-' * 30)
    print(f'Promedio de {materia}: {promedio:.2f}')


def grafico_boxplot_materia(df, materia=None):
    titulo = 'Notas de todas las materias'
    if materia:
        titulo = f'Notas de la materia {materia}'
        df = df[df['materia'] == materia]
    df_materia = df.rename(columns={
        'nombre': 'Nombre', 
        'apellido': 'Apellido', 
        'nota_final': 'Nota',
        'materia': 'Materias'
    })
    plt.figure(figsize=(15, 5))
    sns.boxplot(
        x='Nota', 
        y='Materias', 
        data=df_materia, 
        orient='h', 
        palette='Set2', 
        medianprops={"color": "red"}
    )
    plt.title(titulo)
    plt.xlabel('Nota')
    plt.show()


if __name__ == '__main__':
    archivo = 'notas_materias.csv'
    materia = 'MATEMATICA'

    df = leer_archivo(archivo)
    imprimir_registros_materia_promedio(df, materia)
    grafico_boxplot_materia(df, materia)
    grafico_boxplot_materia(df)