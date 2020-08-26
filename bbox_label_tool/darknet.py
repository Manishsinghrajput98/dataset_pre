import xml.etree.cElementTree as ET
import xmltodict
import cv2
import os
import collections
xml_dir="/home/rajput/Desktop/bbox_label_tool/xmls"
#classes=["dress","top","skirt","pant","bag","eyewear","outerwear","shoe","shirt","suit","short","boot","heel"]

#classes = ["tops","skirts","dresses","bags","eyewear","pants","outerwear","shoes","shirt","shorts","boots","heels"]

#classes=["ethnic_dress","lehenga","medium_dress","salwar_suit","saree","short_dress"]

classes=["kangaroo"]#"byjus","cycle_pure_agarbathies","dream11","hero","honda","lifebuoy","mi","nike","paytm","vivo","walton"]#["Beer","Weapon","smoking","tables","cards"]#,"syringe","bottel","pills","slot"]

for xml_path in os.listdir(xml_dir):
    

    path=os.path.join(xml_dir,xml_path)
    
    with open(path) as fd:
        doc = xmltodict.parse(fd.read())

    anno = doc["annotation"]
    filename = anno["filename"]
    w = int(anno["size"]["width"])
    h = int(anno["size"]["height"])
    
    
    if "object" in anno.keys():  
        txt_file_path = xml_path.replace("xml","txt")
        print(txt_file_path)
        txt_file = open("data/"+txt_file_path,"w")
  
        bbox_array = anno["object"]
        img = cv2.imread(filename)
        i=0
    
        if not isinstance(bbox_array,collections.OrderedDict): 
            i+1
            for bbox_i in bbox_array:
                cat_name = bbox_i["name"]
                cat_index = classes.index(cat_name)  
              
                bbox = bbox_i["bndbox"]
                xmin=int(bbox["xmin"])
                ymin=int(bbox["ymin"])
                xmax=int(bbox["xmax"])
                ymax=int(bbox["ymax"])
            
                #img = cv2.rectangle(img,(xmin,ymin),(xmax,ymax),(0,255,0),10)
                
                xmin = xmin if xmin > 0 else 1
                ymin = ymin if ymin > 0 else 1
                xmax = xmax if xmax < w else w-1
                ymax = ymax if ymax < h else h-1
                
                box_w = xmax-xmin
                box_h = ymax-ymin
                centre_x= xmin+(box_w/2)
                centre_y= ymin+(box_h/2)

                _x = centre_x/float(w)
                _y = centre_y/float(h)
                _w = box_w/float(w)
                _h = box_h/float(h)
                
               
                data = "{} {} {} {} {}\n".format(cat_index,_x,_y,_w,_h)
                txt_file.write(data)
                
        else:
            
            bbox_i = bbox_array
            cat_name = bbox_i["name"]
            cat_index = classes.index(cat_name)


            bbox = bbox_i["bndbox"]
            xmin=int(bbox["xmin"])
            ymin=int(bbox["ymin"])
            xmax=int(bbox["xmax"])
            ymax=int(bbox["ymax"])

            img = cv2.rectangle(img,(xmin,ymin),(xmax,ymax),(255,0,0),10)


            xmin = xmin if xmin > 0 else 1
            ymin = ymin if ymin > 0 else 1
            xmax = xmax if xmax < w else w-1
            ymax = ymax if ymax < h else h-1
            
            box_w = xmax-xmin
            box_h = ymax-ymin
            centre_x= xmin+(box_w/2)
            centre_y= ymin+(box_h/2)

            _x = centre_x/float(w)
            _y = centre_y/float(h)
            _w = box_w/float(w)
            _h = box_h/float(h)
                
                
               
            data = "{} {} {} {} {}\n".format(cat_index,_x,_y,_w,_h)
            txt_file.write(data)

        #cv2.namedWindow("img",cv2.WINDOW_NORMAL)
        #cv2.resizeWindow("img",600,600)
        #cv2.imshow("img",img) 
        #cv2.waitKey(0)


