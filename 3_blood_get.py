import mysql.connector
import datetime


class BloodDonorManager():
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sinan@2004",
            database="blood_db"
        )
        print("connected successfully")

    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()
            if not kwargs.get("blood_group"):
                kwargs["blood_group"] = "A+"
            query = ("insert into donor(name,blood_group,phone,city,last_donation) values( %s,%s,%s,%s,%s)")
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connection.commit()
            print("donor added successfully")
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from donor"
            self.cursor.execute(query)
            record = self.cursor.fetchall()
            for i in record:
                print(i)
        except Exception as e:
            print(e)

    def retrieve(self, id=None):
        try:
            record = self.get_object(id=id)
            if record == None:
                print("donor not fount...")
            print(record)
        except Exception as e:
            print(e)

    def delete(self, id=None):
        try:
            record = self.get_object(id=id)
            values = (id,)
            if record != None:
                query = "delete from donor where id = %s"
                self.cursor.execute(query, values)
                self.connection.commit()
                print("donor delete successfully...")
            else:
                print("donor not found...")
        except Exception as e:
            print(e)

    def get_object(self, id=None):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from donor where id = %s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            return None


donor_instance = BloodDonorManager()
donor_instance.post(name="ravi", blood_group="", mobile="9887900777", city="kochi",
                    last_donation=datetime.datetime.today())
donor_instance.get()
# donor_instance.retrieve(7)
# donor_instance.delete(6)
# print("after deleting a donor____ ")
# donor_instance.get()