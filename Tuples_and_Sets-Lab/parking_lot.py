n = int(input())
parking_lot = set()
for i in range(n):
    direction, car_number = input().split(', ')
    if direction == 'IN':
        parking_lot.add(car_number)
    elif direction == 'OUT':
        if car_number in parking_lot:
            parking_lot.remove(car_number)
if len(parking_lot) == 0:
    print('Parking Lot is Empty')
else:
    for car in parking_lot:
        print(car)
