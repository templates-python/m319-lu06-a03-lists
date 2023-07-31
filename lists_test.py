import lists


def test_add(monkeypatch, capsys):
    cities = ['Zürich', 'Genf', 'Lausanne', 'Bern', 'Winterthur', 'Luzern', 'St. Gallen', 'Lugano']
    lists.add_cities(cities)
    captured = capsys.readouterr()
    assert captured.out == "add_cities:\n ['Zürich', 'Genf', 'Basel', 'Lausanne', 'Bern', 'Winterthur', 'Luzern', 'St. Gallen', 'Lugano', 'Biel']\n"

def test_remove(monkeypatch, capsys):
    cities = ['Zürich', 'Genf', 'Lausanne', 'Bern', 'Winterthur', 'Luzern', 'St. Gallen', 'Lugano']
    lists.remove_cities(cities)
    captured = capsys.readouterr()
    assert captured.out == "remove_cities:\n ['Zürich', 'Lausanne', 'Winterthur', 'Luzern', 'St. Gallen']\n"

def test_find(monkeypatch, capsys):
    cities = ['Zürich', 'Genf', 'Lausanne', 'Bern', 'Winterthur', 'Luzern', 'St. Gallen', 'Lugano']
    lists.find_cities(cities)
    captured = capsys.readouterr()
    assert captured.out == "find_city:\nWinterthur\n1\n"

def test_loop(monkeypatch, capsys):
    cities = ['Zürich', 'Genf', 'Lausanne', 'Bern', 'Winterthur', 'Luzern', 'St. Gallen', 'Lugano']
    lists.loop_cities(cities)
    captured = capsys.readouterr()
    assert captured.out == "loop_cities:\nNr. 1: Zürich\nNr. 2: Genf\nNr. 3: Lausanne\nNr. 4: Bern\nNr. 5: Winterthur\nNr. 6: Luzern\nNr. 7: St. Gallen\nNr. 8: Lugano\n"

def test_sort(monkeypatch, capsys):
    cities = ['Zürich', 'Genf', 'Lausanne', 'Bern', 'Winterthur', 'Luzern', 'St. Gallen', 'Lugano']
    lists.sort_cities(cities)
    captured = capsys.readouterr()
    assert captured.out == "sort_cities:\nNr. 8: Zürich\nNr. 7: Winterthur\nNr. 6: St. Gallen\nNr. 5: Luzern\nNr. 4: Lugano\nNr. 3: Lausanne\nNr. 2: Genf\nNr. 1: Bern\n"