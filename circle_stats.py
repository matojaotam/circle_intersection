from math import sqrt, isclose


def radius_sum(r1, r2):

    return r1 + r2


def euclid_distance(x1, y1, x2, y2):

    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


def has_intersection(circle_1, circle_2):


    x1, y1, r1 = circle_1["x"], circle_1["y"], circle_1["r"]
    x2, y2, r2 = circle_2["x"], circle_2["y"], circle_2["r"]

    d = euclid_distance(x1, y1, x2, y2)
    r_sum = radius_sum(r1, r2)
    r_diff = abs(r1 - r2)

    if d > r_sum:
        return {"is_intersection": False, "intersections_count": 0}

    if isclose(d, r_sum):
        return {"is_intersection": True, "intersections_count": 1}

    if r_diff < d < r_sum:
        return {"is_intersection": True, "intersections_count": 2}

    if isclose(d, r_diff):
        return {"is_intersection": True, "intersections_count": 1}

    if d < r_diff:
        return {"is_intersection": False, "intersections_count": 0}

    return {"is_intersection": False, "intersections_count": 0}