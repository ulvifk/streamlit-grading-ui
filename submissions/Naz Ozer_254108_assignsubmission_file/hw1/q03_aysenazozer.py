matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################

transpose = []

row = len(matrix) #uzunluk = row sayısı

collumn = len(matrix[0]) # bir tane rowdaki eleman sayısı collumn sayısı

for j in range(collumn):           # her bi rcollumns elemanını 
    transpose_l = []               #listeye ekle 
    transpose_l = [matrix[0][j]]   #bu ordera göre
    
    for i in range(1,row):                  # bütün rowlar için
        transpose_l.append(matrix[i][j])    # ekle i nin j indexini 
    transpose.append(transpose_l)           # asıl olaya ekle

print(transpose)
