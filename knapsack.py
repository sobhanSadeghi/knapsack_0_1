def knapsack_greedy(values,weights,capacity):
    n=len(values)
    items=[(values[i],weights[i],i)for i in range(n)]
    items.sort(key=lambda x :x[0]/x[1] ,reverse=True)


    total_value=0
    selected_items=[0]*n

    for value,weight,indx in items:
        if capacity >= weight:
            total_value+=value
            capacity-=weight
            selected_items[indx]=1


    return total_value,selected_items



values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50


max_value,selected_item=knapsack_greedy(values,weights,capacity)

print(f'max value: {max_value}')
print(f' selected items: {selected_item}')