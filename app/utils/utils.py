import os

class GetVars:
    def __init__(self):
        self.goip_addr = os.environ['GOIP_ADDR']
        self.goip_user = os.environ['GOIP_USER']
        self.goip_password = os.environ['GOIP_PASSWORD']
        self.db_host = os.environ['DB_HOST']
        self.db_port = os.environ['DB_PORT']
        self.db_name = os.environ['DB_NAME']
        self.db_user = os.environ['DB_USER']
        self.db_password = os.environ['DB_PASSWORD']
        self.max_retries = int(os.environ['MAX_RETRIES'])
        self.timeout = int(os.environ['SCAN_TIMEOUT'])
        self.retry_delay = int(os.environ['RETRY_DELAY'])
        self.email = os.environ['EMAIL']
        self.smtp_login = os.environ['SMTP_LOGIN']
        self.smtp_password = os.environ['SMTP_PASSWORD']
        self.slack = os.environ['SLACK']
        self.slack_token = os.environ['SLACK_TOKEN']

    def search(self, text):
        try: val = os.environ[text]
        except: val = None
        return val
        
