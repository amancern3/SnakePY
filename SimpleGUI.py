import PySimpleGUI as sg

sg.theme("DarkAmber")

layout = [ [sg.Button('Game 1')], [sg.Text(size=(25,2))],
          [sg.Button('Game 2')], [sg.Text(size=(25,2))],
           [sg.Button('Game 3')], [sg.Text(size=(25, 2))], ]

#sg.Window.size(400,400)
window = sg.Window('Game Launcher', layout)

# Event Loop 
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    #print('You entered ', values[0])

    if (event == 'Game 1'):
        import snake
        snake.main()

window.close()
