import os
import json
from os import listdir
from tkinter import *
from PIL import Image,ImageTk,ImageOps


#***************************enter the path to image***********************************#
image_directory='D:/project/pic'
#*************************************************************************************#
save_image_directory="D:/project/"
#*************************************************************************#

save_image_directory=save_image_directory+"training_images"

os.mkdir(save_image_directory)
data_list=list()

def onclicked_saved():
    if (number==len(image_list)-1):
        save['state']=DISABLED
    has_potholes=pot.get()
    user_rating=rating.get()
    is_pitched=pitched.get()
    has_cracks=cracks.get()

    global data_list
    
    picname=image_list[number].split(".")
    
    img=Image.open(image_directory+'/'+image_list[number])
    img_mirrored=ImageOps.mirror(img)
    crop_box=(0,img.height/4,img.width,img.height)
    img_cropped=img.crop(box=crop_box)

    #dict
    for i in range (3):
        data={}
        new_name=picname[0]+str(i)+"."+picname[-1]
        #data[new_name]={}
        data['image_name']=new_name
        data['has_potholes']=has_potholes
        data['rating']=user_rating
        data['is_pitched']=is_pitched
        data['has_cracks']=has_cracks
        data_list.append(data)

        if (i==0):
            img.save(save_image_directory+"/"+new_name)
        if (i==1):
            img_mirrored.save(save_image_directory+"/"+new_name)
        if (i==2):
            img_cropped.save(save_image_directory+"/"+new_name)



    #if end reached
    if (number<len(image_list)-1):
        onclicked_forward()
    else :
        print("sakyoo")
    





number=0

#forward cliced
def onclicked_forward():
    global number
    number=number+1
    global image
    image.grid_forget()
    display_image(number)
    

def display_image(position):
    
    #load image
    global data_image
    data_image_full=Image.open(image_directory+'/'+image_list[position])
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
root.geometry("630x450")
root.resizable(0,0)


display_image(0)


#forward,next,image,save
forward_button=Button(root,text="NEXT",command=lambda:onclicked_forward())

exit_button=Button(root,text="EXIT",command=root.quit)

save=Button(root,text="SAVE",width=30,command=onclicked_saved)


#potholes radio
pot=IntVar()
potholes_label=Label(root,text="Has Potholes ?")
yes_potholes=Radiobutton(root,variable=pot,value=1,text="Yes")
no_potholes=Radiobutton(root,variable=pot,value=0,text="No")

#rating
rating=IntVar()
rating_label=Label(root,text="Rating")
r_excellent=Radiobutton(root,variable=rating,value=3,text="Excellent")
r_moderate=Radiobutton(root,variable=rating,value=2,text="Moderate")
r_bad=Radiobutton(root,variable=rating,value=1,text="Bad")

#is_pitched radio
pitched=IntVar()
pitch_label=Label(root,text="Is Pitched ?")
yes_pitched=Radiobutton(root,variable=pitched,value=1,text="Yes")
no_pitched=Radiobutton(root,variable=pitched,value=0,text="No")

#has cracks radio
cracks=IntVar()
cracks_label=Label(root,text="Has Cracks?")
yes_cracks=Radiobutton(root,variable=cracks,value=1,text="Yes")
no_cracks=Radiobutton(root,variable=cracks,value=0,text="No")


#display

potholes_label.grid(row=2,column=1,pady=10)
yes_potholes.grid(row=2,column=2)
no_potholes.grid(row=2,column=3)
rating_label.grid(row=3,column=1,pady=10)
r_excellent.grid(row=3,column=2)
r_moderate.grid(row=3,column=3,padx=50)
r_bad.grid(row=3,column=5)
pitch_label.grid(row=4,column=1,pady=10)
yes_pitched.grid(row=4,column=2)
no_pitched.grid(row=4,column=3)
cracks_label.grid(row=5,column=1,pady=10)
yes_cracks.grid(row=5,column=2)
no_cracks.grid(row=5,column=3)
forward_button.grid(row=6,column=5,pady=20)
exit_button.grid(row=6,column=0,pady=20)
save.grid(row=6,column=2,pady=20)


root.mainloop()

#dict to json here we go
json_file = json.dumps(data_list,indent=6)  
    
with open("images.json","w") as outfile:
    outfile.write(json_file)

#bigyadhungana@gmail.com      