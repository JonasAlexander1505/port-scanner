"""
============================================================
  PORT SCANNER - Ferramenta Educacional de Segurança
  Autor: [Seu Nome]
  Descrição: Escaneia portas TCP de um host alvo e identifica
             quais estão abertas, revelando serviços ativos.
  
  ⚠️  AVISO LEGAL: Use somente em ambientes próprios ou com
      autorização explícita. Uso não autorizado pode ser crime
      conforme a Lei 12.737/2012 (Lei Carolina Dieckmann).
============================================================
"""

import socket  # Biblioteca nativa do Python para conexões de rede


# ─────────────────────────────────────────────
#  CONFIGURAÇÕES DO ALVO
# ─────────────────────────────────────────────

ip = "127.0.0.1"  # Endereço alvo — 127.0.0.1 = sua própria máquina (loopback)
                  # Troque pelo IP desejado (somente com autorização!)


# ─────────────────────────────────────────────
#  CABEÇALHO DO SCAN
# ─────────────────────────────────────────────

print(f"Escaneando {ip}...")  # f-string: permite usar variáveis dentro do texto com {}
print("-" * 40)               # Imprime 40 traços como separador visual no terminal


# ─────────────────────────────────────────────
#  LOOP PRINCIPAL — ESCANEIA AS PORTAS
# ─────────────────────────────────────────────

for porta in range(1, 1025):
    # range(1, 1025) gera números de 1 até 1024
    # Portas 1-1024 são as "well-known ports" — onde ficam os principais serviços
    # A cada iteração, a variável 'porta' recebe o próximo número

    # Cria um socket TCP/IPv4
    # AF_INET   = usa endereçamento IPv4 (ex: 192.168.x.x)
    # SOCK_STREAM = usa protocolo TCP (confiável, orientado a conexão)
    conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define tempo máximo de espera por conexão: 0.5 segundos
    # Sem isso o script pode travar em portas que nunca respondem
    # Aumente para 1 ou 2 em redes mais lentas
    conexao.settimeout(0.5)

    # Tenta conectar ao IP na porta atual
    # connect_ex() retorna:
    #   0           → conexão OK = porta ABERTA
    #   outro valor → falhou     = porta fechada ou filtrada por firewall
    resultado = conexao.connect_ex((ip, porta))

    # Se o resultado for 0, a porta está aberta
    if resultado == 0:
        print(f"✅  Porta {porta} — ABERTA")

    # Fecha a conexão após cada tentativa
    # Essencial para liberar recursos do sistema (file descriptors)
    conexao.close()


# ─────────────────────────────────────────────
#  RODAPÉ DO SCAN — Executado após o loop
# ─────────────────────────────────────────────

print("-" * 40)   # Separador final
print("Scan concluído!")
