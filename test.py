sample = {
    'یک': '1', 'دو': '2', 'سه': '3', 'چهار': '4', 'پنج': '5', 'شش': '6', 'هفت': '7', 'هشت': '8', 'نه': '9', 'ده': '10',
    'یازده': '11', 'دوازده': '12', 'سیزده': '13', 'چهارده': '14', 'پانزده': '15', 'شانزده': '16', 'هفده': '17',
    'هجده': '18', 'نوزده': '19',
    'بیست': '20', 'سی': '30', 'چهل': '40', 'پنجاه': '50', 'شصت': '60', 'هفتاد': '70', 'هشتاد': '80', 'نود': '90',
    'صد': '100', 'دویست': '200', 'سیصد': '300', 'پانصد': '500','چهارصد': '400','ششصد': '600','هفتصد': '700','هشتصد': '800','نهصد': '900','یکصد': '100'

}
z = {
    'هزار': '1000', 'میلیون': '1000000', 'میلیارد': '1000000000',
}

# number_str = input()
number_str = ' یکصد میلیارد و دویست میلیون و هفتاد و سه هزار و صد و هشتاد و سه'
number_str = number_str.replace(' ', '') + '    '

numbers = []
stable_number = ''
base_number = ''
count = 0
number_str = number_str.replace(' ', '')
str_result = ''
result = 0
temp_num = 0
zarib_num = None


for num in number_str:
    if num == 'و':
        for zarib in z.keys():
            if zarib in str_result:
                if zarib_num is not None:
                    zarib_num *= int(z[zarib])
                else:
                    zarib_num = int(z[zarib])
                str_result = str_result.replace(zarib, '')
        if str_result == '':
            result += zarib_num
            zarib_num = None
            continue
        if str_result in sample.keys():
            temp_num += int(sample[str_result])
            str_result = ''
            if zarib_num is not None:
                result += zarib_num * temp_num
                zarib_num = None
                temp_num = 0
        else:
            str_result += num
    else:
        str_result += num


for zarib in z.keys():
    if zarib in str_result:
        if zarib_num is not None:
            zarib_num *= int(z[zarib])
        else:
            zarib_num = int(z[zarib])
        str_result = str_result.replace(zarib, '')
if str_result == '':
    result += zarib_num
    zarib_num = None
if str_result in sample.keys():
    temp_num += int(sample[str_result])
    str_result = ''
    if zarib_num is not None:
        result += zarib_num * temp_num
        zarib_num = None
        temp_num = 0
result += temp_num
print(result)