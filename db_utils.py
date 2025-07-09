import mysql.connector
from config import USER, PASSWORD, HOST, DATABASE

class DbConnectionError(Exception):
    pass

#Establish a connection to the MySQL database.
def _connect_to_db():

    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=DATABASE
    )
    return connection

#retrieve data from the affiliate table
def fetch_all_affiliates():
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cursor = db_connection.cursor(dictionary=True)  # Return results as dictionaries
        print("Connected to tiktok_affiliate DB")

        query = """ SELECT * FROM affiliates """
        cursor.execute(query)
        results = cursor.fetchall()

        cursor.close()
        return results

    except Exception:
        raise DbConnectionError("Unable to connect to DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection closed")

# using SELECT DISTINCT to isolate country data
def fetch_available_countries():
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cursor = db_connection.cursor(dictionary=True)  # Return results as dictionaries
        print("Connected to tiktok_affiliate DB")

        query = """SELECT DISTINCT country FROM affiliates"""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()

        countries = [country['country'] for country in results]
        return countries

    except Exception:
        raise DbConnectionError("Unable to connect to DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection closed")

#to view country which videos/affiliate are in a specific country - using JOIN
def fetch_videos_by_country(country):
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cursor = db_connection.cursor(dictionary=True)  # Return results as dictionaries
        print("Connected to tiktok_affiliate DB")

        query = f""" 
                SELECT a.id , a.username, v.product_name
                FROM affiliates a
                JOIN videos v ON a.id = v.affiliate_id
                WHERE a.country = "{country}"
                """
        cursor.execute(query)
        results = cursor.fetchall()

        cursor.close()

        return results

    except Exception:
        raise DbConnectionError("Unable to connect to DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection closed")

#INSERT query to add new row to videos table
def add_video (new_video_dict):
    try:
        db_connection = _connect_to_db()
        cursor = db_connection.cursor(dictionary=True)  # Return results as dictionaries
        print("Connected to tiktok_affiliate DB")

        print("Add this video to DB: ", new_video_dict)

        query = f"""
        INSERT INTO videos (affiliate_id, product_name, views, commission_per_sale, no_of_sales)
        VALUES ('{new_video_dict['affiliate_id']}', '{new_video_dict['product_name']}', '{new_video_dict['views']}', '{new_video_dict['commission_per_sale']}', '{new_video_dict['no_of_sales']}')
        """

        cursor.execute(query)
        db_connection.commit()
        print("Video add completed")

        query = """SELECT * FROM videos
                ORDER BY video_id ASC"""
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result


    except Exception:
        raise DbConnectionError("Unable to connect to DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection closed")

#calulates earnings total per video
def fetch_earnings():
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cursor = db_connection.cursor(dictionary=True)
        print("Retrieving earnings from DB")

        query = """ SELECT DISTINCT video_id, affiliate_id, product_name, commission_per_sale, no_of_sales FROM videos"""
        cursor.execute(query)
        results = cursor.fetchall()


        earnings = [
                {
                "video_id": video["video_id"],
                "affiliate_id": video["affiliate_id"],
                "product_name": video["product_name"],
                "total_commission": video["commission_per_sale"] * video["no_of_sales"]  # total commission earn from sales of the product
                }
            for video in results

            ]

        cursor.close()


        return earnings

    except Exception:
        raise DbConnectionError("Unable to retrieve data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection closed")



#testing connection to mysql

if __name__ == "__main__":
    print("TESTING DB CONNECTION")
    print(fetch_all_affiliates())

