initial_fuel = [int(x) for x in input().split()]
additional_consumption = [int(x) for x in input().split()]
fuel_needed_to_reach_altitude = [int(x) for x in input().split()]

reached_altitudes = 0
failed_altitude = 0

while initial_fuel and additional_consumption and fuel_needed_to_reach_altitude:
    current_fuel = initial_fuel[-1]
    consumption_index = additional_consumption[0]
    needed_fuel = fuel_needed_to_reach_altitude[0]

    fuel_left = current_fuel - consumption_index

    if fuel_left >= needed_fuel:
        reached_altitudes += 1
        print(f'John has reached: Altitude {reached_altitudes}')
        initial_fuel.pop()
        additional_consumption.pop(0)
        fuel_needed_to_reach_altitude.pop(0)
    else:
        failed_altitude = reached_altitudes + 1
        print(f'John did not reach: Altitude {failed_altitude}')
        if reached_altitudes == 0:
            print('John failed to reach the top.\nJohn didn\'t reach any altitude.')
            exit()
        print(f'John failed to reach the top.\nReached altitudes: {", ".join(f"Altitude {i}" for i in range(1, failed_altitude))}')
        exit()


print('John has reached all the altitudes and managed to reach the top!')

