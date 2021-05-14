def concatenated_prod(x, n):
    prod = ""
    for i in range(1, n+1):
        prod += str(x*i)
    return int(prod)

def is_pandigital(x):
    x = str(x)
    for i in range(1, 10):
        if str(i) not in x:
            return False
    return True

print(concatenated_prod(192, 3))
print(concatenated_prod(9, 5))
print(is_pandigital(123456789))