import re

class Events(object):
    def __init__(self):
        self.pattern = {'واقعه': [r"\b((افشا|افشای) (الف|ب))\b", # افشای الف
                                  r"\b((\S+) (تومان|تومن|درصد|واحد|ریال) ((\S+) ){0,3}(مثبت|منفی|رشد|سود|بالا|پایین))\b",# پنجاه درصد رشد
                                  r"\b((واگذاری) ((\S+) ){0,3}(سهام|سهم))\b",# واگذاری 5 درصد از سهام
                                  r"\b((ضرر|سود|اصلاح|اطلاعیه|حقیقی|حقوقی|افزایش سرمایه|تقسیم سود|دامنه نوسان|نوسان شدید|سهم رانتی))\b",
                                  r"((محدوده رشد|برگشت|رشد|صف خرید|صف فروش|نوسان|ریزش|بالا|صعود|نزول|برجام|روند صعودی|روند نزولی|کف سازی|تثبیت))"
                                  ],
                        'گزارش': [r"\bگزارش (\w+)\b"]

                        }

        pass

    def match(self,inp):
        matches = []
        for event in self.pattern:
            for pattern in self.pattern[event]:
                for matched in re.finditer(pattern, inp):
                    matches.append([matched,event])
        return matches

    def run(self,text):
        text = text.replace("\u200C", " ")

        matches = []
        for matched in (self.match(text)):
            #print(matched[0],'\n',matched[1])
            type = matched[1]
            span = [x+1 for x in matched[0].span()]
            marker = matched[0].group(1)


            matches.append({'type':type,'marker':marker,'span':span})

        if len(matches) > 0:
            print(*matches, sep='\n')

        pass

# i = input()
j = 'برکت همین افشای ب باعث شد سهم سه درصد مثبت شود. بخاطر همین میگم پیگیر باشید. گزارش فعالیت ماهانه تقسیم سود ضرر اطلاعیه سهم رانتی است.'
k = 'طبق قوانین امواج که فیبو زدم باید منتظر یه اصلاح باشیم مسیر 2 سبز رنگ و بعد یه حرکت رو به بالا...نزولی'

e = Events()
e.run(k)
print("\nreading from input file:")
with open('input_example', encoding="utf8") as f:
    lines = f.readlines()
    for line in lines:
        e.run(line)

