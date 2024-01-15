from json import load

def load_json():

   with open(__file__[:-8] + "creds.json", encoding='utf-8') as file:
      config = load(file)

   apikey = config["apikey"]
   apikeysecret = config["apikeysecret"]
   bearertoken = config["bearertoken"]
   accesstoken = config["accesstoken"]
   accesstokensecret = config["accesstokensecret"]
   telbottoken = config["telbottoken"]
   admin = config["admin"]
   tweet = config["tweet"]

   return apikey, apikeysecret, bearertoken, accesstoken, accesstokensecret, telbottoken, admin, tweet

apikey, apikeysecret, bearertoken, accesstoken, accesstokensecret, telbottoken, admin, tweet = load_json()