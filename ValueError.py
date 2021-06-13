"""
Kiritil qiymatingizni butun son ekanligini tekshiradi.
Agar kiritgan qiymatingiz butun son bo'lmasa,
Sizdan yana qiymat so'raydi. Toki butun son kiritmaganingizcha davom etadi.
""" 

def valueerror():                                        
    """Siz yoshingizni kiritsangiz tug'ilgan yilingizni qaytaradi."""
    while True:                                          
        yosh = input("Yoshingizni kiriting ->")          
        try:                                             
            yosh = int(yosh)                             
        except ValueError:                               
            print("Yoshni butun son kiriting?")          
        else:                                            
            return (f"Siz {2021-yosh}-yilda tug'ilgansiz.")
            break                                                                                     


print(valueerror())

