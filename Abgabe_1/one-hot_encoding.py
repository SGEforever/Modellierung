import numpy as np

def one_hot_encoder(data):

    categories = np.unique(data)
    
    category_to_index = {}
    for categorie, col in enumerate(categories):
        category_to_index[col] = categorie

    one_hot = np.zeros((len(data), len(categories)))

    for row, value in enumerate(data):
        col = category_to_index[value]
        one_hot[row, col] = 1


    return categories, one_hot

t = one_hot_encoder([1, 5, 1, 2])
print(t)