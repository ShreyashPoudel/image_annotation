import os
import json
from os import listdir
from tkinter import *
from PIL import Image,ImageTk


#***************************enter the path to image***********************************#
image_directory="D:/project/pic"

data={}
def onclicked_saved():
    if (number==len(image_list)-1):
        save['state']=DISABLED
    has_potholes=pot.get()
    user_rating=rating.get()
    print(f"potholes={has_potholes} rating={user_rating}")

    global data
    data[image_list[number]]={}
    data[image_list[number]]['has_potholes']=has_potholes
    data[image_list[number]]['rating']=user_rating
    data[image_list[number]]['is_pitched']="baki"

    if (number<len(image_list)-1):
        onclicked_forward()
    else :
        print ("sakyoo")




number=0


def onclicked_forward():
    global number
    number=number+1
    global image
    image.grid_forget()
    display_image(number)
    

def display_image(position):
    
    #load image
    global data_image
    data_image_full=Image.open('D:/project/pic/'+image_list[position])
    data_image_reduced=data_image_full.resize((250,200))
    data_image=ImageTk.PhotoImage(data_image_reduced)

    #display part
    global  image
    image=Label(root,image=data_image)
    image.grid(row=1,column=2)
    if (position==len(image_list)-1):
        forward_button['state']=DISABLED




#image list

image_list=list()
for i_images in os.listdir(image_directory):
   image_list.append(i_images)


#main window
root=Tk()
root.geometry("630x400")
root.resizable(0,0)


display_image(0)


#forward,next,image,save
forward_button=Button(root,text="NEXT",command=lambda:onclicked_forward())

back_button=Button(root,text="PREVIOUS")

save=Button(root,text="SAVE",width=30,command=onclicked_saved)


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


json_file = json.dumps(data,indent=6)  
    
with open("images.json","w") as outfile:
    outfile.write(json_file)