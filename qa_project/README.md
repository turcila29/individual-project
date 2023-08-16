# individual-project
Welcome to FRAGRANCE WORLD


## 1. Project Overview


In this file I will present the beautiful journey of how Fragrance World was created.
1. Technologies used:

 
I have used the following technologies in my project:

 

1. Kanban (via Jira) for project management and agile framework
2. Git as the version control system
3. GitHub for source code management
4. HTML, CSS, JavaScript and Bootstrap for front-end development
5. Python as the back-end programming language
6. Flask as the API development platform
7. MySQL as the database management system

 
    This was the phase where I sat myself down and really thought about what it means to "build a website".
Therefore, I started breaking everything down into smaller tasks, and those smaller tasks into even smaller tasks until I got to the bottom of it.

 

## 2. How I used Agile Methodology


I thought that the best way of approaching this project was through Agile Methodology. Therefore, I spent about 15 minutes each morning to review and plan what I had to do for the day. Mainly, I took a 15-20 minutes break after every 3 hours of work. Since it was a pretty quick deadline, instead of having 1 week long sprints, I had 2 days long sprints, so after every 2 days I reviewed and tested the progress made so far and planned my next sprint accordingly.
 
## 3. How I used my Kanban board


### Epics, User Stories, Tasks and Acceptance Criteria

I created 9 user stories that covered the must ares of my project, including the home page, cart page, payment, shipping, and so on. Inside each of my user stories, I stored all of the related tasks to keep it well-structured and easy to understand. This is the first draft of the Kanban:
<img width="1440" alt="first kanban part1" src="https://github.com/turcila29/individual-project/assets/62671182/f6405200-d142-4e66-aa4a-4d7726a1bf2a">

<img width="1440" alt="first kanban part2" src="https://github.com/turcila29/individual-project/assets/62671182/e1e5ee47-b8b2-4459-b236-b2bc2d2f5e6a">

And as I progressed through the project I was also moving around my tasks so I know where I stand and how much I got left to do.
<img width="1440" alt="Screenshot 2023-08-15 at 13 52 35" src="https://github.com/turcila29/individual-project/assets/62671182/de700be4-7fc0-409e-877c-1adff9890577">

And eventually, it was all done:
<img width="1440" alt="Screenshot 2023-08-16 at 17 06 14" src="https://github.com/turcila29/individual-project/assets/62671182/2942ddab-5749-4fb5-be2e-4cfde28174b9">





### Risk Assessment
![risk asss](https://github.com/fkia413/ProjectRepo/assets/131884777/6e9fa5fc-48d5-4ff7-b91e-bbb72fe65728)
This displays some of the risks that I may have encountered during the project, including the steps to mitigate any negative impacts. Based on this risk assessment, I was able to make changed to my code to decrease the possibility of the risks happening.

## 4. Using my feature-branch model

 I mostly used my feature branch to work on some backend functions that were messing with the code and after it was done merged them together.
<img width="1440" alt="Screenshot 2023-08-16 at 11 13 35" src="https://github.com/turcila29/individual-project/assets/62671182/8bcc183c-6e06-4cfa-ad45-593c4f9a5342">

## 5. ERD Diagram 

 Creating the database was my favourite thing from this whole project. It felt like sorting out a puzzle that was evolving more and more as I was putting it together. I ended up with 4 tables: customer, product, order and order_detail.
<img width="886" alt="Screenshot 2023-08-16 at 17 19 35" src="https://github.com/turcila29/individual-project/assets/62671182/b874aa40-158c-4494-b7b0-84d4ac257325">

 Customer was the table I used to store the shipping information in.
Product was the the table I used to display the stock onto the product page
Order was the tables used to add and display on the cart page which is linked with customer through a foreign key ( since one customer can have multiple orders)
and order_Detail was the table used to display, add and delete things from the cart and it was linked with product_id and order_id through foreign keys.

## 6. Jenkins

 I have managed to connect my project to jenkins and actually run it from within Jenkins.

<img width="1440" alt="jenkins 1" src="https://github.com/turcila29/individual-project/assets/62671182/9a85e253-abf1-46b9-9f54-34d771313df2">

<img width="1440" alt="jenkins 2" src="https://github.com/turcila29/individual-project/assets/62671182/a9b53e0f-1ac7-4a29-b3cd-a2ebd1935949">

<img width="1440" alt="jenkins 3" src="https://github.com/turcila29/individual-project/assets/62671182/f5465d51-bbf1-45e3-9b79-d515b8c0fa54">

<img width="1440" alt="jenkins 4" src="https://github.com/turcila29/individual-project/assets/62671182/ccebd494-f7a1-4d2e-bfd9-b6d64999cfe4">

 What I failed to do was testing since the bugs and errors I encountered were overwhelming but I managed to go through them but it cost me too much time.

## 7. Future plans

 The Fragrance World website is in a good state as of now but its still a long way from reaching its potential.
The next steps for this project is to run tests until it gets a high coverage so I know it is fully functional and user friendly and after that would be implementing more features to it  such as: more products, a blog were i can write more detailed info about frgrances, a monthly recommandation pannel on the home page, and thats just from the top of my head.

## 8. Licensing
 For coding I used visual studio code.
 For the databse I used sqlite
 For the Kanban board I used Jira
 For the ERD diagram I used draw.io (absolutely amazing!!!)
 I also used Jenkins, but not too much unfortunately.

## 9. Contributors

W3schools, Stackoverflow.

## 10.Acknowledgements
I wanna thank to Earl Gray for helping me out when we I stuck and panicking, my colleagues, and every coding website that I accessed throughout my panicking moments(there were loads).









