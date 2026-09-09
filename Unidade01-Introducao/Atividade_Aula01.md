# Atividade Prática — Detetives dos Dados

## Ciência de Dados e Aprendizagem de Máquina — Aula 01

**Tema:** Introdução à Ciência de Dados e Big Data
**Metodologia:** Trabalho em equipe
**Tempo:** 20 minutos
**Entregável:** Mapa do Problema de Ciência de Dados

---

## 1. Identificação da equipe

| Campo             | Resposta |
| ----------------- | -------- |
| **Turma:**        | Sistemas de Informação         |
| **Data:**         |  19/08        |
| **Equipe:**       | Detetive dos Dados      |
| **Integrante 1:** | João Felipe Silva Santos         |
| **Integrante 2:** | Membro 2         |
| **Integrante 3:** | Membro 3         |
| **Integrante 4:** | Membro 4         |
| **Integrante 5:** | Membro 5         |

---

## 2. Objetivo da atividade

Nesta atividade, sua equipe deverá analisar um **problema real** e pensar como uma equipe de Ciência de Dados poderia utilizar dados para compreender a situação e apoiar uma decisão.

O objetivo não é desenvolver um sistema ou modelo de Machine Learning neste momento.

O objetivo é aprender a **pensar como um cientista de dados**:

> **Problema → Dados → Informação → Análise → Decisão → Benefício**

---

## 3. Escolha do problema

Escolha uma área para investigar:

* [ ] Comércio
* [x] Banco
* [ ] Saúde
* [ ] Transporte
* [x] Educação
* [ ] Entretenimento
* [ ] Indústria
* [ ] Meio ambiente
* [ ] Esportes
* [ ] Outra: __________________________

### Problema escolhido

**Descreva, em poucas linhas, o problema que sua equipe pretende analisar.**

> Abandono estudantil em instituições de ensino superior, muitos estudantes abandonam seus cursos antes de conclusão, causando impactos financeiros para instituições e perdas educacionais para estudantes, é preciso identificar os fatores que levam à saída desses alunos para soluções.

---

## 4. Quem possui esse problema?

Identifique a organização, grupo ou público afetado pelo problema.

**Quem possui ou enfrenta esse problema?**

> Instituições de ensino superior.

### Quem é afetado pelo problema?

> Estudantes que abandonam os cursos, instituições, professores e a sociedade.

---

## 5. Por que esse problema é importante?

Explique por que vale a pena investigar esse problema utilizando dados.

**Qual é o impacto do problema?**

> A evasão estudantil é um problema crítico que afeta a viabilidade financeira das instituições de ensino. Altos índices de evasão representam desperdício de recursos educacionais, redução de receita institucional e perda de capital humano para o mercado.

---

## 6. Qual decisão precisa ser tomada?

Imagine que sua equipe foi contratada para ajudar uma organização.

**Qual decisão a organização precisa tomar?**

> A instituição precisa decidir quais políticas de retenção implementar, como alocação de mentoria acadêmica, programas de bolsa, atendimento psicológico e atividades de engajamento. Também precisa definir quais estudantes devem receber intervenções prioritárias com base em seus fatores de risco identificados.

---

# 7. Identificação dos dados

Agora pense:

> **Quais dados seriam necessários para compreender esse problema?**

Liste pelo menos **5 dados**.

| Nº | Dado necessário | Por que esse dado é importante? |
| -: | --------------- | ------------------------------- |
|  1 | Histórico acadêmico (notas, disciplinas reprovadas) | Indica desempenho e dificuldades acadêmicas que podem levar à evasão |
|  2 | Dados demográficos (idade, sexo, origem geográfica, classe social) | Identifica grupos mais vulneráveis e padrões de evasão por demografia |
|  3 | Situação financeira e tipo de financiamento (bolsa, FIES, próprio) | A dificuldade financeira é um fator crítico para abandono |
|  4 | Frequência em aulas e participação em atividades | Baixa frequência é um indicador precoce de desengajamento |
|  5 | Histórico de atendimento em serviços de apoio (psicológico, pedagógico) | Mostra se o estudante procurou ajuda e que tipo de suporte necessita |
|  6 | Dados socioeconômicos (renda familiar, distância casa-universidade, trabalho paralelo) | Contexto externo influencia a permanência no curso |
|  7 | Avaliações de satisfação e clima acadêmico | Percepção sobre qualidade do ensino, relacionamento com professores e colegas |

---

# 8. Que informações queremos descobrir?

Os dados, quando analisados, podem gerar informações úteis.

**O que sua equipe gostaria de descobrir a partir dos dados?**

### Pergunta 1

> Quais são as disciplinas com maior número de reprovações e há correlação entre reprovação nessas disciplinas e posterior evasão?

### Pergunta 2

> Qual é o perfil demográfico e socioeconômico dos estudantes com maior risco de evasão?

### Pergunta 3

> Como a participação em programas de apoio (mentoria, bolsa, atendimento psicológico) influencia a permanência do estudante?

### Pergunta 4

> Em qual semestre do curso a evasão é mais prevalente e quais eventos ou transições acadêmicas coincidem com períodos de maior evasão?

---

# 9. Quais padrões podemos procurar?

Pense como um cientista de dados.

Sua equipe poderia procurar:

* [x] Tendências
* [x] Comparações
* [x] Grupos semelhantes
* [x] Comportamentos recorrentes
* [x] Valores fora do padrão
* [x] Relações entre variáveis
* [x] Mudanças ao longo do tempo
* [ ] Outros: __________________________

### Explique um padrão que vocês gostariam de encontrar

> Queremos identificar o padrão temporal de evasão: em qual semestre estudantes geralmente abandonam (ex: 1º semestre, 3º semestre), se existe sazonalidade (períodos do ano com mais evasão) e qual é a sequência de eventos que antecede a evasão (queda de frequência → reprovação → desengajamento → abandono). Também buscamos encontrar grupos de risco similares para aplicar intervenções direcionadas.

---

# 10. Qual análise poderia ser realizada?

Como os dados poderiam ser analisados?

Marque uma ou mais possibilidades:

* [x] Análise descritiva
* [x] Comparação entre grupos
* [x] Análise temporal
* [x] Visualização por gráficos
* [x] Identificação de padrões
* [x] Classificação
* [x] Previsão
* [x] Agrupamento
* [ ] Outra: __________________________

### Explique

> Análise descritiva para caracterizar o perfil geral de estudantes evadidos. Comparação entre grupos de estudantes que permaneceram vs. que saíram. Análise temporal para identificar pontos críticos de evasão. Visualizações (gráficos de linha, scatter plot, heatmap) para comunicar resultados. Agrupamento para identificar clusters de risco similares. Classificação para prever quais estudantes têm maior probabilidade de evasão. Previsão para antecipar evasões futuras e permitir intervenções preventivas.

---

# 11. Qual decisão poderia ser tomada?

Depois de analisar os dados, imagine que sua equipe encontrou informações importantes.

**Que decisão poderia ser tomada com base nos resultados?**

> Com base nos resultados, a instituição poderia: (1) criar um sistema de alerta automático para identificar estudantes em risco de evasão; (2) implementar programas de mentoria focados em grupos de alto risco; (3) reforçar apoio pedagógico nas disciplinas com maior taxa de reprovação; (4) disponibilizar auxílio financeiro direcionado a estudantes com dificuldades econômicas; (5) redesenhar o currículo dos semestres críticos para melhorar engajamento; (6) oferecer suporte psicológico preventivo nos períodos de maior evasão.

---

# 12. Qual seria o benefício?

Qual seria o possível benefício da decisão para a organização ou para as pessoas envolvidas?

> Para a instituição: redução de evasão, melhora na taxa de conclusão, aumento de receita, melhoria de indicadores de qualidade. Para estudantes: maior apoio e chances de sucesso, conclusão do curso, melhoria na autoestima e perspectivas de carreira. Para a sociedade: formação de mais profissionais qualificados, redução de desperdício de recursos educacionais. Impacto social e econômico significativo a longo prazo.

---

# 13. Os 5 Vs do Big Data

Analise o problema escolhido pela equipe.

| V              | Pergunta                                                   | Resposta da equipe |
| -------------- | ---------------------------------------------------------- | ------------------ |
| **Volume**     | Existe uma grande quantidade de dados?                     | Sim. Universidades coletam dados de milhares de estudantes ao longo de anos (notas, frequência, registros de atendimento). Acumulam-se rapidamente com múltiplas gerações de estudantes. |
| **Velocidade** | Os dados são gerados ou processados rapidamente?           | Alta. Dados são gerados continuamente (notas lançadas, frequências registradas, atendimentos agendados). Necessário processar em tempo real para alertas. |
| **Variedade**  | Existem diferentes tipos ou formatos de dados?             | Alta variedade. Dados estruturados (notas em tabelas), semiestruturados (documentos de atendimento), e não-estruturados (comentários de professores, conversas de atendimento). |
| **Veracidade** | Os dados podem apresentar erros ou problemas de qualidade? | Sim. Registros incompletos, dados lançados incorretamente, inconsistências entre sistemas, falta de padronização na documentação. |
| **Valor**      | Os dados podem gerar algum benefício ou apoiar decisões?   | Alto valor. Dados permitem identificar padrões de evasão, prever riscos e implementar estratégias efetivas de retenção com impacto direto. |

### Qual dos 5 Vs é mais relevante para o problema?

> **Volume e Valor** são os mais relevantes.

### Justifique

> **Volume** porque as universidades acumulam grandes volumes de dados sobre muitos estudantes ao longo de vários anos, tornando necessárias técnicas de Big Data para processar e analisar. **Valor** é crítico porque os insights extraídos desses dados podem literalmente mudar a vida de estudantes (permitindo que permaneçam nos cursos) e a viabilidade financeira das instituições. O valor potencial de prevenir uma evasão justifica os investimentos em análise de dados.

---

# 14. Mapa do Problema de Ciência de Dados

Complete o fluxo abaixo:

```text
┌─────────────────────────────────────┐
│       PROBLEMA                      │
│ Evasão de estudantes em cursos de   │
│ ensino superior causa perda         │
│ financeira e de capital humano      │
└──────────┬──────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│        DADOS                        │
│ Histórico acadêmico, frequência,    │
│ desempenho, situação financeira,    │
│ dados demográficos, atendimentos    │
└──────────┬──────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│     INFORMAÇÕES                     │
│ Grupos de risco identificados,      │
│ semestres críticos, fatores de      │
│ evasão, padrões temporais           │
└──────────┬──────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│       ANÁLISE                       │
│ Clustering de risco, análise        │
│ temporal, classificação             │
│ preditiva, comparação entre grupos  │
└──────────┬──────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│       DECISÃO                       │
│ Implementar sistema de alertas,     │
│ programas de mentoria focados,      │
│ reforço pedagógico, auxílio         │
│ financeiro direcionado              │
└──────────┬──────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│      BENEFÍCIO                      │
│ Redução de evasão, melhora na       │
│ conclusão de cursos, impacto        │
│ financeiro positivo, formação de    │
│ profissionais qualificados          │
└─────────────────────────────────────┘
