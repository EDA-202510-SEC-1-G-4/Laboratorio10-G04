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

def insert(heap,value,key):
    if heap != None:
        elem = {'key':key,
                'value':value}
        al.insert(heap['elements'],elem)     
     
    return 

def remove(heap):
    rta = []
    coger = heap["elements"]["elements"][1]
    heap["elements"]["elements"][1] = heap["elements"]["elements"][heap["size"]]
    heap["elements"]["elements"][heap["size"]] = coger
    del coger 
    heap["size"] -= 1
    return rta 
    

def swim(heap,pos):
    return 

def sink():
    return 

def default_compare_higher_value():
    return

def default_compare_lower_value():
    return
