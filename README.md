

**Stockease**
Stockease is a small grocery stock management application designed to help small grocery stores manage and update their inventory without the need for manual records.
This application simplifies stock management by replacing traditional paper and book methods with a digital system.


**Features**
Manage grocery stock easily
Update stock quantities
View inventory information
No need for manual entries on paper


**Installation**
Step 1: Clone the repository
Clone the Stockease repository to your local machine:
"git clone https://github.com/kolneyney/Stockease.git"


Step 2: Navigate to the project directory
"cd Stockease"


Step 3: Install required dependencies
"pip install -r requirements.txt"


Step 4: Set up MySQL database
Stockease requires a MySQL database for data storage. Follow these steps to set up your MySQL database:

- Install MySQL if you don’t have it installed. You can download it from "https://dev.mysql.com/downloads/".
- Create a new database for Stockease. You can do this by logging into MySQL and running the following command: "CREATE DATABASE stockease_db;"
- Set up the database schema by importing the provided SQL script. Locate the stockease_schema.sql file in the repository and run the following command in your MySQL terminal: "SOURCE /path/to/stockease_db_schema.sql;"
- Update database credentials in the application:
  open calldatabase.py in def connect_db change your MySQL username, password, and database name. For example:
  DB_USER = 'your_username', 
  DB_PASSWORD = 'your_password', 
  DB_HOST = 'localhost', 
  DB_NAME = 'stockease_db'

  
Step 5: Run the application
  Once the database is set up, you can start the application:
"python main.py"

Follow the prompts in the interface to manage your grocery stock.

**Usage**
Use the application to add, update, and view your inventory.
The data is stored in the MySQL database, so all changes are persistent.
Contributing
Feel free to fork this project, make improvements, and submit pull requests. For any major changes, please open an issue first to discuss what you would like to change.
