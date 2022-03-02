from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt


class Ticker:
    """Represents a ticker symbol."""

    def __init__(self):
        """Initialize attributes."""
        self._ts = TimeSeries(key='8XEA9G8CY0GG1X7Z', output_format='pandas')
        self.ts_data, self.ts_metadata = self._ts.get_daily(symbol='CDEV', outputsize='full')

    def gen_visual(self):
        """Generate a visual representation of the ticker symbol."""

