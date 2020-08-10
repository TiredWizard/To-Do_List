from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
import datetime
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.date.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

while True:
    print("""1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit""")

    choice = int(input())
    if choice == 1:
        print()
        print("Today:")
        today = datetime.datetime.today().date()
        rows = session.query(Table).filter(Table.deadline == today).all()
        if len(rows) == 0:
            print("Nothing to do!")
        else:
            for row in rows:
                print("{}. {}".format(row.id, row.task))

            print()
    elif choice == 2:
        print()
        start_date = datetime.datetime.today().date()
        for n in range(7):
            single_date = start_date + datetime.timedelta(days=n)
            print(single_date.strftime("%A"), single_date.strftime("%d"), single_date.strftime("%b") + ":")
            rows = session.query(Table).filter(single_date == Table.deadline).all()
            if len(rows) == 0:
                print("Nothing to do!")
            else:
                for row in rows:
                    print("{}. {}".format(row.id, row.task))
            print()

    elif choice == 3:
        print()
        print("All tasks:")
        rows = session.query(Table).order_by(Table.deadline).all()
        if len(rows) == 0:
            print("Nothing to do!")
        else:
            for row in rows:
                new_d = datetime.datetime.strptime(str(row.deadline), '%Y-%m-%d')
                new_ds = new_d.strftime("%d")+" "+new_d.strftime("%b")
                print("{}. {}. {}".format(row.id, row.task, new_ds))

            print()
    elif choice == 4:
        print()
        print("Missed tasks:")
        rows = session.query(Table).order_by(Table.deadline).filter(Table.deadline < datetime.datetime.today().date()).all()
        if len(rows) == 0:
            print("Nothing is missed!")
        else:
            for row in rows:
                print("{}. {}".format(row.id, row.task))
        print()
    elif choice == 5:
        print()
        print("Enter Task")
        new_task = input()
        print("Enter deadline")
        new_deadline = input()
        new_deadline_date = datetime.datetime.strptime(new_deadline, '%Y-%m-%d')
        new_row = Table(task=new_task, deadline=new_deadline_date)
        session.add(new_row)
        session.commit()
        print()
    elif choice == 6:
        print()
        print("Choose the number of the task you want to delete:")

        rows = session.query(Table).order_by(Table.deadline).all()
        if len(rows) == 0:
            print("Nothing to do!")
        else:
            for row in rows:
                new_d = datetime.datetime.strptime(str(row.deadline), '%Y-%m-%d')
                new_ds = new_d.strftime("%d")+" "+new_d.strftime("%b")
                print("{}. {}. {}".format(row.id, row.task, new_ds))

            print()

        id_todelete = input()
        session.query(Table).filter(Table.id == id_todelete).delete()
        session.commit()
        print()
    elif choice == 0:
        print()
        print("Bye!")
        break
