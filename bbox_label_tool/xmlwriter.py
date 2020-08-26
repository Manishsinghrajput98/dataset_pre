import xml.etree.cElementTree as ET
import os
anno_dir="xmls/"

def write_xml(image_id,data,w,h):
    xml_file = anno_dir+image_id + ".xml"
        
    annotation=ET.Element('annotation')
    
    image_url = data["url"]
    if os.path.exists(xml_file):
        annotation = ET.parse(xml_file).getroot()
        #print("file exist::",xml_file)
    else:

        filename = ET.SubElement(annotation, 'filename').text=str(image_url)
        size=ET.SubElement(annotation,'size')
        ET.SubElement(size, "width").text = str(w)
        ET.SubElement(size, "height").text= str(h)

    box = data["bbox"]
    #print(box)
    for item in box:
        object=ET.SubElement(annotation,'object')
        ET.SubElement(object, "name").text=str(item["cat"])
        bndbox=ET.SubElement(object,'bndbox')
        ET.SubElement(bndbox, "xmin").text=str(item["left"])
        ET.SubElement(bndbox, "ymin").text=str(item["top"])
        ET.SubElement(bndbox, "xmax").text=str(item["right"])
        ET.SubElement(bndbox, "ymax").text=str(item["bottom"])
     #  ET.SubElement(bndbox, "cat").text=str(item["cat"])
   
    
    tree = ET.ElementTree(annotation)
  
    tree.write(xml_file)


