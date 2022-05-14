#import libraries
import PySimpleGUI as gui
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile

#define root variable
root = Tk()
root.withdraw()

#Encryption function takes in two parameters text and shift
def encrypt(text,shift):
    global encrypted_text
    #empty string to make encrypted text
    encrypted_text = ""
    #for loop the text and for each letter we will get the ASCII code and add the shift to get the new ASCII code ord number
    for i in text:
        cipher_text = (ord(i) + shift)
        #if the ASCII number is within 32-126 then we convert to its corresponding character from the ASCII table and add it to the encrypted empty string
        if cipher_text in range(32,127):
            encrypted_text += chr(cipher_text)
        #if after shift the ASCII number is > 126 or < 32 then take the modulo of 95
        elif cipher_text > 126 or cipher_text < 32:
            cipher_text = (cipher_text % 95)
            #if after the modulo it is greater than 126 then substract 95
            if cipher_text > 126:
                encrypted_text += chr(cipher_text - 95)
            #if after the modulo it is less than 32 then add 95
            elif cipher_text < 32:
                encrypted_text += chr(cipher_text + 95)
            #Else just add it to the encrypted text empty string
            else:
                encrypted_text += chr(cipher_text)
                                  
    #returns encrypted text
    return ("Your encrypted message is: " + encrypted_text)

#Function to use brute force decryption 
def brute_force_decrypt(cipher):
    for key in range(95):
        print("Using keys: " + str(key) + " or " + str(key-95))
        print(encrypt(cipher,key))
        meaningful = input("Is this meaningful text? (Y/N): ")
        meaningful = meaningful.lower()
        if meaningful[0] == "y":
            print("Your text is now deciphered!")
            break


#Opens dialog box to choose a file for encryption and reads the file and returns it as a string
def user_select_file():
    file_path = filedialog.askopenfilename()
    f = open(file_path, "r")
    f = f.read()
    #Replaces \n new lines with a empty string to eliminate new lines making encoding stronger
    f = f.replace("\n", "")
    return f

#Opens dialog box to save the ciphered text to a .txt file in a user selected location
def save_ciphered_text(cipherfile):
    f2 = asksaveasfile(mode='w', defaultextension=".txt")
    f2.write(cipherfile)
    f2.close()
    print("Cipher is saved!")

#Window for decryption
def decrypt_window():
    global file_text
    global window3
    #GUI layout
    decrypt_layout = [[gui.Text("Type message to decrypt:"), gui.InputText()],
                      [gui.Text("OR")],
                      [gui.Text("Choose a text file to decrypt:"), gui.Button("Browse")],
                      [gui.Text("-----------------------------------------------------------------")],
                      [gui.Text("Refer to Python IDE command prompt to check for meaningful text.")],
                      [gui.Submit(), gui.Cancel()]]
    window3 = gui.Window("Decryption", decrypt_layout)
    while True:
        event, values = window3.read()
        if event == None or event == "Cancel":
            break
        elif event == "Submit":
            cipher_text1 = str(values[0])
            brute_force_decrypt(cipher_text1)
            window3.close()
            
        elif event == "Browse":
            cipher_text1 = user_select_file()
            brute_force_decrypt(cipher_text1)
            window3.close()
            

#Window for encryption on GUI
def encrpyt_window():
    global file_text
    #Layout for encrypt GUI
    encrypt_layout = [[gui.Text("First, enter a shifting key:"), gui.InputText()],
                       [gui.Text("------------------------------------------------------------------------")],
                       [gui.Text("Type message to encrypt:"), gui.InputText()],
                       [gui.Text("OR")],
                       [gui.Text("Choose a text file to encrypt:"), gui.Button("Browse")],
                       [gui.Submit(), gui.Cancel()]]
                       
    window2 = gui.Window("Encryption", encrypt_layout)
    while True:
        event, values = window2.read()
        if event == None or event == "Cancel":
            break
        elif event == "Submit":
            readable_text = str(values[1])
            shift_key = int(values[0])
            print(encrypt(readable_text, shift_key))
            save_ciphered_text(encrypted_text)
            window2.close()
            
        elif event == "Browse":
            file_text = user_select_file()
            shift_key = int(values[0])
            print(encrypt(file_text, shift_key))
            save_ciphered_text(encrypted_text)
            window2.close()
            


#First window layout to choose between encrypting or decrypting
layout = [[gui.Text("Would you like to:")],
          [gui.Button("Encrypt")],
          [gui.Text("OR")],
          [gui.Button("Decrypt")],
          [gui.Text("---------")]]

window = gui.Window("Caesar's Cipher", layout)

#User has to choose to either encrypt or decrypt
while True:
    event, values = window.read()
    if event == gui.WINDOW_CLOSED:
        break
    elif event == "Decrypt":
        window.close()
        decrypt_window()
        break
    elif event == "Encrypt":
        window.close()
        encrpyt_window()
        break