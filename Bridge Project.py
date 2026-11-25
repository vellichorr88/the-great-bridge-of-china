#Length of bridge = 1200mm

#Base case 1


def weight_of_carts(weight):
    close_freight = weight
    far_freight = weight*1.10
    weight_loco = far_freight*1.39

    return close_freight, far_freight, weight_loco

def distances(n):
    distances = [n, n - 176, n - 176 - 164, n - 176 - 164 -176, n - 176 - 164 - 176 - 164, n - 176 - 164 - 176 - 164 - 176]

    usable = [0, 0, 0, 0, 0, 0]
    for i in range(6):
        if 0 < distances[i] <= 1200:
            usable[i] = 1

    return distances, usable

def forces(weight, run):
    base_case_loco = 182
    base_case_freight = 135

    close_freight, far_freight, weight_loco = weight_of_carts(weight)


    if run == 1:
        forces = [base_case_loco/2, base_case_loco/2, base_case_freight/2, base_case_freight/2, base_case_freight/2, base_case_freight/2]
    else:
        forces = [weight_loco/2, weight_loco/2, close_freight/2, close_freight/2, far_freight/2, far_freight/2]

    return forces

def reac_forces(n, weight, run):
    #gives the reaction forces based on a certain distance of the locomotive from the first support, and the weight of the lightest loco

    loads = forces(weight, run)
    distance, usable = distances(n)


    #reaction force at opposite point
    moment_a = 0
    for i in range(6):
        moment_a += distance[i] *loads[i] * usable[i]


    reaction_b = moment_a/1200

    sum_y = 0
    for i in range(6):
        sum_y += loads[i] * usable[i]

    reaction_a = sum_y - reaction_b

    return reaction_a, reaction_b


def max_bmd(n, weight, run):

    a, b = reac_forces(n, weight, run)
    distance, usable = distances(n)
    loads = forces(weight, run)
    distance.reverse()
    usable.reverse()
    loads.reverse()

    new_distances = []
    new_loads = []

    for i in range(6):
       if usable[i] == 1:
           new_distances.append(distance[i])
           new_loads.append(loads[i])


    max_force = a
    sum_moments = 0
    distance_from_a = 0
    for i in range(len(new_distances)):
        if max_force <= 0:
            return sum_moments, distance_from_a
        else:
            sum_moments += max_force * (new_distances[i] - distance_from_a)
            distance_from_a = new_distances[i]
            max_force -= new_loads[i]

    return sum_moments, distance_from_a

def max_shear_force(n, weight, run):
    a, b = reac_forces(n, weight, run)
    return max(a, b)




BMD = {}
a = 0
b = 0
for i in range(0, 2000):
    moments, dist = max_bmd(i, 2, 2)
    if dist not in BMD or moments > BMD[dist]:
        if moments > a:
            a = moments
            b = i

        BMD[dist] = moments

A = dict(sorted(BMD.items(), key=lambda item: item[1]))

print(b)
print(max_bmd(b, 2, 2))

max_shear = 0
c = 0
d = 0
for i in range(0, 2000):
    if max_shear_force(i, 2, 2) > c:
        c = max_shear_force(i, 2, 2)
        d = i

print(c)
print(d)





