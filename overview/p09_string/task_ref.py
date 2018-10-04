
# Given a sentence, reverse each word of the sentence individually.


def reverse_sentence(sentence):

    words = sentence.split()

    return " ".join([word[::-1] for word in words])

    # or:
    # res = ""
    # for word in sentence.split():
    #     res += word[::-1]
    #
    # return res


print(reverse_sentence("python from zero to hero"))
