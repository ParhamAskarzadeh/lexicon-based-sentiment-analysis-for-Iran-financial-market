import re


saham = {'name': {'کترام', 'ودی', 'فاذر', 'شراز', 'چکاپا', 'آپ', 'لابسا', 'کاما', 'پکویر', 'ثبهساز', 'کلر', 'پترول',
                 'ورنا', 'لکما', 'بترانس', 'کسرا', 'خفنر', 'ذوب', 'خدیزل', 'شستا', 'شاراک', 'فولاد', 'شپترو', 'وشهر',
                 'قاسم', 'پالایش', 'خساپا', 'پاسا', 'فسبزوار', 'وبرق', 'غزر', 'سفار', 'نوری', 'زگلدشت', 'ولساپا',
                 'وغدیر', 'سپید', 'وآیند', 'بکاب', 'وسالت', 'کیسون', 'تپکو', 'بجهرم', 'فروی', 'ختراک', 'همراه', 'غبشهر',
                 'غنوش', 'کیمیاتک', 'فلوله', 'تفارس-پذیره', 'آرام', 'خفولا', 'بالاس', 'غدشت', 'ثشاهد', 'شاخص بورس',
                 'کتوکا', 'کفپارس', 'زماهان', 'شفن', 'دی', 'خپارس', 'غصینو', 'مادیرا', 'زاگرس', 'قچار', 'کرمان', 'بورس',
                 'شکلر', 'شپلی', 'خکرمان', 'کدما', 'طلا', 'خنصیر', 'وهامونح', 'شلرد', 'برکت', 'کمند', 'وسین', 'سجام',
                 'مفاخر', 'شوینده', 'خکار', 'شیشه01ن', 'افق', 'شپدیس', 'خاور', 'تمحرکه', 'کالا', 'صبا', 'سیمرغ', 'سمگا',
                 'زگلدشتح', 'خکمک', 'فزرین', 'فنفت', 'رتاپ', 'دارا یکم', 'خگستر', 'وآذر', 'ساذری', 'خودکفا', 'غالبر',
                 'بزاگرس', 'غشهداب', 'وساپا', 'قنیشا', 'کگاز', 'فولای', 'وپست', 'خودرو', 'شگویا', 'خلنت', 'ثاخت',
                 'شپنا', 'شتران', 'غگرجی', 'وبملت', 'سیتا', 'گشان', 'وگردش', 'وسدید'},

        'title': {'ایران‌ خودرو', 'کویر تایر', 'گروه سرمایه گذاری میراث فرهنگی', 'پارس فولاد سبزوار',
                  'توسعه وعمران استان کرمان', 'قاسم ایران', 'شرکت ارتباطات سیار ایران',
                  'لوله‌وماشین‌سازی‌ایران‌', 'پتروشیمی زاگرس', 'مجتمع تولید گوشت مرغ ماهان',
                  'پتروشیمی پردیس', 'بورس اوراق بهادار تهران', 'بانک قرض الحسنه رسالت',
                  'سرمایه‌گذاری‌ رنا', 'صنعتی‌ بهشهر', 'آریان کیمیا تک',
                  'سرمایه‌گذاری‌توسعه‌آذربایجان‌', 'سرامیک‌های‌صنعتی‌اردکان‌',
                  'سرمایه‌گذاری‌ غدیر', 'توسعه مولد نیروگاهی جهرم', 'بانک آینده',
                  'خدمات فنی فولاد یزد', 'کارکنان صنعت برق زنجان وقزوی', 'بانک ملت', 'فروشگاههای زنجیره ای افق کوروش',
                  'سرمایه گذاری تامین اجتماعی', 'کشت و دام گلدشت نمونه اصفهان', 'کود شیمیایی اوره لردگان',
                  'بانک گردشگری', 'ایران‌یاساتایرورابر', 'لیزینگ رایان‌ سایپا', 'آبسال‌',
                  'سرمایه گذاری سیمان تامین', 'ماشین سازی نیرو محرکه', 'پارس‌ خودرو', 'گواهی سپرده کالایی شیشه',
                  'مدیریت صنعت شوینده ت.ص.بهشهر', 'پالایش نفت شیراز', 'تجارت الکترونیک پارسیان',
                  'مهندسی‌نصیرماشین‌', 'صندوق س. با درآمد ثابت کمند', 'دشت‌ مرغاب‌',
                  'مهندسی ساختمان تاسیسات راه آهن', 'شرکت کیسون', 'گروه‌صنعتی‌سدید',
                  'گسترش‌ سرمایه‌گذاری‌ایران‌خودرو', 'صندوق پالایشی یکم-سهام', 'شاخص بورس',
                  'ایران خودرو دیزل', 'پالایش نفت اصفهان', 'فراوردههای غذایی وقند چهارمحال', 'صنایع‌ آذرآب‌',
                  'آذریت‌', 'فنرسازی‌خاور', 'پلی اکریل ایران', 'بین‌المللی‌توسعه‌ساختمان',
                  'شیشه‌ و گاز', 'صنایع فولاد آلیاژی یزد', 'معدنی‌ دماوند', 'آسان پرداخت پرشین',
                  'کمک‌فنرایندامین‌', 'سرمایه گذاری صبا تامین', 'تولیدتجهیزات‌سنگین‌هپکو',
                  'سپید ماکیان', 'صنایع تجهیزات نفت', 'صنعتی مینو', 'پتروشیمی نوری', 'صندوق س.پشتوانه طلای لوتوس',
                  'بهساز کاشانه تهران', 'ذوب روی اصفهان', 'کلر پارس', 'اقتصادی و خودکفایی آزادگان', 'پتروشیمی آبادان',
                  'صنعتی زر ماکارون', 'لنت‌ ترمزایران‌', 'بیمه دی', 'بورس کالای ایران',
                  'تولیدی و خدمات صنایع نسوز توکا', 'پتروشیمی خلیج فارس',
                  'ریخته‌گری‌ تراکتورسازی‌ ایران‌', 'سایپا', 'زرین معدن آسیا',
                  'سیمان‌فارس‌', 'سیمرغ', 'سرمایه گذاری هامون صبا', 'باما', 'پالایش نفت تهران',
                  'فولاد مبارکه اصفهان', 'لبنیات‌کالبر', 'صنایع مادیران', 'توسعه بین المللی پدیده شاندیز',
                  'نوش‌مازندران‌', 'توسعه فناوری اطلاعات خوارزمی', 'ذوب آهن اصفهان',
                  'کشت و صنعت شهداب ناب خراسان', 'پتروشیمی شازند', 'سرمایه‌گذاری‌ سایپا',
                  'تامین سرمایه خلیج فارس-پذیره', 'کارخانجات‌مخابراتی‌ایران‌', 'مجتمع سیمان غرب آسیا',
                  'پتروشیمی تندگویان', 'فرآورده‌های‌ نسوز پارس‌', 'گروه اقتصادی کرمان خودرو', 'بانک شهر',
                  'صندوق واسطه گری مالی یکم', 'بیسکویت‌ گرجی‌', 'تولیدی‌ کاشی‌ تکسرام‌',
                  'بانک دی', 'پتروشیمی فناوران', 'بهمن دیزل', 'بیمه سینا', 'گروه صنایع کاغذ پارس', 'نیروکلر',
                  'قند نیشابور', 'گروه دارویی برکت', 'پست بانک ایران', 'صنایع‌جوشکاب‌یزد',
                  'سرمایه‌ گذاری‌ شاهد', 'صندوق س شاخصی آرام مفید', 'ایرکا پارت صنعت', 'ایران‌ ترانسفو',
                  'نیروگاه زاگرس کوثر'}}

a = ["ضرر", "سود", "اطلاعیه", "حقیق", "حقوق", "افزایش", "سرمایه", "تقسیم", "سود", "دامنه", "نوسان", "شدید", "سهم", "رانت"]

def run(txt):
    javab = []

    for i in saham['name']:
        mydict = {}
        x=re.search(i, txt)
        if x != None:
            mydict['type'] = "نماد"
            mydict['marker'] = i
            mydict['span'] = re.findall("\([0-9]+,\s[0-9]+\)", str(x))[0]
            javab.append(mydict)

    for i in saham['title']:
        mydict = {}
        x = re.search(i, txt)
        if x != None:
            mydict['type'] = "شرکت"
            mydict['marker'] = i
            mydict['span'] = re.findall("\([0-9]+,\s[0-9]+\)", str(x))[0]

    for i in a:
        mydict = {}
        x = re.search(i, txt)
        if x != None:
            mydict['type'] = "واقعه"
            mydict['marker'] = i
            mydict['span'] = re.findall("\([0-9]+,\s[0-9]+\)", str(x))[0]

    print(javab)


run("text")

if __name__ == '__main__':
    print('hell')