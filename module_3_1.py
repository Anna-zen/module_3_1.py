calls = 0

def count_calls():
    global calls
    calls = calls + 1
    return calls


def string_info (string) :
    count_calls()
    length = len(string)
    uppercase = string.upper()
    lowercase = string.lower()
    return length, uppercase, lowercase


def is_contains (string, list_to_search) :
    count_calls()
    if string.lower() in [item.lower() for item in list_to_search]:
        return True
    else:
        return False

string = "город"
list_to_search = [ "дом", "улица" , " капиБарра " ,"гоРод" ]
print ( is_contains (string, list_to_search) )
#print (calls)

string = "зоЛОТо"
print (string_info(string))
#print (calls)

list_to_search = [ "аллюминий", "ЗОлото" , "железо" ,"титан" ]
print ( is_contains (string, list_to_search) )
#print (calls)

string = "КАпиБАрра"
list_to_search = [ "дом", "улица" , "Зоопарк" ,"гоРод", "КвазиКАпиБарра" ]
print (string_info(string))
print ( is_contains (string, list_to_search) )

print (calls)