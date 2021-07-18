from collections import Counter


# insert <s> to first and append </s> to end array, return words array
def get_words_array(sentence):
    words_in_sent = sentence.split(' ')
    words_in_sent.insert(0, '<s>')
    words_in_sent.append('</s>')

    return words_in_sent


class BigramModel():

    def __init__(self, train_pos_set, train_neg_set, lambda_arr, epsilon, cut_down, cut_above):
        self.train_positive_set = train_pos_set
        self.train_negative_set = train_neg_set
        self.lambda_arr = lambda_arr  # [h0, h1, h2] => weights for probability
        self.epsilon = epsilon
        self.count_unary_train_pos_dict = {}
        self.count_unary_train_neg_dict = {}
        self.count_binary_train_pos_dict = {}
        self.count_binary_train_neg_dict = {}
        # self.number_words_in_neg = 0
        # self.number_words_in_pos = 0
        self.cut_down = cut_down
        self.cut_above = cut_above

    # cut from down
    def do_alpha_cut(self):
        for word in list(self.count_unary_train_pos_dict):
            if self.count_unary_train_pos_dict[word] <= self.cut_down:
                del self.count_unary_train_pos_dict[word]

        for word in list(self.count_unary_train_neg_dict):
            if self.count_unary_train_neg_dict[word] <= self.cut_down:
                del self.count_unary_train_neg_dict[word]

    # cut from above
    def remove_from_above(self):
        self.count_unary_train_pos_dict = sorted(self.count_unary_train_pos_dict.items(), key=lambda x: x[1],
                                                 reverse=True)
        self.count_unary_train_neg_dict = sorted(self.count_unary_train_neg_dict.items(), key=lambda x: x[1],
                                                 reverse=True)

        self.count_unary_train_pos_dict = dict(self.count_unary_train_pos_dict)
        self.count_unary_train_neg_dict = dict(self.count_unary_train_neg_dict)

        for i in range(self.cut_above):
            print(i)
            print(list(self.count_unary_train_pos_dict)[0])
            self.count_unary_train_pos_dict.pop(list(self.count_unary_train_pos_dict)[0])
            # print('test: ', self.count_unary_train_pos_dict[list(self.count_unary_train_pos_dict)[int(i)]])

            # del self.count_unary_train_pos_dict[list(self.count_unary_train_pos_dict)[i]]
            # del self.count_unary_train_neg_dict[list(self.count_unary_train_neg_dict)[i]]

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

        # self.do_alpha_cut()
        # self.remove_from_above()
        self.calculate_number_words()  # to calculate numbers of all words

    def create_binary_words_dict(self):
        for sentence in self.train_positive_set:
            sentence = get_words_array(sentence)
            words_in_sent = Counter(sentence)
            for word_i in range(len(words_in_sent.keys()) - 1):
                couple_word = (list(words_in_sent.keys())[word_i], list(words_in_sent.keys())[word_i + 1])
                if couple_word in self.count_binary_train_pos_dict.keys():
                    self.count_binary_train_pos_dict[couple_word] += 1
                else:
                    self.count_binary_train_pos_dict[couple_word] = 1

        for sentence in self.train_negative_set:
            sentence = get_words_array(sentence)
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
        for value in self.count_unary_train_pos_dict.values():
            sum_in_pos += value
        sum_in_neg = 0
        for value in self.count_unary_train_neg_dict.values():
            sum_in_neg += value

        self.number_words_in_pos = sum_in_pos
        self.number_words_in_neg = sum_in_neg
        # print(self.number_words_in_neg)
        # print(self.number_words_in_pos)

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
        res = h2 * self.calculate_simple_conditional_probability(word1, word2,
                                                                 dataset_mode) + h1 * self.calculate_unary_probability(
            word2, dataset_mode) + h0 * self.epsilon

        print(res)
        return res

    def calculate_sentence_probability(self, sentence, dataset_mode):
        words_array = get_words_array(sentence)
        PI = self.calculate_unary_probability(words_array[0], dataset_mode)
        for i in range(1, len(words_array)):
            print(self.calculate_conditional_probability(words_array[i - 1], words_array[i], dataset_mode))
            PI *= self.calculate_conditional_probability(words_array[i - 1], words_array[i], dataset_mode)

        return PI

    # start learning and create unary and binary words dictionary
    def learning(self):

        self.create_unary_words_dict()
        self.create_binary_words_dict()

    # recognize sentence is positive or negative
    def recognize_sentence(self, sentence):

        # calculate sentence probability to recognize better probability
        prob_given_sentence_is_negative = self.calculate_sentence_probability(sentence, "negative")
        prob_given_sentence_is_positive = self.calculate_sentence_probability(sentence, "positive")
        if prob_given_sentence_is_positive > prob_given_sentence_is_negative:
            return "positive"
        elif prob_given_sentence_is_positive < prob_given_sentence_is_negative:
            return "negative"
        else:
            return "equal"
