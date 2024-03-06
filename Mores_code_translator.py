from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

app = QApplication([])
window = QWidget()
window.resize(500,250)

pressed_count = 0;

#patterns for comparison
morse_patterns = {
    'a': '.-', 
    'b': '-...', 
    'c': '-.-.', 
    'd': '-..', 
    'e': '.', 
    'f': '..-.', 
    'g': '--.', 
    'h': '....', 
    'i': '..', 
    'j': '.---', 
    'k': '-.-', 
    'l': '.-..', 
    'm': '--', 
    'n': '-.', 
    'o': '---', 
    'p': '.--.', 
    'q': '--.-', 
    'r': '.-.', 
    's': '...', 
    't': '-', 
    'u': '..-', 
    'v': '...-', 
    'w': '.--', 
    'x': '-..-', 
    'y': '-.--', 
    'z': '--..',
    '1': '.----', 
    '2': '..---', 
    '3': '...--', 
    '4': '....-', 
    '5': '.....', 
    '6': '-....', 
    '7': '--...', 
    '8': '---..', 
    '9': '----.', 
    '0': '-----',
}


reverse_text_patterns = {
    '.-': 'a', 
    '-...': 'b', 
    '-.-.': 'c', 
    '-..': 'd', 
    '.': 'e', 
    '..-.': 'f', 
    '--.': 'g', 
    '....': 'h', 
    '..': 'i', 
    '.---': 'j', 
    '-.-': 'k', 
    '.-..': 'l', 
    '--': 'm', 
    '-.': 'n', 
    '---': 'o', 
    '.--.': 'p', 
    '--.-': 'q', 
    '.-.': 'r', 
    '...': 's', 
    '-': 't', 
    '..-': 'u', 
    '...-': 'v', 
    '.--': 'w', 
    '-..-': 'x', 
    '-.--': 'y', 
    '--..': 'z',
    '.----': '1', 
    '..---': '2', 
    '...--': '3', 
    '....-': '4', 
    '.....': '5', 
    '-....': '6', 
    '--...': '7', 
    '---..': '8', 
    '----.': '9', 
    '-----': '0',
}

#layout and required widgets 

text = []
morse_code = []
text_box = QLineEdit()
clear_button = QPushButton("Clear")
translate_morse_button = QPushButton("translate morse")
translate_text_button = QPushButton("translate text")
morse_label = QLabel("Morse")
text_label = QLabel("Text")
morse_code_box = QLineEdit()
main_layout = QHBoxLayout()
col_1 = QVBoxLayout()
col_2 = QVBoxLayout()
row_1 = QHBoxLayout()
row_2 = QHBoxLayout()
row_3 = QHBoxLayout()

col_1.addWidget(text_label)
col_1.addWidget(text_box)
row_2.addWidget(clear_button)
col_1.addWidget(morse_label)
col_1.addWidget(morse_code_box)
col_1.addLayout(row_1)
col_1.addLayout(row_2)
row_2.addWidget(translate_morse_button)
row_2.addWidget(translate_text_button)


# in-app functions
def form_text_to_morse():
    #get text from text_box
    text_box_text = text_box.text()

    #breakdown characters and append in a list and compare
    for character in text_box_text:
        if character.lower() in morse_patterns:
            morse_code.append(morse_patterns[character.lower()])

    result = ' '.join(morse_code)
    morse_code_box.setText(result)
    pressed_count = 1
    if pressed_count == 1:
        translate_morse_button.hide()
        translate_text_button.hide()

def form_morse_to_text():
    mores_code_text = morse_code_box.text()

    for character in mores_code_text:
        if character.lower() in reverse_text_patterns:
            text.append(reverse_text_patterns[character.lower()])

    result = ' '.join(text)
    text_box.setText(result)
    pressed_count = 1
    if pressed_count == 1:
        translate_morse_button.hide()
        translate_text_button.hide()


#clear text in boxes afer finished the comparision

def clear_pressed():
    morse_code_box.clear()
    text_box.clear()
    text.clear()
    morse_code.clear()
    translate_morse_button.show()
    translate_text_button.show()

main_layout.addLayout(col_1)
main_layout.addLayout(col_2)

window.setLayout(main_layout)


#main widget and funciton connection 
clear_button.clicked.connect(clear_pressed)

translate_morse_button.clicked.connect(form_text_to_morse)
translate_text_button.clicked.connect(form_morse_to_text)
window.show()
app.exec()

