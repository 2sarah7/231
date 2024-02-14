import random

class encoder:
    def __init__(self):
        self.keys = ["a","e","i","o","u","y"]
        self.letter_fill = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z']

    def make_encryption(self):
        key_abcs = []
        abcs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z']
        for _ in range(6):            
            letter = random.randint(0,(len(abcs) - 1))
            key_abcs.append(abcs[letter])
            abcs.remove(abcs[letter])
        self.keys = key_abcs
        self.letter_fill = abcs
        print("key: ", key_abcs)
        print("abcs: ", abcs)
        return key_abcs,abcs

    def encoder(self,message,letter_range = 4):
        encoded_message = ""
        list_message = list(message)
        random_letter = lambda x : random.randint(0,(len(x) - 1))
        while len(list_message) > 0:
            amount_letters_between = random.randint(0,letter_range)
            for i in range(amount_letters_between):
                encoded_message += self.letter_fill[random_letter(self.letter_fill)]
            encoded_message += self.keys[random_letter(self.keys)]
            encoded_message += list_message.pop(0)
        print(encoded_message)
        return encoded_message
    
    def encoder_vowel(self,message,letter_range = 4):
        keys = ["a","e","i","o","u","y"]
        abcs = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
        encoded_message = ""
        list_message = list(message)
        
        while len(list_message) > 0:
            amount_letters_between = random.randint(0,letter_range)
            for i in range(amount_letters_between):
                random_letter = lambda x : random.randint(0,(len(x) - 1))
                encoded_message += abcs[random_letter(abcs)]
            encoded_message += keys[random_letter(keys)]
            encoded_message += list_message.pop(0)
        print(encoded_message)
        return encoded_message

            

