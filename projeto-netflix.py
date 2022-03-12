# Vou criar duas listas para montar meu dicionário:
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

# Agora, criando o dicionário:
movie_dict = {'years': years, 'durations': durations}

# Importando pandas:
import pandas as pd

# Criando um DataFrame a partir do dicionário existente:
durations_df = pd.DataFrame(movie_dict)

# Importando a biblioteca para gerar o plot e criando a figura:
import matplotlib.pyplot as plt
fig = plt.figure()

# Criando um gráfico com os anos no eixo 'x' e a duração dos filmes no eixo 'y':
plt.plot(durations_df['years'], durations_df['durations'])

# Criando um título:
plt.title("Netflix Movie Durations 2011-2020")

# Mostrando o gráfico:
plt.show()