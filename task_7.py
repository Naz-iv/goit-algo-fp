import random
import matplotlib.pyplot as plt
from collections import defaultdict

def simulate_dice_rolls(simulation: int):
    results = defaultdict(int)

    for _ in range(simulation):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll = dice1 + dice2

        results[roll] += 1

    return {key: value / num_simulations for key, value in results.items()}


def plot_probabilities(prob: dict):
    x_values = list(prob.keys())
    y_values = list(prob.values())

    plt.bar(x_values, y_values, align="center")
    plt.xlabel("Total dice value")
    plt.ylabel("Probability")
    plt.title("Probability of getting total dice value (With Monte-Carlo method)")
    plt.show()


if __name__ == "__main__":
    num_simulations = 1000000

    probabilities = simulate_dice_rolls(num_simulations)

    print(" Total \t Probability")
    for total, probability in sorted(probabilities.items(), key=lambda x: x[0]):
        print(f"\t{total} \t {probability * 100:.2f}")

    plot_probabilities(probabilities)
