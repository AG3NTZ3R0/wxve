import pandas as pd
import requests


class Stock:
    """Represents a stock."""

    def __init__(self, symbol, api_key, date_range='max', interval='1d', region='US'):
        """
        Initialize attributes.
        """
        self.symbol = symbol
        self._api_url = "https://yh-finance.p.rapidapi.com/stock/v3/get-chart"
        self._api_headers = {
            'x-rapidapi-host': "yh-finance.p.rapidapi.com",
            'x-rapidapi-key': api_key
        }
        self._api_query = {
            'interval': interval,
            'symbol': symbol,
            'range': date_range,
            'region': region,
            'includePrePost': "false",
            'useYfid': "true",
            'includeAdjustedClose': "true",
            'events': "capitalGain,div,split"
        }
        self._response = requests.request('GET', self._api_url, headers=self._api_headers, params=self._api_query)
        self._raw_data = self._response.json()

        self._div_data = list(self._raw_data['chart']['result'][0]['events']['dividends'].values())
        self._div_df = pd.DataFrame.from_records(self._div_data)
        self._div_df['date'] = pd.to_datetime(self._div_df['date'], unit='s')

        self._hist_data = self._raw_data['chart']['result'][0]['indicators']['quote'][0]
        self._hist_df = pd.DataFrame.from_dict(self._hist_data)
        self._hist_df = self._hist_df[['volume', 'open', 'low', 'high', 'close']]
