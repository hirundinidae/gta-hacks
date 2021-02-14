# gta-hacks
## Inspiration
Our team wanted to focus on the theme of education, as we can relate to the disruptions covid has caused in the education system. E-learning has it even harder to understand concepts in school, making most students feel unconfident with the material. Under those circumstances, the best thing you can do is practice, practice, practice. Unfortunately, even this is difficult as most teachers don’t have time to provide lots of extra online resources for students, and obviously, students can’t rely on their physical textbooks anymore. With all these problems in mind, our team came up with the idea of an online database of resources for both students and teachers. 

## What it does
Using our project, users can view Google Drive links directing you to a file containing questions, with some drive links include answer file, and search for these files based on subject, grade, topic, etc. This aims to provide a superior and user-friendly experience to teachers and students alike, as many have trouble with modern technology.

## How we built it
Our team used Django, ReactJS, NextJS, Formik, TailwindCSS and Sass to create this project. Django was used to create a REST API linking the front end with the databases of the backend.

## Challenges we ran into
At the beginning of the hackathon, our team actually changed our plan from using solely Django, to implementing React as well. For some members, learning this new framework in a short amount of time was a huge challenge on its own. With the switch to Django as just an API, we learned how to use the Django REST Framework as well. We also attempted to implement solr for searching the database, but received too many errors, and had to adapt and use some of Django’s built-in features instead. We also had to adapt our Profile model, using AbstractBaseUser. 

## Accomplishments that we're proud of
This was the first hackathon for most of our teammates, and we are really proud that everyone was able to work together and complete the core of our original idea. We also had to make a lot of last-minute changes, which our team adapted really well to it in a short amount of time!

## What we learned
Half of our team was new to GitHub and learned how to manage projects on it during this hackathon. They also learned some new frameworks like Django. In terms of soft skills, we learned quick problem-solving skills due to the time constraint on the hackathon and collaborating with our teammates.

## What's next for Resourca
To expand on our project, we would add a pinning option for users. This would allow users to pin any resources they wanted, and then view them on their profile page. We would also add work towards being able to render the files on the pages, as opposed to a Google Drive link.
