def bubble_sort(A):
    n = len (A)
    for i in range(n - 1):
        for j in range((i + 1), n):
            if A[j] < A[i]:
                A[i],A[j] = A[j],A[i]
    return A

n = int(input("Enter the number of elements: "))
my_list = []
for i in range(n):
    my_list.append(float(input(f"Enter the element{i + 1}: ")))

print("Sorted list! ")
print(bubble_sort(my_list))
