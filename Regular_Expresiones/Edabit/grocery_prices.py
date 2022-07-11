import re


def get_prices(details_list: list) -> list:
    pattern = "[0-9]+\.?[0-9]+"
    prices_list = re.findall(pattern, " ".join(details_list))
    return prices_list

if __name__ == "__main__":
    details = ["artichokes ($1.99)","rotiserrie chicken ($5.99)",
               "gum ($0.75)", "ice cream ($5.99)","banana ($0.20)",
               "sandwich ($8.50)","soup ($1.99)"]
    print(" ".join(details))
    prices = get_prices(details)
    print("Prices:",prices)