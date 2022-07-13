from datetime import datetime as dt
import PySimpleGUI as sg

def dailyRoutine():
  def Time(time, info):
    return [sg.CBox('',s=2), sg.Text(time,s=10), sg.Text(info,s=20), sg.In()]
    
  
  tasks = [
    ['04:00', 'COFFEE/CARDIO'],
    ['05:00', 'BREAKFAST/GYM'],
    ['06:00', 'AM ROUTINE'],
    ['07:00', 'GO TO WORK'],
    ['16:00', 'PICK UP HOUSE'],
    ['17:00', 'STUDY DS&A'],
    ['18:00', 'PROBLEM SET'],
    ['19:00', 'PREP DINNER']
  ]

  layout = [
    [[sg.Text('',s=2),sg.Text('TIME',s=10,justification='center'),sg.Text('TASK',s=20,justification='center'),sg.Text('NOTE',s=50,justification='center')]],
    [Time(x, y) for x, y in tasks],
    [[sg.Button('Save',pad=10,border_width=5,tooltip='Saves a file with task notes'), sg.Button('Exit',pad=10,border_width=5,tooltip='Exits the Scheduler')]]
  ]


  window = sg.Window('Daily Routine', layout)

  event, values = window.read()
  

if __name__ == '__main__':
  dailyRoutine()
