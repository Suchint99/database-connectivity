This project demonstrates a simple graphical user interface (GUI) application that facilitates database connectivity using Python and HTML. It allows users to interact with a database through a user-friendly interface.

Features
Login Interface: A basic HTML login page (Login.html) for user authentication.

Database Operations: HTML page (inline_sql_statements.html) showcasing inline SQL statements for database interactions.

GUI Application: A Python script (Gui_database_connectivity_complete_code.py) that integrates the HTML interfaces and manages database connectivity.

Prerequisites
Python: Ensure Python is installed on your system. You can download it from the official website.

Required Libraries: Install necessary Python libraries using pip:

bash
Copy
Edit
pip install flask mysql-connector-python
Database Setup: Set up a MySQL database and update the connection details in the Python script accordingly.

Getting Started
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/Suchint99/database-connectivity.git
cd database-connectivity
Configure Database Connection:

Open Gui_database_connectivity_complete_code.py.

Update the database connection parameters (host, user, password, database) to match your MySQL setup.

Run the Application:

bash
Copy
Edit
python Gui_database_connectivity_complete_code.py
The application will start, and you can access it via your web browser at http://localhost:5000.

File Structure
Gui_database_connectivity_complete_code.py: Main Python script that runs the Flask application and manages database interactions.

Login.html: HTML page for user login.

inline_sql_statements.html: HTML page demonstrating inline SQL statements.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

License
This project is open-source and available under the MIT License.
