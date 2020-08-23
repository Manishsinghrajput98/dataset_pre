import os
img_dir = "/home/link/Desktop/Training/Images/images"      #change the path of your folder according your system
json_file = "/home/link/Desktop/Training/xmls/"			   #change the path of your folder according your system

json_list = []
for xml in os.listdir(json_file):
    xml_=xml.split('.')[0]
    json_list.append(xml_)


for img in os.listdir(img_dir):
    img_= img.split('.')[0]
    if img_ not in json_list:
       img_name=os.path.join(img_dir+"/"+img_+".jpg")
       print("________",img_name)
       os.remove(img_name)

