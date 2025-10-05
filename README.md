# Alx_Social_Media_API
Alx capstone project(BE)

The project idea: Social media API 
Main Features
These features cover the essential requirements and provide a clear scope for the initial API build.
Core Features (CRUD)
User Management:
Register/Login: User creation and token-based authentication 
Profile (Read/Update): View and modify user profile information
Deactivate: Soft deletion or account deactivation endpoint.
Post Management:
Create: Authenticated users can create new posts.
Read: Retrieve a single post.
List: List all posts by a specific user.
Update/Delete: Users can edit or delete only their own posts.
Following System:
Follow/Unfollow: Endpoint to toggle the follow relationship between two users.
Lists: Endpoints to view a user's list of followers and their list of users they are following.
Personalized Feed:
Feed View: An endpoint that displays a chronological list of posts from all users the authenticated user is currently following.







Simple Project Structure Plan
The project will be organized into a main configuration folder and three specialized Django apps to separate concerns (models, serializers, and views).
social_project/
      *  social_config/ 
                * settings.py
                * urls.py
       * users/  
                 * models.py  
                 * serializers.py
                 * views.py
       * posts/  
                * models.py
                * serializers.py
                * views.py
      *  interactions/ 
               * models.py 
               * serializers.py 
               * views.py 
       * requirements.txt
5. Basic Timeline
Task
duration
ERD
1 week
Setup - User Model – Authentication -
1 week
Profile CRUD - Post Model - Post CRUD – Permissions - User Posts List - Following Model - Follow Endpoint
1 week
Feed Query - Feed Endpoint – Testing - Security Review - Deployment Prep - Deployment
1 week


