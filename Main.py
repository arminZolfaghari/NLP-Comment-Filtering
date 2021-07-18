from Dataset import *
from BigramModel import *
from UnigramModel import *


def do_test(dict_sentences_with_label, model):
    correct_answer_count, number_all_sentences_test = 0, 0
    for label, sentences in dict_sentences_with_label.items():
        for sentence in sentences:
            model_response = model.recognize_sentence(sentence)
            if model_response == label:
                correct_answer_count += 1
            number_all_sentences_test += 1

    return correct_answer_count / number_all_sentences_test


if __name__ == "__main__":

    # read datasets
    positive_train_set, positive_test_set = get_positive_train_test_set()
    negative_train_set, negative_test_set = get_negative_train_test_set()

    # process datasets
    pre_process(positive_train_set), pre_process(positive_test_set)
    pre_process(negative_train_set), pre_process(negative_test_set)

    # create bigram model object
    lambda_arr = [0.1, 0.3, 0.6]  # [h0, h1, h2]
    epsilon = 0.2
    cut_down = 2
    cut_above = 10
    bigram_model = BigramModel(positive_train_set, negative_train_set, lambda_arr, epsilon, cut_down, cut_above)
    bigram_model.learning()  # bigram_model start learning

    # create unigram model object
    lambda_arr = [0.2, 0.8]  # [h0, h1]
    epsilon = 0.2
    cut_down = 2
    cut_above = 10
    unigram_model = UnigramModel(positive_train_set, negative_train_set, lambda_arr, epsilon, cut_down, cut_above)
    unigram_model.learning()  # unigram_model start learning

    # analyse
    # dictionary keys are labels and values are sentences
    dict_test_with_label = {"positive": positive_test_set, "negative": negative_test_set}

    print("*** Bigram model ***")
    bigram_model_accuracy_test = do_test(dict_test_with_label, bigram_model)
    print("Accuracy in test set : ", bigram_model_accuracy_test * 100)

    print("*** Unigram model ***")
    unigram_model_accuracy_test = do_test(dict_test_with_label, unigram_model)
    print("Accuracy in test set : ", unigram_model_accuracy_test * 100)

    # get input from user
    while True:
        input_sent = input("Enter a sentence: ")
        if input_sent == '!q':
            break
        else:
            label = bigram_model.recognize_sentence(input_sent)
            if label == 'positive':
                print('do not filter this')
            elif label == 'negative':
                print('filter this')
            else:
                print('cant say for sure :/')

    # TODO create unigram model object
