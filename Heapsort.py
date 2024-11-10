def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Test cases
def test_heapsort():
    test_cases = [
        {"input": [4, 10, 3, 5, 1], "expected": [1, 3, 4, 5, 10]},
        {"input": [12, 11, 13, 5, 6, 7], "expected": [5, 6, 7, 11, 12, 13]},
        {"input": [4, 4, 4, 4], "expected": [4, 4, 4, 4]},  # Repeated elements
        {"input": [], "expected": []},  # Empty array
        {"input": [5], "expected": [5]},  # Single element
    ]
    
    for i, case in enumerate(test_cases):
        arr = case["input"].copy()
        heapsort(arr)
        assert arr == case["expected"], f"Test case {i + 1} failed: expected {case['expected']}, got {arr}"
        print(f"Test case {i + 1} passed.")

# Run Heapsort tests
test_heapsort()
