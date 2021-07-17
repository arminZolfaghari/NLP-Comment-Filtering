from collections import Counter



def standardize_sentence(sentence):



class BigramModel():

    def __init__(self, train_pos_set, train_neg_set, lambda_arr, epsilon):
        self.train_positive_set = train_pos_set
        self.train_negative_set = train_neg_set
        self.lambda_arr = lambda_arr  # [h0, h1, h2] => weights for probability
        self.epsilon = epsilon
        self.count_unary_train_pos_dict = {}
        self.count_unary_train_neg_dict = {}
        self.count_binary_train_pos_dict = {}
        self.count_binary_train_neg_dict = {}
        self.number_words_in_neg = 0
        self.number_words_in_pos = 0

    def create_unary_words_dict(self):
        for sentence in self.train_positive_set:
            words_in_sent = Counter(sentence)
            for word in words_in_sent.keys():
                if word in self.count_unary_train_pos_dict.keys():
                    self.count_unary_train_pos_dict[word] += 1
                else:
                    self.count_unary_train_pos_dict[word] = 1

        for sentence in self.train_negative_set:
            words_in_sent = Counter(sentence)
            for word in words_in_sent.keys():
                if word in self.count_unary_train_neg_dict.keys():
                    self.count_unary_train_neg_dict[word] += 1
                else:
                    self.count_unary_train_neg_dict[word] = 1

        self.calculate_number_words()  # to calculate numbers of all words

    def create_binary_words_dict(self):
        for sentence in self.train_positive_set:
            words_in_sent = Counter(sentence)
            for word_i in range(len(words_in_sent.keys()) - 1):
                couple_word = (list(words_in_sent.keys())[word_i], list(words_in_sent.keys())[word_i + 1])
                if couple_word in self.count_binary_train_pos_dict.keys():
                    self.count_binary_train_pos_dict[couple_word] += 1
                else:
                    self.count_binary_train_pos_dict[couple_word] = 1

        for sentence in self.train_negative_set:
            words_in_sent = Counter(sentence)
            for word_i in range(len(words_in_sent.keys()) - 1):
                couple_word = (list(words_in_sent.keys())[word_i], list(words_in_sent.keys())[word_i + 1])
                if couple_word in self.count_binary_train_neg_dict.keys():
                    self.count_binary_train_neg_dict[couple_word] += 1
                else:
                    self.count_binary_train_neg_dict[couple_word] = 1


    # calculate p(wi|wi-1) = count(wi-1 wi)/count(wi-1) => p(word2|word1)
    def calculate_simple_conditional_probability(self, word1, word2, dataset_mode):
        if dataset_mode == "positive":
            tuple_words = (word1, word2)
            if word1 in self.count_unary_train_pos_dict and tuple_words in self.count_binary_train_pos_dict:
                res = self.count_binary_train_pos_dict[tuple_words] / self.count_unary_train_pos_dict[
                    word1]  # count(wi-1 wi)/count(wi-1)
            else:
                res = 0  # when word1 isn't in dict or 'word1 word2' isn't in dict
        elif dataset_mode == "negative":
            tuple_words = (word1, word2)
            if word1 in self.count_unary_train_neg_dict and tuple_words in self.count_binary_train_neg_dict:
                res = self.count_binary_train_neg_dict[tuple_words] / self.count_unary_train_neg_dict[
                    word1]  # count(wi-1 wi)/count(wi-1)
            else:
                res = 0  # when word1 isn't in dict or 'word1 word2' isn't in dict

        return res

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
        if dataset_mode == "positive":
            if word in self.count_unary_train_pos_dict:
                res = self.count_unary_train_pos_dict[word] / self.number_words_in_pos
            else:
                res = 0
        elif dataset_mode == "negative":
            if word in self.count_unary_train_neg_dict:
                res = self.count_unary_train_neg_dict[word] / self.number_words_in_neg
            else:
                res = 0

        return res

    # calculate p(wi|wi-1) = h2 * p(wi|wi-1) + h1 * p(wi) + h0 * e
    def calculate_conditional_probability(self, word1, word2, dataset_mode):
        [h0, h1, h2] = self.lambda_arr
        res = h2 * self.calculate_simple_conditional_probability(word1, word2, dataset_mode) + h1 * self.calculate_unary_probability(word2, dataset_mode) + h0 * self.epsilon
        return res

    def recognize_sentence(self, sentence):
        words_in_sentence =
        for i in range(len(sentence_arr)):

