import plotly.express as px
from dice import Dice

dice = Dice()

results = []
for roll_num in range(1000):
    result = dice.roll()
    results.append(result)

frequencies = []
pos_results = range(1, dice.num_sides + 1)
for value in pos_results:
    frequency = results.count(value)
    frequencies.append(frequency)
    # print(f"{value} appears {frequency} times.")

title = "Results of Rolling One D6 1,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=pos_results, y=frequencies, title=title, labels=labels)
fig.show()

# print(frequencies)
