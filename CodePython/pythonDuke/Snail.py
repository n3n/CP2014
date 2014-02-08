from math import ceil, floor

def snail_state(d):
    if d > 20000000:
        return 'fried'
    time = (d-10)/3.0
    if time <= 0:
        # not have anything.
        return d*2*60
    if time == int(time):
        time = time*27 + 20
    else:
        time = ceil(time)*27 + (d-ceil(time)*3)*2
    t_miniute = int(ceil(time*60))
    if t_miniute >= 2152857600:
        return 'dead'
    return t_miniute

d = input()
print snail_state(d)
