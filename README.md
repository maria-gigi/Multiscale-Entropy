# Caracterização do Cérebro Patológico por Meio da Entropia Multiescalar em Pacientes com Depressão

## 📖 Sobre o projeto

Este projeto tem como objetivo investigar diferenças na complexidade da atividade cerebral entre indivíduos diagnosticados com depressão e indivíduos saudáveis, utilizando a **Entropia Amostral Multiescalar (Multiscale Sample Entropy - MSE)** como medida de complexidade dos sinais eletroencefalográficos (EEG).

Foram analisados **56 sujeitos**, distribuídos em dois grupos:

* **28 indivíduos com diagnóstico de depressão;**
* **28 indivíduos do grupo controle.**

A análise foi realizada considerando **cinco regiões cerebrais**, permitindo avaliar como a complexidade dos sinais varia entre grupos e regiões do cérebro.

---

## 🎯 Objetivo

Utilizar a Entropia Amostral Multiescalar como ferramenta para caracterizar alterações na dinâmica cerebral associadas à depressão e verificar estatisticamente diferenças entre grupos e regiões cerebrais.

---

## 🧠 Regiões cerebrais analisadas

As análises foram realizadas agrupando os eletrodos nas seguintes regiões:

| Região                 | Eletrodos                    |
| ---------------------- | ---------------------------- |
| Frontal (F)            | Fp1, Fp2, F3, F4, F7, F8, Fz |
| Centro-Parietal (CP)   | C3, C4, P3, P4, Pz           |
| Occipital (O)          | O1, O2                       |
| Temporal Direita (TD)  | T4, T6                       |
| Temporal Esquerda (TE) | T3, T5                       |

---

## ⚙️ Metodologia

O fluxo metodológico foi dividido em três etapas principais:

### 1. Cálculo da Entropia Multiescalar

Inicialmente foi desenvolvido um algoritmo em Python para calcular a **Entropia Amostral Multiescalar (MSE)** para cada eletrodo do EEG.

Em seguida:

* os eletrodos foram agrupados por região cerebral;
* foi calculada a média da MSE de cada região;
* foram geradas tabelas contendo os valores médios para cada sujeito e para cada escala analisada.

O algoritmo implementa:

* geração do sinal coarse-grained;
* cálculo da Sample Entropy;
* cálculo da MSE para múltiplas escalas;
* agrupamento por regiões cerebrais;
* exportação dos resultados para arquivos de texto.

O código correspondente encontra-se em:

```
mse por areas.py
```

O script realiza o cálculo da Entropia Multiescalar para cada região cerebral e organiza automaticamente os resultados para utilização nas análises estatísticas.

---

### 2. Teste de Normalidade

Após o cálculo das entropias, foi realizada a verificação da normalidade dos dados utilizando o **Teste de Kolmogorov-Smirnov**, separadamente para:

* Grupo Controle;
* Grupo Depressão.

O script:

* lê os arquivos contendo as entropias de cada região;
* executa o teste para todas as escalas;
* organiza os valores de *p* em tabelas;
* exporta os resultados em formato Excel.

Código:

```
normality_test.py
```

---

### 3. Análise Estatística

Após confirmar os pressupostos de normalidade, foi realizada uma **ANOVA Mista (Mixed ANOVA)** utilizando o software **IBM SPSS Statistics**.

A análise considerou:

* **Fator entre sujeitos:** Grupo

  * Controle
  * Depressão

* **Fator intra-sujeitos:** Região cerebral

  * Frontal
  * Centro-Parietal
  * Occipital
  * Temporal Direita
  * Temporal Esquerda

Essa etapa teve como objetivo investigar:

* efeito principal de Grupo;
* efeito principal de Região;
* interação Grupo × Região.

---

## 🛠 Tecnologias utilizadas

* Python
* Pandas
* NumPy
* SciPy
* IBM SPSS Statistics

---

## 📂 Estrutura do projeto

```
├── mse por areas.py           # Cálculo da Entropia Multiescalar por região cerebral
├── normality_test.py          # Teste de normalidade (Kolmogorov-Smirnov)
├── dados/
│   ├── Controle/
│   └── Depressao/
├── resultados/
│   ├── mse/
│   ├── normalidade/
│   └── anova/
└── README.md
```

---

## 📊 Fluxo da análise

```
EEG
        │
        ▼
Cálculo da Entropia Multiescalar (Python)
        │
        ▼
Agrupamento por regiões cerebrais
        │
        ▼
Teste de Normalidade (Kolmogorov-Smirnov)
        │
        ▼
ANOVA Mista (Grupo × Região) no SPSS
        │
        ▼
Interpretação dos resultados
```

---

## 📈 Resultados esperados

A utilização da Entropia Multiescalar permite avaliar a complexidade dos sinais cerebrais em diferentes escalas temporais, possibilitando identificar alterações na dinâmica cerebral associadas à depressão e comparar essas características entre diferentes regiões do cérebro.

---

## 👩‍💻 Autoria

Projeto desenvolvido durante Iniciação Científica na área de Física Aplicada, utilizando Python para processamento dos sinais de EEG e IBM SPSS Statistics para análise estatística.
