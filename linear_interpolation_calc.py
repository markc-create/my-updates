from os import write
from tkinter import *
import datetime
import math
from DecimalToMinutes import decimal_Time_Conv

T2 = 0
L2 = 0
event_type = ""
log_result = ""

def time_conversion_min():
    try:
        time = float(time_conv_entry.get())
        hours_decimal = time
        hours = math.floor(hours_decimal)
        minutes_decimal = (hours_decimal - hours) * 60
        minutes = minutes_decimal + (hours * 60)
        time_conv_label.config(text=f"{minutes:.2f} Minutes")
        time_conv_label.place(x=500,y=250)

    except ValueError or ZeroDivisionError:
        time_conv_label.config(text="Invalid Input")
        time_conv_label.place(x=500, y=250)

def time_conversion_hr():
    try:
        time = float(time_conv_entry.get())
        minutes_decimal = time
        min_to_hours = (minutes_decimal - (minutes_decimal % 60)) / 60
        hours = min_to_hours + ((minutes_decimal % 60) / 60)
        time_conv_label.config(text=f"{hours:.2f} Hours")
        time_conv_label.place(x=500, y=250)

    except ValueError or ZeroDivisionError:
        time_conv_label.config(text="Invalid Input")
        time_conv_label.place(x=500, y=250)

def file_output():
    with open("../../Runtime_Load.txt", "a") as file:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{time}] {event_type}: {log_result}\n")

def calculate_T2_L2():
    global event_type
    global log_result
    try:
        t1 = float(t1_entry.get())
        t3 = float(t3_entry.get())
        l1 = float(l1_entry.get())
        l3 = float(l3_entry.get())
        t2 = t2_entry.get()
        l2 = l2_entry.get()
        if t2 == "" and l2 != "":
            l2 = float(l2)
            t2 = 0.0
            t2 = ((l2 - l1) * (t3 - t1)) / (l3 - l1) + t1
            T2 = t2
            hours,minutes,seconds = decimal_Time_Conv(T2)
            event_type = "Runtime"
            log_result = (f"T1={t1} T2={T2} T3={t3} \nL1={l1} L2={l2} L3={l3} "
                          f"\n{hours} Hours, {minutes} Minutes and {seconds} Seconds")
            calc_results.config(text=f"Runtime:\n{hours} Hours, {minutes} Minutes and {seconds} Seconds",
                                bg="white")
            calc_results.place(x=200, y=440)
        elif l2 == "" and t2 != "":
            t2 = float(t2)
            l2 = 0.0
            l2 = ((t2 - t1) * (l3 - l1)) / (t3 - t1) + l1
            L2 = l2
            event_type = "Load"
            log_result = (f"T1={t1} T2={t2} T3={t3} \nL1={l1} L2={L2} L3={l3}"
                          f"\n{l2:.2f} Watts/Amps per cell")
            calc_results.config(text=f"Load:\n{l2:.2f} Watts or Amps per cell",
                                bg="white")
            calc_results.place(x=200, y=440)
        else:
            calc_results.config(text="Please enter a value for either T2 or L2. \nBoth can't be blank.",
                                bg="white")
            calc_results.place(x=200, y=440)

    except ValueError:
        calc_results.place(x=200,y=440)
    except ZeroDivisionError:
        calc_results.place(x=200, y=440)

# Main Container
window = Tk()
window.geometry("700x600")
window.title("Linear interpolation")
window.config(background="grey")

# Title label
title_label = Label(window,
                    text="ESU Linear Interpolation",
                    font=("Arial",25,"bold"),
                    relief=RAISED,
                    bd=5)
title_label.place(x=175,y=0)

# Description Label
description_label = Label(window,
                          text="Linear interpolation allows you to calculate the value of available load or "
                               "desired run time between two data points on a battery performance specification "
                               "chart. If the load value is known, the corresponding run time can be calculated. "
                               "And vice versa. T1, T2 AND T3 MUST BE THE SAME UNIT OF TIME(Both in hours or both "
                               "in minutes).",
                          font=("Arial",15),
                          bg="grey",
                          justify=LEFT,
                          wraplength=660)
description_label.place(x=30,y=75)

# Time Conversion
time_entry_label = Label(window,
                         text="Enter time in \nhours or minutes:",
                         font=("Arial",15),
                         bg="grey")
time_entry_label.place(x=5,y=235)

time_conv_entry = Entry(window)
time_conv_entry.place(x=170,y=260)
minutes_button = Button(window,
                        text="Convert to\nMinutes",
                        font=("Arial",10,"bold"),
                        command=time_conversion_min,
                        bg="grey")
minutes_button.place(x=300,y=240)

hours_button = Button(window,
                        text="Convert to\nHours",
                        font=("Arial",10,"bold"),
                        command=time_conversion_hr,
                        bg="grey")
hours_button.place(x=400,y=240)

time_conv_label = Label(window,
                        text=f"",
                        font=("Arial",10),
                        bg="white")


# T1
t1_label = Label(window, text="Enter T1:",
                 font=("Arial",15),
                 bg="grey")
t1_label.place(x=0,y=325)
t1_entry = Entry(window)
t1_entry.place(x=100,y=330)

# T2
t2_label = Label(window, text="Enter T2:",
                 font=("Arial",15),
                 bg="grey")
t2_label.place(x=235,y=325)
t2_entry = Entry(window)
t2_entry.place(x=325,y=330)

# T3
t3_label = Label(window, text="Enter T3:",
                 font=("Arial",15),
                 bg="grey")
t3_label.place(x=465,y=325)
t3_entry = Entry(window)
t3_entry.place(x=555,y=330)

# L1
l1_label = Label(window, text="Enter L1:",
                 font=("Arial",15),
                 bg="grey")
l1_label.place(x=0,y=400)
l1_entry = Entry(window)
l1_entry.place(x=100,y=405)

# L2
l2_label = Label(window, text="Enter L2:",
                 font=("Arial",15),
                 bg="grey")
l2_label.place(x=235,y=400)
l2_entry = Entry(window)
l2_entry.place(x=325,y=405)

# L3
l3_label = Label(window, text="Enter L3:",
                 font=("Arial",15),
                 bg="grey")
l3_label.place(x=465,y=400)
l3_entry = Entry(window)
l3_entry.place(x=555,y=405)

# Calc Button
calc_button = Button(window,
                     text="Calculate",
                     command=calculate_T2_L2,
                     font=("Arial",20,"bold"),
                     bg="grey")
calc_button.place(x=25,y=450)
calc_button.bind("<Return>",lambda event: calculate_T2_L2())
calc_results = Label(window,
                         text="Invalid Input \nEnter in a number.",
                         font=("Arial",20),
                         bg="grey")
save_button = Button(window,
                     text="Save",
                     command=file_output,
                     font=("Arial",20,"bold"),
                     bg="grey")
save_button.place(x=25,y=525)
save_description = Label(window,
                         text="Save results to a .txt file \nsaved in the same folder as this program.",
                         font=("Arial",15),
                         bg="grey")
save_description.place(x=120,y=525)

window.mainloop()
