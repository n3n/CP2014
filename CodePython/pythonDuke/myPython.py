def total_cost(type_car, isHasGPS, days, isSIIT):
    return (cars_hire[type_car-1][1]*days + [0,200][isHasGPS]) * [1, 0.9][isSIIT]

cars_hire = [('BMW', 1800), ('Toyota', 1200), ('Honda', 600)]

# Choose car.
for i, car_hire in enumerate(cars_hire):
    print str(i+1)+'.', car_hire[0], str(car_hire[1]) + '/day' 
type_car = input('choose: ')

# want GPS ?
isHasGPS = False
if raw_input('Get GPS? 200/day  (y/n)\nchoose: ') == 'y':
    isHasGPS = True

# number of days of car hire.
days = input('Days for car hire: ')

# SIIT student ?
isSIIT = False
if raw_input('Are you SIIT student? (y/n)\nchoose: ') == 'y':
    isSIIT = True

print '\nTotal cost: ' + str(total_cost(type_car, isHasGPS, days, isSIIT))
print 'Thanks you'
