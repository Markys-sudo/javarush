#from preloaded import MORSE_CODE
MORSE_CODE = {'.-': 'A',
 '-...': 'B',
 '-.-.': 'C',
 '-..': 'D',
 '.': 'E',
 '..-.': 'F',
 '--.': 'G',
 '....': 'H',
 '..': 'I',
 '.---': 'J',
 '-.-': 'K',
 '.-..': 'L',
 '--': 'M',
 '-.': 'N',
 '---': 'O',
 '.--.': 'P',
 '--.-': 'Q',
 '.-.': 'R',
 '...': 'S',
 '-': 'T',
 '..-': 'U',
 '...-': 'V',
 '.--': 'W',
 '-..-': 'X',
 '-.--': 'Y',
 '--..': 'Z',
 '-----': '0',
 '.----': '1',
 '..---': '2',
 '...--': '3',
 '....-': '4',
 '.....': '5',
 '-....': '6',
 '--...': '7',
 '---..': '8',
 '----.': '9',
 '.-.-.-': '.',
 '--..--': ',',
 '..--..': '?',
 '.----.': "'",
 '-.-.--': '!',
 '-..-.': '/',
 '-.--.': '(',
 '-.--.-': ')',
 '.-...': '&',
 '---...': ':',
 '-.-.-.': ';',
 '-...-': '=',
 '.-.-.': '+',
 '-....-': '-',
 '..--.-': '_',
 '.-..-.': '"',
 '...-..-': '$',
 '.--.-.': '@',
 '...---...': 'SOS'}
#decode_morse = ('.... . -.--   .--- ..- -.. .') #should return "HEY JUDE"
def decode_morse(morse_code):
    # Remember - you can use the preloaded MORSE_CODE dictionary:
    # For example:
    # MORSE_CODE['.-'] = 'A'
    # MORSE_CODE['--...'] = '7'
    # MORSE_CODE['...-..-'] = '$'
    new = []
    morse_code = morse_code.upper()
    for value in morse_code:
        for k, v in MORSE_CODE.items():
            if value == v:
                new.append(k)
        if value == " ":
            new.append(' ')
    news = ' '.join(new)
    return print(news)
decode_morse('E E')