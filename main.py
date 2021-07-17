from Dataset import *
from BigramModel import *


if __name__ == "__main__":

    # read datasets
    positive_train_set, positive_test_set = get_positive_train_test_set()
    negative_train_set, negative_test_set = get_negative_train_test_set()

    # process datasets
    pre_process(positive_train_set), pre_process(positive_test_set)
    pre_process(negative_train_set), pre_process(negative_test_set)

    # create bigram model object
    lambda_arr = [0.2, 0.3, 0.5]    # [h0, h1, h2]
    epsilon = 0.2
    cut_down = 2
    cut_above= 10
    bigram_model = BigramModel(positive_train_set, negative_train_set, lambda_arr, epsilon)
    bigram_model.learning()     # start learning


    # analyse
    for i





    # TODO create unigram model object

    # TODO analyse and compare models

    pass