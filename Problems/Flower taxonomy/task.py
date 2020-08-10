iris = {}


def add_iris(id_n, species, petal_length, petal_width, **kwargs):
    global iris
    iris = {
        id_n: {
            'species': species,
            'petal_length': petal_length,
            'petal_width': petal_width
        }
    }

    iris[id_n].update(kwargs)
    return iris
