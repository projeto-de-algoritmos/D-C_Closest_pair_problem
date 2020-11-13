import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def sort_x(e):
    return e.x

def sort_y(e):
    return e.y

def main():
    while(True):
        x = int(float(input()))

        if x == 0: break


        closest_pair_list = [Point(*list(map(float, input().split(" ")))) for _ in range(x)]
        closest_pair_list.sort(key=sort_x)

        min_distance = closest_pair(closest_pair_list)[0]

        if min_distance >= 10000:
            print("INFINITY")
        else:
            print("{:.4f}".format(min_distance))
    
    return 0; 

def closest_pair(lst: 'List'):
    lst_size = len(lst)

    # Condição de parada
    if lst_size <= 1: return 10001, lst
    
    mid = math.ceil(lst_size/2)

    # Mediana
    median = lst[mid]

    min_esq, A = closest_pair(lst[0:mid])
    min_dir, B = closest_pair(lst[mid:lst_size])

    global_min = min(min_esq, min_dir)

    S = sorted([*A, *B], key=sort_y)

    s_limited = [ item for item in lst if euclidiana(item, Point(median.x, item.y)) < global_min ]

    for index, item  in enumerate(s_limited):
        acc = 0
        for i in range(index + 1, len(s_limited)):
            if acc == 7: break
            distance = euclidiana(item, s_limited[i])
            if  distance < global_min:
                global_min = distance

    return global_min, S

def euclidiana(point_a, point_b):
    x = point_b.x - point_a.x
    y = point_b.y - point_a.y

    return math.sqrt(math.pow(x, 2) + math.pow(y,2))

if __name__ == "__main__":
    main()

