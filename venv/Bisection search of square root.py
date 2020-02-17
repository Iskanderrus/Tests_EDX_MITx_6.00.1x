x = 13000
epsilon = 0.01
numGuesses = 0
low = 0
high = x
ans = (high + low) / 2.0

while abs(ans ** 2 - x) >= epsilon:
    print("Low = " + str(low) + " High = " + str(high) + " ans = " + str(ans))
    numGuesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print("Number of Guesses: " + str(numGuesses))
print(str(ans) + " is close to square root of  " + str(x))