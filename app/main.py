from time import sleep
from utils.utils import Vars
from sms_parser.sms_parser import GoipGateway
from slack_sender.slack_sender import SlackSender
from postgres.postgres import DbWriter
from email_sender.email_sender import EmailSender


vars = Vars()
Goip = GoipGateway(vars.goip_addr, vars.goip_user, vars.goip_password)
Database = DbWriter(vars.db_host, vars.db_port, vars.db_name, vars.db_user, vars.db_password, vars.max_retries, vars.retry_delay)
Slack = SlackSender(slack_channel=vars.slack_channel, slack_token=vars.slack_token)
Email = EmailSender(smtp_login=vars.smtp_login, smtp_password=vars.smtp_password, email=vars.email)


while True:
    messages = Goip._receive_messages()
    for i, ch_line_messages in enumerate(messages):
        ports = vars.get_port_names()
        sim = ports[i]
        for message in ch_line_messages:
            _write_status = Database.write(message)
            if _write_status:
                print(f"+ New SMS message from {message['phone']}")
                Slack._send(message, sim)
                Email.send(message, sim)
            else: print(f"The last SMS message from {message['phone']} is already acknowledged")
    sleep(vars.timeout)




