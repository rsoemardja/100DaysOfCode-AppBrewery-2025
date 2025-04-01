import tkinter as Tk

root = tk.Tk()
root.title("Disappearing Text")

label = tk.Label(root, text="Hello, World!", font=("Helvetica", 24), fg="blue")
label.place(anchor="n", relx=0.5, rely=0.5)

def disappear_text():
    label.destroy()
    root.after(2000, disappear_text)
    
label.after(2000, disappear_text)

root.mainloop()