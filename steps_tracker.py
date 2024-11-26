def daily_steps_tracker():
    steps_input = input("Enter the steps taken each day (space-separated): ")
    
    steps_list = list(map(int, steps_input.split()))
    
    if not steps_list:
        print("No steps data provided.")
        return

    highest_steps = max(steps_list)
    lowest_steps = min(steps_list)
    
    average_steps = sum(steps_list) / len(steps_list)
    
    sorted_steps = sorted(steps_list, reverse=True)
    
    print("\n--- Daily Steps Tracker ---")
    print(f"Highest steps: {highest_steps}")
    print(f"Lowest steps: {lowest_steps}")
    print(f"Average steps: {average_steps:.2f}")
    print("Step counts (descending order):", sorted_steps)

daily_steps_tracker()
