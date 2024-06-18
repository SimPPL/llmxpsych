from twikit import Client
import pandas as pd
from tqdm import tqdm
import time


# Initialize client
client = Client(language = 'en-US')

client.login(
    auth_info_1= 'XXXXXXXXX',
    auth_info_2='XXXXXXXX',
    password='XXXXXXXX'
)

# Read the CSV file
df = pd.read_csv('tweetId.csv')

# Create a list to store the results
results = []

# Iterate over the 'tweetId' column with a progress bar
for tweet_id in tqdm(df['tweetId']):
    try:
        # Get the tweet by id
        tweet = client.get_tweet_by_id(str(tweet_id))
        # Store the tweet id and the result in the list
        results.append({'tweetId': tweet_id, 'tweet': tweet})
    except Exception as e:
        print(f"An error occurred with tweet id {tweet_id}: {e}")
        continue
    finally:
        # Pause for a while to avoid hitting the rate limit
        time.sleep(7)  # Adjust this value as needed

# Create a new DataFrame from the results list
result_df = pd.DataFrame(results)

  
# tweet = client.get_tweet_by_id("1592778879885709312")

# print(
#     f'id: {tweet.id}',
#     f'text {tweet.text}',
#     sep='\n'
# )
