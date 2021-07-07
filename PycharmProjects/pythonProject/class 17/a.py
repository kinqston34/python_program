from flask import Flask,render_template,jsonify,Response
app = Flask(__name__)

@ app.route('/')
def home_page():
    import xml.etree.ElementTree as ET  #建立xml tree
    employees = ET.Element('Employees')
    employee1 = ET.SubElement(employees,'Employee')
    id1 = ET.SubElement(employee1,'id')
    id1.text = '1'
    name1 = ET.SubElement(employee1,'name')
    name1.text = 'Mary'
    return Response(ET.tostring(employees),mimetype = 'application/xml') #content-type:(google)

if __name__ == "__main__":
    app.run(debug= True,use_reloader = True)