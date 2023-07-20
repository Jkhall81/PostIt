# PostIt

PostIt is a web application built with Django, PostgreSQL, and deployed on Render. It allows users to create an account, upload pictures, post comments, like other people's comments, view a list of registered users, see users' posts, and follow or unfollow other users.  Users can also update their info to include a user bio, and links to a personal webpage or social media profiles.

## Features

- **User Registration**: Users can create an account to access the application.
- **Picture Upload**: Users can upload pictures of themselves.
- **Commenting**: Users can post comments on pictures.
- **Likes**: Users can like other people's comments.
- **User List**: Users can view a list of registered users.
- **User Posts**: Users can view posts by other users.
- **Follow/Unfollow**: Users can follow or unfollow other users to stay updated on their posts.
- **Update profile information**: to include bio, webpage link, and social media profile links.

## Technologies Used

- Django: The web framework used for developing the application.
- PostgreSQL: The database management system used to store user data.
- Render: The platform used to deploy and host the application.

## Setup

To set up the project locally follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/Jkhall81/PostIt.git
   ```

2. Navigate to the project directory:

   ```
   cd PostIt
   cd Social
   ```
   
3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Create a local database and apply database migrations (NOTE: if you wish to use a different database you can configure your settings.py file as needed):

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server:

   ```
   python manage.py runserver
   ```

## Dependencies

- asgiref==3.7.2
- dj-config-url==0.1.1
- dj-database-url==2.0.0 
- Django==4.2.2
- gunicorn==20.1.0
- Pillow==9.5.0
- psycopg2-binary==2.9.6
- sqlparse==0.4.4
- typing_extensions==4.6.3
- tzdata==2023.3
- whitenoise==6.5.0
- fontawesomefree==6.4.0

## License

This project is licensed under the MIT License. See the LICENSE file for details.
   
