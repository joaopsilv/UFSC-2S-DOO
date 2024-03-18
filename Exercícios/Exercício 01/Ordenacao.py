

class Ordenacao():
    def __init__(self, array_para_ordenar:[]):
        self.array = array_para_ordenar

    def ordena(self): ## BubbleSort
        for _ in range(len(self.array)):
            exchanging = False
            for current in range(len(self.array)-1):
                if self.array[current] > self.array[current+1]:
                    self.array[current], self.array[current+1] = self.array[current+1], self.array[current]
                    exchanging = True
            if not exchanging:
                break
        return self.array

    def toString(self):
        formatted_array = ','.join(map(str, self.array))
        return formatted_array
