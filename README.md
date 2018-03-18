# feeling_hunter
Simple python script that attempts to guess what type of feeling a  twitter user might be experiencing by analyzing polarity and subjectivity of tweets made by user's friends.
# assumptions  (crap)
i) User might be receiving his feelings from tweets of his friends <br>
ii) Total number of posts = 100% of feelings <br>
iii) A sample space of friends is only taken <br>
iv) Positive tweet yeilds positive feeling & negative tweet yields negative feeling.<br />
v) The core concept is that the feelings are reflection of what we observe from our surroundings.
# required python external modules
i) tweepy <br/> 
ii) textblob
# methods
 i) mean_approach  -> This method guesses user's feelings by calculating mean of his friend's polarities of posts. <br>
 ii) mode_approach -> This method guesses user's feelings by calculating mode of his friend's polarities of posts.
# notes
 Even though it seems so much unrealistic to extract feeling from some sentences, it is possible to do such via sentiment analysis. There are so many freely available modules in python for sentiment analysis but I like to use textblob for it. If you're going to read the code, let me tell you that polarity is a number given to text ranging between -1 to 1 meaning that -0.99 is  negative and 0.99 is positive, values around 0 are neutral. Same goes with subjectivity where values near 1 are subjective and values near -1 are objective.
# Thanks
i) Siraj Raval -> https://www.youtube.com/watch?v=si8zZHkufRY
