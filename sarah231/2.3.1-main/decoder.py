
class decoder:
    def __init__(self) -> None:
        pass
    
    def decode_vowel(self,message):
        keys = ["a","e","i","o","u","y"]
        list_message = list(message)
        output_message = ""
        while len(list_message) > 0:
            current_letter = list_message.pop(0)
            if current_letter in keys:
                output_message += list_message.pop(0)
        print(output_message)
        return output_message
    def decode_any(self,encoded_message,keys):
        list_message = list(encoded_message)
        output_message = ""
        while len(list_message) > 0:
            current_letter = list_message.pop(0)
            if current_letter in keys:
                output_message += list_message.pop(0)
        print(output_message)
        return output_message