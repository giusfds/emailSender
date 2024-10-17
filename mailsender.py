import os
from dotenv import load_dotenv
from email_module.smtpmail import SmtpMail
from utilidade_module import Utils

class MailSender:
    def __init__(self):
        # Carrega as variáveis de ambiente do arquivo .env
        load_dotenv()
        self.smtp_user = os.getenv('SMTP_USER')
        self.smtp_password = os.getenv('SMTP_PASSWORD')
        self.smtp_server = os.getenv('SMTP_SERVER')
        self.smtp_port = os.getenv('SMTP_PORT')
        self.pegar_foto = os.getenv('PEGAR_FOTO')

    def gerar_html(self, vendedor_nome, tipo_contrato, nome_empresa, servico_prestado):
        """
        Gera o corpo do e-mail em formato HTML
        """
        html = f"""
            <html>
                <body>
                    <p>Olá pessoa</p>
                </body>
            </html>
            """
        return html

    def pegar_contrato(self):
        """
        Retorna o caminho do anexo
        """
        caminho_arquivo = "Screenshot_2.png"
        return caminho_arquivo

    def enviar_email_contrato(self):
        """
        Envia um e-mail com a foto
        """
        try:
            email = SmtpMail(self.smtp_user, self.smtp_password, (self.smtp_server, int(self.smtp_port)))

            plaintext = 'This is a test message'
            
            if Utils.validar_filepath(self.caminho_assinatura):
                html = self.gerar_html()
                    
            email.set_message(plaintext, "foto", self.smtp_user, html, 'test\\test.txt', 'test\\test.txt')

            email.set_recipients("seu email")

            email.connect()

            email.send_all()

            print(f"E-mail enviado com sucesso.")
        
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}")
