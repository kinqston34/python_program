#encoding
import xml.etree.ElementTree as ET
employees = ET.Element('Employees')
emp1 = ET.SubElement(employees,'Employee')
id1 = ET.SubElement(emp1,'id')
id1.text = '1'
name1 = ET.SubElement(emp1,'name')
name1.text = 'Mary'
# id2 = ET.SubElement(emp2,'id')
# id2.text = '2'
# name2 = ET.SubElement(emp2,'name')
# name2.text = 'John'
print(ET.tostring(employees))
et = ET.ElementTree(employees)
with open(r'c:\Users\user\PycharmProjects\pythonProject\class7\aa.xml',mode = 'wb') as f:
    et.write(f,encoding = 'UTF-8')
