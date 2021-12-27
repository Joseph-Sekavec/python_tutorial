print(2**3)  # 2**3 = 2^3.


def raise_to_power(base_number, power_number):
    result = 1
    for k in range(power_number):
        result = result*base_number
    return result


number = raise_to_power(2, 3)
print(number)
