import tkinter as tk
from tkinter.constants import COMMAND, WORD
from playsound import playsound
import time
import pyttsx3 as pyttsx
import sys


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = tk.Frame(root)
    frm_main.master.title("Morse Decoder")
    frm_main.pack()

    

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    morse_main_frame(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()

def morse_main_frame(frm_main):
    
    # Print Welcome message

    wlcme_msg = tk.Label(frm_main, text="Welcome to Morse Decoder", font="times 20 bold", fg="#007ACC")
    wlcme_msg.grid(row=0, column=0, pady=20, padx=20)

    # Middle Message
    middle_msg = tk.Label(frm_main, text="Enter your message", font="times 15")
    middle_msg.grid(row=1, column=0, pady=20)
    
    #Message Input

    msge_code = tk.Text(frm_main, bg="white", height=3, width=50, wrap=WORD, font="times 15")
    msge_code.grid(row=2, column=0, pady=20, padx=20)
    msge_code.focus()

    ########  Create a buttons that displays "Encode and decode"  ###################

    #Encode
    encode_btn = tk.Button(frm_main, text="Encode", font="times 16", fg="#008080", command=lambda: encode_morse(msge_code.get('1.0', "end-1c"), morse_code_dict()))
    encode_btn.grid(row=3, column=0, pady=20, padx=100, sticky="w")
    
    #Decode
    decode_btn = tk.Button(frm_main, text="Decode", font="times 16", fg="#008080", command=lambda: decode_morse(msge_code.get("1.0", "end-1c"), morse_code_dict()))
    decode_btn.grid(row=3, column=0, pady=20, padx=100, sticky="e")
    
    #######  Bottom message ###########

    dcode_message = tk.Label(frm_main, text="Your message is", font="times 15")
    dcode_message.grid(row=4, column=0, pady=20)

    ########## ALERT ###################

    alert_lbl = tk.Label(frm_main, anchor="w", fg="#FF0000", font="times 17")
    alert_lbl.grid(row=5, column=0, pady=10)

    #########  Decode Output  ##############

    dcode_box = tk.Text(frm_main, bg="white", height=3, width=50, wrap=WORD, font="times 15")
    dcode_box.grid(row=6, column=0, pady=20, padx=30)

    ##########  Clear button  #############

    clear_btn = tk.Button(frm_main, text="Clear", font="times 16", fg="#008080", command=lambda: clear)
    clear_btn.grid(row=7,column=0, pady=20, padx=100, sticky="w")
    

    #########  Quit button  ##############

    quit_btn = tk.Button(frm_main, text="Quit", font="times 16", fg="#FF2424", command=quit_function)
    quit_btn.grid(row=7, column=0, pady=20, padx=100, sticky="e")

    tk.Label(frm_main, text="Created by acrisvall  -   Version 1.0", fg="#CE00CE").grid(row=8, column=0, pady=20)


    def morse_code_dict():

        morse_dict = {  "A" : ".-", 
                        "B" : "-...", 
                        "C" : "-.-.", 
                        "D" : "-..", 
                        "E" : ".", 
                        "F" : "..-.", 
                        "G" : "--.", 
                        "H" : "....", 
                        "I" : "..", 
                        "J" : ".---", 
                        "K" : "-.-", 
                        "L" : ".-..", 
                        "M" : "--", 
                        "N" : "-.",
                        "Ñ" : "––.––",
                        "O" : "---", 
                        "P" : ".--.", 
                        "Q" : "--.-", 
                        "R" : ".-.", 
                        "S" : "...", 
                        "T" : "-", 
                        "U" : "..-", 
                        "V" : "...-", 
                        "W" : ".--", 
                        "X" : "-..-", 
                        "Y" : "-.--", 
                        "Z" : "--..", 
                        "0" : "-----", 
                        "1" : ".----", 
                        "2" : "..---", 
                        "3" : "...--", 
                        "4" : "....-", 
                        "5" : ".....", 
                        "6" : "-....", 
                        "7" : "--...", 
                        "8" : "---..", 
                        "9" : "----.",
                        "," :"--..--",
                        ":": "---...",
                        "." :".-.-.-",
                        "!" :"-.-.--",
                        "'": ".----.",
                        "?" :"..--..",
                        "/" :"-..-.",
                        "-" :"-....-",
                        "(" :"-.--.",
                        ")" :"-.--.-",
                        '@': ".--.-.",
                        "=": "-...-",
                        "+": ".-.-.",
                        '"': ".-..-.",
                        '&': ".-...",
                        " " : ""          # This is to ignore spaces
                        }
        
        return morse_dict

    def encode_morse(text, morse_dict):

        try:
            
            encode = ""

            #Iterates through the text, and obtain each letter of the text

            for letter in text:

                letter = letter.upper()

                if letter != " ":

                    encode += morse_dict[letter] + " "

                else:

                    encode += " "
                    alert_lbl.config(text="Please enter a message")
                    alert_lbl.after(2000, lambda : alert_lbl.config(text=''))

            # Iterates through every symbol and reproduces the sound of it
            for i in encode:
                
                if i == ".":
                    playsound("dit.wav")
                
                elif i == "-":
                    playsound("dah.wav")
            
            # is there is space, the sound is mute for 0.5 seconds
                else: 
                    time.sleep(0.2)
            
            return dcode_box.insert(0.0, encode)

        except ValueError:

            alert_lbl.config(text="Please enter a valid message")
            alert_lbl.after(3000, lambda : alert_lbl.config(text=''))

        except KeyError as key_err:

            alert_lbl.config(text=f"{key_err} is not valid")
            alert_lbl.after(3000, lambda : alert_lbl.config(text=''))

    def decode_morse(code, morse_dict):

        try:


            key_list = list(morse_dict.keys())
            val_list = list(morse_dict.values())

            morse = ""
            normal_text = ""
            code += " "

            for letters in code:
                
                if letters != " ":
                    morse += letters
                    space_found = 0
                
                else:
                    space_found += 1
                    
                    if space_found == 2:
                        
                        normal_text += " "
                        
                    else:
                        normal_text = normal_text + key_list[val_list.index(morse)]

                        morse = ""
            
            dcode_box.insert(0.0, normal_text)


            #This reproduce the text to voice
            engine = pyttsx.init()
            engine.say(normal_text)
            engine.runAndWait()
            
            return ""
    
        except UnboundLocalError:
            alert_lbl.config(text="Please insert morse code")
            alert_lbl.after(2000, lambda : alert_lbl.config(text=''))
            
        except ValueError:
            alert_lbl.config(text="Please insert morse code")
            alert_lbl.after(2000, lambda : alert_lbl.config(text=''))

    def clear():

        msge_code.delete(1.0, tk.END)
        dcode_box.delete(1.0, tk.END)

    clear_btn.config(command=clear)

def quit_function():
    sys.exit(0)



if __name__ == "__main__":
    main()
