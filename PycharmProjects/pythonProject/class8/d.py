from lxml import etree   #換函示庫
root = etree.parse(r'c:\Users\user\PycharmProjects\pythonProject\class8\cc.xml')
l = root.xpath('Employee[id=1 and name="Mary"]') #xpath 搜尋 #[1] 尋找第一筆資料  #[id=1] 針對id搜尋
for element in l:                  #last() 找最後一筆，或最新增加的  #position()<3 直接下位置 #@type =" "針對屬性
    print('tag:',element.tag,'text:',element.text)         # id>1 # id=1 and name="Mary"
    print('attrib:',element.attrib['type'])
    for child in element:
        print('child tag:', child.tag, 'text:', child.text)