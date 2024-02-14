 
# Import customtkinter module
import customtkinter as ctk
import encoder
import decoder
 
# Sets the appearance mode of the application
# "System" sets the appearance same as that of the system
ctk.set_appearance_mode("System")        
 
# Sets the color of the widgets
# Supported themes: green, dark-blue, blue
ctk.set_default_color_theme("blue")    


# Create App class
class App(ctk.CTk):
# Layout of the GUI will be written in the init itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
# Sets the title of our window to "App"
        self.title("Encode/Decode")    
# Dimensions of the window will be 200x200
        self.geometry("600x400")    
        

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
                                         text="Encode")
        self.encodeButton.grid(row=0, column=4,
                                        columnspan=4,
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
                                         text="Encode")
        self.decodeButton.grid(row=2, column=4,
                                        columnspan=4,
                                        padx=20, pady=20,
                                        sticky="ew")

        # fghghg
        encdoded_msg = encoder_test.encoder_vowel("jaziristhebest")
        decoder_test.decode_vowel(encdoded_msg)
 
 
if __name__ == "__main__":
    app = App()
    # Runs the app
    app.mainloop()  
        