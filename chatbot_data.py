########################################################################################################################################
# คำถาม
greetings = ["สวัสดี", "สวัสดีครับ", "สวัสดีค่ะ"]
goodbyes = ["บาย", "ลาก่อน", "ลาก่อนครับ", "ลาก่อนค่ะ"]
name = ["คุณชื่ออะไร", "ชื่ออะไร", "สิ่งนี้ชื่ออะไร"]
who = ["คุณคือใคร", "สิ่งนี้คืออะไร", "คุณคืออะไร"]
calculators = ["คำนวณ", "คิดเลข"]
date = ["วันนี้วันที่เท่าไหร่", "วันนี้วันอะไร", "วันที่เท่าไหร่"]
time = ["ตอนนี้กี่โมง", "ตอนนี้เวลาอะไร", "กี่โมงแล้ว"]
MLis = ["Machine Learning คืออะไร","Machine Learning คือ"]
MLcando = ["Machine Learning ทำอะไรได้บ้าง","Machine Learning ทำอะไรได้"]
NOTGateis = ["NOTGate คืออะไร","NOTGate คือ","NOT Gate คืออะไร","NOT Gate คือ"]
ANDGateis = ["ANDGate คืออะไร","ANDGate คือ","AND Gate คืออะไร","AND Gate คือ"]
ORGateis = ["ORGate คืออะไร","ORGate คือ","OR Gate คืออะไร","OR Gate คือ"]
NANDGateis = ["NANDGate คืออะไร","NANDGate คือ","NAND Gate คืออะไร","NAND Gate คือ"]
NORGateis = ["NORGate คืออะไร","NORGate คือ","NOR Gate คืออะไร","NOR Gate คือ"]
XORGateis = ["XORGate คืออะไร","XORGate คือ","XOR Gate คืออะไร","XOR Gate คือ"]
XNORGateis = ["XNORGate คืออะไร","XNORGate คือ","XNOR Gate คืออะไร","XNOR Gate คือ"]

# สามารถเพิ่มคำถามได้อีก

########################################################################################################################################
# หมวดหมู่
categories_thai = [
    "ทักทาย", 
    "บอกลา", 
    "ชื่ออะไร", 
    "คืออะไร", 
    "คำนวณค่าคณิตศาสตร์", 
    "วันที่เท่าไหร่", 
    "เวลาเท่าไหร่", 
    "MLคืออะไร",
    "MLทำอะไรได้",
    "NOTGateคืออะไร",
    "ANDGateคืออะไร",
    "ORGateคืออะไร",
    "NANDGateคืออะไร",
    "NORGateคืออะไร",
    "XORGateคืออะไร",
    "XNORGateคืออะไร",
]

########################################################################################################################################
# รวมคำถาม
questions_thai = greetings + goodbyes + name + who + calculators + date + time + MLis + MLcando + NOTGateis + ANDGateis + ORGateis + NANDGateis + NORGateis + XORGateis + XNORGateis

########################################################################################################################################
# labels
labels_thai = (
    ["ทักทาย"] * len(greetings) +
    ["บอกลา"] * len(goodbyes) +
    ["ชื่ออะไร"] * len(name) +
    ["คืออะไร"] * len(who) +
    ["คำนวณค่าคณิตศาสตร์"] * len(calculators) +
    ["วันที่เท่าไหร่"] * len(date) +
    ["เวลาเท่าไหร่"] * len(time) +
    ["MLคืออะไร"] * len(MLis) + 
    ["MLทำอะไรได้"] * len(MLcando) +
    ["NOTGateคืออะไร"] * len(NOTGateis) +
    ["ANDGateคืออะไร"] * len(ANDGateis) + 
    ["ORGateคืออะไร"] * len(ORGateis) +
    ["NANDGateคืออะไร"] * len(NANDGateis) +
    ["NORGateคืออะไร"] * len(NORGateis) +
    ["XORGateคืออะไร"] * len(XORGateis) +
    ["XNORGateคืออะไร"] * len(XNORGateis)
)