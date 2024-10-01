n = int(input())
arr = list(map(int, input().split()))  

max_score = max(arr)

runner_up = [x for x in arr if x != max_score]

if runner_up:
    print(max(runner_up))
else:
    print("Barcha ballar bir xil")