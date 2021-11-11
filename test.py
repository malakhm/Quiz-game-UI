from tkinter import *

from PIL import ImageTk

        

root = Tk()
root.title("QUiz Game")
root.geometry("800x1600")



canvas = Canvas(width = 800, height = 500, bg= "#150041")
canvas.pack(expand= TRUE, fill= BOTH)

image = ImageTk.PhotoImage(file = 'quiz_bg.jpg')

canvas.create_image(10, 10, image=image, anchor=NW)


frame1 = Frame(canvas, bg='#ffffff')

frame2 = Frame(canvas, bg='teal')
# FUNCTIONS
def clicked():
    title2 = Label(frame2, text="LOUAY SHARMOUTT", width = 30, borderwidth=1, relief = "raised", font="Impact", bg= "teal").pack(padx = 25, pady=15)
    
    


    


title1 = Label(frame1, text="QUIZ TIME!", width = 30, borderwidth=1, relief = "raised", font="Impact", bg= "#0B0022", fg="white").pack(padx = 4, pady=5)
frame1.pack()


lbl1 = Label(canvas,text="what's your favorite season?", borderwidth=5, relief= "sunken", font = "Georgia", bg="MediumSlateBlue").pack(padx = 4, pady=1)
 

# Radio-Buttons

v15= IntVar()

rd = Radiobutton(canvas, text= "test", background='red', value = 1, variable = v15, command=clicked).pack(padx=15, pady=15)



v16= IntVar()

rd1 = Radiobutton(canvas, text= "test2", background='teal', value = 2, variable = v15).pack(padx=20, pady=20)







root.mainloop()