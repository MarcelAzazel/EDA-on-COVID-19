plt.plot(china["Date_reported"], china["Cumulative_cases"])
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.title("Cases overtime")
plt.xlabel("Date")
plt.ylabel("Cases")
