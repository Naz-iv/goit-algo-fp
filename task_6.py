def greedy_algorithm(items: dict, budget: int):
    # Sort items by calories/cost ratio in descending order
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    selected_items = []
    total_cost = 0
    total_calories = 0

    for item_name, item_info in sorted_items:
        if total_cost + item_info["cost"] <= budget:
            # Add item to selected items
            selected_items.append(item_name)
            total_cost += item_info["cost"]
            total_calories += item_info["calories"]

    return {"items": selected_items, "cost": total_cost, "calories": total_calories}


def dynamic_programming(items, budget):
    # Create a 2D matrix of size (len(items) + 1) x (budget + 1)
    # Matrix stores information about calories, costs for given item
    dp_matrix = [[{"calories": 0, "cost": 0, "items": []} for _ in range(budget + 1)] for _ in range(len(items) + 1)]

    for i, (name, info) in enumerate(items.items(), start=1):
        for j in range(budget + 1):
            if info["cost"] <= j:
                # Select the item if the cost is less than or equal to the budget
                if dp_matrix[i - 1][j]["calories"] < dp_matrix[i - 1][j - info["cost"]]["calories"] + info["calories"]:
                    dp_matrix[i][j]["calories"] = dp_matrix[i - 1][j - info["cost"]]["calories"] + info[
                        "calories"]
                    dp_matrix[i][j]["cost"] = dp_matrix[i - 1][j - info["cost"]]["cost"] + info["cost"]
                    dp_matrix[i][j]["items"] = dp_matrix[i - 1][j - info["cost"]]["items"] + [name]
                else:
                    dp_matrix[i][j] = dp_matrix[i - 1][j]
            else:
                dp_matrix[i][j] = dp_matrix[i - 1][j]

    return dp_matrix[len(items)][budget]


if __name__ == '__main__':
    budgets = (50, 75, 100, 140, 180)
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    algos = {
        "Greedy": greedy_algorithm,
        "Dynamic": dynamic_programming
    }

    for budget in budgets:
        print("Results with budget:", budget, "\n")
        for name, algo in algos.items():
            result = algo(items, budget)
            print(f"{name} Algorithm:")
            print("Selected Items:", result["items"])
            print("Total Calories:", result["calories"])
            print("Total Cost:", result["cost"], "\n")
