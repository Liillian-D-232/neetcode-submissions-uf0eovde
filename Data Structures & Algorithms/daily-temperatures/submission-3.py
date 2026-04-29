class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] #[temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                old_t, old_i = stack.pop()
                result[old_i] = i - old_i
            stack.append((t, i))
        return result