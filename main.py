import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

full_grouped = pd.read_csv(r"C:\Arquivos\Coding\Projects\EDA Covid-19\WHO-COVID-19-global-daily-data.csv")

china = full_grouped[full_grouped["Country"] == "China"]
