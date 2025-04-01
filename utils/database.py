import sqlite3
import re
from threading import Lock
import random
from datetime import datetime, timedelta


class Database:
    def __init__(self, db_name="database/users.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.lock = Lock()
        self.create_users_table()
        self.create_activities_table()
       # self.generate_yoga_activities()

    def create_users_table(self):
        # Create users table if it doesn't exist
        with self.lock:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    mail TEXT UNIQUE NOT NULL,
                    age INTEGER NOT NULL,
                    weight REAL NOT NULL,
                    training_days INTEGER DEFAULT 0,
                    training_time INTEGER DEFAULT 0, 
                    level INTEGER DEFAULT 0,
                    points INTEGER DEFAULT 0
                )
            ''')
            self.conn.commit()
            cursor.close()

    def create_activities_table(self):
        # Create activities table to store yoga activity information
        with self.lock:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS activities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    start_time TEXT NOT NULL,  -- Format: YYYY-MM-DD HH:MM
                    end_time TEXT NOT NULL,    -- Format: YYYY-MM-DD HH:MM
                    duration INTEGER NOT NULL, -- Duration in minutes
                    yoga_pose TEXT NOT NULL    -- Name of the yoga pose
                )
            ''')
            self.conn.commit()
            cursor.close()

    def validate_input(self, username, password, mail, age, weight, confirm_password):
        # Check if fields are empty
        if not all([username, password, mail, age, weight, confirm_password]):
            return False, "All fields must be filled!"

        # Username validation (alphanumeric, 3-20 characters)
        if not re.match(r'^[a-zA-Z0-9]{3,20}$', username):
            return False, "Username must be 3-20 alphanumeric characters!"

        # Email validation
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', mail):
            return False, "Please enter a valid email address!"

        # Password validation (6-20 characters)
        if len(password) < 6 or len(password) > 20:
            return False, "Password must be 6-20 characters!"
        if password != confirm_password:
            return False, "Passwords do not match!"

        # Age validation (must be number between 1-150)
        try:
            age_int = int(age)
            if age_int <= 0 or age_int > 100:
                return False, "Age must be between 1 and 150!"
        except ValueError:
            return False, "Age must be a number!"

        # Weight validation (must be number between 1-150)
        try:
            weight_float = float(weight)
            if weight_float <= 0 or weight_float > 150:
                return False, "Weight must be between 1 and 500 kg!"
        except ValueError:
            return False, "Weight must be a number!"

        return True, ""

    def register_user(self, username, password, mail, age, weight):
        # Register a new user in the users table
        with self.lock:
            cursor = self.conn.cursor()
            try:
                cursor.execute('''
                    INSERT INTO users (username, password, mail, age, weight, training_days, training_time, level, points)
                    VALUES (?, ?, ?, ?, ?, 0, 0, 0, 0)
                ''', (username, password, mail, int(age), float(weight)))
                self.conn.commit()
                return True
            except sqlite3.IntegrityError:
                return False
            finally:
                cursor.close()

    def check_login(self, username, password):
        # Check user credentials for login
        with self.lock:
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT username, password, mail, age, weight, training_days, training_time, level, points
                FROM users 
                WHERE (username = ? OR mail = ?) AND password = ?
            ''', (username, username, password))
            user_data = cursor.fetchone()
            cursor.close()
            return user_data

    def generate_yoga_activities(self):
        # Define 5 yoga pose names
        yoga_poses = ["Downward Dog", "Tree Pose", "Warrior II", "Child's Pose", "Cobra Pose"]

        # Get all usernames from the users table
        with self.lock:
            cursor = self.conn.cursor()
            cursor.execute("SELECT username FROM users")
            usernames = [row[0] for row in cursor.fetchall()]
            cursor.close()

        if not usernames:
            return "No users found in the database!"

        # Generate random activities for each user
        current_date = datetime(2025, 3, 23)  # Use current date as reference
        one_year_ago = current_date - timedelta(days=365)

        with self.lock:
            cursor = self.conn.cursor()
            for username in usernames:
                num_activities = random.randint(50, 200)  # Random number of activities (50-200)
                for _ in range(num_activities):
                    # Random start time within the past year
                    random_days = random.randint(0, 364)
                    random_hour = random.randint(0, 23)
                    random_minute = random.randint(0, 59)
                    start_time = one_year_ago + timedelta(days=random_days, hours=random_hour, minutes=random_minute)

                    # Random duration between 5 and 20 minutes
                    duration = random.randint(5, 20)
                    end_time = start_time + timedelta(minutes=duration)

                    # Random yoga pose
                    yoga_pose = random.choice(yoga_poses)

                    # Insert activity into the activities table
                    cursor.execute('''
                        INSERT INTO activities (username, start_time, end_time, duration, yoga_pose)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (username, start_time.strftime('%Y-%m-%d %H:%M'),
                          end_time.strftime('%Y-%m-%d %H:%M'), duration, yoga_pose))
            self.conn.commit()
            cursor.close()
        return f"Generated yoga activities for {len(usernames)} users."

    def query_activities_by_username(self, username):
        # Query all activities for a specific username
        with self.lock:
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT username, start_time, end_time, duration, yoga_pose
                FROM activities
                WHERE username = ?
                ORDER BY start_time
            ''', (username,))
            activities = cursor.fetchall()
            cursor.close()

        if not activities:
            return f"No activities found for username: {username}"

        # Format the results as a list of dictionaries for better readability
        result = [
            {
                "username": row[0],
                "start_time": row[1],
                "end_time": row[2],
                "duration": row[3],
                "yoga_pose": row[4]
            }
            for row in activities
        ]
        return result

    def query_activities_by_date_and_pose(self, start_date, end_date):
        """
        Query activities by date range, returning dates, durations split by yoga pose, and pose names.
        Accepts QDate objects for start_date and end_date.

        Args:
            start_date (QDate): Start date as a QDate object
            end_date (QDate): End date as a QDate object

        Returns:
            tuple: (dates, durations, yoga_poses) where:
                - dates: List of unique dates in 'YYYY-MM-DD' format
                - durations: 2D list where durations[i][j] is the total duration for pose i on date j
                - yoga_poses: List of yoga pose names corresponding to the first dimension of durations
                - If no results or invalid input, returns a message string
        """

        # Convert QDate to string in 'YYYY-MM-DD' format
        start_date_str = start_date.toString("yyyy-MM-dd")
        end_date_str = end_date.toString("yyyy-MM-dd")

        # Ensure start_date is not after end_date
        if start_date > end_date:
            return "Start date must be before or equal to end date!"

        # Define the fixed list of yoga poses (consistent with generate_yoga_activities)
        yoga_poses = ["Downward Dog", "Tree Pose", "Warrior II", "Child's Pose", "Cobra Pose"]

        with self.lock:
            cursor = self.conn.cursor()
            # Query all activities within the date range
            cursor.execute('''
                SELECT start_time, duration, yoga_pose
                FROM activities
                WHERE start_time >= ? AND start_time <= ?
                ORDER BY start_time
            ''', (f"{start_date_str} 00:00", f"{end_date_str} 23:59"))

            activities = cursor.fetchall()
            cursor.close()

        if not activities:
            return f"No activities found for date range {start_date_str} to {end_date_str}."

        # Process results into date and duration structures
        date_set = set()  # To collect unique dates
        pose_date_duration = {pose: {} for pose in yoga_poses}  # Dictionary for each pose's date-duration pairs

        for start_time, duration, yoga_pose in activities:
            # Extract only the date part from start_time (YYYY-MM-DD)
            date = start_time.split()[0]
            date_set.add(date)
            # Sum durations for each pose on each date
            if date in pose_date_duration[yoga_pose]:
                pose_date_duration[yoga_pose][date] += duration
            else:
                pose_date_duration[yoga_pose][date] = duration

        # Convert to lists
        dates = sorted(date_set)  # Sort dates chronologically
        num_dates = len(dates)

        # Initialize 2D durations list: rows = number of poses, columns = number of dates
        durations = [[0] * num_dates for _ in range(len(yoga_poses))]

        # Fill the 2D list
        for pose_idx, pose in enumerate(yoga_poses):
            for date_idx, date in enumerate(dates):
                durations[pose_idx][date_idx] = pose_date_duration[pose].get(date, 0)

        return dates, durations, yoga_poses

    def close(self):
        # Close the database connection
        self.conn.close()

