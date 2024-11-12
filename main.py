import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

full_grouped = pd.read_csv(r"C:\Arquivos\Coding\Projects\EDA Covid-19\WHO-COVID-19-global-daily-data.csv")

china = full_grouped[full_grouped["Country"] == "China"]

# Removing outliers at the end of 2022 & beginning of 2023
china_in = china[(china["Date_reported"] < "2022-12-01") | (china["Date_reported"] > "2023-02-01")]
