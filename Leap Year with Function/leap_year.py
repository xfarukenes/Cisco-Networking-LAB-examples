# leap year with function
# leap year olabilmesi icin 4'e tam bolunmesi gerekir
# leap year olabilmesi icin 100'e tam bolunmemesi gerekir
# leap year olabilmesi icin 400'e tam bolunmesi gerekir
# bu koşullardan herhangi biri sağlanırsa yıl leap year'dır

# artık yıl kontrolü yapan fonksiyon

def is_year_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# artık yıl kontrolü yaparak o yılın o ayının kaç gün olduğunu döndüren fonksiyon

def days_in_month(year, month):
    # Geçersiz kontrol
    if year < 1 or month < 1 or month > 12:
        return None
    
    # Normal yıl ay günleri
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    # Şubat ve artık yıl kontrolü
    if month == 2 and is_year_leap(year):
        return 29
    
    return days[month - 1]


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
