# While partitioning arrays using Hoare Partition scheme, we make an 
#    assumption: The pivot element is always the first element of the array.

#                   _______ _____ _______
# The partion is   |<=pivot|pivot|>=pivot|
#                   ------- ----- -------

# arranca de las puntas acia el medio,  hasta que detecta una inversion, luego arregla la inversion 
# y sigue con los demas elementos



def hoare(list):
   return 0
    

if __name__ == "__main__":
    lst= [4,3,5,4,4,6,1,2,7,4]
    pivot = hoare(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")


