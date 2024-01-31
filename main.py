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


def draw_badminton_field_and_position(target_P, predict_P, shot_indices):
    """
    Draw badminton court with real and predicted player positions for selected shots.
    :param target_P: List of real positions for two players.
    :param predict_P: List of predicted positions for two players.
    :param shot_indices: List of indices of shots to be plotted.
    """
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

    # Process and plot positions for each selected shot
    for i in shot_indices:
        # Get positions for this shot
        real_A_pos = (target_P[i * 4 + 1], target_P[i * 4])
        real_B_pos = (target_P[i * 4 + 3], target_P[i * 4 + 2])
        pred_A_pos = (predict_P[i * 4 + 1], predict_P[i * 4])
        pred_B_pos = (predict_P[i * 4 + 3], predict_P[i * 4 + 2])

        # Draw player positions
        ax.scatter(
            *real_A_pos, color="blue", marker="^", label=f"Real A (Shot {i+1})"
        )  # Real A
        ax.scatter(
            *pred_A_pos, color="blue", marker="o", label=f"Predicted A (Shot {i+1})"
        )  # Predicted A
        ax.scatter(
            *real_B_pos, color="green", marker="^", label=f"Real B (Shot {i+1})"
        )  # Real B
        ax.scatter(
            *pred_B_pos, color="green", marker="o", label=f"Predicted B (Shot {i+1})"
        )  # Predicted B

    # ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.02), ncol=2)

    plt.show()


if __name__ == "__main__":
    # Sample data
    target_P = [
        670.0,
        209.0,
        332.0,
        200.0,
        594.0,
        242.0,
        325.0,
        203.0,
        608.0,
        226.0,
        417.0,
        263.0,
        537.0,
        259.0,
        375.0,
        244.0,
    ]
    predict_P = [
        655.0,
        138.0,
        273.0,
        130.0,
        655.0,
        214.0,
        282.0,
        130.0,
        655.0,
        188.0,
        282.0,
        130.0,
        655.0,
        187.0,
        282.0,
        130.0,
    ]

    # Example usage
    draw_badminton_field_and_position(
        target_P, predict_P, [0, 1]
    )  # For the first two shots
