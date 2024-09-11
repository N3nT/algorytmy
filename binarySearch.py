def binarySearch(table, value):
    low = 0 # wskazuje pierwszy element listy
    high = len(table) - 1 # wskazuje ostatni element listy
    while low <= high: # dopóki low i high nie wskazują na jeden element
        mid = round((low + high) / 2) # szukamy środkowego elementu
        guess = list[mid]

        if guess == value: # znaleziono
            return mid
        elif guess > value: # wskazana wartość jest za duża
            high = mid - 1 # ostatnim elementem który bierzemy pod uwagę jest element w lewo od środkowego
        else: # wskazana wartość jest za mała
            low = mid + 1 # pierwszym elementem który bierzemy pod uwagę jest element w prawo od środkowego
    return 'Nie znaleziono takiego elementu'

list = [1, 2, 3, 4, 5, 6]
print(binarySearch(list, 4))