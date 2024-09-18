import re

def validar_mail (mail):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, mail) is not None
                                 
def validar_nro(telefono):
    patron1 = r'^\+?(\d{1,3})?\s?-'
    patron2 = r'^?(\d{2,4})\s?-'
    patron3 = r'^?(\d{2,4})\s?-'
    patron4 = r'^?(\d{2,4})$'
    if re.match (patron1, telefono) or re.match (patron2, telefono) or re.match (patron3, telefono) or re.match (patron4, telefono):
        print('Telefono valido')

def validar_codigo_postal(codigo_postal):
    patron = r'^\d{4}$|^[A-Z]\d{4}[A-Z]{3}$'
    return re.match(patron, codigo_postal) is not None

def validar_fecha(fecha):
    patron = r'^\d{4}-\d{2}-\d{2}$'
    if re.match(patron, fecha):
        año, mes, dia = map(int, fecha.split('-'))
        if 1900 <= año <= 2100 and 1 <= mes <= 12 and 1 <= dia <= 31:
            return True
    return False