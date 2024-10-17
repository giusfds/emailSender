import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import COMMASPACE, formatdate
from email import encoders

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

class SmtpMail:
    """
    Classe responsável por compor e enviar emails usando um servidor SMTP. Pode utilizar SSL ou TLS.
    
    :param in_username: Username para login no servidor (requerido)
    :param in_password: Senha para login no servidor (requerido)
    :param in_server: Tupla com servidor e porta SMTP (por padrão é o servidor do Gmail)
    :param use_SSL: Define se a conexão é via SSL (True) ou TLS (False)
    """
    def __init__(self, in_username=None, in_password=None, in_server=None, use_SSL=False):
        # Carrega as variáveis de ambiente se não forem passadas diretamente
        self.username = in_username if in_username else os.getenv('SMTP_USER')
        self.password = in_password if in_password else os.getenv('SMTP_PASSWORD')
        self.server_name = in_server[0] if in_server else os.getenv('SMTP_SERVER')
        self.server_port = in_server[1] if in_server else int(os.getenv('SMTP_PORT'))
        self.use_SSL = use_SSL

        # Configura o servidor SMTP
        if self.use_SSL:
            self.smtpserver = smtplib.SMTP_SSL(self.server_name, self.server_port)
        else:
            self.smtpserver = smtplib.SMTP(self.server_name, self.server_port)
            
        self.connected = False
        self.recipients = []
    
    def __str__(self):
        return f"Type: Mail Sender\nConnection to server {self.server_name}, port {self.server_port}\nConnected: {self.connected}\nUsername: {self.username}"

    def set_message(self, in_plaintext, in_subject="", in_from=None, in_htmltext=None, attachment=None, filename=None):
        """
        Cria a mensagem MIME a ser enviada por e-mail. Permite adicionar assunto e campo 'from'. 
        Anexos e mensagens HTML podem ser adicionados opcionalmente.
        """
        if in_htmltext is not None:
            self.html_ready = True
        else:
            self.html_ready = False

        if self.html_ready:
            self.msg = MIMEMultipart('alternative')
            part = MIMEBase('application', "octet-stream")
            part.set_payload(open(attachment, "rb").read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename={filename}")
            self.msg.attach(part)
            self.msg.attach(MIMEText(in_plaintext, 'plain'))
            self.msg.attach(MIMEText(in_htmltext, 'html'))
        else:
            self.msg = MIMEText(in_plaintext, 'plain')

        self.msg['Subject'] = in_subject
        self.msg['From'] = in_from if in_from else self.username
        self.msg["To"] = None

    def set_recipients(self, in_recipients):
        """Define os destinatários do e-mail."""
        if not isinstance(in_recipients, (list, tuple)):
            raise TypeError("Os destinatários devem ser uma lista ou tupla.")
        self.recipients = in_recipients

    def add_recipient(self, in_recipient):
        """Adiciona um destinatário à lista."""
        self.recipients.append(in_recipient)

    def connect(self):
        """Conecta ao servidor SMTP usando o login e senha fornecidos."""
        if not self.use_SSL:
            self.smtpserver.starttls()
        self.smtpserver.login(self.username, self.password)
        self.connected = True
        print(f"Conectado ao servidor {self.server_name}")

    def disconnect(self):
        """Desconecta do servidor SMTP."""
        self.smtpserver.close()
        self.connected = False

    def send_all(self, close_connection=True):
        """Envia a mensagem para todos os destinatários."""
        if not self.connected:
            raise ConnectionError("Não conectado a nenhum servidor. Tente self.connect() primeiro.")
        
        for recipient in self.recipients:
            self.msg.replace_header("To", recipient)
            self.smtpserver.send_message(self.msg)
            print(f"Enviado para {recipient}")

        if close_connection:
            self.disconnect()
            print("Conexão fechada")
