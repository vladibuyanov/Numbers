import requests
import xml.etree.ElementTree as elt


def convert(day, month, year, price):
    time = f'{day}/{month}/{year}'
    base = f'http://www.cbr.ru/scripts/XML_dynamic.asp?' \
           f'date_req1={time}&date_req2={time}&VAL_NM_RQ=R01235'
    res = requests.get(base).text
    tree = elt.fromstring(res)
    if tree.findall("Record"):
        for element in tree.findall("Record"):
            name = element.find("Value")
            return str(int(name.text[:2]) * int(price))
    else:
        print('Bad day for bank. Try another')
        if day < 1:
            return convert(31, month, year, price)
        else:
            return convert(day - 1, month, year, price)
