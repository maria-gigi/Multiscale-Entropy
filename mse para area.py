import pandas as pd
import numpy as np
import os
from scipy.spatial.distance import pdist

pasta = "pasta_caminho"
sujeitos = os.listdir(pasta)

global tau
dataframes = []
scales = 6

def multiscaleSampleEntropy(x, m, r, tau):
    
    
   if len(x.shape) == 1:
       x = x.reshape(-1, 1)  # Converte um vetor em uma matriz coluna

   # Coarse signal
   ed = len(x)-len(x)%tau   # elimina as linhas que não completam os coarse grain
   y = np.mean(np.reshape(x[0:ed], (-1, tau)), axis=1)

   # (m+1)-element sequences
   X = np.transpose([y[i:i + m + 1] for i in range(len(y) - m)])

   # Matching (m+1)-element sequences
   A = np.sum(pdist(X.T, 'chebyshev') < r * np.nanstd(x, axis=0))

   # Matching m-element sequences
   X = X[:m, :]
   B = np.sum(pdist(X.T, 'chebyshev') < r * np.nanstd(x, axis=0))

   # Take log
   if A == 0 or B == 0:
       e = np.nan
   else:
       e = np.log(B / A)

   return e  # , A, B

for sujeito in sujeitos:
    eeg = pd.read_csv(f"pasta_caminho{sujeito}", sep='\t')
    mse = np.zeros((scales, len(eeg.columns)))
    tamanho_N = int(len(eeg) / 4)

    print(tamanho_N)
    """
    resultados_F = []
    resultados_CP = []
    resultados_O = []
    resultados_TD = []
    resultados_TE = []
    """
    medias = []
    l = 0
    for eletrodo in eeg.columns:

        for tau in range(scales):
            entropies = []
            for i in range(0, len(eeg[eletrodo]) - (len(eeg[eletrodo])%tamanho_N), tamanho_N):
                pedaco = eeg[eletrodo].iloc[i : i + tamanho_N]
                entropy = multiscaleSampleEntropy(np.array(pedaco), 2, 0.2, tau + 1)
                entropies.append(entropy)
            mse[tau, l] = np.mean(entropies)  #[escala, columns = eletrodo]
        l += 1
        dfmse = pd.DataFrame(mse, columns = [eeg.columns], index = ['1', '2', '3', '4', '5', '6'])

    #Separa as colunas para as suas áreas correspondentes, criando um novo df
    F = dfmse.loc[:,  ['Fp1', 'Fp2', 'F3', 'F4', 'F7', 'F8', 'Fz'] ]
    CP = dfmse.loc[:,  ['C3', 'C4', 'P3', 'P4', 'Pz']]
    O = dfmse.loc[:, ['O1', 'O2']]
    TD = dfmse.loc[:, ['T6', 'T4']]
    TE = dfmse.loc[:, ['T5', 'T3']]
    lista_areas = [F, CP, O, TD, TE]

    #Tira a média de cada área por linha, tendo um df [escala, area]
    for area in lista_areas:
        media = area.mean(axis = 1)
        medias.append(media)

    mse_area = pd.DataFrame(medias).transpose()
    mse_area.columns = ['F', 'CP', 'O', 'TD', 'TE']
    dataframes.append(mse_area)
    
all_df = pd.concat(dataframes, axis = 1)

regiao_F = all_df['F']
regiao_O = all_df['O']
regiao_TD = all_df['TD']
regiao_TE = all_df['TE']
regiao_CP = all_df['CP']
regioes = [regiao_F, regiao_O, regiao_TD, regiao_TE, regiao_CP]

for idx, regiao in enumerate(regioes, start = 1):
    # Renomeia as colunas usando o método rename
    regiao.columns = sujeitos
    nome_arquivo = f"mse_area_controle_{idx}.txt"
    caminho_arquivo = os.path.join('pasta_caminho', nome_arquivo)
    regiao.to_csv(caminho_arquivo, sep='\t', index=False)
    print(regiao)
