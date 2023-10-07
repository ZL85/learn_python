from pathlib import Path
import plotly.express as px
from dice import Dice

dice_1 = Dice()
dice_2 = Dice(10)

results = []
for roll_num in range(5000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides
pos_results = range(2, max_result + 1)
for value in pos_results:
    frequency = results.count(value)
    frequencies.append(frequency)


title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=pos_results, y=frequencies, title=title, labels=labels)

fig.update_layout(xaxis_dtick=1)

# fig.show()
out_path = Path("htmls/dice_visual_02.html")
fig.write_html(out_path)
