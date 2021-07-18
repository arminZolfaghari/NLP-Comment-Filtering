import random
import string


# read positive comments file and store
def store_positive_comments_from_file():
    positive_comment_arr = []
    file = open("./dataset/rt-polarity.pos", "r")
    for comment in file:
        positive_comment_arr.append(comment)

    return positive_comment_arr


# read negative comments file and store
def store_negative_comments_from_file():
    negative_comment_arr = []
    file = open("./dataset/rt-polarity.neg", "r")
    for comment in file:
        negative_comment_arr.append(comment)

    return negative_comment_arr


def get_positive_train_test_set():
    positive_dataset = store_positive_comments_from_file()
    dataset_len = len(positive_dataset)
    test_set_len = int(dataset_len * 0.1)
    test_set = []
    for i in range(test_set_len):
        test = positive_dataset.pop(random.randint(0, len(positive_dataset) - 1))
        test_set.append(test)
    train_set = positive_dataset

    return train_set, test_set


def get_negative_train_test_set():
    negative_dataset = store_negative_comments_from_file()
    dataset_len = len(negative_dataset)
    test_set_len = int(dataset_len * 0.1)
    test_set = []
    for i in range(test_set_len):
        test = negative_dataset.pop(random.randint(0, len(negative_dataset) - 1))
        test_set.append(test)
    train_set = negative_dataset

    return train_set, test_set


# remove sign character in sentence
def pre_process(set):
    for i in range(len(set)):
        for char in set[i]:
            if char in string.punctuation:
                set[i] = set[i].replace(char, "")

    # return set


# sett = store_positive_comments_from_file()
# print(sett[0])
# print(sett[1])
#
# pre_process(sett)
# print(sett[0])
# print(sett[1])
