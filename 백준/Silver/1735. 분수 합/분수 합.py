import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())

denominator = b * d
numerator = a * d + b * c

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

GCD = gcd(numerator, denominator)

print(numerator//GCD, denominator//GCD)