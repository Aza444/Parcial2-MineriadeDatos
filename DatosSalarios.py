import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


df = pd.read_excel('Datos salarios.xlsx', sheet_name='Base de datos')

df['Fch comienzo'] = pd.to_datetime(df['Fch comienzo'])
df['Fch nacimiento'] = pd.to_datetime(df['Fch nacimiento'])

current_year = datetime.now().year
df['Edad'] = current_year - df['Fch nacimiento'].dt.year
df['Años experiencia'] = current_year - df['Fch comienzo'].dt.year

plt.style.use('ggplot')  
sns.set_palette("husl")

plt.figure(figsize=(12, 6))
sns.boxplot(x='Facultad', y='Salario', data=df)
plt.title('Distribución de Salarios por Facultad', fontsize=14)
plt.xlabel('Facultad', fontsize=12)
plt.ylabel('Salario (USD)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.regplot(x='Años experiencia', y='Salario', data=df, scatter_kws={'alpha':0.5})
plt.title('Relación entre Salario y Años de Experiencia', fontsize=14)
plt.xlabel('Años de Experiencia', fontsize=12)
plt.ylabel('Salario (USD)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='Sede', hue='Cargo', data=df)
plt.title('Distribución de Cargos por Sede', fontsize=14)
plt.xlabel('Sede', fontsize=12)
plt.ylabel('Cantidad de Empleados', fontsize=12)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout
