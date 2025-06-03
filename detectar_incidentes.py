import csv
from collections import defaultdict
from datetime import datetime
import os

CSV_ENTRADA = "logs_filtrados.csv"
CSV_SAIDA = "incidentes.csv"

# Conta falhas por IP
falhas_por_ip = defaultdict(int)

# Lê os logs filtrados
with open(CSV_ENTRADA, mode="r") as entrada:
    leitor = csv.DictReader(entrada)
    for linha in leitor:
        ip = linha["IP"]
        falhas_por_ip[ip] += 1

# Captura o horário da execução
data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Se o arquivo de saída não existir, cria com o cabeçalho
arquivo_existe = os.path.exists(CSV_SAIDA)
with open(CSV_SAIDA, mode="a", newline="") as saida:
    escritor = csv.writer(saida)

    if not arquivo_existe:
        escritor.writerow(["Data/Hora", "IP", "Tentativas de Falha"])

    for ip, quantidade in falhas_por_ip.items():
        if quantidade > 3:
            escritor.writerow([data_hora, ip, quantidade])


