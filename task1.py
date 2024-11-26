steps_input = input('Enter the number of steps taken each day "separated by spaces": ')
steps_list = list(map(int, steps_input.split()))


print("Highest steps: ",max(steps_list))
print("Lowest steps: ",min(steps_list))
print("Average steps: ",sum(steps_list) / len(steps_list))
print("Steps in descending order: ",sorted(steps_list, reverse=True))