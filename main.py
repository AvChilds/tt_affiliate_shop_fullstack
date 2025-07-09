import requests
import json

#retrieve list of affiliates from affiliate table
def get_all_affiliates_fe():
    endpoint = "http://127.0.0.1:5000/affiliates"
    response = requests.get(endpoint)
    return response.json()

#for list of available countries to select from for user
def get_available_countries_fe():
    endpoint = "http://127.0.0.1:5000/countries"
    response = requests.get(endpoint)
    return response.json()

#user to view which affiliate and videos are from a specific country
def get_videos_by_country(country):
    endpoint = f"http://127.0.0.1:5000/videos/{country}"  # Properly format the URL
    response = requests.get(endpoint)
    return response.json()

#retrieve earnings information for each video
def get_earnings_fe():
    endpoint = "http://127.0.0.1:5000/earnings"
    response = requests.get(endpoint)
    return response.json()

#user input for new video
def collect_new_video_info():
    affiliate_id = input("Affiliate_id (enter 1 - 8): ")
    product_name = input("Name of product: ")
    views = int(input("Number of views (int): "))
    commission_per_sale = float(input("Commission per sale in £ (to 2 decimal places): "))
    no_of_sales = int(input("Number of sales: "))

    new_video_dict = {
        "affiliate_id": affiliate_id,
        "product_name": product_name,
        "views": views,
        "commission_per_sale": commission_per_sale,
        "no_of_sales": no_of_sales
    }
    return new_video_dict

#add video to videos table
def add_new_video_fe(new_video_dict):
    endpoint = "http://127.0.0.1:5000/videos/add"  # Adjust if API is hosted elsewhere
    response = requests.post(endpoint, json=new_video_dict)
    return response.json()


if __name__ == "__main__":
    print ("------------------------------")
    print ("Tiktok Shop Affiliate Database")
    print ("------------------------------")

    while True:
        print("\nOptions:\n1. View all affiliates\n2. View videos by country\n3. View total earnings for each video and the top earner\n4. Add New Video \n5. Exit \n")
        choice = input("Please enter your choice: ")

        if choice == "1":
            affiliates = get_all_affiliates_fe()
            if affiliates:
                for affiliate in affiliates:
                    print(affiliate)

        elif choice == "2":
            countries = get_available_countries_fe()  #provide user a multiple choice of countries to choose from
            country = input(f"Enter name of country from this list {countries}: ").capitalize()
            videos = get_videos_by_country(country)
            if videos:
                print(f"Videos from {country}:")
                for video in videos:
                    print(f"Username: {video['username']}, Product: {video['product_name']}")
            else:
                print(f"Error: Invalid entry. Please try again.")


        elif choice == "3":
            earnings = get_earnings_fe()

            if earnings:
                print("\n Full Earnings table:")
                for item in earnings:
                    print(item)

                top_earner = max(earnings, key=lambda x: x["total_commission"])
                print("\nTop Earning Video:")
                print("Video ID:", top_earner["video_id"])
                print("Affiliate ID:", top_earner["affiliate_id"])
                print("Product Name:", top_earner["product_name"])
                print("Total Commission:", top_earner["total_commission"])


        elif choice == "4":
            new_video_dict = collect_new_video_info()
            updated_db = add_new_video_fe(new_video_dict)
            print("New video data added successfully. \n")
            for video in updated_db:
                print(f"video_id: {video['video_id']}, affiliate_id: {video['affiliate_id']}, product_name: {video['product_name']}, views: {video['views']}, commission_per_sale: {video['commission_per_sale']},no_of_sales:{video['no_of_sales']}")

        elif choice == "5":
            print ("Process completed. Exiting the app now")
            break


        else:
            print("Invalid choice. Please try again.")