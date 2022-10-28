import pygsheets
from datetime import date

client = pygsheets.authorize(service_account_file="students-366915-3be3d74e97e3.json")
sh = client.open('data')
wks = sh.sheet1
worksheet = sh.worksheet('title', 'page 1')


def writing(id: int, date_=None):
    list = worksheet.find(str(id))[0]
    a = str(list).split()[1][1:]
    if date_ is not None:
        list1 = worksheet.find(str(date_))
        if not list1:
            raise ModuleNotFoundError("Siz kiritgan sana hali yo'q")
        b = str(list1[0]).split()
        worksheet.update_value(f"{b[1][:1]}{a}", " +")
        return 'Success'
    else:
        today = date.today()
        d1 = today.strftime("%d.%m.%Y")
        list2 = worksheet.find(str(d1))
        b1 = str(list2[0]).split()
        worksheet.update_value(f"{b1[1][:1]}{a}", " +")
        return "Success"


print(writing(123458, '31.10.2022'))
