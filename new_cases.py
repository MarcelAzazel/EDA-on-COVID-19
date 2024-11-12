# With removed outliers at the end of 2022
plt.plot(china_in["Date_reported"], china_in["New_cases"])
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.title("Cases overtime")
plt.xlabel("Date")
plt.ylabel("Cases")
