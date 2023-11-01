# O(N^2)
class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        result = [0] * len(boxes)
        for i in range(len(boxes)):
            if boxes[i] == "1":
                for j in range(len(boxes)):
                    result[j] += abs(j - i)
        return result


# O(N)
class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        left_count = 0
        left_sum = 0
        right_count = 0
        right_sum = 0
        for i in range(len(boxes)):
            if boxes[i] == "1":
                right_count += 1
                right_sum += i
        result = [0] * len(boxes)
        for i in range(len(boxes)):
            result[i] = left_sum + right_sum
            if boxes[i] == "1":
                left_count += 1
                right_count -= 1
            left_sum += left_count
            right_sum -= right_count
        return result