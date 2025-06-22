import heapq

# Пірамідальне сортування

def heap_sort(iterable, descending=False):
    # Перетворюємо список на купу
    h = list(iterable)
    heapq.heapify(h)
    result = [heapq.heappop(h) for _ in range(len(h))]
    return result[::-1] if descending else result

# Тест основного завдання
arr = [12, 11, 13, 5, 6, 7]
print("Відсортований масив (за зростанням):", heap_sort(arr))
print("Відсортований масив (за спаданням):", heap_sort(arr, descending=True))

def min_total_cost(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        a = heapq.heappop(cables)
        b = heapq.heappop(cables)
        cost = a + b
        total_cost += cost
        heapq.heappush(cables, cost)

    return total_cost

# Тест: об'єднання кабелів
cables = [4, 3, 2, 6]
print("Мінімальні загальні витрати на з'єднання кабелів:", min_total_cost(cables))


