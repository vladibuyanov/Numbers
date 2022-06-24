import requests
import xml.etree.ElementTree as elt


def convert(time, price):
    base = f'http://www.cbr.ru/scripts/XML_dynamic.asp?' \
           f'date_req1={time}&date_req2={time}&VAL_NM_RQ=R01235'
    res = requests.get(base).text
    tree = elt.fromstring(res)
    for element in tree.findall("Record"):
        name = element.find("Value")
        return str(int(name.text[:2]) * int(price))
