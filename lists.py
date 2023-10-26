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
    # TODO: add Biel at the end of the list
    # TODO: add Basel at Index 2
    print('add_cities:\n', cities)


def remove_cities(cities):
    # TODO: remove the last city from the list
    # TODO: remove the city at Index 1
    # TODO: remove Bern from the list
    print('remove_cities:\n', cities)


def find_cities(cities):
    print('find_city:')
    # TODO: print the city at Index 4
    # TODO: print the position of Genf
    pass


def loop_cities(cities):
    print('loop_cities:')
    # TODO: print all cities in the list. output must be 'Nr. x: cityname', i.e. 'Nr. 1: Zürich'


def sort_cities(cities):
    print('sort_cities:')
    # TODO: print all cities ordered by Name (descending). output must be 'Nr. x: cityname', i.e. 'Nr. 8: Zürich'


if __name__ == '__main__':
    main()
