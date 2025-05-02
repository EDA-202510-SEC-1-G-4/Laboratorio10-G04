from DataStructures.List import array_list as al
from DataStructures.Map import
from DataStructures.Map import 
from DataStructures.Map import 

def new_heap(is_min_pq=True):
    heap = {'elements':al.new_list(),
            'size':0,
            'cmp_function':default_compare_lower_value}
    if is_min_pq == False:
        heap['cmp_function'] = default_compare_higher_value
    return heap

def size():
    return

def is_empty():
    return 

def get_first_priority(heap):
    first = None
    if heap['size'] > 0:
        first = heap['elements']['elements'][1]['value']
    return first

def insert(): 
    return 

def remove():
    return

def swim(heap,pos):
    if heap['size'] > 0:
        cmp_function = heap['cmp_function']
        elem = heap['elements']['elements'][pos]
        padre = heap['elements']['elements'][pos//2]
        if not cmp_function(padre,elem):
            heap['elements']['elements'][pos//2] = elem
            heap['elements']['elements'][pos] = padre
    return heap

def sink():
    return 

def default_compare_higher_value():
    return

def default_compare_lower_value():
    return
