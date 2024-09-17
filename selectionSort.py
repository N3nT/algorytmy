def findSmallest(arr): # funkcja znajdująca najniższą liczbę
    smallest = arr[0] # na początku przujmujemy pierwszy element tablicy
    smallest_index = 0 # pierwszy index tablicy

    for i in range(1, len(arr)): # porównujemy wszystkie elementy tablicy zaczynając od indexu 1
        if arr[i] < smallest: # jeżeli [i] element jest mniejszy od smallest to:
            smallest = arr[i] # 1. smallest przyjmuje wartość najmniejszego elementu
            smallest_index = i # 2. smallest_index przyjmuje index najmniejszego elementu (i)
    return smallest_index

def selectionSort(arr):
    newArr = [] # tworzy tablice która będzie zawierać posortowane elementy
    for i in range(len(arr)): # przechodzimy przez wszystkie elementy tablicy
        smallest = findSmallest(arr) # szukamy najmniejszej wartości w tablicy
        newArr.append(arr.pop(smallest)) # dodajemy do nowej tablicy najmniejszy element który jednocześnie jest usuwany z pierwotnej tablicy
    return newArr

print(selectionSort([2,6,7,3,9]))