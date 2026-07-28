import praw 
import pandas as pd
#important variables
num_of_posts=900
subreddit_name="Chainsawman"



reddit =praw.Reddit(
client_id="eooRep-EWsgQSo_jIV9t9A", #client id
client_secret="cilB13w2PkGVk9XmNowgZbjIrJTypA",#client secret 
user_agent="let`s_fight") 

#subreddit name,

subreddit = reddit.subreddit(subreddit_name)

#here we will use top 900 posts from that subreddit
top_posts_list=list(subreddit.top(limit=num_of_posts))

#displaying the first 10
#using enumerate() function to keep traking of the nums (much "pythoni" way)
num=0
for  post in top_posts_list:
    if (num==10):
        break
    num+=1
    print(f"title:{post.title}")
    print(f"score:{post.score}")
    print(f"url:{post.url}")
    print(f"comments:{post.num_comments}")
    print(f"_"*5)



# Create a list of dictionaries using list comprehension
posts= [
{
"Title": post.title,
"score": post.score,
"urls": post.url,
"number of comments":post.num_comments
}
for post in top_posts_list
]

df = pd.DataFrame(posts)#THE DATA FRAME

#saving them into a csv file in case of offline usage
df.to_csv(f"tops_posts_{subreddit_name}.csv",index=True)
