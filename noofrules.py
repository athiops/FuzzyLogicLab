def number_of_rules(inputs, fuzzy_sets_per_input):
    return fuzzy_sets_per_input ** inputs


if __name__ == "__main__":
    inputs = 4
    sets = 3

    rules = number_of_rules(inputs, sets)
    print("Number of rules:", rules)