from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session, declarative_base

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'my_db.db')}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Phonebook(Base):
    __tablename__ = "phonebook1"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    telno = Column(String, index=True)
    addr = Column(String, index=True)
    def __str__(self):
	    return f"<Phone(name='{self.name}', telno='{self.telno}', addr='{self.addr}')>"

Base.metadata.create_all(bind=engine)

def insert_data(db: Session, name: str, telno: str, addr: str):
    phonebook_entry = Phonebook(name=name, telno=telno, addr=addr)
    db.add(phonebook_entry)
    db.commit()
    db.refresh(phonebook_entry)
    return phonebook_entry

def update_data(db: Session, name: str, telno: str, addr: str):
    phonebook_entry = db.query(Phonebook).filter(Phonebook.name == name).first()
    if phonebook_entry:
        phonebook_entry.telno = telno
        phonebook_entry.addr = addr
        db.commit()
        db.refresh(phonebook_entry)
    return phonebook_entry

def delete_data(db: Session, name: str):
    phonebook_entry = db.query(Phonebook).filter(Phonebook.name == name).first()
    if phonebook_entry:
        db.delete(phonebook_entry)
        db.commit()
        
def search_data(db: Session, name: str):
    phonebook_entries = db.query(Phonebook).filter(Phonebook.name == name).all()
    for entry in phonebook_entries:
        print(entry)
        
def display_all(db: Session):
    phonebook_entries = db.query(Phonebook).all()
    for entry in phonebook_entries:
        print(entry)
                                        
def main():
    db = SessionLocal()
    try:
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
                    insert_data(db, name, telno, addr)
                case '2':
                    name = input("수정할 성명 : ")
                    telno = input("수정할 전화번호: ")
                    addr = input("수정할 주소: ")
                    update_data(db, name, telno, addr)
                case '3':
                    name = input("삭제할 이름을 입력하세요: ")
                    delete_data(db, name)
                case '4':
                    name = input("검색할 이름을 입력하세요: ")
                    search_data(db, name)
                case  '5':
                    display_all(db)
                case '6':
                    break
                case _:
                    print("1~6까지의 숫자를 입력하세요")
    finally:
        db.close()


if __name__ == '__main__':
    main()