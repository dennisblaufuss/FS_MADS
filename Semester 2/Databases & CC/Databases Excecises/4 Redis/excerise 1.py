import redis
r = redis.StrictRedis(host="localhost", port=6379, charset="utf-8", decode_responses=True)


def createNewCar(manu, type, price, specials: list):
    car_id = lenCars() + 1
    r.set('car:' + str(car_id) + ':manufactor', str(manu))
    r.set('car:' + str(car_id) + ':type', str(type))
    r.set('car:' + str(car_id) + ':price', str(price))
    for ss in specials:
        r.lpush('car:' + str(car_id) + ':specials', ss)
    return


def lenCars():
    if r.keys('car:*') == []:
        return 0
    l_car_id_tmp = r.keys('car:*')
    l_car_id = []
    for car_id_tmp in l_car_id_tmp:
        car_id = car_id_tmp[4]
        l_car_id.append(int(car_id))
    return max(l_car_id)


def retrieveCar(car_id):
    car = []
    car.append(r.get('car:' + str(car_id) + ':manufactor'))
    car.append(r.get('car:' + str(car_id) + ':type'))
    car.append(r.get('car:' + str(car_id) + ':price'))
    car.append(r.lrange('car:' + str(car_id) + ':specials', 0, -1))


createNewCar('BMW', 'X6', 6000, ['Dickverlängerung'])
