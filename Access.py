import requests
session = requests.Session()
user=str(input("Enter Email Or Uid :"))
pw=str(input("Enter Password: "))
response= session.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+user+"&locale=en_US&password="+pw+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6").json()

print("____________________________________")

print("--------------------Processing----------------------")

print("____________________________________")

print("Your Token: ",response['access_token'])
