import smtplib
import pandas as pd
import io

my_email = "tanhduhieu2k@gmail.com"
password = "neaadonaxpgiusbn"

# Mở file quotes.txt
with io.open("Birthday Wisher (Day 32) start/quotes.txt", "r", encoding="utf-8") as f:
    # Đọc nội dung file
    original_text = f.read()

def sendMail(my_email, password, SUBJECT, TEXT, to_email):
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login(my_email, password)
    message = f'Subject: {SUBJECT}\n\n{TEXT}'
    connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=message.encode("utf-8"))
    connection.close()

file_excel = 'Birthday Wisher (Day 32) start/test.xlsx'
list_header = ["Họ và tên", "Email"]
list_headerVar = ["name", 'email']
list_sheetName = ["TV"]

def CrawlRowExcel(file_excel, list_header, sheet_name):
    df = pd.read_excel(file_excel, sheet_name=sheet_name)
    SUBJECT = "Đơn xin dừng hoạt động"
    
    for index, row in df.iterrows():
        user = {}
        for i in range(len(list_header)):
            data = row[list_header[i]]
            if pd.isna(data):  # Kiểm tra dữ liệu lỗi
                return
            if list_header[i] == "Họ và tên":
                user[list_headerVar[i]] = ' '.join(word.capitalize() for word in data.split())
            else:
                user[list_headerVar[i]] = data.lower()
        
        # Tạo lại văn bản email từ template
        TEXT = original_text  # Lấy lại nội dung gốc từ file
        for key in user.keys():
            if key == 'name':
                TEXT = TEXT.replace('name', user[key])  # Thay thế 'name' bằng tên người dùng

        sendMail(my_email=my_email, password=password, SUBJECT=SUBJECT, TEXT=TEXT, to_email=user['email'])
        print(f"Send success to {user['name']} ({user['email']})")

def main():
    for sheetName in list_sheetName:
        CrawlRowExcel(file_excel=file_excel, list_header=list_header, sheet_name=sheetName)

if __name__ == '__main__':
    main()
