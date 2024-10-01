
import json
import pandas as pd
import matplotlib.pyplot as plt

from DataAnalysis.DataLoader import DataLoader

# Caminho para o arquivo JSON fornecido
file_path = '../Data/exercise.json'

data_loader = DataLoader(file_path)
json_data = data_loader.load_json_data()
df_from_json = data_loader.extract_data()


# Finalmente, podemos criar um gráfico de dispersão para mostrar a relação entre frequência cardíaca média e calorias (supondo que temos os dados de frequência cardíaca)
heart_rate_data = [
    entry["heart_rate"]["average"] for entry in json_data
]

# Adicionar essa informação ao DataFrame
df_from_json['heart_rate_avg'] = heart_rate_data

# Gráfico de dispersão: frequência cardíaca média vs calorias queimadas
plt.figure(figsize=(10, 6))
plt.scatter(df_from_json['heart_rate_avg'], df_from_json['calories'], color='red', label="Dados")
plt.title('Relação entre Frequência Cardíaca Média e Calorias Queimadas')
plt.xlabel('Frequência Cardíaca Média (bpm)')
plt.ylabel('Calorias Queimadas')
plt.grid(True)
plt.legend()
plt.show()
