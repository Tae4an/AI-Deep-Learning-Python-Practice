import sqlite3

conn = sqlite3.connect("practice/06_27/database/my_db.db")

cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS telno (name TEXT, telno TEXT, addr TEXT)' )

cur.execute('CREATE INDEX IF NOT EXISTS telno_idx ON telno (name)')



def insert_data(name, telno, addr):
    cur.execute('INSERT INTO telno (name, telno, addr)  VALUES(?,?,?)',
                (name,telno,addr))
    conn.commit()


def update_data(name, telno, addr):
    cur.execute("UPDATE phonebook SET telno=?, addr=? WHERE name=? ",(telno, addr, name))
    conn.commit()


def delete_data(name):
    cur.execute("DELETE FROM phonebook WHERE name=?", (name))
    conn.commit()


def search_data(name):
    cur.execute("SELECT * FROM phonebook WHERE name=?", (name))
    rows = cur.fetchall()
    for row in rows:
        print(row)


def display_all():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def main():
    while True:
        print("1: 데이터 입력")
        print("2: 데이터 수정")
        print("3: 데이터 삭제")
        print("4: 데이터 검색")
        print("5: 데이터 보기")
        print("6: 종료")
        choice = input("선택하세요 : ")
        match(choice):
            case '1':
                name = input("입력할 성명: ")
                telno = input("입력할 전화번호: ")
                addr = input("입력할 주소: ")
                insert_data(name, telno, addr)
            case '2':
                name = input("수정할 성명 : ")
                telno = input("수정할 전화번호: ")
                addr = input("수정할 주소: ")
                update_data(name, telno, addr)
            case '3':
                name = input("삭제할 이름을 입력하세요: ")
                delete_data(name)
            case '4':
                name = input("검색할 이름을 입력하세요: ")
                search_data(name)
            case  '5':
                display_all()
            case '6':
                break
            case _:
                print("1~6까지의 숫자를 입력하세요")

if __name__ == '__main__':
    main()

conn.close()