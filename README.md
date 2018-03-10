# feeling_hunter
Simple python script that attempts to guess what type of feeling a user might be experiencing by analyzing polarity and subjectivity of tweets made by user's friends.
# assumptions  (crap)
i) User might be receiving his feelings from tweets of his friends
ii) Total number of posts = 100% of feelings <br>
iii) A sample space of friends is only taken 
# required python external modules
tweepy & textblob
# methods
 i) mean_approach -> This method guesses user's feelings by calculating mean of his friend's polarities of posts. <br>
 ii) mode_approach -> This method guesses user's feelings by calculating mode of his friend's polarities of posts.
