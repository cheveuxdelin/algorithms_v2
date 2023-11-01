class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        number_of_odd = 0
        number_of_even = 0
        for number in position:
            if number % 2 == 0:
                number_of_even += 1
            else:
                number_of_odd += 1
        return min(number_of_odd, number_of_even)