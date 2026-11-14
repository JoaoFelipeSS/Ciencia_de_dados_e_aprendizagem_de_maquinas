# Unidade 04 — Aprendizado de Máquina

## Projeto: previsão de churn de clientes de telecom com CRISP-DM

Projeto da disciplina **Ciência de Dados e Aprendizagem de Máquina** (Profa. Kadidja Valéria), que aplica as seis fases da metodologia CRISP-DM a um problema de cancelamento de clientes (churn) em uma operadora de telecomunicações.

**Autor:** João Felipe Soares Silva

### O problema

Na base analisada, 26,5% dos clientes cancelaram o serviço, e eles respondiam por 30,5% da receita mensal. O objetivo é identificar com antecedência os clientes com maior risco de sair, para que a equipe de retenção faça uma oferta direcionada.

O cenário de negócio é uma simulação didática. Os dados são o conjunto público [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) (amostra da IBM), com 7.043 clientes e 21 colunas.

### As seis fases

| Fase | Notebook | O que contém |
|---|---|---|
| 1. Entendimento do Negócio | [01_entendimento_do_negocio.ipynb](notebooks/01_entendimento_do_negocio.ipynb) | Objetivos, critérios de sucesso, riscos, premissas financeiras e plano de projeto |
| 2. Entendimento dos Dados | [02_entendimento_dos_dados.ipynb](notebooks/02_entendimento_dos_dados.ipynb) | Dicionário de dados, análise exploratória, hipóteses e relatório de qualidade |
| 3. Preparação dos Dados | [03_preparacao_dos_dados.ipynb](notebooks/03_preparacao_dos_dados.ipynb) | Seleção, limpeza, construção de atributos e base preparada |
| 4. Modelagem | [04_modelagem.ipynb](notebooks/04_modelagem.ipynb) | Comparação de cinco técnicas, ajuste de hiperparâmetros, tratamento de atributos redundantes e escolha do limiar |
| 5. Avaliação | [05_avaliacao.ipynb](notebooks/05_avaliacao.ipynb) | Resultados no conjunto de teste, simulação da campanha, análise de sensibilidade e decisão |
| 6. Implementação | [06_implementacao.ipynb](notebooks/06_implementacao.ipynb) | Plano de implementação e de monitoramento, relatório final e lições aprendidas |

### Resultados

Modelo final: **regressão logística** com 19 atributos e limiar de decisão de 0,21. Resultados no conjunto de teste (1.409 clientes que o modelo não viu):

| Critério definido na Fase 1 | Meta | Resultado |
|---|---|---|
| Cancelamentos alcançados pela campanha (recall) | ≥ 70% | 84,8% (317 de 374) |
| ROC-AUC | ≥ 0,80 | 0,843 |
| Retorno líquido simulado da campanha | Positivo e maior do que contatar toda a base | $ 52,4 mil contra $ 27,5 mil |
| Fatores de risco com sentido comercial | Sim | Tempo de casa, tipo de internet e tipo de contrato |

Os clientes com maior risco têm contrato mensal, menos de um ano de casa, internet por fibra e nenhum serviço de segurança ou suporte técnico.

**Ressalva:** o dataset não traz custos nem resultados de campanhas de retenção. O retorno financeiro é uma simulação baseada em premissas (custo de $ 50 por contato, 30% de sucesso da oferta e 12 mensalidades preservadas por cliente retido), registradas em `src/negocio.py`. A Fase 5 mostra em quais cenários a conclusão se mantém e em quais a campanha daria prejuízo. Por isso a recomendação final é implementar o modelo como piloto controlado.

### Estrutura

```
Unidade04_Aprendizado_de_maquinas/
├── notebooks/            # um notebook por fase do CRISP-DM
├── src/
│   ├── preparacao.py     # regras de preparação dos dados (Fase 3), usadas também na pontuação
│   └── negocio.py        # premissas e simulação do retorno da campanha
├── data/
│   ├── raw/              # dataset original, sem alterações
│   └── processed/        # base preparada e conjuntos de treino e teste
├── models/               # modelo treinado e arquivo de configuração (limiar, atributos, premissas)
├── reports/              # lista de retenção de exemplo gerada na Fase 6
└── requirements.txt
```

### Como executar

```bash
pip install -r requirements.txt
jupyter notebook
```

Execute os notebooks em ordem, de 01 a 06, a partir da pasta `notebooks/`. Cada um grava os arquivos que o seguinte utiliza. A semente aleatória é fixa (42), então os resultados se repetem a cada execução. Pequenas diferenças nas últimas casas decimais podem aparecer em outras versões das bibliotecas.

Os notebooks foram executados com Python 3.13, pandas 3.0 e scikit-learn 1.9. O arquivo `models/modelo_churn.joblib` deve ser carregado com a mesma versão do scikit-learn; em outra versão, execute novamente o notebook 04 para gerá-lo.
