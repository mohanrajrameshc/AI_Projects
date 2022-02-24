# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 11:25:28 2021

@author: MOHAN RAJ
"""
import tkinter as tk
from tkinter import messagebox as mb

def cambox():
    sd.social()
    #if mb.askyesno('Verify', 'Really quit?'):
     #   mb.showwarning('Yes', sd.social())
    #else:
     #   mb.showinfo('No', 'Video Prediction has been dtoped')

def videobox():
    if mb.askyesno('Verify', 'Verify thus the video contains in video folder?'):
        mb.showwarning('Yes', sd_video.social())
    else:
        mb.showinfo('No', 'Camera Prediction has been Stoped')




from tkinter import * 
from tkinter.ttk import *
import sd
import sd_video
#import sd_samp

def vid():
    #sd_video.social()
    tk.Button(text='Are you want to open the Video Prediction', command=videobox).pack(fill=tk.X)
    tk.mainloop()
def cam():
    tk.Button(text='Are you want to open the Camera Prediction', command=cambox).pack(fill=tk.X)
    tk.mainloop()

    #sd.social()
    
    
    
class NewWindow(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("New Window") 
        self.geometry("200x200") 
        label = Label(self, text ="Social Distance Predictition") 
        label.pack()
    
  
  
# creates a Tk() object 
master = Tk()  
# sets the geometry of  
# main root window 
master.geometry("500x500") 
  
label = Label(master, text ="Social Distance Prediction") 
label.pack(side = TOP, pady = 10) 
  
# a button widget which will 
# open a new window on button click 
btn = Button(master, text="Camera Prediction",command=cam) 
  
# Following line will bind click event 
# On any click left / right button 
# of mouse a new window will be opened 
btn.pack(pady = 10) 
btn = Button(master, text="Video Prediction",command=vid) 
  
# Following line will bind click event 
# On any click left / right button 
# of mouse a new window will be opened 
btn.pack(pady = 10) 
  
# mainloop, runs infinitely 
mainloop() 