
class Squares:
    def __init__(self, length):
        self.length = length
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.length:
            raise StopIteration

        self.current += 1
        return self.current ** 2

square_num = Squares(5)
print(square_num)
# for sq in square_num:
#     print(sq)

# print(next(square_num))
