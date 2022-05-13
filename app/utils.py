from typing import Dict, List

# Converts list to a dictionary
def convert_list_to_dict(a: List) -> Dict:
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct


""" This funciton notifes users if their desired model is available and sends them an email """


def send_email(body: Dict):
    return body
