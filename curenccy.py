from time import sleep
from datetime import datetime, timedelta
import requests

class CurrencyAPI(object):
    cache = {}

    def __init__(self, api_key, name, cache_lifetime_hours=12):
        self.key = api_key
        self.name = name
        self.cache_lifetime = timedelta(hours=cache_lifetime_hours)

    def set_to_cache(self, data_key, value):
        self.cache[data_key] = {
            'data': value,
            'timestamp': datetime.now()
        }
        print(f'Кешовано: {data_key} -- {value}')

    def get_from_cache(self, data_key):
        entry = self.cache.get(data_key)
        if not entry:
            return None

        if datetime.now() - entry['timestamp'] <= self.cache_lifetime:
            return entry['data']
        else:
            print(f"Кеш за {data_key} прострочений")
            return None

    def status_code(self, status_code):
        if status_code == 200:
            print('all ok')
        elif status_code == 404:
            print('ресурс недоступний')
        elif status_code == 428:
            print('ПОЧЕКАЙ')
            sleep(4)

    def __repr__(self):
        return f'{self.name} : API -- дата : {datetime.now().strftime("%Y-%m-%d")}'


class MonoApi(CurrencyAPI):
    CURRENCY_CODES = {
        'UAH': 980,
        'USD': 840,
        'EUR': 978,
        'GBP': 826,
        'PLN': 985,
        'CHF': 756,
        'CZK': 203,
        'SEK': 752,
        'CAD': 124
    }

    def __init__(self, api_key, name, cache_lifetime_hours = 12):
        super().__init__(api_key, name, cache_lifetime_hours)
        self.url = 'https://api.monobank.ua/bank/currency'

    def convert_to_code(self, currency):
        if isinstance(currency, str):
            currency = currency.upper()
            return self.CURRENCY_CODES.get(currency)
        return currency

    def get_currency(self, currency_a='USD', currency_b='UAH'):
        code_a = self.convert_to_code(currency_a)
        code_b = self.convert_to_code(currency_b)
        if not code_a or not code_b:
            print(f"Невідома валюта: {currency_a} або {currency_b}")
            return None

        cache_key = f'{code_a}_{code_b}'
        cached = self.get_from_cache(cache_key)

        if cached:
            print("З кешу:")
        else:
            cached = self.parsing_data(code_a, code_b)

        if cached:
            print(f"{currency_a.upper()} → {currency_b.upper()}: "
                  f"{cached['rateBuy']} / {cached['rateSell']}")
            return cached
        else:
            print("Дані недоступні")
            return None

    def parsing_data(self, currency_code_a, currency_code_b):
        response = requests.get(self.url)
        self.status_code(response.status_code)

        if response.status_code == 200:
            data = response.json()
            for item in data:
                if (item.get("currencyCodeA") == currency_code_a and
                    item.get("currencyCodeB") == currency_code_b):
                    cache_key = f'{currency_code_a}_{currency_code_b}'
                    self.set_to_cache(cache_key, {
                        'rateBuy': item['rateBuy'],
                        'rateSell': item['rateSell']
                    })
                    return self.get_from_cache(cache_key)
            print('Валюта не знайдена')
        return None


mono = MonoApi('ключ', 'MonoBank', cache_lifetime_hours=12)
mono.get_currency('USD', 'UAH')