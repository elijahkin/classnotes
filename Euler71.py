# Produces correct result in 0.79 seconds

val = 3/float(7)
d = 1000000

closest_numer = 0
closest_denom = 1
for denom in range(1, d+1):
    numer = int(val * denom)
    # print("{}/{}".format(numer, denom), abs(numer/denom - val), abs(closest_numer/closest_denom - val))
    if abs(numer/float(denom) - val) < abs(closest_numer/float(closest_denom) - val) and abs(numer/float(denom) - val) != 0:
        closest_numer = numer
        closest_denom = denom
print("{}/{}".format(closest_numer, closest_denom))