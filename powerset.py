from itertools import combinations


def power_set_generator():
    print("[!] Example Input: a, b, c, d")
    subset = input("Input: ").split("," or ", ")
    power_set = [var for length in range(len(subset)+1) for var in combinations(subset, length)]
    power_set = str(power_set).replace("(", '{').replace(")", '}')
    return power_set


if __name__ == "__main__":
    print(power_set_generator())
