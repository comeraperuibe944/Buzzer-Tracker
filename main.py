import os, sys, io
import M5
from M5 import *
from hardware import *
import time



label0 = None
labelSettings = None
label1 = None
label2 = None
label3 = None
label4 = None
label5 = None
label6 = None
label7 = None
label8 = None
label9 = None
label10 = None
label11 = None
label12 = None
label13 = None
label14 = None
label15 = None


varBtnACounter = None
varCursor = None
listChart = None
varTrueCounter = None
i = None
varPagina = None
mapNotesNames = None
constSpaces = None

def upRange(start, stop, step):
  while start <= stop:
    yield start
    start += abs(step)

def downRange(start, stop, step):
  while start >= stop:
    yield start
    start -= abs(step)

# Changing musical notes with A button
def SettingsChangeNote():
  global varBtnACounter, varCursor, listChart, varTrueCounter, i, varPagina, mapNotesNames, constSpaces, label0, labelSettings, label1, label2, label3, label4, label5, label6, label7, label8, label9, label10, label11, label12, label13, label14, label15
  if varBtnACounter==1:
    listChart[int(varTrueCounter - 1)] = 'C7'
  elif varBtnACounter==2:
    listChart[int(varTrueCounter - 1)] = 'D7'
  elif varBtnACounter==3:
    listChart[int(varTrueCounter - 1)] = 'E7'
  elif varBtnACounter==4:
    listChart[int(varTrueCounter - 1)] = 'F7'
  elif varBtnACounter==5:
    listChart[int(varTrueCounter - 1)] = 'G7'
  elif varBtnACounter==6:
    listChart[int(varTrueCounter - 1)] = 'A7'
  elif varBtnACounter==7:
    listChart[int(varTrueCounter - 1)] = 'B7'
  elif varBtnACounter==8:
    listChart[int(varTrueCounter - 1)] = 'C8'
  else:
    listChart[int(varTrueCounter - 1)] = ' '

# Update screen labels
def RefreshAllLabelsText():
  global varBtnACounter, varCursor, listChart, varTrueCounter, i, varPagina, mapNotesNames, constSpaces, label0, labelSettings, label1, label2, label3, label4, label5, label6, label7, label8, label9, label10, label11, label12, label13, label14, label15
  label2.setText(str((str(((str(((str((varPagina / 10))).replace('.', ''))) + str(constSpaces)))) + str((listChart[int((varPagina + 0) - 1)])))))
  label3.setText(str((str(((str(((str(((varPagina + 1) / 10))).replace('.', ''))) + str(constSpaces)))) + str((listChart[int((varPagina + 1) - 1)])))))
  label4.setText(str((str(((str(((str(((varPagina + 2) / 10))).replace('.', ''))) + str(constSpaces)))) + str((listChart[int((varPagina + 2) - 1)])))))
  label5.setText(str((str(((str(((str(((varPagina + 3) / 10))).replace('.', ''))) + str(constSpaces)))) + str((listChart[int((varPagina + 3) - 1)])))))
  label6.setText(str((str(((str(((str(((varPagina + 4) / 10))).replace('.', ''))) + str(constSpaces)))) + str((listChart[int((varPagina + 4) - 1)])))))
  label7.setText(str((str(((str(((str(((varPagina + 5) / 10))).replace('.', ''))) + str(constSpaces)))) + str((listChart[int((varPagina + 5) - 1)])))))
  label8.setText(str((str(((str(((str(((varPagina + 6) / 10))).replace('.', ''))) + str(constSpaces)))) + str((listChart[int((varPagina + 6) - 1)])))))
  label9.setText(str((str(((str(((str(((varPagina + 7) / 10))).replace('.', ''))) + str(constSpaces)))) + str((listChart[int((varPagina + 7) - 1)])))))
  label10.setText(str((str(((str(((str(((varPagina + 8) / 10))).replace('.', ''))) + str(constSpaces)))) + str((listChart[int((varPagina + 8) - 1)])))))
  label11.setText(str((str(((str((varPagina + 9)) + str(constSpaces)))) + str((listChart[int((varPagina + 9) - 1)])))))
  label12.setText(str((str(((str((varPagina + 10)) + str(constSpaces)))) + str((listChart[int((varPagina + 10) - 1)])))))
  label13.setText(str((str(((str((varPagina + 11)) + str(constSpaces)))) + str((listChart[int((varPagina + 11) - 1)])))))
  label14.setText(str((str(((str((varPagina + 12)) + str(constSpaces)))) + str((listChart[int((varPagina + 12) - 1)])))))
  label15.setText(str((str(((str((varPagina + 13)) + str(constSpaces)))) + str((listChart[int((varPagina + 13) - 1)])))))

# Updates selection
def RefreshCursorPosition():
  global varBtnACounter, varCursor, listChart, varTrueCounter, i, varPagina, mapNotesNames, constSpaces, label0, labelSettings, label1, label2, label3, label4, label5, label6, label7, label8, label9, label10, label11, label12, label13, label14, label15
  if varCursor==0:
    label1.setColor(0xffffff, 0x009900)
  elif varCursor==1:
    label2.setColor(0xffffff, 0x009900)
  elif varCursor==2:
    label3.setColor(0xffffff, 0x009900)
  elif varCursor==3:
    label4.setColor(0xffffff, 0x009900)
  elif varCursor==4:
    label5.setColor(0xffffff, 0x009900)
  elif varCursor==5:
    label6.setColor(0xffffff, 0x009900)
  elif varCursor==6:
    label7.setColor(0xffffff, 0x009900)
  elif varCursor==7:
    label8.setColor(0xffffff, 0x009900)
  elif varCursor==8:
    label9.setColor(0xffffff, 0x009900)
  elif varCursor==9:
    label10.setColor(0xffffff, 0x009900)
  elif varCursor==10:
    label11.setColor(0xffffff, 0x009900)
  elif varCursor==11:
    label12.setColor(0xffffff, 0x009900)
  elif varCursor==12:
    label13.setColor(0xffffff, 0x009900)
  elif varCursor==13:
    label14.setColor(0xffffff, 0x009900)
  elif varCursor==14:
    label15.setColor(0xffffff, 0x009900)
  else:
    pass

# Updates all labels to default color
def RefreshAllLabelsColors():
  global varBtnACounter, varCursor, listChart, varTrueCounter, i, varPagina, mapNotesNames, constSpaces, label0, labelSettings, label1, label2, label3, label4, label5, label6, label7, label8, label9, label10, label11, label12, label13, label14, label15
  label1.setColor(0x33ff33, 0x000000)
  label2.setColor(0xffffff, 0x000000)
  label3.setColor(0xffffff, 0x000000)
  label4.setColor(0xffffff, 0x000000)
  label5.setColor(0xffffff, 0x000000)
  label6.setColor(0xffffff, 0x000000)
  label7.setColor(0xffffff, 0x000000)
  label8.setColor(0xffffff, 0x000000)
  label9.setColor(0xffffff, 0x000000)
  label10.setColor(0xffffff, 0x000000)
  label11.setColor(0xffffff, 0x000000)
  label12.setColor(0xffffff, 0x000000)
  label13.setColor(0xffffff, 0x000000)
  label14.setColor(0xffffff, 0x000000)
  label15.setColor(0xffffff, 0x000000)


def btnA_wasHold_event(state):
  global label0, labelSettings, label1, label2, label3, label4, label5, label6, label7, label8, label9, label10, label11, label12, label13, label14, label15, varBtnACounter, varCursor, listChart, varTrueCounter, varPagina, mapNotesNames, constSpaces, i
  varBtnACounter = 0
  SettingsChangeNote()
  RefreshAllLabelsText()


def btnA_wasClicked_event(state):
  global label0, labelSettings, label1, label2, label3, label4, label5, label6, label7, label8, label9, label10, label11, label12, label13, label14, label15, varBtnACounter, varCursor, listChart, varTrueCounter, varPagina, mapNotesNames, constSpaces, i
  if varTrueCounter > 0:
    varBtnACounter = 1 + varBtnACounter % 8
    SettingsChangeNote()
    RefreshAllLabelsText()
  else:
    label1.setText(str('⏹️ Playing...'))
    i_end = len(listChart)
    for i in (1 <= i_end) and upRange(1, i_end, 1) or downRange(1, i_end, 1):
      Speaker.tone(int(mapNotesNames[(listChart[int(i - 1)])]), 120)
      time.sleep_ms(170)
    Speaker.end()
    label1.setText(str('⏹️ Play'))


def btnB_wasClicked_event(state):
  global label0, labelSettings, label1, label2, label3, label4, label5, label6, label7, label8, label9, label10, label11, label12, label13, label14, label15, varBtnACounter, varCursor, listChart, varTrueCounter, varPagina, mapNotesNames, constSpaces, i
  varBtnACounter = 0
  if varCursor == 1 and varTrueCounter > 1:
    varPagina = (varPagina if isinstance(varPagina, (int, float)) else 0) + -1
    varTrueCounter = (varTrueCounter if isinstance(varTrueCounter, (int, float)) else 0) + -1
    RefreshAllLabelsColors()
    RefreshCursorPosition()
    RefreshAllLabelsText()
  elif varCursor > 1 or varCursor == 1 and varTrueCounter == 1:
    varCursor = (varCursor if isinstance(varCursor, (int, float)) else 0) + -1
    varTrueCounter = (varTrueCounter if isinstance(varTrueCounter, (int, float)) else 0) + -1
    RefreshAllLabelsColors()
    RefreshCursorPosition()
  else:
    pass


def btnPWR_wasClicked_event(state):
  global label0, labelSettings, label1, label2, label3, label4, label5, label6, label7, label8, label9, label10, label11, label12, label13, label14, label15, varBtnACounter, varCursor, listChart, varTrueCounter, varPagina, mapNotesNames, constSpaces, i
  varBtnACounter = 0
  if varCursor >= 14:
    if varTrueCounter == len(listChart):
      listChart.append(' ')
    varPagina = (varPagina if isinstance(varPagina, (int, float)) else 0) + 1
    varTrueCounter = (varTrueCounter if isinstance(varTrueCounter, (int, float)) else 0) + 1
    RefreshAllLabelsColors()
    RefreshCursorPosition()
    RefreshAllLabelsText()
  else:
    varCursor = (varCursor if isinstance(varCursor, (int, float)) else 0) + 1
    varTrueCounter = (varTrueCounter if isinstance(varTrueCounter, (int, float)) else 0) + 1
    RefreshAllLabelsColors()
    RefreshCursorPosition()


def setup():
  global label0, labelSettings, label1, label2, label3, label4, label5, label6, label7, label8, label9, label10, label11, label12, label13, label14, label15, varBtnACounter, varCursor, listChart, varTrueCounter, varPagina, mapNotesNames, constSpaces, i

  M5.begin()
  label0 = Widgets.Label("BuzzerTracker 1.1", 0, 0, 1.0, 0x25ff05, 0x000000, Widgets.FONTS.DejaVu9)
  labelSettings = Widgets.Label("by Comera", 70, 15, 1.0, 0x0aff00, 0x000000, Widgets.FONTS.DejaVu9)
  label1 = Widgets.Label("⏸️ Play", 0, 15, 1.0, 0x25ff05, 0x000000, Widgets.FONTS.DejaVu9)
  label2 = Widgets.Label("label2", 0, 30, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu9)
  label3 = Widgets.Label("label3", 0, 45, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu9)
  label4 = Widgets.Label("label4", 0, 60, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu9)
  label5 = Widgets.Label("label5", 0, 75, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu9)
  label6 = Widgets.Label("label6", 0, 90, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu9)
  label7 = Widgets.Label("label7", 0, 105, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu9)
  label8 = Widgets.Label("label8", 0, 120, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu9)
  label9 = Widgets.Label("label9", 0, 135, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu9)
  label10 = Widgets.Label("label10", 0, 150, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu9)
  label11 = Widgets.Label("label11", 0, 165, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu9)
  label12 = Widgets.Label("label12", 0, 180, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu9)
  label13 = Widgets.Label("label13", 0, 195, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu9)
  label14 = Widgets.Label("label14", 0, 210, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu9)
  label15 = Widgets.Label("label15", 0, 225, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu9)

  BtnA.setCallback(type=BtnA.CB_TYPE.WAS_HOLD, cb=btnA_wasHold_event)
  BtnA.setCallback(type=BtnA.CB_TYPE.WAS_CLICKED, cb=btnA_wasClicked_event)
  BtnB.setCallback(type=BtnB.CB_TYPE.WAS_CLICKED, cb=btnB_wasClicked_event)
  BtnPWR.setCallback(type=BtnPWR.CB_TYPE.WAS_CLICKED, cb=btnPWR_wasClicked_event)

  listChart = 'E7,D7,C7,D7,E7,E7,E7, ,D7,D7,E7,D7,C7, , , '.split(',')
  mapNotesNames = {'C7':'2093','D7':'2349','E7':'2637','F7':'2793','G7':'3135','A7':'3520','B7':'3951','C8':'4186',' ':'0'}
  constSpaces = '  '
  varPagina = 1
  varCursor = 0
  varTrueCounter = 0
  varBtnACounter = 0
  RefreshAllLabelsText()
  RefreshAllLabelsColors()
  RefreshCursorPosition()


# MADE BY COMERA.
def loop():
  global label0, labelSettings, label1, label2, label3, label4, label5, label6, label7, label8, label9, label10, label11, label12, label13, label14, label15, varBtnACounter, varCursor, listChart, varTrueCounter, varPagina, mapNotesNames, constSpaces, i
  M5.update()


if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")
