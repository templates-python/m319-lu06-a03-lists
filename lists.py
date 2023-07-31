def main():
    cities = ['Zürich', 'Genf', 'Lausanne', 'Bern', 'Winterthur', 'Luzern', 'St. Gallen', 'Lugano']
    add_cities(cities)

    cities = ['Zürich', 'Genf', 'Lausanne', 'Bern', 'Winterthur', 'Luzern', 'St. Gallen', 'Lugano']
    remove_cities(cities)

    cities = ['Zürich', 'Genf', 'Lausanne', 'Bern', 'Winterthur', 'Luzern', 'St. Gallen', 'Lugano']
    find_cities(cities)
    loop_cities(cities)
    sort_cities(cities)


def add_cities(cities):
    cities.append('Biel')  # add Biel at the end of the list
    cities.insert(2, 'Basel')  # add Basel at Position 2
    print('add_cities:\n', cities)


def remove_cities(cities):
    cities.pop()  # remove the last city from the list
    cities.pop(1)  # remove the city at position 1
    cities.remove('Bern')  # remove Bern from the list
    print('remove_cities:\n', cities)


def find_cities(cities):
    print('find_city:')
    print(cities[4])  # print the city at position 4
    print(cities.index('Genf'))  # print the position of Genf


def loop_cities(cities):
    print('loop_cities:')
    # print all cities in the list. output must be 'Nr. x: cityname', i.e. 'Nr. 1: Zürich'
    number = 1
    for city in cities:
        print(f'Nr. {number}: {city}')
        number += 1


def sort_cities(cities):
    print('sort_cities:')
    # print all cities ordered by Name (descending). output must be 'Nr. x: cityname', i.e. 'Nr. 8: Zürich'
    number = len(cities)
    for city in sorted(cities, reverse=True):
        print(f'Nr. {number}: {city}')
        number -= 1

if __name__ == '__main__':
    main()