import mysql.connector
import  datetime



class BloodDonorManager():
    def __init__(self):
        self.connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="MuHamdammed@77",
            database="blood_db"
        )
        print("connected successfully")

    def post(self,**kwargs):
       try:
           self.cursor = self.connection.cursor()
           if not kwargs.get("blood_group"):
               kwargs["blood_group"]="A+"
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
        except Exception as e :
            print(e)
    def retrieve(self,id=None):
        try:
            record=self.get_object(id=id)
            if record==None:
                print("donor not fount...")
            print(record)
        except Exception as e:
            print(e)
    def delete(self,id=None):
        try:
            record=self.get_object(id=id)
            values=(id,)
            if record != None:
                query="delete from donor where id = %s"
                self.cursor.execute(query,values)
                self.connection.commit()
                print("donor delete successfully...")
            else:
                print("donor not found...")
        except Exception as e:
            print(e)
    def get_object(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from donor where id = %s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            return record
        except Exception as e:
            return  None
    def put(self,id=None,**kwargs):
     try:
        record=self.get_object(id=id) #check
        if record != None :
            self.cursor=self.connection.cursor()
            placeholder="" #create an empty string
            #this variable will be used to construct the set part of the sql query
            for k in kwargs.keys():
                placeholder += k + "=%s ," #build the set condition
                # set name"%s", city ="%s",blood_group="%s".....
                placeholder =placeholder.rstrip(", ")
                query=f"update donor set{placeholder} where id=%s"
                values=[v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connection.commit()
                print("donor details successfully updated....")
        else:
            print("donor is not found...")
     except Exception as e:
         print(e)



donor_instance=BloodDonorManager()

#donor_instance.post(name="arjun",blood_group="AB+",mobile="980080777",city="kochi",last_donation=datetime.datetime.today()) #for inserting the values

#donor_instance.get()  #display all values

#donor_instance.retrieve(2)   # display for one value


# donor_instance.delete(4)       # for delete the values its id
# print("after deleting a donor____ ")
# donor_instance.get()

# donor_instance.put(id=5)
