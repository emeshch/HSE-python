class TokenManipulator:
    '''
    all the manipulations are carried out here
    '''

    def __init__(self, text):
        self.text = text
        self.tokens = input_text.split()       # preliminary tokenizing
        self.new_tokens = []                   # result will be stored here
        self.list_of_tokens = []               # result in tuples, just for fun

    def find_tokens(self):
        '''
        actually the main method
        '''
        for token in self.tokens:
            # token = token.replace('\ufeff', '')
            self.cut_token(token, self.text, pos)

    def cut_token(self, word, text, pos):
        '''
        extracts the nonletter characters from the tokens,
        cuts the tokens
        '''

        if word.isalpha():
            pos = self.locate(word, self.text, pos)
        else:
            for element in word:
                if not element.isalpha():
                #     pass  # print(word, element)
                # else:
                    # print("hoho! word ", word, "\t element ", element)
                    token1 = word[:word.find(element)]
                    pos = self.locate(token1, self.text, pos)

                    token2 = element
                    pos = self.locate(token2, self.text, pos)

                    token3 = word[word.find(element)+1:]
                    # print('we got', ' ', token1, ' ', token2, ' ', token3)
                    self.cut_token(token3, text, pos)
                    break

    def locate(self, word, text, p=0):
        '''
        finds the position of the token in the input text,
        puts the tokens into the list which will later be shown as a result,
        returns the token position so we could go through the text
         and compute the right positions for the tokens that look exactly the same
        '''
        pos = text.find(word, p)
        self.list_of_tokens.append((pos, word))
        self.new_tokens.append(str(pos) + ' ' + word)
        pos += len(word)
        return pos


input_text = open("textfile.txt", encoding="utf-8").read()
# input_text = "привет, какое-ниб^удь слово, слово здравствуй!"
pos = 0
t = TokenManipulator(input_text)
t.find_tokens()


# for item in new_tokens:
#     item.strip("()\"'\,.?!")
# for item in new_tokens:
#     text.find(item)

print("\n".join(t.new_tokens))
# print("and now as tuples")
# print(t.list_of_tokens)

