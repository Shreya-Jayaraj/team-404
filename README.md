![StackUp Banner]([https://tinkerhub.frappe.cloud/files/stackup%20banner.jpeg])
# Project Name
**EventVox** is a comprehensive event listing platform designed to streamline the organization and participation in various events hosted at a college campus. 

The platform offers a range of features to enhance the user experience:

**Event Listing and Description:** Users can easily view a curated list of events along with detailed descriptions. This feature enables attendees to make informed decisions about which events to participate in.

**User Authentication:** EventVox provides a secure user authentication system, allowing individuals to sign up and log in to the platform. This feature ensures that users have personalized access to the platform's functionalities and their event-related activities.

**Event Management for Registered Users:** Registered users have the capability to create events. They can also update/delete events that they host. This functionality empowers event organizers to efficiently manage their events, keeping the information accurate and up-to-date for potential attendees.

**About Page:** The platform includes an informative "About" page that provides users with background information about EventVox. This page may detail the platform's mission, vision, team, or any other relevant information that enhances user trust and understanding.

EventVox aims to create a user-friendly environment that caters to both event organizers and attendees. By combining event listing, user authentication, event creation, and an informative about page, the platform ensures a seamless and engaging experience for all users involved in the event management process.

## Team members
1. Devika Rajeevan [https://github.com/mummylovestocode]
2. Shreya Jayaraj [https://github.com/Shreya-Jayaraj]
3. Amarthya Shekhar [https://github.com/amarthya01]
4. Diya Pratheep [https://github.com/NotaWhiteHatJr]
   
## Team Id
Team-404

## Link to product walkthrough
[https://drive.google.com/file/d/1OGBZ6-UBjNGSzmA9RSmRKhFhwvYtrS9V/view?usp=sharing]

## How it Works ?
**Working of project**

**User Registration and Authentication:** Users access the EventVox platform and have the option to sign up or log in. Django handles user registration and authentication through its built-in authentication system. When a user signs up, their information is stored securely in the database.

**Event Listing:** Users can view a list of events on the platform. Django retrieves event information from the database and dynamically generates the event list page.

**Event Creation/Update:** Registered users who are event organizers have the privilege to create new events or update existing ones. Django provides a form for users to input event details, which are then validated and stored in the database.

**About Page:** The "About" page provides information about the EventVox platform, its mission, team, or any other relevant details. 

**Database Interaction:** Django uses its Object-Relational Mapping (ORM) system to interact with the database. Models define the structure of the database tables, and queries are used to retrieve, create, update, and delete data.

**Frontend and Templates:** Django uses templates to dynamically generate HTML pages. These templates can include placeholders for dynamic data, such as event details, user information, etc. CSS, JavaScript and Bootstrap was used to enhance the user interface and add interactivity.

**Routing and Views:** Django uses URL patterns to route requests to the appropriate views. Views are Python functions or classes that handle user requests, retrieve necessary data from the database, and render the appropriate templates. 

Video of the project demo : [https://drive.google.com/file/d/1SNTCUEwGhQ9UA4z5kr67ryo_KDy0CDw3/view?usp=drive_link]

## Libraries used
1. Pip package installer must be installed from python
   Code - python3 get-pip.py
3. Pillow library from pip in python has to be installed.
   Code - pip install pillow


## How to configure
1. Install Python  
2. Install Virtual Environment (optional but recommended):  
code - python -m venv venv  
	--Activate the virtual environment  
		Windows - .\venv\Scripts\activate  
		macOS/Linux - source venv/bin/activate  
3. Install Django  
code-pip install django

## How to Run
1. Run Migrations  
code - python manage.py migrate  
2. Run the Development Server  
code - python manage.py runserver  
Your Django application should now be accessible at http://127.0.0.1:8000/ in your web browser.  
