
from connect_rds_util import connect_to_postgres, connect_to_violation_logs_db
from create_violation_table import ensure_database_exists, create_violation_logs_table
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import pandas as pd

def log_violation_to_rds(image_url, detected_items_in_image, no_of_violation_class,confidence):
    try:
        #Ensure DataBase Exists:
        ensure_database_exists()

        #Ensure violation_logs_table exists:
        create_violation_logs_table()
        
        #connecting to violation_logs_db table
        print("Connecting to violation logs db")
        conn = connect_to_violation_logs_db()
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        if conn is None:
            return

        cursor = conn.cursor()
        cursor.execute("""INSERT INTO violation_logs_db (image_url, detected_items, no_of_violation_class, confidence)
                       VALUES (%s, %s, %s, %s);""", 
                       (image_url, detected_items_in_image, no_of_violation_class, confidence))

        print("Inserting INTO violation_logs_db Successfull\n")

        cursor.execute("""Select id, image_url as Uploaded_File_on_S3,
                       detected_items,
                       no_of_violation_class as Total_Unique_items_detected_in_image,
                       confidence as confidence_Score_Violations_Detected_in_image 
                       from violation_logs_db order by timestamp desc limit 5""")
        result = cursor.fetchall()
        for i in result:
           print(i,"\n")

        df_logs = pd.read_sql_query("SELECT * FROM violation_logs_db", conn)
        print(df_logs)

        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Violation logged successfully in the database")
        return(df_logs)
    except Exception as e:
        print("❌ Error logging to RDS:", e)
        return None


# image_url = "C:/Users/dhars/Downloads/Dhass/codeing/GUVI/2. MainBoot/4.Project_Code/Final Project - 1/Project6_Code/Intelliguard_PPE_Detection/runs/detect/predict208/3a491fa6a3e34d17b0cd56c157fb951b.jpg"
# detected_items_in_image  = "no_googles,no_shoes"
# no_of_violation_class = "no_googles,no_shoes"
# confidence = 0.0
# log_violation_to_rds(image_url, detected_items_in_image,no_of_violation_class, confidence)