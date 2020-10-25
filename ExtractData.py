import numpy as np
import pandas as pd


class CovidData:
    def __init__(self, url):
        self.url = url

    def data(self):
        return pd.read_csv(self.url)
