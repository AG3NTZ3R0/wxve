import seaborn as sns


class Ocean:
    """Save the Ocean!"""

    def __init__(self):
        """Initialize attributes."""
        self.message = "10% of all proceeds are donated towards ocean conservation."
        self.data = sns.load_dataset('iris')

    def gen_visual(self, style='seaborn'):
        """Generate a visual representation of the stock."""
        print(self.data.head())


ocean = Ocean()
ocean.gen_visual()
