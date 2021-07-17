from collections import Counter


# insert <s> to first and append </s> to end array, return words array
def get_words_array(sentence):
    words_in_sent = sentence.split(' ')
    words_in_sent.insert(0, '<s>')
    words_in_sent.append('</s>')

    return words_in_sent


class UnigramModel():

    def __init__(self, train_pos_set, train_neg_set, lambda_arr, epsilon):
        self.train_positive_set = train_pos_set
        self.train_negative_set = train_neg_set
        self.lambda_arr = lambda_arr  # [h0, h1, h2] => weights for probability
        self.epsilon = epsilon
        self.count_unary_train_pos_dict = {}
        self.count_unary_train_neg_dict = {}
        self.number_words_in_neg = 0
        self.number_words_in_pos = 0
        self.alpha_cut = 2

    def do_alpha_cut(self):
        for word in self.count_unary_train_pos_dict.keys():
            if self.count_unary_train_pos_dict[word] <= 2:
                del self.count_unary_train_pos_dict[word]

        for word in self.count_unary_train_neg_dict.keys():
            if self.count_unary_train_neg_dict[word] <= 2:
                del self.count_unary_train_neg_dict[word]

    def create_unary_words_dict(self):
        for sentence in self.train_positive_set:
            sentence = get_words_array(sentence)
            words_in_sent = Counter(sentence)
            for word in words_in_sent.keys():
                if word in self.count_unary_train_pos_dict.keys():
                    self.count_unary_train_pos_dict[word] += 1
                else:
                    self.count_unary_train_pos_dict[word] = 1

        for sentence in self.train_negative_set:
            sentence = get_words_array(sentence)
            words_in_sent = Counter(sentence)
            for word in words_in_sent.keys():
                if word in self.count_unary_train_neg_dict.keys():
                    self.count_unary_train_neg_dict[word] += 1
                else:
                    self.count_unary_train_neg_dict[word] = 1

        self.calculate_number_words()  # to calculate numbers of all words

    # calculate number of all words in dictionary
    def calculate_number_words(self):
        sum_in_pos = 0
        for key, value in self.count_unary_train_pos_dict:
            sum_in_pos += value
        sum_in_neg = 0
        for key, value in self.count_unary_train_neg_dict:
            sum_in_neg += value

        self.number_words_in_pos = sum_in_pos
        self.number_words_in_neg = sum_in_neg

    # calculate p(w) = count(w)/M   (M: all words in dictionary)
    def calculate_unary_probability(self, word, dataset_mode):
        res = 0
        if dataset_mode == "positive":
            if word in self.count_unary_train_pos_dict.keys():
                res = self.count_unary_train_pos_dict[word] / self.number_words_in_pos

        elif dataset_mode == "negative":
            if word in self.count_unary_train_neg_dict.keys():
                res = self.count_unary_train_neg_dict[word] / self.number_words_in_neg

        return res

    # recognize sentence: is positive or negative
    def recognize_sentence(self, sentence):
        words_array = get_words_array()