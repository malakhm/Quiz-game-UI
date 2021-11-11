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
title1 = Label(frame1, text="QUIZ TIME!", width = 30, borderwidth=1, relief = "raised", font="Impact", bg= "#0B0022", fg="white").pack(padx = 4, pady=5)
frame1.pack()


lbl1 = Label(canvas,text="what's your favorite season?", borderwidth=5, relief= "sunken", font = "Georgia", bg="steelblue").pack(padx = 4, pady=1)
 
# lbl1_window = canvas.create_window(10, 10, anchor=NW, window=lbl1)



v0 = IntVar()

v1 = IntVar()

v2 = IntVar()

v3 = IntVar()

v4 = IntVar()

v5 = IntVar()

rd1 = Radiobutton(canvas, text="Summer",
                 
                 background= "pink",
                 font = "consolas 10" , 
                value = 1, variable=v0).pack(padx = 5, pady=5)


rd2 = Radiobutton(canvas, text="Winter", 
                 background="pink",
                 font = "consolas 10" ,
                 value = 2, variable=v0).pack(padx = 10, pady=10)


lbl2 = Label(canvas, text="tea or coffee?", borderwidth=5, relief= "sunken", font = "Georgia", bg="steelblue").pack(padx = 7, pady=2)




rd3 = Radiobutton(canvas, text="Tea",
                background="pink",
                font = "consolas 10" , 
                padx=10, variable=v1, 
                value = 3).pack(padx = 7, pady=2)

rd4 = Radiobutton(canvas, text="Coffee",  
                  background="pink",
                  font = "consolas 10" ,
                  padx=10, variable=v1, 
                  value = 4).pack(padx = 7, pady=2)

lbl3 = Label(canvas, text = "POP music or Rock?", borderwidth=5, relief= "sunken", font = "Georgia", bg="steelblue").pack(padx = 7, pady=2)



rd5 = Radiobutton(canvas, text="POP", 
                 background="pink",
                 font = "consolas 10" , 
                 padx=10, variable=v2, 
                 value = 5).pack(padx = 7, pady=2)

rd6 = Radiobutton(canvas, text="Rock",  
                 background="pink",
                 font = "consolas 10" , 
                 padx=10, variable=v2, 
                 value = 6).pack(padx = 7, pady=2)

lbl4 = Label(canvas, text = "reading a book or watching a movie?", borderwidth=5, relief= "sunken", font = "Georgia", bg="steelblue").pack(padx = 7, pady=2)



rd7 = Radiobutton(canvas, text="Reading a book",
                  background="pink",
                 font = "consolas 10" , 
                 padx=1, variable=v3, 
                 value = 7).pack(padx = 7, pady=2)

rd8 = Radiobutton(canvas, text="Watching a movie", 
                 background="pink",
                 font = "consolas 10" ,
                 padx=5, variable=v3,
                 value = 8).pack(padx = 7, pady=2)

lbl5 = Label(canvas, text = "Football or BasketBall??",borderwidth=5, relief= "sunken", font = "Georgia", bg="steelblue").pack(padx = 7, pady=2)



rd9 = Radiobutton(canvas, text="Football", 
                  background="pink",
                  font = "consolas 10" ,
                  padx=10, variable=v4, 
                  value = 10).pack(padx = 7, pady=2)

rd10 = Radiobutton(canvas, text="BasketBall",  
                   background="pink",
                  font = "consolas 10" ,
                  padx=10, variable=v4, 
                  value = 11).pack(padx = 7, pady=2)


lbl6 = Label(canvas, text = "Pubg or Fortnite?",borderwidth=5, relief= "sunken", font = "Georgia", bg="steelblue").pack(padx = 7, pady=2)



rd11 = Radiobutton(canvas, text="Pubg", 
                  background="pink",
                  font = "consolas 10" , 
                  padx=10, variable=v5, 
                  value = 11).pack(padx = 7, pady=2)

rd12= Radiobutton(canvas, text="Fortnite",  
                  background="pink",
                  font = "consolas 10" , 
                  padx=10, variable=v5, 
                  value = 12).pack(padx = 7, pady=2)






window= Tk()
window.title("small window")
window.geometry("200x350")




window.mainloop()


root.mainloop()
