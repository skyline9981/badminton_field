import matplotlib.pyplot as plt

# Original dimensions and new dimensions
original_width = 61
original_height = 134
new_width = 300
new_height = 660

# Scale factors
scale_factor_width = new_width / original_width
scale_factor_height = new_height / original_height


# New coordinate function
def new_coords(x, y):
    return 25 + x * scale_factor_width, 150 + y * scale_factor_height


# Set up new figure and axis
fig, ax = plt.subplots(figsize=(6, 10))

# Set new axis limits and aspect ratio
ax.set_xlim(25, 325)
ax.set_ylim(150, 810)
ax.set_aspect("equal")

# Draw court boundary
court_boundary = [[0, 0], [61, 0], [61, 134], [0, 134], [0, 0]]
court_boundary_scaled = [new_coords(x, y) for x, y in court_boundary]
ax.plot(*zip(*court_boundary_scaled))

# Draw dashed lines inside the court
dashed_lines = [
    [(4.2, 0), (61 - 4.2, 0), (61 - 4.2, 134), (4.2, 134), (4.2, 0)],
    [(61 / 2, 0), (61 / 2, 134 / 2 - 19.8)],
    [(61 / 2, 134 / 2 + 19.8), (61 / 2, 134)],
    [(0, 134 / 2 - 19.8), (61, 134 / 2 - 19.8)],
    [(0, 134 / 2 + 19.8), (61, 134 / 2 + 19.8)],
    [(0, 7.2), (61, 7.2)],
    [(0, 134 - 7.2), (61, 134 - 7.2)],
]
for line in dashed_lines:
    scaled_line = [new_coords(x, y) for x, y in line]
    ax.plot(*zip(*scaled_line), "k--")

# Draw net
net_line = [(0, 134 / 2), (61, 134 / 2)]
scaled_net_line = [new_coords(x, y) for x, y in net_line]
ax.plot(*zip(*scaled_net_line), "r-")

ax.grid(False)

# Show plot
plt.show()
