class Matrix:
    def __init__(self, matrix):
     self.matrix = matrix
     def __str__ (self):
         return '\n'.join (map(lambda r: ' '.join(map( str, r)), self.matrix))+ '\n'
     def __add__ (self, other):
         return Matrix (map(lambda s_1,s_2: map (lambda x,y: x+y, s_1,s_2), self.matrix, other.matrix))
    first = Matrix ([[1,2,3],[4,5,6],[7,8,9]])
    second = Matrix ([[1,2,3],[4,5,6],[7,8,9]])
    print (first)
    print (second)
    s = first + second
    print (s)