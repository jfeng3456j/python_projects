import math


class FindAllPrimes:
    def findAllPrimes(self, num: int) -> list:
        print("Find all the primes up to a given integer. ")

        result = []
        if num < 2:
            return result

        for i in range(2, num + 1):
            is_prime = True
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    is_prime = False
                    break

            if is_prime:
                result.append(i)

        return result

