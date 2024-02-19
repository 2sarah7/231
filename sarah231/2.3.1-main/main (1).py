import encoder
import decoder

encoder_test = encoder.encoder()
decoder_test = decoder.decoder()

key = encoder_test.make_encryption()[0]

encoded_message = encoder_test.encoder("working")


decoder_test.decode_any(encoded_message,keys=key)

message = input("What message do you want to encode? ")
encdoded_msg = encoder_test.encoder_vowel(message)
decoder_test.decode_vowel(encdoded_msg)