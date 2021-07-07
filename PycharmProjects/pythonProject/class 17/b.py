import requests
r = requests.get('http://127.0.0.1:5000/')
import xml.etree.ElementTree as ET
xmlTree = ET.ElementTree(ET.fromstring(r.text))
employees = xmlTree.getroot()
for employee in employees:
    print(employee.tag)
    for child_tag in employee:
        print(child_tag.tag,child_tag.text)