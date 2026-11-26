
import math


def parcel_charge(weight_g, length, width, height, zone):

    actual = math.ceil(weight_g / 1000)

    volumetric = math.ceil((length * width * height) / 5000)

    W = max(actual, volumetric)

    if zone == "LOCAL":
        charge = 40 + 15 * W
    else:
        charge = 70 + 25 * W

    return charge


n = int(input())

total = 0
charges = []

for i in range(n):

    weight_g, length, width, height, zone = input().split()

    charge = parcel_charge(int(weight_g), int(
        length), int(width), int(height), zone)

    charges.append(charge)
    total = total + charge

if total >= 300:
    total = total - 50

print("Output:")

for charge in charges:
    print(charge)

print(total)
