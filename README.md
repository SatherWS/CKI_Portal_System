# CKI_Portal_System
With this software members of Circle K International can an create account, sign up for service projects and track the amount of service hours earned by their club.

## Requirements
* Python 3 or greater
* Django Framework verion 2.1 or greater

## How to Run
1. CD into the project's directory 
2. Run script manage.py
3. Search in web browser 127.0.0.1:8000

## Screenshots of the Project
Image 1
Users sign up through GUI and are added to users table of the database as shown in image below. 

![Alt text](https://github.com/SatherWS/CKI_Portal_System/blob/master/CKI%20App/signup.PNG)

Image 2
The user 'Test User' with email address 'test@website.com' is added to the table Users.

![Alt text](https://github.com/SatherWS/CKI_Portal_System/blob/master/database_imgs/users_table.PNG)

Image 3
The user 'Test User is allowed to sign up for service projects that belong to his club 'Stockton University'. Entries into the 'Service Project' table can only be added by the website administrator or higher ranking members of the club.

![Alt Text](https://github.com/SatherWS/CKI_Portal_System/blob/master/CKI%20App/projects.PNG)

Image 4 
Once signed up for a project the user is added to the associative entity 'Worker for Project' using this data users are able to see which of their fellow club members are signed up for the same project.

![workers](https://github.com/SatherWS/CKI_Portal_System/blob/master/CKI%20App/users.PNG)

Image 5
In the below image we can confirm that the current user 'Test User' has been added to the associative entity relate to 'Project 1' of the club 'Stockton University'.
![workers](https://github.com/SatherWS/CKI_Portal_System/blob/master/database_imgs/workers_table.PNG)

