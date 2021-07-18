from Dataset import *
from BigramModel import *


def do_test(test_set, label, model):
    correct_answer_count = 0
    for sentence in test_set:
        model_response = model.recognize_sentence(sentence)
        if model_response == label or model_response == "equal":
            correct_answer_count += 1

    print(correct_answer_count / len(test_set))
    return correct_answer_count/len(test_set)


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
    bigram_model = BigramModel(positive_train_set, negative_train_set, lambda_arr, epsilon, cut_down, cut_above)
    bigram_model.learning()     # start learning
    # print(bigram_model.count_unary_train_pos_dict)


    # analyse
    accuracy_pos_test = do_test(positive_test_set, "positive", bigram_model)
    print("Accuracy in positive test set : ", accuracy_pos_test * 100)
    accuracy_neg_test = do_test(negative_test_set, "negative", bigram_model)
    print("Accuracy in positive test set : ", accuracy_neg_test * 100)







    # TODO create unigram model object
