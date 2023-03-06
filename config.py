sender_email = "your-eamil@gmail.com"
#get your Email app password form https://myaccount.google.com/
sender_email_app_password  = "passwordpassword"


# get your Compatable free API key from https://newsdata.io/
newsdata_api_key = "abc-qwertyuiopasdfghjklzxcvbnm"

# list all the client details
client_details = {"abc@gmail.com": {"name": "Mr Bean", "topic": "entertainment"},
           "xyz@yahoo.com": {"name": "Miss Musk", "topic": "beauty"},
           "qwerty@outlook.com": {"name": "Tom Cruise", "topic": "cars"}}

if __name__ == "__main__":
    for email in client_details.keys():
        print(f"{client_details[email]['name']}: {email}")