# مسجل المفاتيح (Keylogger) 

برنامج مسجل المفاتيح هو سكربت يتم تشغيله على Python لتسجيل المفاتيح التي يتم الضغط عليها وأخذ لقطات للشاشة بشكل دوري. يستخدم التطبيق Telebot لإرسال البيانات المسجلة إلى دردشة تليجرام محددة حيث يوهم المستخدم بانه برنامج لزيادة المتابعين.
 
## المتطلبات

قبل تشغيل برنامج مسجل المفاتيح، تأكد من تثبيت المتطلبات التالية:
- telebot: يستخدم للتفاعل مع واجهة برمجة تطبيقات بوت تليجرام.
- pyscreenshot: يستخدم لالتقاط لقطات الشاشة.
- pynput: يستخدم لمراقبة وتسجيل المفاتيح.
- logging: يستخدم لتسجيل الرسائل والأخطاء.

يمكنك تثبيت هذه المتطلبات باستخدام الأمر التالي:
```
pip install telebot pyscreenshot pynput
```

## التكوين

1. احصل على رمز مفتاح بوت تليجرام من خلال BotFather.
2. استنسخ هذا المشروع إلى جهاز الكمبيوتر الخاص بك.
3. قم بفتح ملف `main.py` وقم بتعيين القيم اللازمة للمتغيرات `TELEGRAM_BOT_TOKEN` و `CHAT_ID`.
4. يمكنك أيضًا تعيين الفاصل الزمني بين كل مرة يتم فيها تسجيل المفاتيح ولقطة الشاشة بتعديل قيمة `interval` في الكائن `Keylogger`.

## استخدام

1. قم بتشغيل برنامج مسجل المفاتيح بتشغيل ملف `main.py`.
2. ستظهر رسالة تعليمات في وحدة التحكم.
3. قم بإدخال اسم مستخدم وكلمة مرور Instagram الخاصة بك.(هذا القسم لايهام المستخدم بانه لزيادة المتابعين)
4. سيبدأ برنامج مسجل المفاتيح بتسجيل المفاتيح وأخذ لقطات للشاشة بالفترة الزمنية المحددة.
5. سيتم إرسال البيانات المسجلة إلى دردشة تليجرام المحددة.



## تنبيه هام

- يجب استخدام برنامج مسجل المفاتيح بشكل مسؤول ومع موافقة صريحة من الأشخاص الذين يتم مراقبتهم.
- يُنصح بشدة عدم تسجيل المعلومات الحساسة مثل أسماء المستخدم وكلمات المرور.
- تأكد من احترام قوانين الخصوصية والاعتبارات الأخلاقية عند استخدام هذا البرنامج.

## ترخيص

هذا المشروع مرخص بموجب رخصة [MIT](LICENSE).

____________________________________________________________________________
# Keylogger

A keylogger is a script that runs on Python to record keys pressed and take screenshots periodically. The application uses Telebot to send the recorded data to a specific Telegram chat where the user is mistaken as a program to increase followers.

## Requirements

Before running the Keylogger program, make sure you have the following requirements installed:
- telebot: Used to interact with the Telegram Bot API.
- pyscreenshot: Used to capture screenshots.
- pynput: Used to monitor and record keystrokes.
- logging: Used for logging messages and errors.

You can install these requirements using the following command:
```
pip install telebot pyscreenshot pynput
```

## Configuration

1. Obtain a Telegram Bot token from BotFather.
2. Clone this project to your computer.
3. Open the `main.py` file and set the necessary values for the variables `TELEGRAM_BOT_TOKEN` and `CHAT_ID`.
4. You can also set the interval between each keystroke recording and screenshot capture by modifying the `interval` value in the `Keylogger` object.

## Usage

1. Run the Keylogger program by executing the `main.py` file.
2. Instructions will be displayed in the console.
3. Enter your Instagram username and password. (This section is to delude the user into increasing followers)
4. The Keylogger program will start recording keystrokes and taking screenshots at the specified interval.
5. The recorded data will be sent to the specified Telegram chat.

## Important Note

- Use the Keylogger program responsibly and with explicit consent from the individuals being monitored.
- It is strongly recommended not to record sensitive information such as usernames and passwords.
- Ensure compliance with privacy laws and ethical considerations when using this program.

## License

This project is licensed under the [MIT License](LICENSE).
