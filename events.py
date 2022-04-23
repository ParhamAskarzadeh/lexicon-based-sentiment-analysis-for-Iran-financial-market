import re

class Events(object):
    def __init__(self):
        self.pattern = {'واقعه': [r"\b((افشا|افشای) (الف|ب))\b", # افشای الف
                                  r"\b(((\S+) ){1,2}(تومان|تومن|درصد|واحد|ریال) ((\S+) ){0,2}(مثبت|منفی|رشد|سود|افزایش|کاهش))\b",# پنجاه درصد رشد
                                  r"\b((مثبت|منفی|رشد|سود|افزایش|کاهش) ((\S+) ){0,5}(درصدی|واحدی|درصد|واحد))\b",# رشد 3 درصدی
                                  r"\b((حقیقی|حقوقی|حقیقی ها|حقوقی ها) ((\S+) ){0,3}(ورود|وارد|خروج|خارج|تزریق) (\S+))\b",  #حقیقی ها به بازار پول تزریق کردند
                                  r"\b((ورود|وارد|خروج|خارج|تزریق) ((\w+) ){0,2}(حقیقی|حقوقی))\b",  # ورود پول حقیقی
                                  r"\b((به|از) ((\S+) ){0,7}(عبور|رسید))\b",
                                  r"\b((واگذاری) ((\S+) ){0,3}(سهام|سهم))\b",# واگذاری 5 درصد از سهام
                                  r"\b((اصلاح|اطلاعیه|افزایش سرمایه|تقسیم سود|دامنه نوسان|نوسان شدید|سهم رانتی|سبزپوش))\b",
                                  r"((روند مثبت|محدوده رشد|برگشت|صف خرید|صف فروش|نوسان|ریزش|صعود|نزول|روند صعودی|روند نزولی|کف سازی|تثبیت))"
                                  ],
                        'گزارش': [r"\bگزارش (\w+ \w+)\b"]

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
j = 'برکت همین افشای ب باعث شد سهم سه درصد مثبت شود. بخاطر همین میگم پیگیر باشید. جریان آغاز معاملات فزر با ۲.۱۵ واحد تاثیر مثبت بر روند صعودی بازار فرابورس اثر گذار بود.'
k = 'طبق قوانین امواج که فیبو زدم باید منتظر یه اصلاح باشیم مسیر 2 سبز رنگ و بعد یه حرکت رو به بالا...نزولی'

e = Events()
e.run(j)
print("\nreading from input file:")
with open('input_example', encoding="utf8") as f:
    lines = f.readlines()
    for i,line in enumerate(lines):
        if i > -1:
            print(i+1)
            e.run(line)

