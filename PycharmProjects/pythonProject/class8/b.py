import xml.etree.ElementTree as ET
xml_tree = ET.parse(r'c:\Users\user\PycharmProjects\pythonProject\class8\bb.xml')
employees = xml_tree.getroot()
for employee in employees:
    print(employee.tag)
    print(employee.attrib['id'])
    print(employee.attrib['name'])