# While partitioning arrays using Hoare Partition scheme, we make an 
#    assumption: The pivot element is always the first element of the array.

#       
# The partion is   |<=pivot|pivot|>pivot|
#       
# arranca de las puntas acia el medio,  
# hasta que detecta una inversion, al final se swapea el pivot con 
# donde deberia estar
# 
# Detalles Importantes: 
#    A- low <=, para que se preserve el pivot
#    B- mientras se escanea, garantizar l<h
#    C- primero achicar de derecha a izquierda, sino falla en input ya particionadas, ej: [4,5]
#
# Conclusion: No me gusta porque depende muchos de detalles, como por ejemplo "C"
# Los corner cases son parte importante de que funcione bien :(
# 
#
def hoare(list):
    return 0

if __name__ == "__main__":
    lst= [4,1,5,3,5,6,1,2,4,7,3,2]
    pivot = hoare(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")
    assert lst == [2, 1, 2, 3, 3, 4, 1, 4, 6, 7, 5, 5]
    
    lst= [4,1,5,3,5,6,1,2,7,3,2]
    pivot = hoare(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")
    assert lst == [1, 1, 2, 3, 3, 2, 4, 6, 7, 5, 5]

    lst= [4,1]
    pivot = hoare(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")
    assert lst == [1, 4]

    lst= [4,5,6,8]
    pivot = hoare(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")
    assert lst == [4,5,6,8]
    
    lst= [4,5]
    pivot = hoare(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")
    assert lst == [4,5]

    lst= [4,3]
    pivot = hoare(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")
    assert lst == [3,4]





