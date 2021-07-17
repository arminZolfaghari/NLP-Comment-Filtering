from collections import Counter



class BigramModel():

    def __init__(self, train_pos_set, train_neg_set):
        self.train_positive_set = train_pos_set
        self.train_negative_set = train_neg_set
        self.train_pos_dict = {}
        self.train_neg_dict = {}


    def create_words_dict(self, words_dict, dataset):  # dataset is an array of sentences (each element is a sentence)
        # dataset example = ["this is sent1", "this is sent2"]
        for sentence in dataset:
            print('sent: ', sentence)
            words_in_sent = sentence.split(' ')
            print(words_in_sent)
            words_in_sent = Counter(words_in_sent)
            print(words_in_sent)
            for word in words_in_sent.keys():
                print('word: ', word)
                if word in words_dict.keys():
                    words_dict[word] += 1
                else:
                    words_dict[word] = 1
        return words_dict



