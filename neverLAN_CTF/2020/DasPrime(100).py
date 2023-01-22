import math

def main():
    primes = []
    count = 2
    index = 0
    while index < 10497:
        isprime = True
        for x in range(2, count):
            if count % x == 0:
                isprime = False
                continue
        if isprime:
            primes.append(count)
            print(index, primes[index])
            index += 1
        count += 1
if __name__ == "__main__":
    main()

#Flag: 110573
