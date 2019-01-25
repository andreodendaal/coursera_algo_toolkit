# Uses python3
import sys
import math

def f_gcd(x, y):
   """This function implements the Euclidian algorithm
   to find G.C.D. of two numbers"""

   while(y):
       x, y = y, x % y

   return x


# define lcm function
def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   #lcm = (x*y)//f_gcd(x,y)
   lcm = (x * y) // (math.gcd(int(a), int(b)))
   return lcm


if __name__ == "__main__":
    #a = int(input())
    #b = int(input())
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

# 1 1000000
# 18 35 -> 630 ctr 18
# 226553150 1023473145 -> 46374212988031350 ctr 45310630