########################################################################################################################################
# Import
import sympy
import datetime
from googletrans import Translator

translator = Translator()

########################################################################################################################################
# Function
# Function calculate 
def calculateEng(expressionEng):
    try:
        result = sympy.sympify(expressionEng)
        return str(result.evalf())
    except:
        return "Cannot be calculated!"

# Function transengtothai   
def TranslatorEngtoThai_response(TranslatorEngtoThai):
    TranslatorEngtoThai_Ans = translator.translate(TranslatorEngtoThai, src='en', dest='th').text
    return TranslatorEngtoThai_Ans

# Function get date  
def get_date_eng():
    now = datetime.datetime.now()
    return "Today is " + now.strftime("%Y-%m-%d")

# Function get time
def get_time_eng():
    now = datetime.datetime.now()
    return "It's " + now.strftime("%H:%M:%S")