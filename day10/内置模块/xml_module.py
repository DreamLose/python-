import xml.etree.cElementTree as ET
# child.tag() 获取标签名称
# child.attrib() 获取标签属性
# child.text() 获取标签内容
"""
tree = ET.parse("xml_test")  # 读取文件
root = tree.getroot()   #获取根
print(root.tag)  # 标签名称

# 遍历xml文档
for child in root:
    print(child.tag,child.attrib,child.text)
    for i in child:
        print(i.tag,i.attrib,i.text)
    print("+++++++++++++")

# 只遍历指定节点
for node in root.iter('year'):
    print(node.tag,node.text)
    print("+++++++++++++")

# 修改内容
for node in root.iter("year"):
    new_year = int(node.text) + 1
    node.text = str(new_year)  #修改内容
    node.set("updated","false")  # 修改标签属性
    tree.write('xml_new.xml')

# 删除node 删除所有rank大于50的标签
for country in root.findall("country"):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)
tree.write('out_xml.xml')
"""
# 创建xml文件
new_xml = ET.Element("namelist") # 创建根节点标签

# 插入字节点
name = ET.SubElement(new_xml,'name',attrib={"enrolled":"yes"})
age = ET.SubElement(name,'age',attrib={"checked":"no"})
sex = ET.SubElement(name,'sex')
sex.text = "male"
name2 = ET.SubElement(new_xml,'name',attrib={"enrolled":"no"})
age2 = ET.SubElement(name2,'age')
age2.text = "11"
sex2 = ET.SubElement(name2,'sex')
sex2.text = "man"
# 生成文档
et = ET.ElementTree(new_xml)
et.write("creatNew.xml",encoding='utf-8',xml_declaration=True)
# ET.dump(new_xml) # 打印生成的格式