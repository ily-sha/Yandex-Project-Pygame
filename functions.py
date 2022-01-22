import random


def get_shape_type(restart=False):
    shapes = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']
    shapes_queue = ['I', 'J', 'L', 'O', 'S', 'T', 'Z'] * 5
    shapes_history = []
    if not restart:
        shape_number = random.randint(0, 34)
        shape = shapes_queue[shape_number]
        del shapes_queue[shape_number]
        shapes_history.append(shape)
        if len(shapes_history) > 35:
            shapes_history = shapes_history[len(shapes_history) - 35:]
        i, j, l, o, s, t, z = 0, 0, 0, 0, 0, 0, 0
        for k in shapes_history:
            if k == 'I':
                i += 1
            elif k == 'J':
                j += 1
            elif k == 'L':
                l += 1
            elif k == 'O':
                o += 1
            elif k == 'S':
                s += 1
            elif k == 'T':
                t += 1
            elif k == 'Z':
                z += 1
        shapes_quantity = [i, j, l, o, s, t, z]
        shapes_quantity.sort(reverse=True)
        if i == shapes_quantity[0]:
            shapes_queue.append('I')
        elif j == shapes_quantity[0]:
            shapes_queue.append('J')
        elif l == shapes_quantity[0]:
            shapes_queue.append('L')
        elif o == shapes_quantity[0]:
            shapes_queue.append('O')
        elif s == shapes_quantity[0]:
            shapes_queue.append('S')
        elif t == shapes_quantity[0]:
            shapes_queue.append('T')
        elif z == shapes_quantity[0]:
            shapes_queue.append('Z')
        return shape