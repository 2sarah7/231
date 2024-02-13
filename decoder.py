import tkinter as tk

codedMessage = ""
decodedMessage = ""

root = tk.Tk()
root.title("Decoder")
root.geometry("400x400")
frame = tk.Frame(root)

def decode():
    global codedMessage, decodedMessage
    codedMessage = entryBox.get()
    codedMessage = codedMessage.upper()
    print(codedMessage)
    for i in range(1, len(codedMessage)):
        if codedMessage[i] in vowels:
            i += 1
            decodedMessage = decodedMessage + codedMessage[i]
    label2.config(text=decodedMessage)



label = tk.Label(text="Enter the coded message: ")
label.pack()
# Where you put in the coded message:
entryBox = tk.Entry(root, width=30)
entryBox.pack()
# Button to press that decodes it, label below will show the decoded message
button = tk.Button(root, text="Decode", command=decode)
button.pack()
label2 = tk.Label(text="HI")
label2.pack()



vowels = ["A", "E", "I", "O", "U", "Y"]


root.mainloop()