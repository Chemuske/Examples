import PySimpleGUI as sg
import convert
import deconvert

sg.theme('DarkAmber')

language = ["Ru","En"]
layout_encryption = [  
            [sg.Text('Select language', size=(15,)), sg.Combo(language,  size=(3, 10))],
            [sg.Text('Enter your message', size=(15,)), sg.InputText()],
            [sg.Text('Enter shift amount', size=(15,)), sg.InputText()],
            [sg.Text('Result ', size=(15,)), sg.InputText(key = '-output_encryption-')],
            [sg.Button('Convert'), sg.Button('Cancel')]]

layout_decryption = [  
            [sg.Text('Select language', size=(15,)), sg.Combo(language,  size=(3, 10))],
            [sg.Text('Enter your message', size=(15,)), sg.InputText()],
            [sg.Text('Enter shift amount', size=(15,)), sg.InputText()],
            [sg.Text('Result ', size=(15,)), sg.InputText(key = '-output_decryption-')],
            [sg.Button('Deconvert'), sg.Button('Cancel')]]

tabgrp = [  [sg.TabGroup([[
    sg.Tab('Encryption', layout_encryption),
    sg.Tab('Decryption', layout_decryption)]])]]

window = sg.Window('Caesar cipher', tabgrp)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Convert':
        text_elem = window['-output_encryption-']
        text_elem.update(convert.main(values[0], values[1], str(values[2])))
    if event == 'Deconvert':
        text_elem = window['-output_decryption-']
        text_elem.update(deconvert.main(values[3], values[4], str(values[5])))
window.close()