import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_context('talk') # Un trucazo que les va a servir desde ahora hasta que digan F

def read_file(path):
    """
    Leo archivo y transformo en DataFrame. A demás, convierto en formato fecha las
    columnas fecha_fin_cursada y fecha_final. Al final retorno dicho DataFrame
    """
    df_students = pd.read_csv(path)
    df_students['fecha_fin_cursada'] = pd.to_datetime(df_students['fecha_fin_cursada'])
    df_students['fecha_final'] = pd.to_datetime(df_students['fecha_final'])
    return df_students


def missing_students(df_students: pd.DataFrame, N=2):
    """
    A partir de un DataFrame, busco los estudiantes que aprobaron la cursada y
    no rindieron el final dado un valor N entero. Imprimo resultado.
    """
    curr_year = 2023
    df_students_filter = df_students[
        (curr_year - df_students['fecha_fin_cursada'].dt.year >= N)
        & (df_students['nota_final'].isna())
    ]
    print(f'Estudiantes que aprobaron la cursada hace {N} anios y no rindieron final:')
    print(df_students_filter)


def make_graph(df):
    """
    Realizo gráfico de notas de final vs diferencia en meses entre
    fin de cursada y final.
    """
    df['diff_months'] = ((df.fecha_final - df.fecha_fin_cursada)/np.timedelta64(1, 'M'))
    df['diff_months'] = df['diff_months'].apply(np.floor).astype('Int64')
    sns.scatterplot(data=df, x='nota_final', y='diff_months')
    plt.show()


if __name__ == '__main__':
    path = './EstudiantesAprobados.csv'
    N = 2 # Cantidad de anios

    df_students = read_file(path=path)
    missing_students(df_students=df_students)
    make_graph(df=df_students)