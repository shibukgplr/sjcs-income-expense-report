-- Create the database
CREATE DATABASE IF NOT EXISTS school_website;

-- Use the database
USE school_website;

-- Table for storing principal and vice-principal messages
CREATE TABLE IF NOT EXISTS messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type VARCHAR(20) NOT NULL, -- 'principal' or 'vice_principal'
    message TEXT NOT NULL
);

-- Table for storing news, notices, and announcements
CREATE TABLE IF NOT EXISTS news (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing school toppers' information
CREATE TABLE IF NOT EXISTS toppers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    year INT NOT NULL,
    percentage FLOAT NOT NULL,
    photo VARCHAR(255) NOT NULL -- Path to the uploaded photo
);

-- Table for storing events and activities
CREATE TABLE IF NOT EXISTS events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    date DATE NOT NULL,
    photo VARCHAR(255) NOT NULL -- Path to the uploaded photo
);

-- Table for storing teachers' information
CREATE TABLE IF NOT EXISTS teachers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    subject VARCHAR(100) NOT NULL,
    qualifications VARCHAR(255) NOT NULL,
    photo VARCHAR(255) NOT NULL -- Path to the uploaded photo
);

-- Table for storing gallery images
CREATE TABLE IF NOT EXISTS gallery (
    id INT AUTO_INCREMENT PRIMARY KEY,
    caption VARCHAR(255),
    photo VARCHAR(255) NOT NULL -- Path to the uploaded photo
);

-- Table for admin users
CREATE TABLE IF NOT EXISTS admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- Insert a default admin user with a hashed password
-- The password is 'admin' and has been hashed using Werkzeug
INSERT INTO admin (username, password) VALUES ('admin', 'pbkdf2:sha256:260000$Vcg0h3a5Yq3a3Vj0$d2de82c1c1b3f7e5a4e3f4e3b7a5e8b5c6d8f9a0c8e3d6e5a4d3c2b1a0b9d8e7');

-- Insert some sample data
INSERT INTO messages (type, message) VALUES ('principal', 'Welcome to our school! This is a message from the principal.');
INSERT INTO messages (type, message) VALUES ('vice_principal', 'Welcome to our school! This is a message from the vice-principal.');
INSERT INTO news (title, content) VALUES ('Welcome!', 'Welcome to our new school website!');
INSERT INTO toppers (name, year, percentage, photo) VALUES ('John Doe', 2023, 98.5, 'john_doe.jpg');
INSERT INTO events (title, description, date, photo) VALUES ('Annual Day', 'Our annual day celebration.', '2023-12-20', 'annual_day.jpg');
INSERT INTO teachers (name, subject, qualifications, photo) VALUES ('Jane Smith', 'Mathematics', 'M.Sc. in Mathematics', 'jane_smith.jpg');
INSERT INTO gallery (caption, photo) VALUES ('School Building', 'school_building.jpg');
