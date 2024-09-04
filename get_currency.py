import xmltodict

def get_full_text():
    with open("archives/currency.xml", "rb") as currency_archive:
        dic_currency = xmltodict.parse(currency_archive)

    currency = dic_currency["xml"]
    return currency


def get_all_available_currency_code_converters():
    with open("archives/currency-converters.xml", "rb") as currency_converters_archive:
        dic_currency_converters = xmltodict.parse(currency_converters_archive)

    currency_converters = dic_currency_converters["xml"]

    dic_converters_available = {}

    for per_converter in currency_converters:
        origin_currency_code, destiny_currency_code = per_converter.split("-")

        if origin_currency_code in dic_converters_available:
            dic_converters_available[origin_currency_code].append(destiny_currency_code)
        else:
            dic_converters_available[origin_currency_code] = [destiny_currency_code]

    return dic_currency_converters