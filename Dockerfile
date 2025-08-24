# PASSO 1: Escolha a imagem base
# Vamos usar uma imagem oficial do Python 3.9, que é leve e estável.
FROM python:3.9-slim

# PASSO 2: Defina o diretório de trabalho dentro do contêiner
# Todos os comandos a seguir serão executados a partir desta pasta.
WORKDIR /app

# PASSO 3: Copie o arquivo de dependências para dentro do contêiner
# Copia apenas o requirements.txt primeiro para aproveitar o cache do Docker.
COPY requirements.txt .

# PASSO 4: Instale as dependências
# Roda o pip install dentro do contêiner.
RUN pip install --no-cache-dir -r requirements.txt

# PASSO 5: Copie o código fonte do seu projeto
# Copia a pasta 'src' para dentro da pasta '/app' no contêiner.
COPY src/ .

# PASSO 6: Defina o comando que será executado quando o contêiner iniciar
# Diz ao Docker para rodar "python main.py"
CMD ["python", "main.py"]