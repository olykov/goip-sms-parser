import base64
import requests
import re
import csv


class GoipGateway:
    def __init__(self, goip_addr, goip_user, goip_password):
        self.goip_addr = goip_addr
        self.goip_user = goip_user
        self.goip_password = goip_password

    def _receive_messages(self):
        auth_string = f"{self.goip_user}:{self.goip_password}"
        auth_header = {
            "Authorization": f"Basic {base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')}"
        }

        response = requests.get(f"{self.goip_addr}/default/en_US/tools.html?type=sms_inbox", headers=auth_header)
        data = response.text

        data = data.replace('\\"', '"').encode('latin1').decode('utf-8')
        sms_dump_arr = re.findall(r'sms= \[(.*?)\]', data, re.IGNORECASE | re.DOTALL)

        all_messages = []
        for sim_key, sim_val in enumerate(sms_dump_arr):
            for sms_val in csv.reader([sim_val], skipinitialspace=True, quotechar="'"):
                messages = [{'date': sms_val[i], 'phone': sms_val[i+1], 'text': sms_val[i+2]} for i in range(0, len(sms_val)-2, 3) if sms_val[i] != '""']
                all_messages.append(messages)
        return all_messages