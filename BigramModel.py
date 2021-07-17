from collections import Counter


class BigramModel():


    def __init__(self, train_pos_set, train_neg_set, lambda_arr, epsilon):
        self.train_positive_set = train_pos_set
        self.train_negative_set = train_neg_set
        self.lambda_arr = lambda_arr        # [h0, h1, h2] => weights for probability
        self.epsilon = epsilon
        self.count_unary_train_pos_dict = {}
        self.count_unary_train_neg_dict = {}
        self.count_binary_train_pos_dict = {}
        self.count_binary_train_neg_dict = {}


    def create_pos_words_dict(self):
        for sentence in self.train_positive_set:
            words_in_sent = sentence.split(' ')
            words_in_sent.insert(0, '<s>')
            words_in_sent.append('</s>')
            words_in_sent = Counter(words_in_sent)
            for word in words_in_sent.keys():
                if word in self.train_pos_dict.keys():
                    self.train_pos_dict[word] += 1
                else:
                    self.train_pos_dict[word] = 1

    def create_neg_words_dict(self):
        for sentence in self.train_negative_set:
            words_in_sent = sentence.split(' ')
            words_in_sent.insert(0, '<s>')
            words_in_sent.append('</s>')
            words_in_sent = Counter(words_in_sent)
            for word in words_in_sent.keys():
                if word in self.train_neg_dict.keys():
                    self.train_neg_dict[word] += 1
                else:
                    self.train_neg_dict[word] = 1


    # calculate p(wi|wi-1) = count(wi-1 wi)/count(wi-1)
    def calculate_simple_conditional_probability(self, word1, word2):
        if word1

    # calculate p(wi|wi-1) = h2 * p(wi|wi-1) + h1 * p(wi) + h0 * e
    def calculate_conditional_probability(self, word1, word2):



    def recognize_sentence(self, sentence):
        sentence_arr = sentence.split(" ")
        for i in range(len(sentence_arr)):
            pass
