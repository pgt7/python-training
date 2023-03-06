
class Converter:
    def __init__(self, message):
        self.message = str(message)

    # convert message to dictionary
    def convert(self):

        # properties
        arr = list(self.message.split(" "))
        dic = {}

        # fill dictionary with array
        for item in arr:
            if(item in dic.keys()):
                dic[item] += 1
            else:
                dic[item] = 1

        # return the dictionary
        return dic