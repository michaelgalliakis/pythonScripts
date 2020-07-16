import xml.etree.ElementTree as ET
import math

lite = False

if lite:
    tree = ET.parse('./data/dimens_lite.xml')
else:
    tree = ET.parse('./data/dimens.xml')

root = tree.getroot()

outputTree = ET.Element("resources")

for row in root:
    name = row.get('name')
    value = row.text
    # print(name, value)
    num = ''
    unit = ''
    for s in list(value):
        if s.isdigit():
            num += s
        else:
            unit += s
    if unit == 'sp':
        newNum = math.floor(int(num) + (int(num) * 0.50))
    else:
        newNum = math.floor(int(num) + (int(num) * 0.40))
    print(num + ' ' + unit, str(newNum) + ' ' + unit)
    ET.SubElement(outputTree, "dimen", name=name).text = str(newNum) + unit

elementTree = ET.ElementTree(outputTree)

if lite:
    elementTree.write("./data/dimens_lite2.xml")
else:
    elementTree.write("./data/dimens2.xml")
