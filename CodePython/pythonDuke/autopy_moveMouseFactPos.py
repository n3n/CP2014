import autopy

def move_fact(tar_x, tar_y):
    cnt = 0
    cur_x, cur_y = -1, -1
    while cur_x != tar_x or cur_y != tar_y:
        autopy.mouse.move(tar_x, tar_y)
        cur_x, cur_y = autopy.mouse.get_pos()
        print cur_x, cur_y, tar_x, tar_y
        cnt += 1
    print cnt

move_fact(100,600)
