import xml.etree.ElementTree as ET
xml_tree = ET.parse(r'c:\Users\user\PycharmProjects\pythonProject\class8\cc.xml')
root = xml_tree.getroot()
l = root.findall('Employee')
for element in l:
    print('tag:',element.tag,'text:',element.text)
    print('attrib:',element.attrib['type'])
    for child in element:
        print('child tag:', child.tag, 'text:', child.text)
        #print('attrib:', child.attrib['type'])