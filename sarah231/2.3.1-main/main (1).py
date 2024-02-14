import encoder
import decoder

encoder_test = encoder.encoder()
decoder_test = decoder.decoder()

key = encoder_test.make_encryption()[0]

encoded_message = encoder_test.encoder("working")


decoder_test.decode_any(encoded_message,keys=key)

encdoded_msg = encoder_test.encoder_vowel("jaziristhebest")
decoder_test.decode_vowel(encdoded_msg)