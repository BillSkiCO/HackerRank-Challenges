#!/usr/bin/env python
# -*- coding: utf-8 -*-


class City():
    
    def __init__(self):
        """
        self.roadto: list of cities that this city has roads to (One Way)
        self.paths_to_me: Useful for storing number of paths for path counting solution
        self.visited: Useful to check for cycles
        """
        self.roadto = []
        self.paths_to_me = 0
        self.visited = False
        self.is_in_cycle = False
        self.is_connected_to_warfare_capital = False
        
# Note: city index will have to be (title - 1). Example: City #3 will have index [3-1] -> city_list[2]
city_list = []

# Instantiate dynamic programming cache
connected_to_warfare_capital = []

# From STDIN input: n[0] = Number of cities, n[2] = number roads
n = input().split(' ')

# Found all cities... Way cooler in Civ 5.
for i in range(int(n[0])):
    a = City()
    city_list.append(a)

# Store road connections inside of city
for j in range(int(n[1])):
    # road_info[0] == city from, road_info[1] == city to
    road_info = input().split(' ')
    city_list[int(road_info[0])-1].roadto.append(int(road_info[1]))
    
    
def cycle_test(list_of_cities, number_of_cities):
    """
    "BFS" Check each city for roads that lead to already visited cities. If present, cycle exists.
    Also, store city numbers that are connected to the warfare capital in cache for path addition later.
    
    :param list_of_cities: Take in a list of city objects
    :param number_of_cities: Take in the number of cities in the list (int)
    :return: True if cycle_test detects a cycle, list of cities conencted to warfare capital if no cycle found
    """
    
    for city_index in range(number_of_cities):
        list_of_cities[city_index].visited = True
        check_these = list_of_cities[city_index].roadto
        
        # Dynamic Programming to get cities that are connected to the warfare capital for path addition.
        # Number_of_cities just so happens to be the city name of the warfare capital as well! =]
        if number_of_cities in check_these:
            connected_to_warfare_capital.append(city_index)
            list_of_cities[city_index].is_connected_to_warfare_capital = True
            
            if list_of_cities[city_index].is_connected_to_warfare_capital and \
                    list_of_cities[city_index].is_in_cycle:
                return True
            
        for target_city in check_these:
            if list_of_cities[target_city-1].visited:
                list_of_cities[target_city-1].is_in_cycle = True
                list_of_cities[city_index].is_in_cycle = True


def number_of_paths(list_of_cities, number_of_cities, connected_to_warfare_capital_list):
    """
    Function to return the number of paths to the warfare capital. Utilizes connected_to_warfare_capital_list
    to only check adjacent cities and add their paths_to_me variables.
    
    :param list_of_cities: Take in a list of city objects that has been pre-checked to not contain any cycles.
    :param number_of_cities: Take in the number of cities in the list (int)
    :return: number of paths to warfare capital
    """
    
    total_paths = 0
    
    for city_name in range(number_of_cities):
        for connected_city in list_of_cities[city_name].roadto:
            list_of_cities[connected_city-1].paths_to_me += 1
    
    # Add up number of paths in cities adjacent to war capital to get final path number!
    for city_index_number in connected_to_warfare_capital_list:
        total_paths += list_of_cities[city_index_number].paths_to_me
    
    return total_paths


def check_if_connected_to_war(list_of_cities, number_of_cities):
    # Warfare capital is connected to itself...
    list_of_cities[number_of_cities-1]is_connected_to_warfare_capital = True
    
    for x in range(number_of_cities-1,0,-1)
        for y in (list_of_cities[x].roadto)
            if list_of_cities[y-1].is_connected_to_warfare_capital:
                list_of_cities[x].is_connected_to_warfare_capital = True
                
    



        
if cycle_test(city_list, int(n[0])):
    print('INFINITE PATHS')
else:
    print(number_of_paths(city_list, int(n[0]), connected_to_warfare_capital)%(10**9))