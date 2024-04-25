nums = [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 5, 6]

def remove(nums) -> int:
    lenght=len(nums) # primero guardo en una variable la longitud original del array
    value=int() # declaro esta variable que representara los valores duplicados del array que quiero agregar al final
    index_first_duplicated = 0 # esta variable me servira para almacenar el indice del primer duplicado
    for num in range(len(nums)): #hago el ciclo for con el range para que me de la posicion que a su vez puede ser usada como los mismos valores del array.
        while nums.count(num) > 2 :#valido que hayan mas de dos elementos iguales dentro del array, uso while porque debo quitar todos los elementos repetidos hasta que me queden 2
            print(num)
            if index_first_duplicated == 0:
                index_first_duplicated = nums.index(nums[num])+2 #al encontrar el primer elemento que se repita tres veces o mas, lo que hago es que a la posicion del primer elemento le sumo 2, lo que me daria la posicion del tercero independientemente de cuantos mas haya
            nums.pop(nums.index(num)) #elimino los primeros elementos duplicados que encuentre, asi no tengo que recorrer el arreglo para eliminar de atras hacia delante
            value = nums[num] #almaceno en value el valor duplicado
        while len(nums) < lenght: #debido a que estoy eliminando elementos, me queda un array con menor tamaño, lo que hago es que mientras el arreglo sin duplicados tenga un menor tamaño respecto al original, le introduzco los valores duplicados al final
            nums.append(value)
        continue
    return index_first_duplicated,nums

print(remove(nums))