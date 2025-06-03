import csv
#olá esse é meu comentario ! 
# Caminho do log de autenticação
LOG_PATH = "/var/log/auth.log"
# Nome do CSV de saída
OUTPUT_CSV = "logs_filtrados.csv"

# Lê o conteúdo do log
with open(LOG_PATH, "r") as logfile:
    linhas = logfile.readlines()

# Cria e escreve no CSV
with open(OUTPUT_CSV, mode="w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Data", "Usuário", "IP", "Mensagem"])  # Cabeçalho

    for linha in linhas:
        if "Failed password" in linha or "invalid user" in linha:
            partes = linha.split()

            # Data e hora: primeiros 3 elementos
            data = f"{partes[0]} {partes[1]} {partes[2]}"

            # Usuário
            if "invalid user" in linha:
                idx_user = partes.index("user") + 1
                usuario = partes[idx_user]
            else:
                usuario = "desconhecido"

            # IP
            if "from" in partes:
                idx_ip = partes.index("from") + 1
                ip = partes[idx_ip]
            else:
                ip = "desconhecido"

            # Apenas a mensagem limpa (sem prefixos)
            mensagem = linha.strip().split(":")[-1].strip()

            # Escreve a linha formatada no CSV
            writer.writerow([data, usuario, ip, mensagem])

