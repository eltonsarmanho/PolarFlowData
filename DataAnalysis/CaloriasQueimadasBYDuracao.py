import json
import pandas as pd
import matplotlib.pyplot as plt

from DataAnalysis.DataLoader import DataLoader

# Caminho para o arquivo JSON fornecido
file_path = '../Data/exercise.json'

data_loader = DataLoader(file_path)
json_data = data_loader.load_json_data()
df = data_loader.extract_data()




# Criar o gráfico
plt.figure(figsize=(10, 6))
plt.scatter(df['duration'], df['calories'], color='blue', label="Dados Individuais")

# Ajustar o gráfico com rótulos
plt.title('Relação entre Duração do Treino e Calorias Queimadas')
plt.xlabel('Duração do Treino (segundos)')
plt.ylabel('Calorias Queimadas')
plt.grid(True)
plt.legend()

# Mostrar o gráfico
plt.show()