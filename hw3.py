def quick_sort(arr):
    # 使用堆疊來模擬遞迴
    stack = [(0, len(arr) - 1)]
    
    while stack:
        start, end = stack.pop()
        if start >= end:
            continue
        
        # 選擇樞軸並進行分區操作
        pivot_index = partition(arr, start, end)
        
        # 印出目前的排序過程
        print(f"分區操作後: {arr}")
        
        # 將子區域放入堆疊
        if pivot_index - 1 > start:
            stack.append((start, pivot_index - 1))
        if pivot_index + 1 < end:
            stack.append((pivot_index + 1, end))
    
    return arr

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            print(f"交換元素: {arr}")
    
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    print(f"樞軸交換後: {arr}")
    return i + 1

# Demo data
demo_data = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]

print("初始數據:", demo_data)

# Sort the demo data using quick_sort
sorted_data = quick_sort(demo_data)

print("排序結果:", sorted_data)
