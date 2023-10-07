from pathlib import Path
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=20)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=20)
# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.plasma, s=20)

ax.set_title("Squares Numbers", fontsize=26)
ax.set_xlabel("Value", fontsize=16)
ax.set_ylabel("Square of Value", fontsize=16)

ax.tick_params(labelsize=16)

ax.axis([0, 1100, 1, 1100000])
# ax.ticklabel_format(style="plain")

# plt.show()
out_path = Path("images/squares_plot.png")
plt.savefig(out_path, bbox_inches="tight")
