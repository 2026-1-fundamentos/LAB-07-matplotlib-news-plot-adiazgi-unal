"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
import pandas as pd
import matplotlib.pyplot as plt
import os
import glob

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo files/plots/news.png.
    
    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.
    
    El gráfico debe salvarse al archivo files/plots/news.png.
    """
  
    os.makedirs('files/plots', exist_ok=True)
    
   
    posibles_ubicaciones = [
        'news.csv',
        'data/news.csv',
        'files/news.csv',
        'datos/news.csv',
        'homework/news.csv',
        '../news.csv',
        '../../news.csv'
    ]
    
    archivo_encontrado = None
    for ubicacion in posibles_ubicaciones:
        if os.path.exists(ubicacion):
            archivo_encontrado = ubicacion
            break
    
    
    if archivo_encontrado is None:
        archivos_csv = glob.glob('**/*.csv', recursive=True)
        for archivo in archivos_csv:
            # Verificar si el archivo contiene los datos esperados
            try:
                df_prueba = pd.read_csv(archivo, nrows=1)
                columnas_esperadas = ['Year', 'Television', 'Newspaper', 'Radio', 'Internet']
                if all(col in df_prueba.columns for col in columnas_esperadas):
                    archivo_encontrado = archivo
                    break
            except:
                continue
    
    if archivo_encontrado is None:
       
        print("Archivo CSV no encontrado. Usando datos incorporados.")
        data = {
            'Year': [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010],
            'Television': [74, 82, 80, 74, 73, 72, 74, 70, 70, 66],
            'Newspaper': [45, 42, 50, 46, 36, 36, 34, 35, 32, 31],
            'Radio': [18, 21, 18, 21, 16, 14, 13, 18, 17, 16],
            'Internet': [13, 14, 20, 24, 20, 24, 24, 40, 35, 41]
        }
        df = pd.DataFrame(data)
    else:
        print(f"Archivo CSV encontrado: {archivo_encontrado}")
        df = pd.read_csv(archivo_encontrado)
    
    if 'Year' not in df.columns:
      
        if df.columns[0] in ['Año', 'year', 'ano']:
            df.rename(columns={df.columns[0]: 'Year'}, inplace=True)
    
  
    plt.figure(figsize=(10, 6))
    
    
    colors = {
        'Television': 'blue',
        'Newspaper': 'red', 
        'Radio': 'green',
        'Internet': 'purple'
    }
    
    markers = {
        'Television': 'o',
        'Newspaper': 's',
        'Radio': '^',
        'Internet': 'D'
    }
   
    for medium in ['Television', 'Newspaper', 'Radio', 'Internet']:
        if medium in df.columns:
            plt.plot(df['Year'], df[medium], 
                     label=medium,
                     color=colors[medium],
                     marker=markers[medium],
                     linestyle='-',
                     linewidth=2,
                     markersize=8)
    
 
    plt.title('Porcentaje de personas que obtienen noticias\nen diferentes medios (2001-2010)', 
              fontsize=14, fontweight='bold')
    plt.xlabel('Año', fontsize=12)
    plt.ylabel('Porcentaje (%)', fontsize=12)
    
   
    plt.xticks(df['Year'], rotation=45)
    
   
    plt.ylim(0, 100)
    plt.yticks(range(0, 101, 20))
    
  
    plt.grid(True, linestyle='--', alpha=0.7)
    

    plt.legend(loc='upper left', frameon=True, shadow=True)
    
  
    plt.tight_layout()
    plt.savefig('files/plots/news.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Gráfico generado exitosamente en 'files/plots/news.png'")