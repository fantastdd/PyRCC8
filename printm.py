from basesplit import bsplit
from helpfuncs import translate

# print matrix with relations split into base relations
def printMatrix(Matrix):
   for i in xrange(len(Matrix)):
      for j in xrange(i+1,len(Matrix)):
         print i, j, [translate(p) for p in bsplit[Matrix[i][j]-1][1]]

def matrixToString(matrix):
   matrix_str = ""
   for i in xrange(len(matrix)):
      for j in xrange(i+1,len(matrix)):
         #do not print ALL relations (code = 0)
         if(matrix[i][j] > 0):
            matrix_str += str(i) + "," +  str(j) + "," +  str([translate(p) for p in bsplit[matrix[i][j]-1][1]]) + '\n'
   return matrix_str
