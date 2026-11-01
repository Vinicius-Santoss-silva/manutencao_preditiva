# Manutenção Preditiva com Python

Projeto de **Análise de Dados aplicada à Engenharia Mecânica**, desenvolvido para simular o monitoramento das condições operacionais de um equipamento e identificar sinais de degradação antes de uma possível falha.

O projeto utiliza dados simulados de sensores, analisa **temperatura, vibração e pressão** e gera automaticamente gráficos, um painel de monitoramento e um diagnóstico da condição do equipamento.

![Painel de Manutenção Preditiva](painel_manutencao_preditiva.png)

## 🎯 Objetivo

Demonstrar como **Python e análise de dados** podem ser aplicados à manutenção industrial para transformar medições de sensores em informações úteis para tomada de decisão.

A análise acompanha a evolução dos parâmetros operacionais e identifica alterações que podem indicar deterioração das condições do equipamento.

## 📊 Variáveis monitoradas

- Temperatura
- Vibração
- Pressão
- Evolução dos indicadores ao longo do tempo

## ⚙️ Diagnóstico automático

Além da visualização dos dados, o programa aplica regras de análise sobre o comportamento dos indicadores.

No cenário simulado foram identificadas tendências como:

- aumento progressivo da vibração;
- redução da pressão;
- alteração das condições operacionais do equipamento.

O sistema então gera automaticamente um diagnóstico de condição.

### Resultado do cenário analisado

**STATUS: RISCO ELEVADO DE FALHA**

**Recomendação: programar inspeção e manutenção.**

> Este projeto utiliza uma lógica baseada em regras e tendências dos sensores. Não se trata ainda de um modelo de Machine Learning para previsão de falhas.

## 🛠️ Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Visual Studio Code
- Git
- GitHub

## 🔄 Fluxo da análise

1. Carregamento dos dados dos sensores.
2. Organização e tratamento dos dados com Pandas.
3. Análise da evolução das variáveis.
4. Avaliação das tendências operacionais.
5. Aplicação das regras de diagnóstico.
6. Identificação do nível de risco.
7. Geração dos gráficos individuais.
8. Geração automática do painel de monitoramento.
9. Exportação das visualizações em formato PNG.

## 📈 Visualizações geradas

O projeto gera automaticamente:

- `grafico_temperatura.png`
- `grafico_vibracao.png`
- `grafico_pressao.png`
- `painel_manutencao_preditiva.png`

O painel consolida os principais indicadores e facilita a identificação visual de mudanças nas condições de operação.

## 📁 Estrutura do projeto

```text
manutencao_preditiva/
│
├── analise_manutencao.py
├── dados_maquina.csv
├── grafico_pressao.png
├── grafico_temperatura.png
├── grafico_vibracao.png
├── painel_manutencao_preditiva.png
├── .gitignore
└── README.md
```

## ▶️ Como executar

Clone o repositório ou faça o download dos arquivos.

Com Python instalado, instale as bibliotecas necessárias:

```bash
pip install pandas numpy matplotlib
```

Depois execute:

```bash
python analise_manutencao.py
```

O programa realizará a análise dos dados, exibirá o diagnóstico no terminal e gerará as visualizações do monitoramento.

## 🏭 Aplicação na Engenharia

Em uma aplicação industrial real, uma solução semelhante poderia receber dados diretamente de sensores instalados em equipamentos como:

- motores;
- bombas;
- rolamentos;
- compressores;
- redutores;
- ventiladores industriais.

O monitoramento contínuo desses dados pode contribuir para a identificação antecipada de condições anormais e apoiar estratégias de manutenção baseada em condição.

## 🚀 Possíveis evoluções

O projeto pode evoluir com:

- aquisição de dados reais por sensores;
- integração com ESP32 e sistemas IoT;
- banco de dados para armazenamento histórico;
- dashboard interativo;
- limites operacionais configuráveis;
- análise estatística;
- detecção automática de anomalias;
- modelos de Machine Learning;
- estimativa de probabilidade de falha;
- indicadores de saúde do equipamento;
- integração com sistemas de manutenção.

## 💡 Contexto do projeto

Este projeto faz parte do meu portfólio e integra conhecimentos de **Engenharia Mecânica, Python e Análise de Dados**.

A proposta é demonstrar de forma prática como dados operacionais podem ser utilizados para apoiar decisões relacionadas à **manutenção, confiabilidade e desempenho de equipamentos**.