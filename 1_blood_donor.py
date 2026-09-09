import mysql.connector

class BloodDonorManager:
    def __init__(self):
        self.connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="MuHamdammed@77",
            database="blood_db"
        )
        print("Connected Successfully")


donor_instance =BloodDonorManager()