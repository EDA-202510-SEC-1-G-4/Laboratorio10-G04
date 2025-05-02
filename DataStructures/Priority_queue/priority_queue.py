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

def size(pq):
    return pq["size"]

def is_empty(pq):
    return pq["size"] == 0

def get_first_priority(heap):
    first = None
    if heap['size'] > 0:
        first = heap['elements']['elements'][1]['value']
    return first

def insert(pq,value,key): 

    return 

def remove():
    return

def swim(heap,pos):
    return 

def sink(pq,pos):
    array = pq['elements']['elements']
    boole = array[2*pos+1]['key'] < array[2*pos]['key']
    menor = array[2*pos]['key']
    if boole:
        menor = array[2*pos+1]['key']

    while array[pos]['key'] < menor:
        if array[pos] < menor:
            
        else:
            pos = 2*pos+2
     



    return 

def default_compare_higher_value():
    return

def default_compare_lower_value():
    return
