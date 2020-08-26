import os
import cv2
import xmlwriter


cat=["kangaroo"] 

label_dir="Labels"
dataset_dir="Images/kangaroo"
data={}

for img_path in os.listdir(dataset_dir):
    
    complete_path=os.path.join(dataset_dir,img_path)
    print(complete_path)
    h,w,c = cv2.imread(complete_path).shape
    image_id=img_path.split('.')[0]
    data[image_id] = {"bbox":"","url":""}
    data[image_id]["url"] = img_path
    
    boxes_a = []
   
    for cat_i in cat:
        
        #print(cat_i)
        
        cat_path=os.path.join(label_dir,cat_i)
        
       # if image_id in os.listdir(cat_path):
        label_file_path = cat_path+"/"+str(image_id)+".txt"
        if not os.path.exists(label_file_path):
            continue
        
        label_file = open(label_file_path,"r")
        lines = label_file.readlines()
      
        for line in lines[1:]:
            line = line[:-1]
           
            box=line.split(" ")
            boxes={"cat":"","left":"","top":"","right":"","bottom":""}
            boxes["cat"] = cat_i
            boxes["left"]=box[0]
            boxes["top"]=box[1]
            boxes["right"]=box[2]
            boxes["bottom"]=box[3]
            boxes_a.append(boxes)
            
    data[image_id]["bbox"] = boxes_a
    #print(data)
    xmlwriter.write_xml(image_id, data[image_id],w,h) 
    f= open("trainval.txt","a")
    f.write(image_id)
    f.write("\n")
    f.close()        
   

