# Dynamic School Website with Flask and MariaDB

This is a dynamic school website project built with Flask, MariaDB, and Bootstrap.

## Features

### Public Website
- Homepage with dynamic news and events.
- About Us page with messages from the Principal and Vice Principal.
- School Toppers page with student details and photos.
- Activities & Events page with images and descriptions.
- Teachers Information page.
- Contact page with a form and embedded map.

### Admin Console
- Secure admin login/logout.
- Dashboard for managing website content.
- Add, edit, and delete functionality for:
  - Principal and Vice Principal messages.
  - News and announcements.
  - School toppers.
  - Events and activities.
  - Teachers.
  - Gallery images.
- File uploads for images.

## Setup and Installation

### 1. Clone the repository
```bash
git clone <repository-url>
cd school_website
```

### 2. Set up the MariaDB database
- Make sure you have MariaDB installed and running.
- Log in to your MariaDB server and run the following command to create the database and tables:
```bash
mysql -u your_username -p < database_schema.sql
```
This will create the `school_website` database, all the necessary tables, and a default admin user.

### 3. Create a virtual environment and install dependencies
- It is recommended to use a virtual environment to manage the project's dependencies.
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
- Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 4. Configure the application
- Create a `.env` file in the root of the project directory.
- Add the following line to the `.env` file, replacing the placeholder values with your MariaDB credentials:
```
DATABASE_URL='mysql+pymysql://your_username:your_password@localhost/school_website'
```
- You can also set a `SECRET_KEY` in the `.env` file for production use.

### 5. Run the application
- Once the setup is complete, you can run the application with the following command:
```bash
python run.py
```
- The application will be available at `http://127.0.0.1:5000`.

## Admin Access
- The admin panel is available at `http://127.0.0.1:5000/admin`.
- The default login credentials are:
  - **Username:** admin
  - **Password:** admin
```
