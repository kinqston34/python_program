#decoding xml->python
#strptime
import xml.etree.ElementTree as ET
xml_tree = ET.parse(r'c:\Users\user\PycharmProjects\pythonProject\class7\aa.xml')
employees = xml_tree.getroot()
for employee in employees:
    print(employee.tag)
    for child_tag in employee:
        print(child_tag.tag)
        print(child_tag.text)
