from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt


class Stock:
    """Represents a stock."""

    def __init__(self, symbol, av_key):
        """Initialize attributes."""
        self.symbol = symbol
        self._ts = TimeSeries(key=av_key, output_format='pandas')
        self._ts_data, self._ts_metadata = self._ts.get_daily(symbol=self.symbol, outputsize='full')

    def gen_visual(self, style='seaborn'):
        """Generate a visual representation of the stock."""
        plt.style.use(style)
        self._ts_data['4. close'].plot()
        plt.title(f"Daily Time Series for {self.symbol}")
        plt.show()
