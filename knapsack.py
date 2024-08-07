def knapsack(n,items, max_weight):
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(max_weight + 1):
            if items[i-1][1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - items[i-1][1]] + items[i-1][2])
            else:
                dp[i][w] = dp[i-1][w]
    
    w = max_weight
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(items[i-1])
            w -= items[i-1][1]
    
    selected_items.reverse()
    return dp[n][max_weight], selected_items


n = int(input("\nEnter number of items: "))
items = []
print("\nEnter adjacency list edges [item,weight,value] separated by space:")
for i in range(n):
    items.append(list(map(int,input(f"Edge {i+1}: ").split())))

max_weight = int(input("enter the max_weight"))
max_value, selected_items = knapsack(n,items, max_weight)
print("Maximum Value:", max_value)
print("Selected Items:", selected_items)

