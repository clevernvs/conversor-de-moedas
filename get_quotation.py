import requests

def get_converter_by_currency_code(origin_code, destiny_code):
    url = f"https://economia.awesomeapi.com.br/last/{origin_code}-{destiny_code}"
    request = requests.get(url)
    
    quotation = request.json()[f"{origin_code}{destiny_code}"]["bid"]
    return quotation
