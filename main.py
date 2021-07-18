from instabot import Bot
bot = Bot()
# bot.login(username ="yourUserId",password ='YourPassword')
# Post First Picture
bot.upload_photo("pic.png",caption="My First Post")
# follow someone
bot.follow("elonrmuskk")
# what to send message
bot.send_message(" hi !!! bro ,[usernameYouWantToMessage]")
# what to see follower of someone
followers = bot.get_user_followers("username")
#pass
#print followers
for follower in followers:
    print(bot.get_user_info(follower))
# unfollow someone
bot.unfollow("userID")
# unfollow everyone
bot.unfollow_everyone()
# similarly you can block someone and many other things.
# visit this gitHub Id : "instabot"