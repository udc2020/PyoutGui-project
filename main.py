""" Script Automation By Ultrasdzcoder   """

import pyautogui as pag
import time

def get_position():
   # Get Curent postion X , Y Mouse
   print("get Current Position !")
   time.sleep(8)
   print(pag.position())


def header():
   print("Wait 8 seconds")
   time.sleep(8)
   print('Starting')

def clean_screen():
   # Clean Screen 
   pag.click(x=1919, y=1076)

def create_folder():
   pag.rightClick(958,540)
   pag.moveTo(1042,858,3)
   pag.moveTo(1343,856,3)
   pag.moveTo(1409,854,3)
   pag.moveTo(1403,615,3)
   pag.click(1403,615)
   pag.typewrite("allstudents")
   pag.typewrite(['enter'])

def create_text_file():
   pag.moveTo(964,528,2)
   pag.doubleClick(964,528)
   pag.moveTo(486,234,2)
   pag.rightClick(486,234)
   pag.moveTo(532,579,2)
   pag.click(532,579)
   pag.moveTo(953,587,2)
   pag.moveTo(950,791,2)
   pag.click()
   pag.typewrite("student")
   

def insert_into_file():
   pag.typewrite(['enter'])
   pag.typewrite(['enter'])
   pag.typewrite("student")
   pag.moveTo(618,1045,2)
   pag.click()
  

def open_excel():
   pag.doubleClick(1850,55)
   
def copy_student():
   # Select All Excel Sheet 
   pag.moveTo(29,247,3)
   pag.click()
   # Copy It 
   pag.hotkey("Ctrl","c")
   pag.click(617,1058) 
   # Save in Text File 
   pag.hotkey("Ctrl","v")
   pag.hotkey("Ctrl","s")
   

def main():
   header()
   clean_screen()
   create_folder()
   create_text_file() 
   insert_into_file()
   clean_screen()
   open_excel()
   copy_student()
  
   
   



if __name__ == "__main__":
   main()