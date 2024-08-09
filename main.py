import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyAyLkb-KSQLOzXCGygGU8l-_SZ_WqN_8W0"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

text='''Boss Thank you all for coming today. First of all, I would like you all to meet Mr. Mark Johnson. He is our new salesperson with the company.

Susan: I think Mark has met everyone, oh, except for Ann.

Ann: Hello, Mark. I am Ann Nice to meet you. I am a salesperson, too.

Mark: It’s nice to meet you, Ann Maybe you can help to teach me about my new job.

Ann: Sure. We can be a .team You help me, I’ll help you.

Boss: That sounds good to me, too. Now let’s talk about business. Linda, will you please take notes of our meeting for us?

Linda: Sure, I have my pen and paper ready.

Boss: Great. Please read the notes of our last meeting for us.

Linda: Okay. First, we talked about the budget for next year.

Susan: I will budget is getting smaller every year.

Linda: Second, we talked about the new products we are going to selling.

Mark: She means the new products you and I will be selling.

Linda: O.K. Third, we talked about the profits that we had last month. And fourth, we talked about the bills we had to pay.

Boss: We always have more bills than profits.

Linda: Finally, we talked about raising the cost of our new products.

Susan: I’m afraid our customers will think our product is too expensive.

Linda: Why is everyone whispering?

Boss: Sorry, Linda. O.K. We have a few things to talk about today. Susan, would you like to give your report.

Susan: Yes, thank you. I have a sales graph I would like to show everyone. This shows how well we are selling our products this year.

Susan: This line is the sales of our products. And this line is the sales of our competitors’ products.

Ann: So if that line goes up, am I doing a good job?

Susan: Exactly.

Ann: O.K. And if that line goes up, does my salary go up?

Susan: Good question, Ann. We’ll talk about that after the meeting.

Mark: Susan, do we have many competitors?

Susan: No, not really but enough to keep us busy. Anyway, good job, Ann. I’m sure you and Mark will do even better next month!

Boss: Thank you, Susan. Very good. Tom, do you have anything to tell everyone.

Tom: Yes. Don’t forget, if you want me to buy something for your office, the deadline is tomorrow.

Susan: Oh!! I need a new typewriter. Mine is broken.

Tom: O.K. No problem. If anyone wants me to buy something, tell me before the deadline.

Boss: O.K. Is that everything? O.K. I think that’s all. You can go now.

Susan: Oh, wait!! Mark has a presentation he would like to give about his new job.

Mark: Oh, yeah, O.K.
Susan: Mark, Friday at 1 o’clock, I would like you to go with me to a seminar.

Mark: Sure, no problem. Friday at 1 o’clock.

Susan: Maybe you should write that on your calendar so you don’t forget.

Mark: Really, no problem, I can remember. I promise.

Susan: O.K. See you on Friday.

Mark: O.K.

Susan: Oh! Mark. Now you should probably call some customers and make some appointments.

Mark: O.K.

Mark: Let’s see … Who would be a good company to call? Hmm … this looks like a good company. Maybe they would be interested in our products.

Operator: N.S.T Company. Good afternoon.

Mark: Yes. Hello, my name is Mark Johnson, I’m calling from the Wilson Marketing Company. May I please speak to the Production Manager?

Operator: That would be Jim Pearson, just a moment. I will connect you.

Jim: Hello. This is Jim Pearson. Can I help you?

Mark: Yes, hello, Mr. Pearson. My name is Mark Johnson. I am calling from the Wilson Marketing Company. How are you today?

Jim: Fine, thank you, Mr. Johnson.

Mark: Are you the Production Manager?

Jim: Yes, I am. How can I help you?

Mark: Actually, I think I can help you.

Jim: Really? How?

Mark: I have many products that I can show you that will help your company to save a lot of money. You will have more production and better quality if you use our products.

Jim: Really? That’s very interesting. Are they expensive products or are they cheap products?

Mark: We can talk about the price later. I would like to meet with you to talk with you more if you are free.

Jim: Actually, Mr. Johnson, i am very busy every day this week.

Mark: Do you have one hour free this week? I promise, I won’t be wasting your time.

Jim: Well, I have a little bit of time at lunch time on Friday.

Mark: If it is convenient, we can eat lunch together on Friday.

Jim: That would be fine.

Mark: How about 1 o’clock on Friday at the Blue Moon Restaurant.

Jim: 1 o’clock on Friday. That’s fine! O.K. Then I will see you at the Blue Moon Restaurant.

Mark: 1 o’clock on Friday. Fine. Thank you very much for your time, Mr. Pearson.

Jim: You’re welcome, Mr. Johnson. Goodbye.

Mark: Goodbye.

Boss: Mark, I need you to help me.

Mark: Who? Me? Help you? Sure!! I’ll do anything to help you, sir.

Boss: Anything?

Mark: Anything.

Boss: I need you to take me to the airport this week.

Mark: Sure. No problem! When?

Boss: Friday at 1 o’clock.

Mark: Friday at 1 o’clock?

Boss: Yes. Thank you for your help. I appreciate it.

Mark: Oh, no! I have 3 appointments on Friday at 1 o’clock. I have a seminar with Susan Friday at 1 o’clock. I must meet my customer Friday at 1 o’clock. And I must take my boss to the airport Friday at 1 o’clock.

Mark: Number one, cancel the seminar with Susan. Number two, ask someone to take my boss to te airport for me. Number three, meet my customer Friday at 1 o’clock at the restaurant. And number four … buy a new calendar.
Jim: You must be Mark Johnson?

Mark: You must be Mr. Pearson?

Jim: Yes. Sorry I am late.

Mark: Never mind. Please sit down. Would you like something to drink?

Jim: Yes. Some tea would be nice.

Mark: Waitress! A cup of tea, please. So Mr. Pearson, I hear that your company is very large.

Jim: Yes, it is a very large company. We have more than 1 million customers.

Mark: Wow! And it seems that your company is not only domestic, but it is also an international company?

Jim: Yes. It is an international company. It has customers in more than 10 countries.

Mark: Wow! I think you must be a very busy man.

Jim: Yes! I stay very busy.

Waitress: O.K. What can I get for you to eat today?

Jim: I would like a steak.

Waitress: Alright and what can I get for you, sir?

Mark: I think I would like a steak also.

Waitress: O.K. I’ll have that back in about 5 minutes.

Jim: Thank you.

Jim: How long have you worked at Wilson Marketing Company?

Mark: Well, not very long. Actually, this is my first week. But I have worked in chemical sales for several years.

Jim: Really? How do you like it?

Mark: Oh, I love it. It is a very good job. And the products that I will sell to you are very good also.

Jim: That is, if I buy the products. I have to know about them first before I decide to buy them.

Mark: That’s true, that’s true. Today, I just wanted to meet with you for a short time and talk with you about how our products can help you. These papers explain how the products will help.

Jim: What is this page about?

Mark: O.K. This page list our products’ specifications and explains the chemical processes of our products.

Jim: I see. And how about this page?

Mark: Well, this page is a report about the new high technology that we used to research and develop our products.

Jim: O.K. And how about this page?

Mark: O.K. This page lists all of the advantages your company will receive when you use our products.

Jim: Good. Could you give me a few days to read them and to talk with my staff about them?

Mark: Sure, no problem. Maybe I can meet with you again next week and we can discuss our products. Then?

Jim: Yes. I think it would be fine.

Mark: Thank you … Also I need a receipt, please.

Waitress: O.K. I’ll be right back.

Mark: O.K. Here are some papers and brochures with information about our products.

Jim: Thank you. You know Mark, I am really glad I met you today. It seems like we’re already friends.

Mark: Thank you, Mr. Pearson. So when would be a good day to meet next week?

Jim: I think Tuesday morning is good. Are you free then?

Mark: Just a moment. Yes. Tuesday is fine. So I will meet you at your office on next Tuesday and if you have any questions about our products, you can ask me then.

Jim: O.K. Thank you for lunch, Mark. It was delicious.

Mark: You’re welcome. Alright. So, see you next Tuesday.

Jim: Yes, that will be fine. Goodbye, Mark.

Mark: Goodbye, Mr. Pearson.
Jim: Oh! Hello, Mark. Coming please.

Mark: Hello. How are you today?

Jim: Fine, thank you.

Mark: Did you have a nice weekend?

Jim: Yes, it was very nice. I spent time with my family. I took my children to a football game.

Mark: Sounds like you had a nice time. I hope you are not too busy to talk with me today.

Jim: No! Never mind. I have read all of your papers about the products

Mark: Oh good. What do you think? Are you interested?

Jim: Your products are very interesting. But I have some questions about the products.

Mark: No problem. What would you like to know?

Jim: O.K. Tell me about these products, Mark.

Mark: O.K. Well, you can use these products in your machines at your factory.

Jim: Really? How will they help?

Mark: Well, first of all, they can help your machines to run faster.

Jim: You mean they will help to improve the production if I use these products.

Mark: Yes. You will have more production and you will have better quallity if you use these products.

Jim: For my factory, which product is the best use?

Mark: Let’s see. I think this product is the best for your factory.

Jim: Why?

Mark: Well, because you can use this product in all of your machines and it’s very easy to use.

Jim: Is it dangerous or toxic?

Mark: Oh, not at all. Not at all!

Jim: And can I store this in my warehouse?

Mark: Yes, you can.

Jim: For how long?

Mark: You can store this product in your warehouse for over 1 year.

Jim: Can I test this product before I buy it?

Mark: You sure can. As a matter of fact, I’ve brought a small sample for you to test in your factory.

Mark: A small sample, I think this will be enough for you to test.

Jim: Yes!! I am very sure that will be enough. Can you help my workers at the factory to test this product?

Mark: Yes, I can. It’s very easy. When would you like to test it?

Jim: If you have enough time, you could go to the factory today. I can call and let them know you are coming.

Mark: Today? Sure, that’s fine. That’s fine.

Jim: Hello. Is this Tom? Yes, this is Jim. Today, a sales-techinician will bring a sample to test in the machines. Can you help him? O.K. Thank you.

Mark: Wow! That sure was easy!

Jim: Everything is easy when you are the Production Manager.

Mark: O.K. So after we have tested the product in these machines, when would you like for me to come again to discuss the results?

Jim: Give me one or two weeks. I want to look at the data. Then I will call you.

Mark: No problem. We can discuss all of the details then.

Mark: O.K. Thank you very much for your interest, Jim.

Jim: I hope it will help my factory to have more production.

Mark: It will. I guarantee it.

Jim: O.K. Well, thank you very much, Mark

Mark: Thank you, Jim.

Jim: Goodbye.

Mark: Goodbye.

'''

prompt = f'''You are provided with the discussion done in a meeting given in {text}. The task is to generate a Minutes of Meeting.Following are 7 steps that can help you compose an effective meeting minutes report: 1.Make an outline i.e. As the meeting occurs, you can then arrange your notes so that each of your points connects to a clear overall topic. 2. Include Factual Information i.e.Add factual details, such as where and when the meeting takes place. Include a list of the meeting's participants. 3.Write down the purpose i.e. Record the purpose of the meeting as either the meeting title or as a distinct section. Some meetings may encompass a range of ideas and conversations. Including the meeting purpose in your report can help you synthesise the most important topics of conversation. 4. Record decisions made i.e.Write down any decisions made during the meeting. If these decisions involved a vote, include a tally of how many people voted for each option. You might also want to keep track of how many people voted for options that ultimately the meeting participants didn't decide to pursue. This way, if the rejected or accepted decision becomes a conversation topic at a future meeting, participants can refer back to the minutes report. 5.Compose action items i.e.
Create a separate section for actionable items that specific individuals or teams plan to complete prior to the next meeting. Record any dependables, meaning tasks that need to be accomplished before others, or deadlines for these actions. This list of actionable items can help professionals or departments recall their responsibilities once the meeting concluded.
6. Add details for the next meeting i.e Include any additional information relevant to the next meeting. This may include topics you didn't get to discuss at this meeting or that you plan to discuss further at the next one. It might also consist of the next meeting date and time, location or participants.7. Be Concise i.e.Strive to only record the most relevant or crucial main ideas discussed at the meeting. It's okay if your minutes report doesn't capture information related to every minute of the actual meeting. The goal of meeting minutes reports is typically to summarise the meeting for participants to refer back to or for company leaders to receive progress reports.DO NOT PROVIDE ASTRICTS IN ANSWER.

Output Format -

[Title of meeting]
Location: [where you held the meeting]
Date: [day of meeting]
Time: [time of meeting]
Attendance:
[participant - note if they did or didn't show up for meeting]
[participant - note if they did or didn't show up for meeting]
[participant - note if they did or didn't show up for meeting]
Agenda items:
[agenda item 1]
[main idea discussed in relation to agenda item]
[main idea discussed in relation to agenda item]
[main idea discussed in relation to agenda item]
[agenda item 2]
[main idea discussed in relation to agenda item]
[main idea discussed in relation to agenda item]
[main idea discussed in relation to agenda item]
Next steps:
[actionable item]
[actionable item]
[actionable item]
'''
response=model.generate_content(prompt)
print(response.text)