# CODECHELLA
![#codechella #twitter](https://pbs.twimg.com/media/EnJYZEKVoAA8WbX.jpg)

# Welcome to Our Team Project: "Profile Analyser"

## Team Introduction 

| Name             | College  | Image |
| -------------    |----------------|------|
| [Akash Srivastava](https://www.linkedin.com/in/akash-s-233ab3160/)|Vellore Institute of Tecnology (Electrical and Electronics Engineering)[2017-2021]|![Akash Srivastava](https://media-exp1.licdn.com/dms/image/C5103AQERq-Hiqnqq9Q/profile-displayphoto-shrink_400_400/0?e=1611187200&v=beta&t=tZAaYCPdQ9zND5MawR7A731_TRxMZ2zeKaE5aBULQlc)|
| [Arush Bhat](https://www.linkedin.com/in/aarush-bhat/)|Vellore Institute of Tecnology (Computer Science and Engineering) [2019-2023]|![Arush Bhat](https://media-exp1.licdn.com/dms/image/C4D03AQHjjuanpnz7Ig/profile-displayphoto-shrink_400_400/0?e=1611187200&v=beta&t=pUiN61Oy2DkUd5FeNrFmK3UZWQCUPmioPujGodGDCt0)|
| [Sunny Tiwari](https://www.linkedin.com/in/sunny-tiwari-aa7392199/)|IIEST Shibpur (Electronics and Communication Engineering) [2017-2021]|![Sunny Tiwari](https://media-exp1.licdn.com/dms/image/C4E03AQFmt9f6bePadQ/profile-displayphoto-shrink_400_400/0?e=1611187200&v=beta&t=y6ovNrKTlJm_qzIDmSv2-UPNr53rxnYObWxnXwb8qjc)|
|[Nandita Gaur](https://www.linkedin.com/in/nanditagaur/)|ABES Engineering College (Computer Science and Engineering) [2017-2021]|![Nandita Gaur](https://media-exp1.licdn.com/dms/image/C5103AQHiTvJNfvJGcQ/profile-displayphoto-shrink_400_400/0?e=1611187200&v=beta&t=mp9yk0XsV7Xb2FSFRDiQkppYDdsoxNBGvoQNUbu1JMc)|

## Project Youtube Demo Link 

<a href="https://www.youtube.com/results?search_query=hackathon"><img src="https://i.ytimg.com/an_webp/5ZrYKULK-10/mqdefault_6s.webp?du=3000&sqp=CJbX4v0F&rs=AOn4CLCzbfSaW9Z-4wDwgwNTfDvwm_uZFQ" 
alt="Project Analyser" width="240" height="180" border="10" /></a>


## Project Explanation (Problem and Solution)
### **Problem Statement**

Everyone wants to see certain kinds of tweets on their dashboard, for example, Motivational or Technical. Finding out and following those kinds of handles is a tedious task, as Twitter Bio can be abstract and deceiving at times. We have to find a way to quickly have an idea about what kind of content is generally tweeted by a handle so that all users, especially visually impaired users can save their time of manually analyzing a profile by going through all the tweets one by one.

### **Solution**

We can deploy a new feature to Twitter, called Profile Analyzer. It will scan the tweets posted on any handle and give a brief report, which will include:

1. **Badge**: To show how actively the user tweets.
2. **Analysis Report**: Graphs and Charts showing the percentage of tweets based on different categories.
3. **Top Tweets**: Most popular tweets of all the categories.
4. **Sentiments**: To know the user mindset if it is Positive, Negative, or Neutral.
5. **Tags**: To tag each user profile by the most common category of his tweet.
6. **Summary**: A summary of the complete analysis report with an immersive reader for ease of access to visually impaired users.

## Tech Stack used and Use Case

### Uses Cases

![Use Case-1](https://github.com/AkashSrivastava1721/Profile_Analyser_-Codechella/blob/main/Readme%20Utilities/profile%20analyzer.jpg)

### Tech Stack
1. **FrontEnd**: HTML, CSS, BootStrap.
2. **BackEnd**: Flask using Python.
3. Databases.
4. JSON Objects.
5. Twitter API.
6. Natural Language Processing based API.
7. Visualization tools.
8. Cloud Services: Heroku for hosting

## Challenges faced during building this project
1. Implementing Natural Language Processing model was tough in the given time frame. So, we had to look for an API.
2. One of our team members had an emergency at the eleventh hour. He was handling the Frontend using NodeJS. Other two members had to complete the frontend using their basic knowledge of frontend.
3. Implementing more dynamism to the project could be tacky in limited time.

## Our Innovation and Implementation

### Innovation

Tagging the profile of user after performing analysis on their tweets could be a blessing for Twitter users. It will be a great ease of access tool which will save the time of going through all the tweets one by one to judge the category of contentent tweeted.

### Implementation

User will first enter the twitter handle. Backend will validate if the user handle is valid or not. After validation, the Twitter API will return user_timeline. Backend will pick 500 tweets for now. The Natural Language Processing based API will categorise each tweet into a specific category. The counter will count the tweets in top frequent categories. User data will be bundled into a JSON Object and passed to the database. Frontend will pick data from the Database and display Badges, Analysis charts, Sentiments, top tweets in each category and a Summary with immersive reader for visually impaired user. At the end, the most frequent category will be used to tag the twitter handle.
![Implementation-1](https://github.com/AkashSrivastava1721/Profile_Analyser_-Codechella/blob/main/Readme%20Utilities/Implementation.jpg)

## Conclusion Note
Most of the features have been implemented to make Twitter easier to use by allowing the user to see the tweet summary of a handle without actually looking at all the tweets. Team Work and good communication among the members was very helpful in building this project.
