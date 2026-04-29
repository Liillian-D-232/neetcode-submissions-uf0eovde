class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for x in operations:
            if x == "D":
                record.append(2*record[-1])
            elif x == "C":
                record.pop()
            elif x == '+':
                temp = (record[-2] + record[-1])
                record.append(temp)
            else:
                record.append(int(x))
        return sum(record)