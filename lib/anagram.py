# your code goes here!
class Anagram():
    def __init__(self,word):
        self.word = word
    
    def match(self,match_list):

        my_word_list = [letter for letter in self.word]
        return_list = []

        for i in range(0,len(match_list)):
            letter_list = [letter for letter in match_list[i]]
            if sorted(my_word_list) == sorted(letter_list):
                return_list.append(match_list[i])
        
        return return_list
            
