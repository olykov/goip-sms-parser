import time
from utils.utils import GetVars
from sms_parser.sms_parser import GoipGateway
from slack_sender.slack_sender import SlackSender
from postgres.postgres import DbWriter
from email_sender.email_sender import EmailSender

vars = GetVars()
Goip = GoipGateway(vars.goip_addr, vars.goip_user, vars.goip_password)
Database = DbWriter(vars.db_host, vars.db_port, vars.db_name, 
                    vars.db_user, vars.db_password, vars.max_retries, 
                    vars.retry_delay)

while True:
    messages = Goip.receive_messages()
    for i, ch_line_messages in enumerate(messages):
        sim_name = vars.search(f"SIM_PORT_{i+1}")
        for message in ch_line_messages:
            _write_status = Database.write(message)
            if _write_status:
                print(f"+ New SMS message for *{sim_name}* from {message['phone']}")
                if bool(str(vars.slack).lower() == 'true'):
                    Slack = SlackSender(slack_channel=vars.search(f"SIM_PORT_{i+1}_SLACK"), slack_token=vars.slack_token) 
                    Slack.send(message, sim_name)
                if bool(str(vars.email).lower() == 'true'):
                    Email = EmailSender(email=vars.search(f"SIM_PORT_{i+1}_EMAIL"), smtp_login=vars.smtp_login, smtp_password=vars.smtp_password)
                    Email.send(message, sim_name)
            else: print(f"The last SMS message for *{sim_name}* from {message['phone']} is already acknowledged")
    time.sleep(vars.timeout)




