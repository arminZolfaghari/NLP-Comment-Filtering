
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

