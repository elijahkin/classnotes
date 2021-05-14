def product_sum(a):
    N = 1
    for k in a:
        N *= k
    if N == sum(a):
        return N
    else:
        return 0

print(product_sum((1, 2, 3)))
print(product_sum((1, 2, 4)))