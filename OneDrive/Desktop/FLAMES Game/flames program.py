import tkinter as tk
from tkinter import messagebox
from tkinter import font

def clear_entry():
    entry_name1.delete(0, tk.END)
    entry_name2.delete(0, tk.END)


def calculate_flames():
    name1 = (entry_name1.get()).lower()
    name2 = (entry_name2.get()).lower()
    
    count = len(name1) + len(name2)
    if len(name1)==0 or len(name2)==0:
        messagebox.showinfo("Error", "Please enter your names")
        return
        
    d1 = {}
    d2 = {}
    
    for i in name1:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
    for i in name2:
        if i in d2:
            d2[i] += 1
        else:
            d2[i] = 1
            
    for i in name1:
        if i in name2 and d2[i] != 0:
            d2[i] -= 1
            d1[i] -= 1
            count -= 2
            continue
    
    flames = ["F", "L", "A", "M", "E", "S"]
    while len(flames)>1:
        n=len(flames)
        rem=count%n
        if rem==0:
            s=flames[rem:rem-1]
            flames=s
        else:
            s=flames[rem:]+flames[:rem-1]
            flames=s
    
    result = ""
    if flames[0] == "F":
        result = name1.upper()+" "+"and"+" "+name2.upper()+" "+"You both are FRIENDS"
    elif flames[0] == "L":
        result = name1.upper()+" "+"and"+" "+name2.upper()+" "+"You both are LOVERS"
    elif flames[0] == "A":
        result = name1.upper()+" "+"and"+" "+name2.upper()+" "+"You both have ATTRACTION"
    elif flames[0] == "M":
        result = name1.upper()+" "+"and"+" "+name2.upper()+" "+"You both get MARRIED"
    elif flames[0] == "E":
        result = name1.upper()+" "+"and"+" "+name2.upper()+" "+"You both are ENEMIES"
    elif flames[0] == "S":
        result = name1.upper()+" "+"and"+" "+name2.upper()+" "+"You both are SISTERS"
    
    messagebox.showinfo("FLAMES Result",result)
    clear_entry()



root = tk.Tk()
root.title("FLAMES Calculator")
root.configure(bg="#FFC0CB") 


font_head = font.Font(family="Helvetica", size=40,weight="bold")
font_label = font.Font(family="Helvetica", size=16)
font_entry = font.Font(family="Helvetica", size=16)
font_button = font.Font(family="Helvetica", size=16, weight="bold")


label_name = tk.Label(root, text="F.L.A.M.E.S", bg="#FFC0CB", fg="cadet blue",font=font_head)
label_name.pack(pady=(30, 10))  

label_name1 = tk.Label(root, text="Enter Your Name:", bg="#FFC0CB", fg="dark slate grey", font=font_label)
label_name1.pack(pady=(50, 10))  

entry_name1 = tk.Entry(root, fg="LightBlue4",font=font_entry)
entry_name1.pack(pady=(0, 10))  

label_name2 = tk.Label(root, text="Enter Your Person's Name:", bg="#FFC0CB", fg="dark slate grey", font=font_label)
label_name2.pack(pady=(20, 10)) 

entry_name2 = tk.Entry(root, fg="LightBlue4",font=font_entry)
entry_name2.pack(pady=(0, 20))  


button_calculate = tk.Button(root, text="Calculate FLAMES", command=calculate_flames, bg="#FFB6C1", fg="cadet blue", font=font_button)
button_calculate.pack(pady=(10, 20))


root.mainloop()




