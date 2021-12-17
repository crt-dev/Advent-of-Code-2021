class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def __repr__(self):
        return "({},{})".format(self.x, self.y)


eg_target_min = Point(20, -10)
eg_target_max = Point(30,  -5)
ex_target_min = Point(25, -260)
ex_target_max = Point(67,  -200)

def plot_trajectory(target_min, target_max, v0):
    p = [Point(0, 0)]
    v = [v0]
    x_direction = int(v0.x / abs(v0.x))
    t = 1
    while True:
        np = Point(p[t-1].x + v[t-1].x, p[t-1].y + v[t-1].y)
        nv = Point(v[t-1].x - x_direction if abs(v[t-1].x) > 0 else 0, v[t-1].y - 1)

        if target_min.x <= np.x <= target_max.x and target_min.y <= np.y <= target_max.y:
            #Register hit
            return True, max([pos.y for pos in p])

        if nv.x == 0 and target_min.x < np.x > target_max.x or np.y < target_min.y:
            #Register miss
            return False, None

        p.append(np)
        v.append(nv)
        t += 1


def solution_p1(target_min, target_max, v0x):
    """
    Observed that for any positive y the probe passes through y axis equal to initial velocity.
    therefore v0y has to be
    x just has to be in bounds
    """
    v0 = Point(v0x, abs(target_min.y) - 1)
    return plot_trajectory(target_min, target_max, v0)


def solution_p2_ex():
    target_min = Point(20, -10)
    target_max = Point(30,  -5)

    vx_range = range(6, target_max.x + 1)
    print(list(vx_range))
    vy_range = range(abs(target_min.y) - 1, target_min.y -1, -1)
    print(list(vy_range))
    hits = set()

    for v0x in vx_range:
        for v0y in vy_range:
            v0 = Point(v0x, v0y)
            result, y = plot_trajectory(target_min, target_max, v0)
            if result:
                hits.add(v0)

    print(len(hits))


def solution_p2_eg():
    vx_range = range(6, eg_target_max.x + 1)
    vy_range = range(abs(eg_target_min.y) - 1, eg_target_min.y -1, -1)
    return find_permutations(eg_target_min, eg_target_max, vx_range, vy_range)


def solution_p2_ex():
    """
    Trial and error approach as I can see where approx bounds will be through observation
    """
    vx_range = range(7, ex_target_max.x + 2)
    vy_range = range(abs(ex_target_min.y), ex_target_min.y - 2, -1)
    return find_permutations(ex_target_min, ex_target_max, vx_range, vy_range)


def find_permutations(target_min, target_max, vx_range, vy_range):
    hits = set()
    count = 1
    for v0x in vx_range:
        for v0y in vy_range:
            if count % 10000 == 0:
                print("processing ", count)
            v0 = Point(v0x, v0y)
            result, y = plot_trajectory(target_min, target_max, v0)
            if result:
                hits.add(v0)
            count += 1

    return len(hits)


print("p1eg y_max = ", solution_p1(eg_target_min, eg_target_max, 6)) #45
print("p1ex y_max = ", solution_p1(ex_target_min, ex_target_max, 10)) #33670
print("p2eg permutations = ", solution_p2_eg()) #112
print("p2ex permutations = ", solution_p2_ex()) #4903
