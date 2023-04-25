class ConvetionException(Exception):
	pass


class FinConvertion:
	@staticmethod
	def FinConverter(quete: str, base: str, amount: str):
            
            if base == quete:
                raise ConvetionException('Невозможно перевести одинаковые валюты')
            
            try:
                quete_ticker = keys[quete]
            except KeyError:
                raise ConvetionException(f"Не удалось обработать валюту {quete}")
            try:
                base_ticker = keys[base]
            except KeyError:
                raise ConvetionException(f"Не удалось обработать валюту {base}")
            try:
                amount = float(amount)
            except ValueError:
                raise ConvetionException('Не удалось обработать количество')
