def calculate_shipping(weight, distance):
    base_rate = 5.0
    cost = base_rate + (weight * 0.5) + (distance * 0.1)
    return round(cost, 2)

def estimate_delivery(distance):
    days = 1 + (distance // 500)
    return int(days)

# Example usage
if __name__ == "__main__":
    print("Shipping cost:", calculate_shipping(10, 100), "USD")
    print("Estimated delivery:", estimate_delivery(1000), "days")
