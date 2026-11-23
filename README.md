<div align="center">

# Ciência de Dados & Aprendizagem de Máquina

### Projetos de Dados | Data Science | Machine Learning

Atividades e projetos desenvolvidos na disciplina **Ciência de Dados e Aprendizagem de Máquina**, do problema de negócio ao modelo de machine learning.

![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0)
![License: CC0](https://img.shields.io/badge/License-CC0_1.0-lightgrey)

</div>

---

## Destaque: previsão de churn com CRISP-DM

Projeto completo da **Unidade 04**: um modelo que identifica clientes de uma operadora de telecom com maior risco de cancelar o serviço, desenvolvido nas seis fases do CRISP-DM.

| Métrica (conjunto de teste) | Meta | Resultado |
|---|---|---|
| Recall (cancelamentos alcançados) | ≥ 70% | **84,8%** |
| ROC-AUC | ≥ 0,80 | **0,843** |
| Retorno simulado da campanha | maior que contatar toda a base | **$ 52,4 mil** contra $ 27,5 mil |

**[Ver o projeto completo](Unidade04_Aprendizado_de_maquinas/)**

---

## Conteúdo

| Unidade | Tema | O que tem lá |
|---|---|---|
| [01 · Big Data](Unidade01_BigData/) | Introdução à Ciência de Dados e Big Data | Atividade "Detetives dos Dados": mapa de um problema de ciência de dados (evasão no ensino superior) e os 5 Vs do Big Data |
| [02 · Análise e Ciência de Dados](Unidade02_analise_e_ciencia_de_dados/) | Python, pandas e visualização | Notebooks de manipulação de dados tabulares com pandas e de visualização e interpretação de dados |
| [03 · Gestão de Projetos](Unidade03_Gestao_de_Projetos/) | Definição de projetos de ciência de dados | Documento de definição de projeto: usabilidade e acessibilidade de portais municipais para idosos |
| [04 · Aprendizado de Máquina](Unidade04_Aprendizado_de_maquinas/) | CRISP-DM e classificação | Projeto de previsão de churn: 6 notebooks, código, dados, modelo treinado e relatório |

---

## Estrutura do repositório

```
.
├── Unidade01_BigData/                      # atividade da aula 01
├── Unidade02_analise_e_ciencia_de_dados/   # notebooks de pandas e visualização
├── Unidade03_Gestao_de_Projetos/           # definição do projeto de ciência de dados
├── Unidade04_Aprendizado_de_maquinas/      # projeto CRISP-DM de churn
│   ├── notebooks/  src/  data/  models/  reports/
│   └── requirements.txt
├── certificados/                           # certificados de cursos
└── LICENSE
```

---

## Como executar

```bash
git clone https://github.com/JoaoFelipeSS/Ciencia_de_dados_e_aprendizagem_de_maquinas.git
cd Ciencia_de_dados_e_aprendizagem_de_maquinas/Unidade04_Aprendizado_de_maquinas
pip install -r requirements.txt
jupyter notebook
```

Os notebooks da Unidade 02 também podem ser abertos direto no Google Colab (links no [README da unidade](Unidade02_analise_e_ciencia_de_dados/)).

---

## Certificados

- [Introdução à Ciência de Dados: conceitos e ferramentas (turma set/2026)](certificados/introducao_a_ciencia_de_dados_conceitos_e_ferramentas_turma_set2026_certificado.pdf)

---

## Autor

**João Felipe Soares Silva**, estudante de Sistemas de Informação.

[![GitHub](https://img.shields.io/badge/GitHub-JoaoFelipeSS-181717?logo=github)](https://github.com/JoaoFelipeSS)

## Licença

Distribuído sob a licença [CC0 1.0 Universal](LICENSE).
