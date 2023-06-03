from linebot import LineBotApi
from linebot.models import TextSendMessage

CHANNEL_ACCESS_TOKEN = "****"
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

import tweepy        
bearer_token = "*****"

client = tweepy.Client(bearer_token)

user_id = 347849994

def main():
        response = client.get_users_tweets(
                                        user_id,
                                        max_results=100
                                        
                                        )

        tweet_data = []

        # By default, only the ID and text fields of each Tweet will be returned
        for tweet in response.data:

            USER_ID = "******"
            messages = TextSendMessage(text = (str(tweet.text)))
            line_bot_api.push_message(USER_ID,messages = messages)
                
        
        

if __name__ == "__main__":
    main()