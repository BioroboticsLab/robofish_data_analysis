import numpy as np
import math



def motion_velocity(dat):
    '''
    get the forward velocities of all fish for all frames
    :param dat: formative tracking data, n rows;
    :return: (n-1 * fish_num) forward velocity matrix
    '''
    (r, c) = dat.shape
    fish_num = int(c/4)
    X = np.zeros(shape=(r-1, fish_num))

    for i in range(r-1):
        for j in range(fish_num):
            X[i, j] = np.linalg.norm(dat[i + 1, 2 + j * 4:4 + j * 4] - dat[i, 2 + j * 4:4 + j * 4])

    return X


def forward_acc(dat, delta_t=1):
    '''
    get the forward accelerations of all fish for all frames
    acc(t) = (vf(t+delta_t)-vf(t)) / delta_t
    :param dat: formative tracking data, n rows;
    :param delta_t: the duration
    :return: the (n - delta_t * fish_num) forward acceleration matrix
    '''
    vf = forward_velocity(dat)
    (r, c) = vf.shape
    X = np.zeros(shape=(r-delta_t, c))
    for i in range (r-delta_t):
        X[i, :] =  (vf[i+delta_t]-vf[i])/delta_t

    return X


def turning_velocity(dat):
    '''
    get the turning velocities of all fish for all frames
    :param dat: formative tracking data, n rows;
    :return: the (n-1 * fish_num) turning velcotiy matrix
    '''
    (r, c) = dat.shape
    fish_num = int(c/4)
    X = np.zeros(shape=(r-1, fish_num))
    for i in range(r-1):
        for j in range(fish_num):
            X[i, j] = _angle_difference(dat[i, 4 + j * 4], dat[i+1, 4 + j * 4])

    return X


def turning_acc(dat, delta_t=1):
    '''
    get the turning accelerations of all fish for all frames
    acc(t) = (vt(t+delta_t)-vt(t)) / delta_t
    :param dat: formative tracking data, n rows;
    :param delta_t: the duration
    :return: the (n - delta_t * fish_num) turning acceleration matrix
    '''
    vt = turning_velocity(dat)
    (r, c) = vt.shape
    X = np.zeros(shape=(r-delta_t, c))
    for i in range (r-delta_t):
        # X[i, :] = (vt[i + delta_t] - vt[i]) / delta_t
        for j in range(c):
            X[i,j] = _angle_difference(vt[i,j], vt[i+delta_t,j])/delta_t

    return X


def included_angle(dat, id_a, id_b):
    '''
    get the included_angle between fish a and fish b for all frames
    (orientation of fish b - orientation of fish a)
    :param dat: formative tracking data, n rows;
    :param id_a: the id of fish a;
    :param id_b: the id of fish b;
    :return (n*1) included angle matrix:
    '''
    (r, _) = dat.shape
    X = np.zeros(shape=(r, 1))

    for i in range(r):
        X[i] = _angle_difference(dat[i][id_a*4], dat[i][id_b*4])

    return X


def linked_angle(dat, id_a, id_b):
    '''
    get the linked angle of fish a to fish b for all frames
    :param dat: formative tracking data, n rows;
    :param id_a: the id of fish a;
    :param id_b: the id of fish b;
    :return: (n*1) linked angle matrix
    '''
    (r, _) = dat.shape
    X = np.zeros(shape=(r, 1))
    for i in range(r):
        # the unit vector of fish a
        fish_a_vx = math.cos(dat[i][id_a*4])
        fish_a_vy = math.sin(dat[i][id_a*4])
        # the vector from fish a to fish b
        fish_a2b_v = dat[i][(id_b-1)*4+2:(id_b-1)*4+4] - dat[i][(id_a-1)*4+2:(id_a-1)*4+4]
        X[i] = _angle_between_vector([fish_a_vx,fish_a_vy], fish_a2b_v)

    return X


def relative_linked_angle_acc(dat, id_a, id_b, delta_t=1):
    '''
    get the acceleration of the linked angle of fish a to fish b for all frames
    let a(t) be the linked angle of fish a to fish b at frame t
    acc(t) = (a(t+delta_t)-a(t)) / delta_t
    :param dat: formative tracking data, n rows;
    :param id_a: the id of fish a;
    :param id_b: the id of fish b;
    :param delta_t: the duration
    :return: the (n - delta_t * fish_num) relative linked angle acceleration matrix
    '''
    vl = linked_angle(dat, id_a, id_b)
    (r, c) = vl.shape
    X = np.zeros(shape=(r - delta_t, 1))
    for i in range(r - delta_t):
        X[i] = _angle_difference(vl[i], vl[i + delta_t]) / delta_t

    return X


def vector_a2b(dat, id_a, id_b):
    '''
    get fish a to fish b vector for all frames
    :param dat: formative tracking data, n rows;
    :param id_a: the id of fish a;
    :param id_b: the id of fish b;
    :return: the (n*2) fish a to fish b matrix
    '''
    (r, _) = dat.shape
    X = np.zeros(shape=(r, 2))
    for i in range(r):
        X[i] = dat[i][(id_b-1)*4+2:(id_b-1)*4+4] - dat[i][(id_a-1)*4+2:(id_a-1)*4+4]

    return X

def relative_velocities(dat, id_a, id_b):
    '''
    get the ralative velocities(forward and turning) of fish b to fish a for all frames
    :param dat: formative tracking data, n rows;
    :param id_a: the id of fish a;
    :param id_b: the id of fish b;
    :return: the (n*2) relative velocities[vf, vt] matrix
    '''

    rp = relative_position(dat, id_a, id_b)
    (r, _) = rp.shape
    X = np.zeros(shape=(r - 1, 2))

    for i in range(r-1):
        X[i,0] = np.linalg.norm(rp[i+1, 0:2] - rp[i, 0:2])
        X[i,1] = _angle_difference(rp[i, 2], rp[i+1, 2])
    return X


def relative_vf_acc(dat, id_a, id_b, delta_t=1):
    '''
    get the acceleration of the relative forward velocity of fish b to fish a for all frames
    let rvf(t) be the relative forward velocity of fish a to fish b at frame t
    acc(t) = (rvf(t+delta_t) - rvf(t)) / delta_t
    :param dat: formative tracking data, n rows;
    :param id_a: the id of fish a;
    :param id_b: the id of fish b;
    :param delta_t: the duration;
    :return: the (n - delta_t * fish_num) relative forward velocity acceleration matrix
    '''
    rv = relative_velocities(dat, id_a, id_b)
    # get the forward velocity
    rvf = rv[:,0:1]
    (r, _) = rvf.shape
    X = np.zeros(shape=(r - delta_t, 1))
    for i in range(r - delta_t):
        X[i] = (rvf[i+delta_t] - rvf[i]) / delta_t

    return X


def relative_position(dat, id_a, id_b):
    '''
    get the relative position(x,y,ori) of fish b to fish a for all frames
    the fish a is fixed in origin and towards the positive direction of x-axis
    :param dat: formative tracking data, n rows;
    :param id_a: the id of fish a;
    :param id_b: the id of fish b;
    :return: n*3 matrix (x, y, ori)
    '''
    (r, _) = dat.shape
    X = np.zeros(shape=(r, 3))
    for i in range(r):
        fish_a2b_v = dat[i][(id_b - 1) * 4 + 2:(id_b - 1) * 4 + 4] - dat[i][(id_a - 1) * 4 + 2:(id_a - 1) * 4 + 4]
        ori_diff = _angle_difference(dat[i][id_a*4], dat[i][id_b*4])
        rotation_fish_b = np.dot(_rotation_matrix(-dat[i][id_a*4]), fish_a2b_v)
        x = rotation_fish_b[0,0]
        y = rotation_fish_b[0,1]
        X[i] = [x,y,ori_diff]
    return X

def nearby_fish(dat, fish_id):
    '''
    get the sorted distance of nearby fish
    :param dat: formative tracking data, n rows;
    :param fish_id: the id of fish that we calculate
    :return: sorted distance matrix, the id-map matrix of the distance matrix
    '''
    (r, c) = dat.shape
    fish_num = int(c/4)
    dist_matrix = np.zeros(shape=(r, fish_num - 1))
    id_matrix   = np.zeros(shape=(r, fish_num - 1))

    for i in range(r):
        dist_list = []
        dist_dic = {}
        posi = dat[i][(fish_id - 1) * 4 + 2:(fish_id - 1) * 4 + 4]
        for j in range(fish_num):
            if (j+1) == fish_id:
                continue
            j_posi = dat[i][j * 4 + 2: j * 4 + 4]
            d = np.linalg.norm(posi - j_posi)
            dist_list.append(d)
            dist_dic[d] = j + 1

        dist_list.sort()

        id_list = []

        for j in range(len(dist_list)):
            id_list.append(dist_dic[dist_list[j]])
        dist_matrix[i] = dist_list
        id_matrix[i]   = id_list

    return dist_matrix, id_matrix


def dist_to_tank(dat, fish_id, rays_num = 5, view_field = math.pi):
    '''
    get the distances form fish position to tank along the rays (left to right)
    :param dat: formative tracking data, n rows;
    :param fish_id: the id of fish that we calculate
    :param rays_num: the number of the rays
    :param view_field:
    :return: (n*rays_num) distance matrix
    '''
    part_size = view_field / (rays_num - 1)
    (r, _) = dat.shape
    X = np.zeros(shape=(r, rays_num))
    for i in range(r):
        posi_x = dat[i][(fish_id - 1) * 4 + 2]
        posi_y = dat[i][(fish_id - 1) * 4 + 3]
        ori    = dat[i][(fish_id - 1) * 4 + 4]

        ray_dists = [_ray_to_tank(posi_x, posi_y, ori)]
        half_num = int((rays_num-1)/2)
        for j in range(half_num):
            left = _norm_angle(ori + part_size * (j+1), math.pi)
            ray_dists = [_ray_to_tank(posi_x, posi_y, left)] + ray_dists
            right = _norm_angle(ori - part_size * (j+1), math.pi)
            ray_dists = ray_dists + [_ray_to_tank(posi_x, posi_y, right)]

        X[i] = ray_dists

    return X

# utils

def _angle_difference(a,b):
    a = _norm_angle(a, math.pi)
    b = _norm_angle(b, math.pi)
    return _norm_angle(b-a, 0)

def _norm_angle(theta, center):
    '''Normalize an angle in radians
    [0, 2*pi) if center = pi
    [-pi,pi] if center = 0
    '''
    # return theta % (2*math.pi)
    return (theta + math.pi - center) % (2*math.pi) + center - math.pi

def _angle_between_vector(v1,v2):

    '''
    :param v1: the vector 1
    :param v2: the vector 2
    :return: the angle from v1 to v2, if counterclockwise angle return positiv, then negativ
    '''

    dotv = v1[0] * v2[0] + v1[1] * v2[1]
    detv = v1[0] * v2[1] - v1[1] * v2[0]

    return math.atan2(detv, dotv)

def _rotation_matrix(theta):
    c = math.cos(theta)
    s = math.sin(theta)
    return np.matrix([[c, -s], [s, c]])


def _ray_to_tank(x, y, ori, tank_x = 88, tank_y = 88):
    '''

    :param x: point_x
    :param y: point_y
    :param ori: the orientation of ori
    :param tank_x:
    :param tank_y:
    :return: distance from point to tank along ray
    '''
    if ori == 0:
        return tank_x - x
    elif ori == math.pi/2:
        return tank_y - y
    elif ori == math.pi:
        return x
    elif ori == math.pi*3/2:
        return y
    elif ori > 0 and ori < math.pi/2:
        d1 = (tank_x - x) / math.cos(ori)
        d2 = (tank_y - y) / math.cos(math.pi/2 - ori)
        if d1 >= d2:
            return d2
        else:
            return d1
    elif ori > math.pi/2 and ori < math.pi:
        d1 = x / math.cos(math.pi - ori)
        d2 = (tank_y - y) / math.cos(ori - math.pi/2)
        if d1 >= d2:
            return d2
        else:
            return d1
    elif ori > math.pi and ori < math.pi*3/2:
        d1 = x / math.cos(ori - math.pi)
        d2 = y / math.cos(math.pi*3/2 - ori)
        if d1 >= d2 :
            return d2
        else:
            return d1
    elif ori > math.pi * 3/2 and ori < 2 * math.pi:
        d1 = (tank_x - x) / math.cos(math.pi*2 - ori)
        d2 = y / math.cos(ori - math.pi * 3/2)
        if d1 >= d2:
            return d2
        else :
            return d1
    else:
        return 0
