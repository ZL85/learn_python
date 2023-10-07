import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3, marker="o")

ax.set_title("Squares Numbers", fontsize=26)
ax.set_xlabel("Value", fontsize=16)
ax.set_ylabel("Square of Value", fontsize=16)

ax.tick_params(labelsize=16)

plt.show()
