
"""
Bo'lish qonun qoidasiga binoan 0 ga bo'lish mumkin emas.
Shuning uchun siz kiritgan birinchi qiymat 5 bo'lsa,
dasturni ishlatish vaqtida muammo chiqmasligi uchun errorni
yo'qotish uchun dastur yozdik.
Ya'na kiritgan sonlaringiz butun son bo'lmasa ham qayta kiritishni so'raydi.
Toki ZeroDivisionError va ValueError hatolarga yo'l qo'ymasangiz datur to'xtaydi. 
:)
"""

def zerodivisionerror():                                                                       
    """Ikkita son kiritasiz agar ZeroDivisionError va ValueError yuz bermasa dastur tugaydi."""
    while True:                                                                                
        value1 = input("1-sonni kiriting->")                                                   
        value2 = input("2-sonni kiriting->")                                                   
        try:                                                                                   
            value1 = int(value1)                                                               
            value2 = int(value2)                                                               
            value3 = value2/(5-value1)                                                         
        except ValueError:                                                                     
            print("Iltimos butun son kiriting")                                                
        except ZeroDivisionError:                                                              
            print(f"0 ga bo'lish mumkin emas. 5-{value1}=0. Qayta urinib ko'ring.")            
        else:                                                                                  
            print(f"Natija = {value3}")                                                        
            break                                                                              
                                                                                               
zerodivisionerror()                                                                            

