import csv
# References
'''
1-https://en.wikipedia.org/wiki/Python_(programming_language)
2-https://www.protechtraining.com/mastering-web-development-using-html5-css3-and-jquery-pt9211#:~:text=Mastering%20Web%20Development%20using%20HTML5%2C%20CSS3%2C%20and%20jQuery%20is%20an,the%20entire%20spectrum%20of%20user
3-https://en.wikipedia.org/wiki/Node.js
4-https://en.wikipedia.org/wiki/React_(web_framework)
5-https://en.wikipedia.org/wiki/Java_(programming_language)
'''
# Academy Parent Class
class Academy:
    course = ""

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    # Getter Methods
    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def display(self):
        return f"Student Info:\nStudent Name: {self.name}\tEmail: {self.email}\tPhone: {self.phone}\t{self.course}"


class Python_Course(Academy):
    course = "Python Programming"

    def __init__(self, name, email, phone, amount):
        super(Python_Course, self).__init__(name, email, phone)
        self.amount = amount
        self.completed = False

    # Setter Methods
    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def set_phone(self, phone):
        self.phone = phone

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def set_status(self, status):
        self.completed = status

    def get_phone(self):
        return self.phone

    def get_amount(self):
        if self.amount == 10000:
            return f"Receipt:\nPaid: {self.amount}\n10000 left to be paid."

        elif self.amount == 20000:
            return f"Receipt:\nPaid: {self.amount}"
        else:
            return "Receipt:\n Payment: Not Done"

    def pay_installment(self, amount):
        if self.amount == 20000:
            return f"Payment Dues Already Cleared!\n{Python_Course.get_amount(self)}"
        elif self.amount == 10000:
            if amount >= 10000:
                returnMoney = amount - 10000
                self.amount = 20000
                return f"{Python_Course.get_amount(self)}\nHere is your Refund:{returnMoney}\nHave A Good Day!"

            elif amount < 10000:
                return f"Opps!,Not Enough Money to Pay for Second Installment,\n{Python_Course.get_amount(self)}\nSorry"
        else:
            returnMoney = amount - 10000
            self.amount = 10000
            return f"{Python_Course.get_amount(self)}\nHere is your Refund:{returnMoney}\nHave A Good Day!"

    def get_status(self):
        return self.completed

    def full_pay(self, amount):
        if self.amount != 20000:
            if amount >= 20000:
                returnMoney = amount - 20000
                self.amount = 20000
                return f"{Python_Course.get_amount(self)}\nHere is your Refund:{returnMoney}\nHave A Good Day!"
            elif amount > 10000 and amount < 20000:
                print(
                    "Not Adequate Money For Full Installment\n Note Full Installment:20000\nYou can Still Pay Half Installment which is 10000")
                ask = input("Do You wish to pay half installment(Yes/No)")
                ask = ask.upper()
                if ask == "YES":
                    returnMoney = amount - 10000
                    self.amount = 10000
                    return f"{Python_Course.get_amount(self)}\nHere is your Refund:{returnMoney}\nHave A Good Day!"
                else:
                    return f"Have A Good Day!"
            else:
                return f"Not Adequate Money For Full Installment nor Half Installment\n Note Full Installment:20000 and Half Installment:10000"
        else:
            return f"Already Paid \n{Python_Course.get_amount(self)}"

    def withdraw(self):
        if Python_Course.get_status(self) and self.amount == 20000:
            self.amount = 0
            return f"Congratulation on Completing Course Money Refunded!\nRecipt: 20000"
        elif not Python_Course.get_amount(self) and self.amount == 20000:
            self.amount = 0
            return f"Course Money Refunded!\nRecipt: 20000"
        elif not Python_Course.get_status(self) and self.amount == 10000:
            return f"Course Money Refunded!\nRecipt: 10000"
        else:
            return "Already Refunded!"

    def display(self):
        return f"{super().display()}\n-------\n{Python_Course.get_amount(self)}"


class HTML_CSS(Academy):
    course = "Web-Development with HTML&CSS"

    def __init__(self, name, email, phone, amount):
        super(HTML_CSS, self).__init__(name, email, phone)
        self.amount = amount
        self.completed = False

    # Setter Methods
    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def set_phone(self, phone):
        self.phone = phone

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def get_amount(self):
        if self.amount == 10000:
            return f"Receipt:\nPaid: {self.amount}\n10000 left to be paid."

        elif self.amount == 20000:
            return f"Receipt:\nPaid: {self.amount}"
        else:
            return "Receipt:\n Payment: Not Done"

    def set_status(self, status):
        self.completed = status

    def get_status(self):
        return self.completed

    def pay_installment(self, amount):
        if self.amount == 20000:
            return f"Payment Dues Already Cleared!\n{HTML_CSS.get_amount(self)}"
        elif self.amount == 10000:
            if amount >= 10000:
                returnMoney = amount - 10000
                self.amount = 20000
                return f"{HTML_CSS.get_amount(self)}\nHere is your Refund:{returnMoney}\nHave A Good Day!"

            elif amount < 10000:
                return f"Opps!,Not Enough Money to Pay for Second Installment,\n{HTML_CSS.get_amount(self)}\nSorry"
        else:
            returnMoney = amount - 10000
            self.amount = 10000
            return f"{HTML_CSS.get_amount(self)}\nHere is your Refund:{returnMoney}\nHave A Good Day!"

    def full_pay(self, amount):
        if self.amount != 20000:
            if amount >= 20000:
                returnMoney = amount - 20000
                self.amount = 20000
                return f"{HTML_CSS.get_amount(self)}\nHere is your Refund:{returnMoney}\nHave A Good Day!"
            elif amount > 10000 and amount < 20000:
                print(
                    "Not Adequate Money For Full Installment\n Note Full Installment:20000\nYou can Still Pay Half Installment which is 10000")
                ask = input("Do You wish to pay half installment(Yes/No)")
                ask = ask.upper()
                if ask == "YES":
                    returnMoney = amount - 10000
                    self.amount = 10000
                    return f"{HTML_CSS.get_amount(self)}\nHere is your Refund:{returnMoney}\nHave A Good Day!"
                else:
                    return f"Have A Good Day!"
            else:
                return f"Not Adequate Money For Full Installment nor Half Installment\n Note Full Installment:20000 and Half Installment:10000"
        else:
            return f"Already Paid \n{HTML_CSS.get_amount(self)}"

    def withdraw(self):
        if HTML_CSS.get_status(self) and self.amount == 20000:
            self.amount = 0
            return f"Congratulation on Completing Course Money Refunded!\nRecipt: 20000"
        elif not HTML_CSS.get_amount(self) and self.amount == 20000:
            self.amount = 0
            return f"Course Money Refunded!\nRecipt: 20000"
        elif not HTML_CSS.get_status(self) and self.amount == 10000:
            return f"Course Money Refunded!\nRecipt: 10000"
        else:
            return "Already Refunded!"

    def display(self):
        return f"{super().display()}\n-------\n{HTML_CSS.get_amount(self)}"


class NodeJS(Academy):
    course = "NodeJS Fundamentals"

    def __init__(self, name, email, phone, amount):
        super(NodeJS, self).__init__(name, email, phone)
        self.amount = amount
        self.completed = False

    # Setter Methods
    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def set_phone(self, phone):
        self.phone = phone

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def get_amount(self):
        if self.amount == 10000:
            return f"Receipt:\nPaid: {self.amount}\n10000 left to be paid."

        elif self.amount == 20000:
            return f"Receipt:\nPaid: {self.amount}"
        else:
            return "Receipt:\n Payment: Not Done"

    def get_status(self):
        return self.completed

    def set_status(self, status):
        self.completed = status

    def pay_installment(self, amount):
        if self.amount == 20000:
            return f"Payment Dues Already Cleared!\n{NodeJS.get_amount(self)}"
        elif self.amount == 10000:
            if amount >= 10000:
                returnMoney = amount - 10000
                self.amount = 20000
                return f"{NodeJS.get_amount(self)}\nHere is your Refund:{returnMoney}\nHave A Good Day!"

            elif amount < 10000:
                return f"Opps!,Not Enough Money to Pay for Second Installment,\n{NodeJS.get_amount(self)}\nSorry"
        else:
            returnMoney = amount - 10000
            self.amount = 10000
            return f"{NodeJS.get_amount(self)}\nHere is your Refund:{returnMoney}\nHave A Good Day!"

    def full_pay(self, amount):
        if self.amount != 20000:
            if amount >= 20000:
                returnMoney = amount - 20000
                self.amount = 20000
                return f"{NodeJS.get_amount(self)}\nHere is your Refund:{returnMoney}\nHave A Good Day!"
            elif amount > 10000 and amount < 20000:
                print(
                    "Not Adequate Money For Full Installment\n Note Full Installment:20000\nYou can Still Pay Half Installment which is 10000")
                ask = input("Do You wish to pay half installment(Yes/No)")
                ask = ask.upper()
                if ask == "YES":
                    returnMoney = amount - 10000
                    self.amount = 10000
                    return f"{NodeJS.get_amount(self)}\nHere is your Refund:{returnMoney}\nHave A Good Day!"
                else:
                    return f"Have A Good Day!"
            else:
                return f"Not Adequate Money For Full Installment nor Half Installment\n Note Full Installment:20000 and Half Installment:10000"
        else:
            return f"Already Paid \n{NodeJS.get_amount(self)}"

    def withdraw(self):
        if NodeJS.get_status(self) and self.amount == 20000:
            self.amount = 0
            return f"Congratulation on Completing Course Money Refunded!\nRecipt: 20000"
        elif not NodeJS.get_amount(self) and self.amount == 20000:
            self.amount = 0
            return f"Course Money Refunded!\nRecipt: 20000"
        elif not NodeJS.get_status(self) and self.amount == 10000:
            return f"Course Money Refunded!\nRecipt: 10000"
        else:
            return "Already Refunded!"

    def display(self):
        return f"{super().display()}\n-------\n{NodeJS.get_amount(self)}"


class React(Academy):
    course = "React Fundamentals"

    def __init__(self, name, email, phone, amount):
        super(React, self).__init__(name, email, phone)
        self.amount = amount
        self.completed = False

    # Setter Methods
    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def set_phone(self, phone):
        self.phone = phone

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def get_status(self):
        return self.completed

    def set_status(self, status):
        self.completed = status

    def get_amount(self):
        if self.amount == 10000:
            return f"Receipt:\nPaid: {self.amount}\n10000 left to be paid."

        elif self.amount == 20000:
            return f"Receipt:\nPaid: {self.amount}"
        else:
            return "Receipt:\n Payment: Not Done"

    def pay_installment(self, amount):
        if self.amount == 20000:
            return f"Payment Dues Already Cleared!\n{React.get_amount(self)}"
        elif self.amount == 10000:
            if amount >= 10000:
                returnMoney = amount - 10000
                self.amount = 20000
                return f"{React.get_amount(self)}\nHere is your Refund:{returnMoney}\nHave A Good Day!"

            elif amount < 10000:
                return f"Opps!,Not Enough Money to Pay for Second Installment,\n{React.get_amount(self)}\nSorry"
        else:
            returnMoney = amount - 10000
            self.amount = 10000
            return f"{React.get_amount(self)}\nHere is your Refund:{returnMoney}\nHave A Good Day!"

    def full_pay(self, amount):
        if self.amount != 20000:
            if amount >= 20000:
                returnMoney = amount - 20000
                self.amount = 20000
                return f"{React.get_amount(self)}\nHere is your Refund:{returnMoney}\nHave A Good Day!"
            elif amount > 10000 and amount < 20000:
                print(
                    "Not Adequate Money For Full Installment\n Note Full Installment:20000\nYou can Stay Half Installment which is 10000")
                ask = input("Do You wish to pay half installment(Yes/No)")
                ask = ask.upper()
                if ask == "YES":
                    returnMoney = amount - 10000
                    self.amount = 10000
                    return f"{React.get_amount(self)}\nHere is your Refund:{returnMoney}\nHave A Good Day!"
                else:
                    return f"Have A Good Day!"
            else:
                return f"Not Adequate Money For Full Installment nor Half Installment\n Note Full Installment:20000 and Half Installment:10000"
        else:
            return f"Already Paid \n{React.get_amount(self)}"

    def withdraw(self):
        if React.get_status(self) and self.amount == 20000:
            self.amount = 0
            return f"Congratulation on Completing Course Money Refunded!\nRecipt: 20000"
        elif not React.get_amount(self) and self.amount == 20000:
            self.amount = 0
            return f"Course Money Refunded!\nRecipt: 20000"
        elif not React.get_status(self) and self.amount == 10000:
            return f"Course Money Refunded!\nRecipt: 10000"
        else:
            return "Already Refunded!"

    def display(self):
        return f"{super().display()}\n-------\n{React.get_amount(self)}"


class Java(Academy):
    course = "JAVA Programming"

    def __init__(self, name, email, phone, amount):
        super(Java, self).__init__(name, email, phone)
        self.amount = amount
        self.completed = False

    # Setter Methods
    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def set_phone(self, phone):
        self.phone = phone

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_status(self):
        return self.completed

    def set_status(self, status):
        self.completed = status

    def get_amount(self):
        if self.amount == 10000:
            return f"Receipt:\nPaid: {self.amount}\n10000 left to be paid."

        elif self.amount == 20000:
            return f"Receipt:\nPaid: {self.amount}"
        else:
            return "Receipt:\n Payment: Not Done"

    def get_phone(self):
        return self.phone

    def pay_installment(self, amount):
        if self.amount == 20000:
            return f"Payment Dues Already Cleared!\n{Java.get_amount(self)}"
        elif self.amount == 10000:
            if amount >= 10000:
                returnMoney = amount - 10000
                self.amount = 20000
                return f"{Java.get_amount(self)}\nHere is your Refund:{returnMoney}\nHave A Good Day!"

            elif amount < 10000:
                return f"Opps!,Not Enough Money to Pay for Second Installment,\n{Java.get_amount(self)}\nSorry"
        else:
            returnMoney = amount - 10000
            self.amount = 10000
            return f"{Java.get_amount(self)}\nHere is your Refund:{returnMoney}\nHave A Good Day!"

    def full_pay(self, amount):
        if self.amount != 20000:
            if amount >= 20000:
                returnMoney = amount - 20000
                self.amount = 20000
                return f"{Java.get_amount(self)}\nHere is your Refund:{returnMoney}\nHave A Good Day!"
            elif amount > 10000 and amount < 20000:
                print(
                    "Not Adequate Money For Full Installment\n Note Full Installment:20000\nYou can Still Pay Half Installment which is 10000")
                ask = input("Do You wish to pay half installment(Yes/No)")
                ask = ask.upper()
                if ask == "YES":
                    returnMoney = amount - 10000
                    self.amount = 10000
                    return f"{Java.get_amount(self)}\nHere is your Refund:{returnMoney}\nHave A Good Day!"
                else:
                    return f"Have A Good Day!"
            else:
                return f"Not Adequate Money For Full Installment nor Half Installment\n Note Full Installment:20000 and Half Installment:10000\nYou can Stay Half Installment which is 10000"
        else:
            return f"Already Paid \n{Java.get_amount(self)}"

    def withdraw(self):
        if Java.get_status(self) and self.amount == 20000:
            self.amount = 0
            return f"Congratulation on Completing Course Money Refunded!\nRecipt: 20000"
        elif not Java.get_status(self) and self.amount == 20000:
            self.amount = 0
            return f"Course Money Refunded!\nRecipt: 20000"
        elif not Java.get_status(self) and self.amount == 10000:
            return f"Course Money Refunded!\nRecipt: 10000"
        else:
            return "Already Refunded!"

    def display(self):
        return f"{super().display()}\n-------\n{Java.get_amount(self)}"


if __name__ == "__main__":
    # Details
    python_info="Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace."
    html_css_info="Mastering Web Development using HTML5, CSS3, and jQuery is an in-depth web design and development course geared for software developers who need to understand what the latest in web technologies, performance, optimization, and responsive design practices that are central to targeting the entire spectrum of user platforms and browsers. This comprehensive course provides a balanced mixture of theory and practical labs designed to take students through HTML5, CSS3 and related technologies. "
    node_info="Node.js is an open-source, cross-platform, JavaScript runtime environment that executes JavaScript code outside a web browser"
    react_info="React is an open-source JavaScript library for building user interfaces. It is maintained by Facebook and a community of individual developers and companies. React can be used as a base in the development of single-page or mobile applications. "
    java_info="Java is a general-purpose programming language that is class-based, object-oriented, and designed to have as few implementation dependencies as possible"

    with open("./Academy/welcome.txt","r",encoding='utf-8') as hello:
        for char in hello:
            print(char)
        hello.close()
    try:
        option=int(input())
    except ValueError:
        print("Please Input Only Integer Values as per ID")
    else:
        if option==1:
            try:
                with open("Academy/courses.txt", "r", encoding='utf-8') as course:
                    for char in course:
                        print(char)
                    course.close()
                id_ask=int(input("Please Select Course ID for details about the course:\n"))
            except ValueError:
                print("Please Input Only Integer Values as per ID")
            else:
                if id_ask==1:
                    print(python_info)
                    join=input("Do you want to get enrolled?(Y/N)")
                    join=join.upper()
                    if join=="Y":
                        try:
                            name=input("What is Your Name?")
                            email=input("What is Your Email?")
                            phone=int(input("What is Your Phone Number?"))
                            amountS=int(input("Payment"))
                        except ValueError:
                            print("Please Enter Data Correctly")
                        else:
                            if amountS<10000:
                                obj=Python_Course(name,email,phone,amountS)
                                print(obj.full_pay(amountS))
                            elif amountS>10000:
                                obj=Python_Course(name,email,phone,amountS)
                                print(obj.full_pay(amountS))
                                file=open("./Academy/students_info.csv",newline='')
                                try:
                                    last_line=file.readlines()[-1]
                                except:
                                    n=1
                                else:
                                    n=int(last_line[0])+1
                                file.close()
                                with open("./Academy/students_info.csv",'a') as file:
                                    fileWrite=csv.writer(file)
                                    fileWrite.writerow([n,name,email,phone,amountS,"False"])


                    else:
                        print("Thank You!,Have a Good Day.")

                elif id_ask==2:
                    print(html_css_info)
                    join=input("Do you want to get enrolled?(Y/N)")
                    join=join.upper()
                elif id_ask==3:
                    print(node_info)
                    join=input("Do you want to get enrolled?(Y/N)")
                    join=join.upper()
                elif id_ask==4:
                    print(react_info)
                    join=input("Do you want to get enrolled?(Y/N)")
                    join=join.upper()
                elif id_ask==5:
                    print(java_info)
                    join=input("Do you want to get enrolled?(Y/N)")
                    join=join.upper()
                else:
                    print("Sorry No Course ID exists")
        elif option==2:
            pass
        elif option==3:
            file=open("./Academy/students_info.csv",newline='')
            reader=csv.reader(file)
            header=next(reader) #This is header or column of our file
            data=[row for row in reader]  #remaining file
            print(header)
            print(data[0][5])
        elif option==4:
            pass
        else:
            print("No Certain Option Found")



