class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        x = n
        i = 0
        m = len(flowerbed)

        if m == 1:
            return flowerbed[0] == 0 or n == 0

        while x and i < m:

            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    x -= 1
                    i += 2
                    continue

            elif i == m - 1:
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    x -= 1
                    i += 2
                    continue

            else:
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    x -= 1
                    i += 2
                    continue

            i += 1

        return x == 0