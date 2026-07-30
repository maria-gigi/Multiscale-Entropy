import pandas as pd
from scipy.stats import kstest

# Lendo os arquivos Excel
F = pd.read_excel('C:/Users/DELL/Documents/BACK UP GIMAR/OneDrive/Documentos/Faculdade/IC/SamPen - F.xlsx')
CP = pd.read_excel('C:/Users/DELL/Documents/BACK UP GIMAR/OneDrive/Documentos/Faculdade/IC/SampEn - CP.xlsx')
O = pd.read_excel('C:/Users/DELL/Documents/BACK UP GIMAR/OneDrive/Documentos/Faculdade/IC/SampEn - O.xlsx')
TD = pd.read_excel('C:/Users/DELL/Documents/BACK UP GIMAR/OneDrive/Documentos/Faculdade/IC/SampEn - TD.xlsx')
TE = pd.read_excel('C:/Users/DELL/Documents/BACK UP GIMAR/OneDrive/Documentos/Faculdade/IC/SampEn - TE.xlsx')

# Definindo as escalas
escalas = F.columns[1:]

# Função para realizar o teste de normalidade Kolmogorov-Smirnov e retornar os p-values
def normality_test_ks(regiao):
    p_values = {}
    for escala in escalas:
        controle = regiao[regiao['Grupos'] == 'Controle'][escala]
        depressao = regiao[regiao['Grupos'] == 'Depressão'][escala]
        
        # Teste de normalidade Kolmogorov-Smirnov
        _, p_value_controle = kstest(controle, 'norm', args=(controle.mean(), controle.std()))
        _, p_value_depressao = kstest(depressao, 'norm', args=(depressao.mean(), depressao.std()))
        
        p_values[escala] = {'Controle': p_value_controle, 'Depressão': p_value_depressao}
        
    return p_values

# Lista de regiões e seus nomes
regioes = {'F': F, 'CP': CP, 'O': O, 'TD': TD, 'TE': TE}

# DataFrames para armazenar os p-values
df_p_values_controle = pd.DataFrame(index=escalas)
df_p_values_depressao = pd.DataFrame(index=escalas)

# Iterando sobre as regiões e coletando os p-values
for nome_regiao, regiao in regioes.items():
    p_values = normality_test_ks(regiao)
    df_p_values_controle[nome_regiao] = pd.Series({escala: p_values[escala]['Controle'] for escala in escalas})
    df_p_values_depressao[nome_regiao] = pd.Series({escala: p_values[escala]['Depressão'] for escala in escalas})

# Arredondando os valores para 3 casas decimais
df_p_values_controle = df_p_values_controle.round(3)
df_p_values_depressao = df_p_values_depressao.round(3)

# Ajustando as opções de exibição do pandas
pd.set_option('display.float_format', lambda x: f'{x:.3f}')

# Exibindo os DataFrames resultantes
print("P-values para o grupo Controle:")
print(df_p_values_controle)
print("\nP-values para o grupo Depressão:")
print(df_p_values_depressao)

# Se quiser salvar o resultado em arquivos Excel
df_p_values_controle.to_excel('resultados_p_values_controle.xlsx')
df_p_values_depressao.to_excel('resultados_p_values_depressao.xlsx')
