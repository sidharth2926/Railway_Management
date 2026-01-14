# Railway_Management
🚆 Railway Reservation Management System

This project is a console-based Railway Reservation Management System developed in Python using MySQL for persistent data storage. It simulates core functionalities of an Indian railway system with separate Management and User access.

🔧 Technologies Used

Python (Core logic & CLI interaction)

MySQL (Database management)

mysql-connector-python (Database connectivity)

🗄️ Database Design

The system automatically creates and uses a MySQL database named Railway with the following tables:

train – Stores train details (name, fare, distance, date, route)

passenger – Manages passenger bookings and PNR records

bills – Tracks railway bills and payment status

worker – Stores railway staff details with auto-generated worker IDs

🔐 Authentication System

Management Login (Password-protected)

Add and display trains

Add and view bills

Add and manage workers

View passenger payment details

User Login

Check train availability

Book tickets and generate PNR numbers

Check booking confirmation

View payment details

Cancel tickets securely using PNR and phone number

⚙️ Key Features

Dynamic PNR number generation using randomization

Automatic database and table creation

Role-based access control (Management vs User)

Secure CRUD operations with MySQL

Menu-driven interface for easy navigation

▶️ How It Works

User connects to MySQL by entering the database password.

The system initializes the database and required tables.

Users select login type (Management/User).

Operations are performed through structured menus.

All data is stored persistently in MySQL.

📌 Project Objective

This project demonstrates practical implementation of:

Python–MySQL integration

Database-driven applications

Basic software architecture for reservation systems

It is suitable for academic projects, DBMS learning, and Python backend practice.
