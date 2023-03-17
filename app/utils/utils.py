import os

class Vars:
    def __init__(self):
        self.goip_addr = os.environ['GOIP_ADDR']
        self.goip_user = os.environ['GOIP_USER']
        self.goip_password = os.environ['GOIP_PASSWORD']
        self.db_host = os.environ['DB_HOST']
        self.db_port = os.environ['DB_PORT']
        self.db_name = os.environ['DB_NAME']
        self.db_user = os.environ['DB_USER']
        self.db_password = os.environ['DB_PASSWORD']
        self.slack_token = os.environ['SLACK_TOKEN']
        self.slack_channel = os.environ['SLACK_CHANNEL']
        self.max_retries = int(os.environ['MAX_RETRIES'])
        self.timeout = int(os.environ['TIMEOUT'])
        self.retry_delay = int(os.environ['RETRY_DELAY'])
        self.smtp_login = os.environ['SMTP_LOGIN']
        self.smtp_password = os.environ['SMTP_PASSWORD']
        self.email = os.environ['EMAIL']
        self.ports = {
            0: "Empty sim1",
            1: "Empty sim2",
            2: "Empty sim3",
            3: "Empty sim4"
        }
        
