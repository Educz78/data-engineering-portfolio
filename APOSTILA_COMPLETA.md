Apostila Completa: Do Zero ao Pipeline de Dados em Docker
Introdução
Este documento é o registro completo da jornada de construção de um pipeline de dados de ponta a ponta. Ele serve como um guia de estudo e consulta, detalhando cada fase do projeto, desde a configuração do ambiente até a profissionalização e containerização da solução, incluindo os erros encontrados e suas respectivas soluções.

Objetivo Final: Construir um pipeline de dados robusto e portátil que extrai dados de uma API, os transforma e carrega em um Data Warehouse na nuvem, tudo executado dentro de um contêiner Docker.

Módulo 1: A Fundação - Preparação do Ambiente
Nenhum projeto sólido pode ser construído sobre uma base instável. Esta fase garantiu que tivéssemos um ambiente de desenvolvimento profissional.

1.1. Configurando o WSL (Windows Subsystem for Linux)
A base do nosso trabalho foi um ambiente Linux rodando no Windows.

Verificação: Confirmamos que o WSL já estava instalado e na versão 2, a ideal para integração com Docker.

Sucesso: A versão 2 do WSL para o Ubuntu-22.04 foi confirmada.

1.2. Configurando o Google Cloud Platform e BigQuery
Preparamos nosso "armazém de dados" na nuvem.

Criação da Conta: Uma conta foi criada na GCP, com um alerta de orçamento para segurança.

Criação do Dataset: Nosso espaço de trabalho no BigQuery, o dataset meu_primeiro_pipeline, foi criado com sucesso.

Sucesso: O dataset aparece no painel do BigQuery, pronto para receber tabelas.

1.3. Configurando o Git e GitHub
Preparamos nossa "vitrine" e sistema de versionamento.

Repositório: Criado o data-engineering-portfolio no GitHub.

Clone Local: O repositório foi clonado com sucesso para nossa máquina local (WSL).

Sucesso: O comando git clone baixa o projeto do GitHub para nossa pasta local.

Módulo 2: O Protótipo - Pipeline v1
Nesta fase, o foco foi criar um script funcional que provasse a viabilidade do projeto.

2.1. Código Inicial (pipeline.py)
Todo o código foi escrito em um único script para agilidade. A execução foi bem-sucedida, carregando os dados na nuvem.

Resultado: A execução do script pipeline.py confirmou que os dados foram extraídos, transformados e carregados.

Sucesso: A mensagem "Dados carregados com sucesso no BigQuery!" confirma o fim do processo.

2.2. Análise com SQL
Validamos o resultado final consultando os dados diretamente no BigQuery.

Resultados: As queries SQL retornaram os insights esperados, provando que os dados estavam corretos e prontos para análise.

Sucesso: As queries para "temperatura média" e "top 10 temperaturas" executadas no BigQuery.

Módulo 3: A Profissionalização - Pipeline v2
Transformamos nosso protótipo em uma aplicação de software robusta.

3.1. Refatoração do Código
Separamos as responsabilidades do nosso código em uma estrutura de pastas e arquivos limpa.

Nova Estrutura: Criamos as pastas src e sql e os arquivos config.py, utils.py, main.py, requirements.txt.

Sucesso: A nova estrutura de arquivos e pastas no VS Code.

Execução: O pipeline refatorado foi executado com sucesso a partir do src/main.py, produzindo o mesmo resultado final, mas com uma base de código muito superior.

3.2. Dockerização
Empacotamos nossa aplicação em um contêiner portátil com um Dockerfile.

Dockerfile: A "receita" para construir nosso contêiner foi criada.

Execução Final: O pipeline foi executado com sucesso de dentro do contêiner Docker, provando sua portabilidade.

Sucesso Final: O log completo da execução do docker run, mostrando o carregamento bem-sucedido para o BigQuery.

Módulo 4: Diário de Bordo - Erros e Soluções
Nenhum projeto real é uma linha reta. Esta seção documenta os desafios que superamos, transformando problemas em aprendizado.

Erro 1: Login como root no WSL

Sintoma: O terminal sempre abria como superusuário.

Diagnóstico: O usuário padrão do WSL não estava configurado. O sistema não encontrava o usuário eduar.

Solução: Criamos o usuário eduar (adduser eduar) e o definimos como padrão no arquivo /etc/wsl.conf.

O erro getpwnam(eduar) failed foi a chave para o diagnóstico.

Erro 2: Autenticação do GCP no Docker

Sintoma: O erro could not locate runnable browser ao rodar dentro do contêiner.

Diagnóstico: O contêiner é um ambiente isolado e não tinha acesso às credenciais salvas no WSL.

Solução: Usamos um "volume" (-v) no comando docker run para "mapear" a pasta de credenciais do WSL para dentro do contêiner.

O erro clássico de autenticação em um ambiente não-interativo.

Erro 3: Integração Docker e WSL Desativada

Sintoma: O comando docker não era encontrado no terminal do WSL.

Diagnóstico: A "ponte" entre o Docker Desktop e a distribuição Ubuntu estava desligada.

Solução: Ativamos o interruptor para Ubuntu-22.04 nas configurações do Docker Desktop (Resources > WSL Integration).

A mensagem de erro nos deu a solução exata.
A tela de configuração onde a "ponte" foi ativada.

Erro 4: Dockerfile Vazio

Sintoma: O docker build falhava com a mensagem the DockerFile cannot be empty.

Diagnóstico: O arquivo Dockerfile foi criado, mas seu conteúdo não foi salvo antes da execução.

Solução: Salvar o arquivo (Ctrl + S) e rodar o build novamente.

O erro que nos lembrou da importância de salvar os arquivos.

Erro 5: Módulo não encontrado no Contêiner

Sintoma: ModuleNotFoundError: No module named 'requests' dentro do Docker.

Diagnóstico: O docker build usou uma versão em cache do requirements.txt que estava vazia.

Solução: Reconstruir a imagem com a flag --no-cache para forçar a releitura de todos os arquivos.

O erro que nos ensinou sobre o cache do Docker.

Módulo 5: "Deploy" no Portfólio
O projeto foi finalizado e "enviado" para a vitrine pública no GitHub.

Finalização: O código refatorado e o novo Dockerfile foram enviados com git add ., git commit e git push.

Resultado: O repositório no GitHub agora reflete a versão final e profissional do projeto.

A página final do nosso projeto no GitHub, um ativo de portfólio completo.