# 🔍 Port Scanner em Python

> Ferramenta educacional de port scanning desenvolvida para fins de aprendizado em segurança ofensiva e defesa cibernética.

---

## 📌 O que é um Port Scanner?

Todo computador conectado à rede possui **65.535 portas TCP/UDP**. Cada serviço ativo ocupa uma ou mais dessas portas. Um Port Scanner tenta se conectar a cada porta do alvo e identifica quais estão abertas — revelando quais serviços estão em execução e possíveis superfícies de ataque.

### Portas mais comuns:

| Porta | Serviço       | Descrição                        |
|-------|---------------|----------------------------------|
| 21    | FTP           | Transferência de arquivos        |
| 22    | SSH           | Acesso remoto seguro             |
| 23    | Telnet        | Acesso remoto (inseguro)         |
| 25    | SMTP          | Envio de e-mails                 |
| 53    | DNS           | Resolução de nomes               |
| 80    | HTTP          | Sites sem criptografia           |
| 443   | HTTPS         | Sites com criptografia TLS/SSL   |
| 3306  | MySQL         | Banco de dados                   |
| 3389  | RDP           | Área de trabalho remota Windows  |

---

## 🛠️ Tecnologias utilizadas

- **Python 3.x**
- Biblioteca `socket` *(nativa — sem instalação necessária)*

---

## ▶️ Como usar

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/port-scanner.git
cd port-scanner
```

### 2. Execute o script
```bash
python scanner.py
```

### 3. Resultado esperado
```
Escaneando 127.0.0.1...
----------------------------------------
✅  Porta 22  — ABERTA
✅  Porta 80  — ABERTA
✅  Porta 443 — ABERTA
----------------------------------------
Scan concluído!
```

---

## ⚙️ Customização

Dentro do arquivo `scanner.py`, você pode alterar:

```python
ip = "127.0.0.1"        # Troque pelo IP alvo (somente com autorização!)

range(1, 1025)          # Intervalo de portas escaneadas
                        # Ex: range(1, 65536) para varrer todas as portas

conexao.settimeout(0.5) # Timeout por porta em segundos
                        # Aumente para redes lentas, diminua para redes rápidas
```

---

## 🧠 Como funciona (por dentro)

```
Para cada porta de 1 até 1024:
  1. Cria um socket TCP/IPv4
  2. Define timeout de 0.5s
  3. Tenta conectar ao alvo na porta atual
  4. connect_ex() retorna:
      → 0           = porta ABERTA  ✅
      → outro valor = porta FECHADA ❌
  5. Fecha o socket
```

---

## 🧪 Ambiente de prática seguro

Teste sempre em ambientes controlados:

| Plataforma | Descrição | Link |
|---|---|---|
| 🟢 TryHackMe | Labs guiados para iniciantes | [tryhackme.com](https://tryhackme.com) |
| 🟡 HackTheBox | Máquinas desafiadoras | [hackthebox.com](https://hackthebox.com) |
| 🔴 VulnHub | VMs vulneráveis locais | [vulnhub.com](https://vulnhub.com) |
| 🔵 Metasploitable | VM vulnerável para prática | Download via VulnHub |

---

## 🗺️ Próximos scripts (roadmap)

- [ ] **v2** — Banner Grabbing (identificar versão dos serviços)
- [ ] **v3** — Threads para scan mais rápido
- [ ] **v4** — Exportar resultado em `.txt` / `.csv`
- [ ] **v5** — Integração com Shodan API

---

## ⚠️ Aviso Legal

Este projeto foi desenvolvido **exclusivamente para fins educacionais**.

> O uso de ferramentas de port scanning sem autorização explícita do proprietário do sistema é **crime** no Brasil, previsto na **Lei 12.737/2012 (Lei Carolina Dieckmann)**, podendo resultar em detenção de 3 meses a 1 ano e multa.

**Use somente em:**
- ✅ Sua própria máquina ou rede
- ✅ Ambientes virtuais (VirtualBox, VMware)
- ✅ Plataformas de CTF/prática autorizadas
- ✅ Ambientes com autorização escrita do proprietário

---

## 👨‍💻 Autor

**[Seu Nome]**
Analista de Suporte e Infraestrutura | Pós-graduação em Segurança e Defesa Cibernética

[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin)](https://linkedin.com/in/seu-perfil)
[![GitHub](https://img.shields.io/badge/GitHub-black?style=flat&logo=github)](https://github.com/seu-usuario)

---

## 📄 Licença

MIT License — veja o arquivo [LICENSE](LICENSE) para detalhes.
