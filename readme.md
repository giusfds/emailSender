
# Documentação da Classe `SmtpMail`

## Visão Geral

A classe `SmtpMail` permite a composição e o envio de e-mails utilizando um servidor SMTP. É uma solução flexível que suporta conexões via SSL ou TLS e pode ser facilmente configurada com credenciais de login armazenadas em um arquivo `.env`. A classe permite a inclusão de mensagens em texto simples, HTML, e a adição de anexos.

## Funcionalidades

- Conexão a servidores SMTP (por exemplo, Gmail, servidores personalizados).
- Envio de e-mails com suporte a texto simples, HTML e anexos.
- Gerenciamento de múltiplos destinatários.
- Suporte a conexões seguras (SSL/TLS).
- Opções para personalização do assunto, remetente e corpo do e-mail.

## Requisitos

Para utilizar esta classe, você deve ter as seguintes bibliotecas instaladas:

- `smtplib`: Para enviar e-mails através do protocolo SMTP.
- `email`: Para construir mensagens de e-mail.
- `python-dotenv`: Para carregar variáveis de ambiente a partir de um arquivo `.env`.

Você pode instalar a biblioteca `python-dotenv` utilizando o pip:

```bash
pip install python-dotenv
```

## Estrutura do Código

### Importações Necessárias

```python
import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import COMMASPACE, formatdate
from email import encoders
```

### Inicialização da Classe

```python
smtp_mail = SmtpMail()
```

**Parâmetros do Construtor:**
- `in_username`: (opcional) Nome de usuário para login no servidor SMTP.
- `in_password`: (opcional) Senha para login no servidor SMTP.
- `in_server`: (opcional) Tupla com o servidor e a porta SMTP. Se não fornecido, serão carregados do arquivo `.env`.
- `use_SSL`: (opcional) Booleano que define se a conexão deve usar SSL (padrão é `False` para TLS).

### Métodos Principais

1. **set_message**

   ```python
   smtp_mail.set_message(in_plaintext, in_subject="", in_from=None, in_htmltext=None, attachment=None, filename=None)
   ```

   **Descrição**: Define o conteúdo do e-mail, incluindo corpo em texto simples, assunto, remetente, corpo em HTML e anexos.

   **Parâmetros**:
   - `in_plaintext`: Corpo do e-mail em texto simples (obrigatório).
   - `in_subject`: Linha de assunto do e-mail (opcional).
   - `in_from`: Endereço do remetente (opcional).
   - `in_htmltext`: Corpo do e-mail em HTML (opcional).
   - `attachment`: Caminho do arquivo a ser anexado (opcional).
   - `filename`: Nome do arquivo anexado (opcional).

2. **set_recipients**

   ```python
   smtp_mail.set_recipients(in_recipients)
   ```

   **Descrição**: Define a lista de destinatários para os quais o e-mail será enviado.

   **Parâmetros**:
   - `in_recipients`: Lista ou tupla com os endereços de e-mail dos destinatários (obrigatório).

3. **add_recipient**

   ```python
   smtp_mail.add_recipient(in_recipient)
   ```

   **Descrição**: Adiciona um destinatário à lista de e-mails.

   **Parâmetros**:
   - `in_recipient`: Endereço de e-mail do destinatário a ser adicionado.

4. **connect**

   ```python
   smtp_mail.connect()
   ```

   **Descrição**: Conecta ao servidor SMTP usando o nome de usuário e a senha fornecidos.

5. **disconnect**

   ```python
   smtp_mail.disconnect()
   ```

   **Descrição**: Desconecta do servidor SMTP.

6. **send_all**

   ```python
   smtp_mail.send_all(close_connection=True)
   ```

   **Descrição**: Envia a mensagem para todos os destinatários especificados.

   **Parâmetros**:
   - `close_connection`: (opcional) Define se a conexão deve ser fechada após o envio (padrão é `True`).

### Exemplo de Uso

```python
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Cria uma instância da classe SmtpMail
smtp_mail = SmtpMail()

# Define o corpo do e-mail
smtp_mail.set_message(
    in_plaintext="Olá, este é um teste de e-mail!",
    in_subject="Teste de Envio",
    in_htmltext="<h1>Olá</h1><p>Este é um teste de e-mail!</p>"
)

# Define os destinatários
smtp_mail.set_recipients(["destinatario@example.com"])

# Conecta ao servidor SMTP
smtp_mail.connect()

# Envia o e-mail
smtp_mail.send_all()

# Desconecta
smtp_mail.disconnect()
```

### Considerações Finais

A classe `SmtpMail` fornece uma interface simples e eficiente para o envio de e-mails, permitindo a personalização e o uso seguro de informações sensíveis. Ao armazenar credenciais em um arquivo `.env`, você aumenta a segurança do seu aplicativo.
