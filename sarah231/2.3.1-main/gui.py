 
# Import customtkinter module
# import customtkinter as ctk
import os
import encoder
import decoder
 
try:
  import customtkinter as ctk
except:
  os.system("pip install customtkinter")
  import customtkinter as ctk
  
# Sets the appearance mode of the application
# "System" sets the appearance same as that of the system
ctk.set_appearance_mode("System")        
 
# Sets the color of the widgets
# Supported themes: green, dark-blue, blue
ctk.set_default_color_theme("blue")    

encoder_test = encoder.encoder()
decoder_test = decoder.decoder()

# fghghg
# encdoded_msg = encoder_test.encoder_vowel("jaziristhebest")
# decoder_test.decode_vowel(encdoded_msg)

# Create App class
class App(ctk.CTk):
# Layout of the GUI will be written in the init itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
# Sets the title of our window to "App"
        self.title("Encode/Decode")    
# Dimensions of the window will be 200x200
        self.geometry("800x400")    
        

        self.encodeLabel = ctk.CTkLabel(self,
                                      text="Message to be encrypted: ")
        
        
        self.encodeLabel.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")

        self.encodeEntry = ctk.CTkEntry(self,
                         placeholder_text="Message")
        self.encodeEntry.grid(row=0, column=1,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")

        self.encodeButton = ctk.CTkButton(self,
                                         text="Encode", command=self.encrypt_message)
        self.encodeButton.grid(row=0, column=4,
                                        columnspan=4,
                                        padx=20, pady=20,
                                        sticky="ew")
        self.encodeMessage = ctk.CTkLabel(self,
                                      text="Message")
        self.encodeMessage.grid(row=0, column=8,
                            padx=20, pady=20,
                            sticky="ew")



        self.decodeLabel = ctk.CTkLabel(self,
                                      text="Message to be decrypted: ")
        self.decodeLabel.grid(row=2, column=0,
                            padx=20, pady=20,
                            sticky="ew")

        self.decodeEntry = ctk.CTkEntry(self,
                         placeholder_text="Message")
        self.decodeEntry.grid(row=2, column=1,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")

        self.decodeButton = ctk.CTkButton(self,
                                         text="Decode", command=self.decrypt_message)
        self.decodeButton.grid(row=2, column=4,
                                        columnspan=4,
                                        padx=20, pady=20,
                                        sticky="ew")
        self.decodeMessage = ctk.CTkLabel(self,
                                      text="Message")
        self.decodeMessage.grid(row=2, column=8,
                            padx=20, pady=20,
                            sticky="ew")
    def encrypt_message(self):
            msg = self.encodeEntry.get()
            encrypted_msg = encoder_test.encoder_vowel(msg.lower())
            self.encodeMessage.configure(text=encrypted_msg)
            print("Encrypted message:", encrypted_msg)
            
    def decrypt_message(self):
            msg = self.decodeEntry.get()
            decrypted_msg = decoder_test.decode_vowel(msg)
            print("Decrypted message: ", decrypted_msg)
            self.decodeMessage.configure(text=decrypted_msg)
            
            
 
 
if __name__ == "__main__":
    app = App()
    # Runs the app
    app.mainloop()  
        