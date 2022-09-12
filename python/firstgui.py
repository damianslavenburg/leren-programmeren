import PySimpleGUI as sg


layout = [
    [sg.Text("hello from PySimleGUi")],
    [sg.Button('ok')]
]  
window=sg.Window("demo", layout)

while True:
    event, values = window.read()
    if event == "ok" or event == sg.WIN_CLOSED:
        break
window.close()
