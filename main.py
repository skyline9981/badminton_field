import matplotlib.pyplot as plt


import matplotlib.colors as mcolors


def draw_badminton_field_and_position(player_positions, shot_indices):
    """
    Draw badminton court with real and predicted positions for selected shots with distinct colors for each shot,
    and a correctly colored and non-overlapping legend.

    :param player_positions: List of tuples containing pairs of real and predicted coordinates for two players (A and B)
    :param shot_indices: List of indices of shots to be plotted
    """
    # Set up figure and axis
    fig, ax = plt.subplots(
        figsize=(6, 12)
    )  # Increased figure height for better legend placement

    # Set axis limits and aspect ratio
    ax.set_xlim(0, 61)
    ax.set_ylim(0, 134)
    ax.set_aspect("equal")

    # Draw court boundary
    plt.plot([0, 61, 61, 0, 0], [0, 0, 134, 134, 0])
    plt.plot([(4.2), (61 - 4.2), (61 - 4.2), (4.2), (4.2)], [0, 0, 134, 134, 0], "k--")

    # Draw center line and center circle
    plt.plot([61 / 2, 61 / 2], [0, 134 / 2 - 19.8], "k--")
    plt.plot([61 / 2, 61 / 2], [134 / 2 + 19.8, 134], "k--")

    # Short service lines
    plt.plot([0, 61], [134 / 2 - 19.8, 134 / 2 - 19.8], "k--")
    plt.plot([0, 61], [134 / 2 + 19.8, 134 / 2 + 19.8], "k--")

    # Long service lines
    plt.plot([0, 61], [7.2, 7.2], "k--")
    plt.plot([0, 61], [134 - 7.2, 134 - 7.2], "k--")

    # Draw net
    plt.plot([0, 61], [134 / 2, 134 / 2], "r-")

    # Define distinct colors for each shot
    colors = list(mcolors.TABLEAU_COLORS)  # using Tableau colors for distinction

    # Plot real and predicted positions for selected shots with different colors
    for i, index in enumerate(shot_indices):
        real_positions = player_positions["Target P"][index]
        pred_positions = player_positions["Predict P"][index]
        color = colors[i % len(colors)]

        # Real positions of players A and B
        plt.scatter(
            *real_positions[0], c=color, marker="o", label=f"Real A (Shot {index+1})"
        )
        plt.scatter(
            *real_positions[1], c=color, marker="o", label=f"Real B (Shot {index+1})"
        )

        # Predicted positions of players A and B
        plt.scatter(
            *pred_positions[0],
            c=color,
            marker="^",
            label=f"Predicted A (Shot {index+1})",
        )
        plt.scatter(
            *pred_positions[1],
            c=color,
            marker="^",
            label=f"Predicted B (Shot {index+1})",
        )

    # Add legend at the bottom, outside of the plot
    plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.02), ncol=2)
    # save plot
    plt.savefig("plot.png")

    # Show plot
    plt.show()


def format_player_positions(data):
    # Splitting the data into Target P and Predict P lists
    target_p = data["Target P"]
    predict_p = data["Predict P"]

    # Initializing lists to hold the corrected positions
    target_positions_corrected = []
    predict_positions_corrected = []

    # Function to reorder tuples based on y coordinate
    def reorder_tuple(pair):
        return (pair[1], pair[0]) if pair[0][1] > 67 else (pair[0], pair[1])

    # Reordering and appending the tuples for both Target P and Predict P
    for i in range(0, len(target_p), 2):
        target_positions_corrected.append(reorder_tuple((target_p[i], target_p[i + 1])))
        predict_positions_corrected.append(
            reorder_tuple((predict_p[i], predict_p[i + 1]))
        )

    # Creating the final dictionary
    player_positions_corrected = {
        "Target P": target_positions_corrected,
        "Predict P": predict_positions_corrected,
    }

    return player_positions_corrected


if __name__ == "__main__":
    # Sample data
    data = {
        "Target P": [(19, 125), (24, 34), (22, 106), (17, 43), (23, 89), (23, 46)],
        "Predict P": [(16, 115), (18, 20), (15, 121), (12, 27), (36, 90), (26, 32)],
    }

    # Formatting the data
    formatted_data = format_player_positions(data)
    print(formatted_data)
    # Corrected test data to match the format
    # player_positions_corrected = {
    #     "Target P": [
    #         ((19, 125), (24, 34)),
    #         ((22, 106), (17, 43)),
    #         ((23, 89), (23, 46)),
    #     ],
    #     "Predict P": [
    #         ((16, 115), (18, 20)),
    #         ((15, 121), (12, 27)),
    #         ((36, 90), (26, 32)),
    #     ],
    # }

    # Example usage: plot positions for shots 1 and 2
    draw_badminton_field_and_position(formatted_data, [0, 1])
