



class BigramModel():

    def __init__(self, train_pos_set, train_neg_set, lambda_arr):
        self.train_positive_set = train_pos_set
        self.train_negative_set = train_neg_set
        self.lambda_arr = lambda_arr    # [h0, h1, h2]


    def recognize_sentence(self, sentence):
        sentence_arr = sentence.split(" ")
        for i in range(len(sentence_arr)):


