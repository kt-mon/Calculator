import tkinter as tk

def press_button(value):
    current = entry_var.get()
    entry_var.set(current + value)

def calculate():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

def clear():
    entry_var.set("")

def delete():
    current = entry_var.get()
    entry_var.set(current[:-1])


window = tk.Tk()
window.title("Calculate")
window.geometry("300x400")
window.configure(bg="white")

entry_var = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_var, font=("Arial",26), bd=10, relief="sunken",justify="right")
entry.pack(fill="both",ipadx=8,ipady=15,padx=10,pady=10)

button = [
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["c","0","=","+"]
]

for row in button:
    frame = tk.Frame(window)
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        if btn_text == "=":
            btn = tk.Button(frame, text=btn_text, font=("Arial",18), bg="lightgreen", command= calculate)
        elif btn_text == "c":
            btn = tk.Button(frame, text=btn_text, font=("Arial",18), bg="lightgreen",command= clear)
        else:
            btn = tk.Button(frame, text=btn_text, font=("Arial",18),bg="lightgreen",command=lambda txt = btn_text : press_button(txt))
        btn.pack(side="left", expand=True, fill="both", padx=2,pady=2)


del_button = tk.Button(window, font=("Arial",18), text="Del", bg="#ccc", command= delete)
del_button.pack(fill="x",padx=10, pady=5)

window.mainloop()