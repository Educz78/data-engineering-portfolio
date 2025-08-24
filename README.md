# Portfólio de Engenharia de Dados

Bem-vindo ao meu portfólio! Este repositório contém os projetos que desenvolvi para praticar e demonstrar minhas habilidades em Engenharia de Dados.

## 🚀 Projeto 1: Pipeline de Dados com API Pública e BigQuery

### Objetivo do Projeto
Automatizar a extração diária de dados de uma API pública, carregá-los em um Data Warehouse na nuvem (BigQuery) e usar SQL para responder perguntas de negócio.

### 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Bibliotecas:** Pandas, Requests, pandas-gbq
* **Nuvem:** Google Cloud Platform (GCP)
* **Data Warehouse:** Google BigQuery
* **Ambiente de Desenvolvimento:** WSL 2 (Ubuntu) com Docker

### 📊 Análise e Resultados
Após o carregamento dos dados para o BigQuery, as seguintes consultas SQL foram utilizadas para extrair insights:

**1. Consulta dos 10 horários com maior previsão de temperatura:**
```sql
SELECT
  data_hora,
  temperatura_celsius
FROM
  `meu_primeiro_pipeline.previsao_tempo_sp`
ORDER BY
  temperatura_celsius DESC
LIMIT 10;

SELECT
  DATE(data_hora) AS dia,
  ROUND(AVG(temperatura_celsius), 2) AS temperatura_media_celsius
FROM
  `meu_primeiro_pipeline.previsao_tempo_sp`
GROUP BY
  dia
ORDER BY
  dia;

### 📝 Setup do Ambiente
Aqui descrevo os passos que segui para configurar meu ambiente de desenvolvimento local e na nuvem.
* **WSL 2 e Ubuntu:** Ativado o Windows Subsystem for Linux e instalada a distribuição Ubuntu 22.04.
* **Docker Desktop:** Instalado e configurado para usar o backend do WSL 2, com 4 CPUs e 8GB de memória alocados.
* **Google Cloud (GCP):** Conta criada com sucesso, com um projeto (`[graceful-tenure-469816-p4]`) e um alerta de orçamento configurado para segurança.
* **BigQuery:** A API foi ativada e um dataset chamado `meu_primeiro_pipeline` foi criado na localização `southamerica-east1`.
* **Autenticação:** O `gcloud` CLI foi instalado e configurado para autenticação local via `gcloud auth application-default login`.

---

