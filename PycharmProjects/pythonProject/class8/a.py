import xml.etree.ElementTree as ET
employees = ET.Element('Employees')
emp1 = ET.SubElement(employees,'Employee')
emp1.set('id','1')
emp1.set('name','Mary')
emp2 = ET.SubElement(employees,'Employee')
emp2.set('id','2')
emp2.set('name','John')
print(ET.tostring(employees))
et = ET.ElementTree(employees)
with open(r'c:\Users\user\PycharmProjects\pythonProject\class8\bb.xml',mode = 'wb') as f:
    et.write(f,encoding = 'UTF-8')