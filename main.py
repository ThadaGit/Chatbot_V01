########################################################################################################################################
# Import
import random
import re
import tkinter as tk
from tkinter import Scrollbar

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from googletrans import Translator

translator = Translator()

########################################################################################################################################
# ดึงข้อมูล
# ข้อมูลคำถามและคำตอบ
from chatbot_data import questions_thai, labels_thai
from chatbot_data_eng import questions_english, labels_english
from chatbot_responses import response_thai
from chatbot_responses_eng import response_eng

# ฟังก์ชันต่างๆ
from chatbot_function import calculate, TranslatorThaitoEng_response, get_date, get_time
from chatbot_function_eng import calculateEng, TranslatorEngtoThai_response, get_date_eng, get_time_eng

########################################################################################################################################
# สร้างโมเดลสำหรับการจัดหมวดหมู่คำถาม
model = make_pipeline(
    TfidfVectorizer(),
    MultinomialNB()
)

########################################################################################################################################
# questions
questions = questions_thai + questions_english

# labels
labels = labels_thai + labels_english

model.fit(questions, labels)

########################################################################################################################################
# main
def chatbot_response(question):
    if "แปลเป็นไทย" in question or "transtothai" in question:
        # หาตำแหน่งของคำว่า "แปลเป็นไทย" หรือ "transtothai"
        translation_start = question.find("แปลเป็นไทย") if "แปลเป็นไทย" in question else question.find("transtothai")       
        # ดึงข้อความที่ต้องการแปลออกมา
        text_to_translate = question[translation_start + len("แปลเป็นไทย") if "แปลเป็นไทย" in question else translation_start + len("transtothai"):].strip()        
        # ทำการแปลภาษา
        response = TranslatorEngtoThai_response(text_to_translate)
        return response
    
    if "แปลเป็นอังกฤษ" in question or "transtoeng" in question:
        # หาตำแหน่งของคำว่า "แปลเป็นอังกฤษ" หรือ "transtoeng"
        translation_start = question.find("แปลเป็นอังกฤษ") if "แปลเป็นอังกฤษ" in question else question.find("transtoeng")    
        # ดึงข้อความที่ต้องการแปลออกมา
        text_to_translate = question[translation_start + len("แปลเป็นอังกฤษ") if "แปลเป็นอังกฤษ" in question else translation_start + len("transtoeng"):].strip()              
        # ทำการแปลภาษา
        response = TranslatorThaitoEng_response(text_to_translate)                
        return response

    predicted_category = model.predict([question])[0]
    
    ####################################################################################################################################
    # response thai
    if   predicted_category == "ทักทาย":
        response = random.choice(response_thai["greetings_responses"])
    elif predicted_category == "บอกลา":
        response = random.choice(response_thai["goodbyes_responses"])
    elif predicted_category == "ชื่ออะไร":
        response = random.choice(response_thai["name_responses"])
    elif predicted_category == "คืออะไร":
        response = random.choice(response_thai["who_responses"])
    elif predicted_category == "คำนวณค่าคณิตศาสตร์":
        expression = re.sub(r'\bคำนวณ|คิดเลข\b', '', question)
        response = calculate(expression)
    elif predicted_category == "วันที่เท่าไหร่":
        response = get_date()
    elif predicted_category == "เวลาเท่าไหร่":
        response = get_time()
    elif predicted_category == "MLคืออะไร":
        response = random.choice(response_thai["MLis_responses"])
    elif predicted_category == "MLทำอะไรได้":
        response = random.choice(response_thai["MLcando_responses"])
    elif predicted_category == "NOTGateคืออะไร":
        response = random.choice(response_thai["NOTGateis_responses"])
    elif predicted_category == "ANDGateคืออะไร":
        response = random.choice(response_thai["ANDGateis_responses"])
    elif predicted_category == "ORGateคืออะไร":
        response = random.choice(response_thai["ORGateis_responses"])
    elif predicted_category == "NANDGateคืออะไร":
        response = random.choice(response_thai["NANDGateis_responses"])
    elif predicted_category == "NORGateคืออะไร":
        response = random.choice(response_thai["NORGateis_responses"])
    elif predicted_category == "XORGateคืออะไร":
        response = random.choice(response_thai["XORGateis_responses"])
    elif predicted_category == "XNORGateคืออะไร":
        response = random.choice(response_thai["XNORGateis_responses"])

    ####################################################################################################################################
    # response english
    elif predicted_category == "Hi":
        response = random.choice(response_eng["greetings_responses_eng"])
    elif predicted_category == "Goodbye":
        response = random.choice(response_eng["goodbyes_responses_eng"])
    elif predicted_category == "What name?":
        response = random.choice(response_eng["name_responses_eng"])
    elif predicted_category == "Who?":
        response = random.choice(response_eng["who_responses_eng"])
    elif predicted_category == "Calculate":
        expressionEng = re.sub(r'\bCalculate|calculate\b', '', question)
        response = calculateEng(expressionEng)
    elif predicted_category == "What date?":
        response = get_date_eng()
    elif predicted_category == "What time?":
        response = get_time_eng()
    elif predicted_category == "What is ML?":
        response = random.choice(response_eng["MLis_responses_eng"])
    elif predicted_category == "What can do ML?":
        response = random.choice(response_eng["MLcando_responses_eng"])
    elif predicted_category == "What is NOTGate?":
        response = random.choice(response_eng["NOTGateis_responses_eng"])
    elif predicted_category == "What is ANDGATE?":
        response = random.choice(response_eng["ANDGateis_responses_eng"])
    elif predicted_category == "What is ORGATE?":
        response = random.choice(response_eng["ORGateis_responses_eng"])
    elif predicted_category == "What is NANDGATE?":
        response = random.choice(response_eng["NANDGateis_responses_eng"])
    elif predicted_category == "What is NORGATE?":
        response = random.choice(response_eng["NORGateis_responses_eng"])
    elif predicted_category == "What is XORGATE?":
        response = random.choice(response_eng["XORGateis_responses_eng"])
    elif predicted_category == "What is XNORGATE?":
        response = random.choice(response_eng["XNORGateis_responses_eng"])

    ####################################################################################################################################
    # response error
    else:
        response = "I don't understand your question."
    return response

########################################################################################################################################
# function interface show chat text
def send_message(event=None):
    user_input = input_text.get()
    response = chatbot_response(user_input)
    chat_text.config(state=tk.NORMAL)  # เปิดใช้งาน Text widget เพื่อสามารถแสดงผลได้
    chat_text.insert(tk.END, f"User: {user_input}\n")
    chat_text.insert(tk.END, f"Chatbot: {response}\n")
    chat_text.config(state=tk.DISABLED)  # ปิดใช้งาน Text widget ให้ไม่สามารถ
    input_text.delete(0, tk.END)

########################################################################################################################################
# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Chatbot")

# กำหนดขนาดของหน้าต่าง
root.geometry("600x600")

# สร้างแชทและข้อมูลผู้ใช้
chat_text = tk.Text(root, state=tk.DISABLED)  # กำหนดให้ Text widget ใช้งานได้เฉพาะการแสดงผลเท่านั้น
chat_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

scrollbar = Scrollbar(root, command=chat_text.yview)

# scrollbar ชิดขอบขวาของปุ่ม Send และยาวตั้งจากบนสุดถึงล่างสุดของเฟรม
scrollbar.grid(row=0, column=1, rowspan=2, sticky="ns", in_=root)

# ปรับค่าให้ Scrollbar อยู่ชิดขอบล่าง
scrollbar.config(command=chat_text.yview, orient=tk.VERTICAL)
chat_text.config(yscrollcommand=scrollbar.set)

input_text = tk.Entry(root)
input_text.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="ew", ipady=2)

send_button = tk.Button(root, text="Send", command=send_message, bg="blue", fg="white")
send_button.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="e")  # ปรับค่า ipady ตามความสูงที่ต้องการ

# ใช้งานปุ่ม Enter เพื่อส่งข้อความ
root.bind("<Return>", send_message)

# ปรับขนาดและการขยายในแถวและคอลัมน์
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# เริ่มการทำงานของหน้าต่าง
root.mainloop()
