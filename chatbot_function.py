########################################################################################################################################
# Import
import sympy
import datetime
from googletrans import Translator

translator = Translator()

########################################################################################################################################
# Function
# Function คิดเลข
def calculate(expression):
    try:
        result = sympy.sympify(expression)
        return str(result.evalf())
    except:
        return "ไม่สามารถคำนวณได้"

# Function แปลอังกฤษเป็นไทย
def TranslatorThaitoEng_response(TranslatorThaitoEng):
    TranslatorThaitoEng_Ans = translator.translate(TranslatorThaitoEng, src='th', dest='en').text
    return TranslatorThaitoEng_Ans

# Function ดึงวันที่ 
def get_date():
    now = datetime.datetime.now()
    return "วันนี้วันที่ " + now.strftime("%Y-%m-%d")

# Function ดึงเวลา
def get_time():
    now = datetime.datetime.now()
    return "ตอนนี้เวลา " + now.strftime("%H:%M:%S")