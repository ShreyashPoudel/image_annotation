from tkinter import *
from PIL import Image,ImageTk

#main window
root=Tk()
root.geometry("630x400")
root.resizable(0,0)

#load image
data_image_full=Image.open('D:/project/pic/peakpx.jpg')
data_image_reduced=data_image_full.resize((250,200))
data_image=ImageTk.PhotoImage(data_image_reduced)


#forward,next,image,save
forward_button=Button(root,text="NEXT")
back_button=Button(root,text="PREVIOUS")
image=Button(image=data_image)
save=Button(root,text="SAVE",width=30)


#potholes radio
pot=IntVar()
potholes_label=Label(root,text="Has Pothoes")
yes_potholes=Radiobutton(root,variable=pot,value=1,text="yes")
no_potholes=Radiobutton(root,variable=pot,value=0,text="no")

#rating
rating=IntVar()
rating_label=Label(root,text="Rating")
r_excellent=Radiobutton(root,variable=rating,value=3,text="Excellent")
r_moderate=Radiobutton(root,variable=rating,value=2,text="Moderate")
r_bad=Radiobutton(root,variable=rating,value=1,text="Bad")

#display
image.grid(row=1,column=2)
potholes_label.grid(row=2,column=1,pady=10)
yes_potholes.grid(row=2,column=2)
no_potholes.grid(row=2,column=3)
rating_label.grid(row=3,column=1,pady=10)
r_excellent.grid(row=3,column=2)
r_moderate.grid(row=3,column=3,padx=50)
r_bad.grid(row=3,column=5)
forward_button.grid(row=4,column=5,pady=20)
back_button.grid(row=4,column=0,pady=20)
save.grid(row=4,column=2,pady=20)


root.mainloop()