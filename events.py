import re

class Events(object):
    def __init__(self):
        self.addad = r"\b((.+) (درصد))\b"
        self.pattern = {'واقعه': [r"\b((افشا|افشای) (الف|ب))\b",
                                  r"\b((\S+) (درصد) ((\S+) ){0,3}(مثبت|منفی))\b"
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
j = 'برکت همین افشای ب باعث شد سهم سه درصد مثبت شود. بخاطر همین میگم پیگیر باشید. گزارش فعالیت ماهانه '

e = Events()
e.run(j)
print("\nreading from input file:")
with open('input_example', encoding="utf8") as f:
    lines = f.readlines()
    for line in lines:
        e.run(line)

