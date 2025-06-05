# utils/database.py
import psycopg2
import re
from threading import Lock
import random
from datetime import datetime, timedelta

# --- PostgreSQL 连接信息 ---
DB_HOST = "47.120.75.108"
DB_NAME = "my_database3"
DB_USER = "postgres"
DB_PASSWORD = "123456."


# --- ---

class Database:
    def __init__(self, host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD):
        try:
            self.conn = psycopg2.connect(
                host=host,
                dbname=dbname,
                user=user,
                password=password
            )
            self.conn.autocommit = False
            self.lock = Lock()
            print("Database connection successful!")
            self.create_users_table()
            self.create_friends_table()
            self.create_activities_table()
            self.create_posts_table()
            self.create_comments_table()
            self.create_shop_courses_table()  # New table
            self.create_user_courses_table()  # New table

            # Initial data generation
            # Check if users exist before generating data that depends on users
            users_exist = self._execute_query("SELECT 1 FROM users LIMIT 1", fetch='one')
            if users_exist:
                self.generate_yoga_activities()
                self.generate_posts_data()
                self.generate_shop_courses_data()  # New data generation
                self.generate_user_courses_data()  # New data generation
            else:
                print("No users found. Skipping data generation for activities, posts, and courses.")

        except psycopg2.Error as e:
            print(f"Database connection error: {e}")
            self.conn = None
            self.lock = None

    def _execute_query(self, query, params=None, fetch=False, commit=False):
        if not self.conn or not self.lock:
            print("Database connection is not available.")
            return None

        with self.lock:
            cursor = None
            try:
                cursor = self.conn.cursor()
                cursor.execute(query, params)
                result = None
                if fetch == 'one':
                    result = cursor.fetchone()
                elif fetch == 'all':
                    result = cursor.fetchall()
                if commit:
                    self.conn.commit()
                return result
            except psycopg2.Error as e:
                if self.conn:
                    self.conn.rollback()
                print(f"Database Error: {e}")
                return None
            finally:
                if cursor:
                    cursor.close()

    def create_users_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
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
        '''
        self._execute_query(query, commit=True)

    def create_friends_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS friends (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                friend_username TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
                UNIQUE (user_id, friend_username)
            )
        '''
        self._execute_query(query, commit=True)

    def create_activities_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS activities (
                id SERIAL PRIMARY KEY,
                username TEXT NOT NULL,
                start_time TEXT NOT NULL,
                end_time TEXT NOT NULL,
                duration INTEGER NOT NULL,
                yoga_pose TEXT NOT NULL
            )
        '''
        self._execute_query(query, commit=True)
        index_query = "CREATE INDEX IF NOT EXISTS idx_activities_start_time ON activities (start_time);"
        self._execute_query(index_query, commit=True)

    def create_posts_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS posts (
                id SERIAL PRIMARY KEY,
                author_username TEXT NOT NULL,
                post_time TEXT NOT NULL,
                content TEXT NOT NULL,
                image_url TEXT,
                video_url TEXT,
                likes INTEGER DEFAULT 0,
                favorites INTEGER DEFAULT 0,
                FOREIGN KEY (author_username) REFERENCES users(username) ON DELETE CASCADE
            )
        '''
        self._execute_query(query, commit=True)

    def create_comments_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS comments (
                id SERIAL PRIMARY KEY,
                post_id INTEGER NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
                commenter_username TEXT NOT NULL REFERENCES users(username) ON DELETE CASCADE,
                comment_time TEXT NOT NULL,
                content TEXT NOT NULL,
                FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
                FOREIGN KEY (commenter_username) REFERENCES users(username) ON DELETE CASCADE
            )
        '''
        self._execute_query(query, commit=True)

    def create_shop_courses_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS shop_courses (
                id SERIAL PRIMARY KEY,
                course_name TEXT UNIQUE NOT NULL,
                course_description TEXT,
                points_required INTEGER DEFAULT 1000,
                image_path TEXT DEFAULT 'E:\\Python\\projects_2025\\YOLO\\YOLO_YUJIA\\image_test\\File1.jpeg',
                video_path TEXT DEFAULT 'E:\\Python\\projects_2025\\YOLO\\YOLO_YUJIA\\image_test\\a572aebe6f920fc91b6fc5b226550a2b.mp4'
            )
        '''
        self._execute_query(query, commit=True)

    def create_user_courses_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS user_courses (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                username TEXT NOT NULL, -- For convenience, though user_id is the key
                course_name TEXT NOT NULL, -- Name of the course, should match shop_courses.course_name
                purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (course_name) REFERENCES shop_courses(course_name) ON DELETE CASCADE, -- Ensures course exists
                UNIQUE (user_id, course_name) -- Prevents user from buying the same course multiple times
            )
        '''
        self._execute_query(query, commit=True)

    def validate_input(self, username, password, mail, age, weight, confirm_password):
        if not all([username, password, mail, age, weight, confirm_password]):
            return False, "All fields must be filled!"
        if not re.match(r'^[a-zA-Z0-9]{3,20}$', username):
            return False, "Username must be 3-20 alphanumeric characters!"
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', mail):
            return False, "Please enter a valid email address!"
        if len(password) < 6 or len(password) > 20:
            return False, "Password must be 6-20 characters!"
        if password != confirm_password:
            return False, "Passwords do not match!"
        try:
            age_int = int(age)
            if age_int <= 0 or age_int > 150:
                return False, "Age must be between 1 and 150!"
        except ValueError:
            return False, "Age must be a number!"
        try:
            weight_float = float(weight)
            if weight_float <= 0 or weight_float > 500:
                return False, "Weight must be between 1 and 500 kg!"
        except ValueError:
            return False, "Weight must be a number!"
        return True, ""

    def register_user(self, username, password, mail, age, weight):
        query = '''
            INSERT INTO users (username, password, mail, age, weight, training_days, training_time, level, points)
            VALUES (%s, %s, %s, %s, %s, 0, 0, 0, 0)
        '''
        params = (username, password, mail, int(age), float(weight))
        # Re-using _execute_query for INSERT and handling potential errors
        # This simplified version assumes _execute_query can handle the specifics if adapted,
        # or you stick to the original detailed try-except block for registration.
        # For now, keeping original detailed block for register_user.
        with self.lock:
            cursor = None
            try:
                cursor = self.conn.cursor()
                cursor.execute(query, params)
                self.conn.commit()
                return True
            except psycopg2.IntegrityError as e:
                self.conn.rollback()
                if 'users_username_key' in str(e):
                    print(f"Registration failed: Username '{username}' already exists.")
                elif 'users_mail_key' in str(e):
                    print(f"Registration failed: Email '{mail}' already exists.")
                else:
                    print(f"Registration failed due to integrity error: {e}")
                return False
            except psycopg2.Error as e:
                self.conn.rollback()
                print(f"Database Error during registration: {e}")
                return False
            finally:
                if cursor:
                    cursor.close()

    def check_login(self, username, password):
        # CRITICAL FIX: Added 'id' to the SELECT statement
        query = '''
            SELECT id, username, password, mail, age, weight, training_days, training_time, level, points
            FROM users
            WHERE (username = %s OR mail = %s) AND password = %s
        '''
        user_data_tuple = self._execute_query(query, (username, username, password), fetch='one')
        if user_data_tuple:
            return user_data_tuple
        return None

    def add_friend(self, user_id, friend_username):
        check_friend_query = "SELECT id FROM users WHERE username = %s"
        friend_exists = self._execute_query(check_friend_query, (friend_username,), fetch='one')
        if not friend_exists:
            return False, "Friend username does not exist!"

        get_self_username_query = "SELECT username FROM users WHERE id = %s"
        self_username_tuple = self._execute_query(get_self_username_query, (user_id,), fetch='one')
        if not self_username_tuple or self_username_tuple[0] == friend_username:
            return False, "You cannot add yourself as a friend!"

        insert_query = '''
            INSERT INTO friends (user_id, friend_username)
            VALUES (%s, %s)
        '''
        # Simplified with _execute_query, but original detailed block for add_friend is fine too.
        # Sticking to original for nuanced error messages.
        with self.lock:
            cursor = None
            try:
                cursor = self.conn.cursor()
                cursor.execute(insert_query, (user_id, friend_username))
                self.conn.commit()
                return True, "Friend added successfully!"
            except psycopg2.IntegrityError:
                self.conn.rollback()
                return False, "Friend relationship already exists!"
            except psycopg2.Error as e:
                self.conn.rollback()
                print(f"Database Error adding friend: {e}")
                return False, f"Error adding friend: {e}"
            finally:
                if cursor:
                    cursor.close()

    def get_friends(self, user_id):
        query = "SELECT friend_username FROM friends WHERE user_id = %s"
        results = self._execute_query(query, (user_id,), fetch='all')
        return [row[0] for row in results] if results else []


    def are_friends(self, user_id, potential_friend_username):
        """Checks if user_id is already friends with potential_friend_username."""
        query = "SELECT 1 FROM friends WHERE user_id = %s AND friend_username = %s"
        result = self._execute_query(query, (user_id, potential_friend_username), fetch='one')
        return result is not None

    def create_post(self, author_username, content, image_url=None, video_url=None):
        query = '''
            INSERT INTO posts (author_username, post_time, content, image_url, video_url)
            VALUES (%s, %s, %s, %s, %s)
        '''
        post_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        params = (author_username, post_time, content, image_url, video_url)
        # _execute_query returns None on error or if commit is True and fetch is not specified.
        # We need a way to confirm success, e.g., by checking if an exception was raised.
        # For INSERTs, it's better to handle commit and rollback explicitly or ensure _execute_query signals success.
        # Assuming if _execute_query doesn't return specific error, it's okay.
        return self._execute_query(query, params, commit=True) is not None  # Simple check

    def get_posts(self, username=None):
        if username:
            query = '''
                SELECT id, author_username, post_time, content, image_url, video_url, likes, favorites
                FROM posts
                WHERE author_username = %s
                ORDER BY post_time DESC
            '''
            params = (username,)
        else:
            query = '''
                SELECT id, author_username, post_time, content, image_url, video_url, likes, favorites
                FROM posts
                ORDER BY post_time DESC
            '''
            params = None
        results = self._execute_query(query, params, fetch='all')
        if results is None: return []
        return [{
            "id": row[0], "author_username": row[1], "post_time": row[2],
            "content": row[3], "image_url": row[4], "video_url": row[5],
            "likes": row[6], "favorites": row[7]
        } for row in results]

    def add_comment(self, post_id, commenter_username, content):
        query = '''
            INSERT INTO comments (post_id, commenter_username, comment_time, content)
            VALUES (%s, %s, %s, %s)
        '''
        comment_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        params = (post_id, commenter_username, comment_time, content)
        return self._execute_query(query, params, commit=True) is not None

    def get_comments(self, post_id):
        query = '''
            SELECT id, post_id, commenter_username, comment_time, content
            FROM comments
            WHERE post_id = %s
            ORDER BY comment_time ASC
        '''
        results = self._execute_query(query, (post_id,), fetch='all')
        if results is None: return []
        return [{
            "id": row[0], "post_id": row[1], "commenter_username": row[2],
            "comment_time": row[3], "content": row[4]
        } for row in results]

    def generate_yoga_activities(self):
        check_query = "SELECT COUNT(*) FROM activities LIMIT 1"
        count_result = self._execute_query(check_query, fetch='one')
        if count_result and count_result[0] > 0:
            print("Yoga activities data already exists. Skipping generation.")
            return
        # ... (rest of the method remains the same)
        yoga_poses = ["Downward Dog", "Tree Pose", "Warrior II", "Child's Pose", "Cobra Pose"]
        get_users_query = "SELECT username FROM users"
        users_result = self._execute_query(get_users_query, fetch='all')
        if not users_result: return "No users found."
        usernames = [row[0] for row in users_result]
        current_date = datetime(2025, 3, 23)
        one_year_ago = current_date - timedelta(days=365)
        insert_query = 'INSERT INTO activities (username, start_time, end_time, duration, yoga_pose) VALUES (%s, %s, %s, %s, %s)'
        activities_to_insert = []
        for username in usernames:
            num_activities = random.randint(50, 200)
            for _ in range(num_activities):
                random_days = random.randint(0, 364)
                random_hour = random.randint(0, 23);
                random_minute = random.randint(0, 59)
                start_time = one_year_ago + timedelta(days=random_days, hours=random_hour, minutes=random_minute)
                duration = random.randint(5, 20)
                end_time = start_time + timedelta(minutes=duration)
                yoga_pose = random.choice(yoga_poses)
                activities_to_insert.append((username, start_time.strftime('%Y-%m-%d %H:%M'),
                                             end_time.strftime('%Y-%m-%d %H:%M'), duration, yoga_pose))
        if activities_to_insert:
            with self.lock:
                cursor = None
                try:
                    cursor = self.conn.cursor()
                    cursor.executemany(insert_query, activities_to_insert)
                    self.conn.commit()
                    print(f"Generated yoga activities for {len(usernames)} users.")
                except psycopg2.Error as e:
                    self.conn.rollback();
                    print(f"DB Error generating yoga activities: {e}")
                finally:
                    if cursor: cursor.close()

    def query_activities_by_username(self, username):
        # ... (method remains the same)
        query = 'SELECT username, start_time, end_time, duration, yoga_pose FROM activities WHERE username = %s ORDER BY start_time'
        results = self._execute_query(query, (username,), fetch='all')
        if results is None: return f"Error querying activities for {username}"
        if not results: return f"No activities for {username}"
        return [{"username": r[0], "start_time": r[1], "end_time": r[2], "duration": r[3], "yoga_pose": r[4]} for r in
                results]

    def query_activities_by_date_and_pose(self, start_date, end_date):
        # ... (method remains the same)
        try:
            start_date_str = start_date.toString("yyyy-MM-dd") if hasattr(start_date, 'toString') else str(start_date)
            end_date_str = end_date.toString("yyyy-MM-dd") if hasattr(end_date, 'toString') else str(end_date)
            datetime.strptime(start_date_str, '%Y-%m-%d');
            datetime.strptime(end_date_str, '%Y-%m-%d')
        except (ValueError, AttributeError) as e:
            return f"Invalid date: {e}. Use 'YYYY-MM-DD' or QDate."
        if start_date_str > end_date_str: return "Start date must be <= end date."
        yoga_poses = ["Downward Dog", "Tree Pose", "Warrior II", "Child's Pose", "Cobra Pose"]
        query = 'SELECT start_time, duration, yoga_pose FROM activities WHERE start_time >= %s AND start_time <= %s ORDER BY start_time'
        params = (f"{start_date_str} 00:00", f"{end_date_str} 23:59")
        activities = self._execute_query(query, params, fetch='all')
        if activities is None: return f"Error querying activities."
        if not activities: return f"No activities found for date range."
        date_set = set();
        pose_date_duration = {pose: {} for pose in yoga_poses}
        for start_time_str, duration, yoga_pose in activities:
            try:
                date = start_time_str.split()[0];
                datetime.strptime(date, '%Y-%m-%d')
                date_set.add(date)
                if yoga_pose in pose_date_duration:
                    pose_date_duration[yoga_pose][date] = pose_date_duration[yoga_pose].get(date, 0) + duration
            except (IndexError, ValueError):
                print(f"Skipping activity: invalid start_time {start_time_str}"); continue
        if not date_set: return f"No valid activities in range after filtering."
        dates = sorted(list(date_set));
        num_dates = len(dates)
        durations_matrix = [[0] * num_dates for _ in range(len(yoga_poses))]
        for pose_idx, pose in enumerate(yoga_poses):
            for date_idx, date in enumerate(dates):
                durations_matrix[pose_idx][date_idx] = pose_date_duration[pose].get(date, 0)
        return dates, durations_matrix, yoga_poses

    def generate_posts_data(self):
        check_query = "SELECT COUNT(*) FROM posts LIMIT 1"
        count_result = self._execute_query(check_query, fetch='one')
        if count_result and count_result[0] > 0:
            print("Posts data already exists. Skipping generation.")
            return
        # ... (rest of the method remains the same)
        get_users_query = "SELECT username FROM users";
        users_result = self._execute_query(get_users_query, fetch='all')
        if not users_result: return "No users found."
        usernames = [row[0] for row in users_result]
        image_url = r"E:\Python\projects_2025\YOLO\YOLO_YUJIA\image_test\File1.jpeg"
        video_url = r"E:\Python\projects_2025\YOLO\YOLO_YUJIA\image_test\a572aebe6f920fc91b6fc5b226550a2b.mp4"
        content_templates = ["Today is a {} day!", "Just finished {}!", "Feeling {} today", "My {} experience",
                             "Sharing some {} thoughts"]
        adjectives = ["great", "wonderful", "tired", "exciting", "peaceful"];
        nouns = ["yoga", "work", "meal", "journey", "moment"]
        comment_templates = ["Wow, {} post!", "I {} this!", "Looks {}!", "Really {} content", "Thanks for {} this"]
        post_insert_query = 'INSERT INTO posts (author_username, post_time, content, image_url, video_url, likes, favorites) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id'
        comment_insert_query = 'INSERT INTO comments (post_id, commenter_username, comment_time, content) VALUES (%s, %s, %s, %s)'
        with self.lock:
            cursor = None
            try:
                cursor = self.conn.cursor();
                generated_posts_count = 0;
                generated_comments_count = 0
                for _ in range(3):
                    author = random.choice(usernames)
                    content_base = random.choice(content_templates)
                    word = random.choice(adjectives if '{}' in content_base and 'day' in content_base else nouns)
                    content = content_base.format(word)
                    post_time_dt = datetime.now() - timedelta(days=random.randint(0, 6), hours=random.randint(0, 23),
                                                              minutes=random.randint(0, 59))
                    post_time_str = post_time_dt.strftime('%Y-%m-%d %H:%M:%S')
                    likes = random.randint(0, 100);
                    favorites = random.randint(0, 50)
                    cursor.execute(post_insert_query,
                                   (author, post_time_str, content, image_url, video_url, likes, favorites))
                    post_id_tuple = cursor.fetchone()
                    if not post_id_tuple: self.conn.rollback(); continue
                    post_id = post_id_tuple[0];
                    generated_posts_count += 1
                    comments_to_insert = []
                    for _ in range(3):
                        commenter = random.choice(usernames)
                        comment_content = random.choice(comment_templates).format(random.choice(adjectives))
                        comment_time_dt = post_time_dt + timedelta(minutes=random.randint(1, 1440))
                        comment_time_dt = min(comment_time_dt, datetime.now())
                        comment_time_str = comment_time_dt.strftime('%Y-%m-%d %H:%M:%S')
                        comments_to_insert.append((post_id, commenter, comment_time_str, comment_content))
                    if comments_to_insert: cursor.executemany(comment_insert_query,
                                                              comments_to_insert); generated_comments_count += len(
                        comments_to_insert)
                self.conn.commit()
                print(f"Generated {generated_posts_count} posts and {generated_comments_count} comments.")
            except psycopg2.Error as e:
                self.conn.rollback(); print(f"DB Error generating posts/comments: {e}")
            finally:
                if cursor: cursor.close()

    def generate_shop_courses_data(self):
        check_query = "SELECT COUNT(*) FROM shop_courses"
        count_result = self._execute_query(check_query, fetch='one')
        if count_result and count_result[0] > 0:
            print("Shop courses data already exists. Skipping generation.")
            return

        courses_to_insert = []
        base_image_path = r"E:\Python\projects_2025\YOLO\YOLO_YUJIA\image_test\File1.jpeg"
        base_video_path = r"E:\Python\projects_2025\YOLO\YOLO_YUJIA\image_test\a572aebe6f920fc91b6fc5b226550a2b.mp4"

        course_names = [
            "Introduction to Hatha Yoga", "Vinyasa Flow Essentials", "Yin Yoga for Deep Stretch",
            "Power Yoga Challenge", "Restorative Yoga for Relaxation", "Meditation and Pranayama",
            "Ashtanga Primary Series Intro", "Yoga for Back Pain Relief", "Advanced Inversions Workshop",
            "Prenatal Yoga Gentle Flow"
        ]
        course_descriptions = [
            "A beginner-friendly introduction to fundamental yoga postures and breathing techniques.",
            "Learn to link breath with movement in this dynamic and energizing Vinyasa class.",
            "Hold passive poses for longer periods to target deep connective tissues and increase flexibility.",
            "Build strength, stamina, and flexibility with this challenging Power Yoga sequence.",
            "Calm your nervous system and promote healing with gentle, supported restorative poses.",
            "Explore various meditation techniques and yogic breathing exercises (pranayama) for mental clarity.",
            "An introduction to the foundational sequence of Ashtanga yoga.",
            "Specific yoga poses and sequences designed to alleviate and prevent back pain.",
            "Master challenging inversions like headstands and handstands with proper technique and safety.",
            "Safe and gentle yoga practices tailored for expectant mothers at all stages of pregnancy."
        ]

        for i in range(10):
            course_name = course_names[i]
            description = course_descriptions[i]
            points = random.randint(800, 1500)  # Random points, or keep it 1000
            # For simplicity, using the same image/video for all, or you can have a list of paths
            courses_to_insert.append((course_name, description, points, base_image_path, base_video_path))

        query = '''
            INSERT INTO shop_courses (course_name, course_description, points_required, image_path, video_path)
            VALUES (%s, %s, %s, %s, %s)
        '''
        if courses_to_insert:
            with self.lock:
                cursor = None
                try:
                    cursor = self.conn.cursor()
                    cursor.executemany(query, courses_to_insert)
                    self.conn.commit()
                    print(f"Generated {len(courses_to_insert)} shop courses.")
                except psycopg2.Error as e:
                    self.conn.rollback()
                    print(f"Database Error generating shop courses: {e}")
                finally:
                    if cursor:
                        cursor.close()

    def generate_user_courses_data(self):
        check_query = "SELECT COUNT(*) FROM user_courses"
        count_result = self._execute_query(check_query, fetch='one')
        if count_result and count_result[0] > 0:
            print("User courses data already exists. Skipping generation.")
            return

        users_query = "SELECT id, username FROM users"
        users = self._execute_query(users_query, fetch='all')
        if not users:
            print("No users found to generate user courses.")
            return

        shop_courses_query = "SELECT course_name FROM shop_courses"
        shop_courses_results = self._execute_query(shop_courses_query, fetch='all')
        if not shop_courses_results:
            print("No shop courses found to assign to users.")
            return

        available_course_names = [row[0] for row in shop_courses_results]
        if not available_course_names:
            print("No available course names from shop_courses.")
            return

        user_courses_to_insert = []
        for user_id, username in users:
            num_courses_to_add = random.randint(1, min(3, len(available_course_names)))
            if not available_course_names: continue  # Should not happen if check above is done

            # Ensure user doesn't get assigned the same course multiple times in this generation step
            # and that we don't pick more courses than available.
            courses_for_this_user = random.sample(available_course_names,
                                                  k=min(num_courses_to_add, len(available_course_names)))

            for course_name in courses_for_this_user:
                user_courses_to_insert.append((user_id, username, course_name))

        query = '''
            INSERT INTO user_courses (user_id, username, course_name)
            VALUES (%s, %s, %s)
            ON CONFLICT (user_id, course_name) DO NOTHING -- Avoid errors if somehow a duplicate is generated (shouldn't with sample)
        '''
        if user_courses_to_insert:
            with self.lock:
                cursor = None
                try:
                    cursor = self.conn.cursor()
                    cursor.executemany(query, user_courses_to_insert)
                    self.conn.commit()
                    print(f"Generated user courses for {len(users)} users.")
                except psycopg2.Error as e:
                    self.conn.rollback()
                    print(f"Database Error generating user courses: {e}")
                finally:
                    if cursor:
                        cursor.close()

    def get_shop_courses(self):
        query = "SELECT id, course_name, course_description, points_required, image_path, video_path FROM shop_courses"
        results = self._execute_query(query, fetch='all')
        if results is None: return []
        return [{
            "id": row[0], "name": row[1], "description": row[2],
            "points_required": row[3], "image_path": row[4], "video_path": row[5]
        } for row in results]

    def get_user_purchased_courses(self, user_id):
        # Joins user_courses with shop_courses to get full details
        query = """
            SELECT sc.id, sc.course_name, sc.course_description, sc.points_required, sc.image_path, sc.video_path
            FROM user_courses uc
            JOIN shop_courses sc ON uc.course_name = sc.course_name
            WHERE uc.user_id = %s
        """
        results = self._execute_query(query, (user_id,), fetch='all')
        if results is None: return []
        return [{
            "id": row[0], "name": row[1], "description": row[2],
            "points_required": row[3], "image_path": row[4], "video_path": row[5]
        } for row in results]

    def get_user_info(self, user_id):  # Utility to get fresh user info like points
        query = "SELECT id, username, points FROM users WHERE id = %s"
        result = self._execute_query(query, (user_id,), fetch='one')
        if result:
            return {"id": result[0], "username": result[1], "points": result[2]}
        return None

    def get_course_details_by_name(self, course_name):
        query = "SELECT id, course_name, course_description, points_required, image_path, video_path FROM shop_courses WHERE course_name = %s"
        result = self._execute_query(query, (course_name,), fetch='one')
        if result:
            return {
                "id": result[0], "name": result[1], "description": result[2],
                "points_required": result[3], "image_path": result[4], "video_path": result[5]
            }
        return None

    def purchase_course(self, user_id, username, course_name, course_points_required):
        with self.lock:
            cursor = None
            try:
                cursor = self.conn.cursor()
                # 1. Check if user already owns the course
                cursor.execute("SELECT 1 FROM user_courses WHERE user_id = %s AND course_name = %s",
                               (user_id, course_name))
                if cursor.fetchone():
                    return False, "Course already purchased."

                # 2. Check user points
                cursor.execute("SELECT points FROM users WHERE id = %s", (user_id,))
                user_points_tuple = cursor.fetchone()
                if not user_points_tuple or user_points_tuple[0] < course_points_required:
                    return False, "Not enough points."

                # 3. Deduct points
                new_points = user_points_tuple[0] - course_points_required
                cursor.execute("UPDATE users SET points = %s WHERE id = %s", (new_points, user_id))

                # 4. Add course to user_courses
                cursor.execute("INSERT INTO user_courses (user_id, username, course_name) VALUES (%s, %s, %s)",
                               (user_id, username, course_name))

                self.conn.commit()
                return True, "Course purchased successfully."
            except psycopg2.Error as e:
                self.conn.rollback()
                print(f"Database error during course purchase: {e}")
                return False, f"Database error: {e}"
            finally:
                if cursor:
                    cursor.close()

    def add_user_points(self, user_id, points_to_add):
        query = "UPDATE users SET points = points + %s WHERE id = %s RETURNING points"
        with self.lock:  # Ensure thread safety for point updates
            cursor = None
            try:
                cursor = self.conn.cursor()
                cursor.execute(query, (points_to_add, user_id))
                updated_points_tuple = cursor.fetchone()
                self.conn.commit()
                if updated_points_tuple:
                    return True, updated_points_tuple[0]  # Return success and new total points
                return False, "Failed to update points or user not found."
            except psycopg2.Error as e:
                if self.conn: self.conn.rollback()
                print(f"Database Error adding points: {e}")
                return False, str(e)
            finally:
                if cursor: cursor.close()

    def count_user_courses(self, user_id):
        query = "SELECT COUNT(*) FROM user_courses WHERE user_id = %s"
        result = self._execute_query(query, (user_id,), fetch='one')
        return result[0] if result else 0

    def admin_get_all_user_details(self):
        query = """
            SELECT id, username, password, mail, age, weight, 
                   training_days, training_time, level, points 
            FROM users ORDER BY id ASC
        """
        results = self._execute_query(query, fetch='all')
        if results is None: return None
        keys = ["id", "username", "password", "mail", "age", "weight",
                "training_days", "training_time", "level", "points"]
        return [dict(zip(keys, row)) for row in results]

    def admin_add_user(self, username, password, mail, age, weight, points=0, level=0, training_days=0,
                       training_time=0):
        query = '''
            INSERT INTO users (username, password, mail, age, weight, points, level, training_days, training_time)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id
        '''
        # Note: Storing plain text password as per existing structure. Hashing is recommended.
        params = (username, password, mail, int(age), float(weight), int(points), int(level), int(training_days),
                  int(training_time))
        result = self._execute_query(query, params, commit=True, fetch='one')
        return result is not None

    def admin_update_user(self, user_id, data_dict):
        # data_dict = {'column_name': new_value, ...}
        if not data_dict: return False
        set_clauses = [f"{key} = %s" for key in data_dict.keys()]
        query = f"UPDATE users SET {', '.join(set_clauses)} WHERE id = %s"
        params = list(data_dict.values()) + [user_id]
        self._execute_query(query, tuple(params), commit=True)
        return True  # Assuming success if no exception

    def admin_delete_user(self, user_id):
        # Consider cascading deletes defined in DB schema or manual cleanup of related data
        # For example, posts by this user, comments, friends, user_courses, activities.
        # If ON DELETE CASCADE is set for foreign keys, much of this is automatic.
        # For this example, we rely on DB cascades for posts, comments, user_courses, friends.
        # Activities might need manual consideration if not cascaded and you want them removed.

        # Explicitly delete related activities if not handled by cascade and desired
        self._execute_query("DELETE FROM activities WHERE username = (SELECT username FROM users WHERE id = %s)",
                            (user_id,), commit=False)  # commit with user delete

        query = "DELETE FROM users WHERE id = %s"
        self._execute_query(query, (user_id,), commit=True)
        return True

    # --- Shop Course Management ---
    def admin_get_all_shop_courses(self):  # Renamed to avoid conflict, effectively same as get_shop_courses
        return self.get_shop_courses()  # Reuse existing method

    def admin_add_shop_course(self, name, description, points, image_path, video_path):
        query = '''
            INSERT INTO shop_courses (course_name, course_description, points_required, image_path, video_path)
            VALUES (%s, %s, %s, %s, %s) RETURNING id
        '''
        params = (name, description, int(points), image_path, video_path)
        result = self._execute_query(query, params, commit=True, fetch='one')
        return result is not None

    def admin_update_shop_course(self, course_id, data_dict):
        if not data_dict: return False
        set_clauses = [f"{key} = %s" for key in data_dict.keys()]
        # Ensure correct column names from shop_courses table
        # e.g., course_name, course_description, points_required, image_path, video_path
        query = f"UPDATE shop_courses SET {', '.join(set_clauses)} WHERE id = %s"
        params = list(data_dict.values()) + [course_id]
        self._execute_query(query, tuple(params), commit=True)
        return True

    def admin_delete_shop_course(self, course_id):
        # User_courses referencing this course via course_name might cause issues if not ON DELETE CASCADE
        # Or handle by preventing deletion if courses are purchased.
        # For simplicity, assuming ON DELETE CASCADE or admin understands implications.
        query = "DELETE FROM shop_courses WHERE id = %s"
        self._execute_query(query, (course_id,), commit=True)
        return True

    # --- Post Management ---
    def admin_get_all_posts(self):
        query = '''
            SELECT id, author_username, post_time, content, image_url, video_url, likes, favorites
            FROM posts ORDER BY post_time DESC
        '''
        results = self._execute_query(query, fetch='all')
        if results is None: return None
        keys = ["id", "author_username", "post_time", "content", "image_url", "video_url", "likes", "favorites"]
        return [dict(zip(keys, row)) for row in results]

    def admin_add_post(self, author_username, content, image_url=None, video_url=None):
        # Admin posting might use a specific "admin" username or the actual admin's username
        return self.create_post(author_username, content, image_url, video_url) is not None

    def admin_update_post(self, post_id, data_dict):
        # Typically, admin might edit 'content', 'image_url', 'video_url'
        if not data_dict: return False
        set_clauses = [f"{key} = %s" for key in data_dict.keys()]
        query = f"UPDATE posts SET {', '.join(set_clauses)} WHERE id = %s"
        params = list(data_dict.values()) + [post_id]
        self._execute_query(query, tuple(params), commit=True)
        return True

    def admin_delete_post(self, post_id):
        # Comments associated with this post should be deleted by ON DELETE CASCADE
        query = "DELETE FROM posts WHERE id = %s"
        self._execute_query(query, (post_id,), commit=True)
        return True

    # --- Comment Management ---
    def admin_get_comments_for_post(self, post_id):
        # Same as get_comments, but for admin context
        return self.get_comments(post_id)  # Returns list of dicts

    def admin_add_comment(self, post_id, commenter_username, content):
        # Admin might use their own username or a generic "Admin" username
        return self.add_comment(post_id, commenter_username, content)

    def admin_update_comment(self, comment_id, content):
        query = "UPDATE comments SET content = %s WHERE id = %s"
        self._execute_query(query, (content, comment_id), commit=True)
        return True

    def admin_delete_comment(self, comment_id):
        query = "DELETE FROM comments WHERE id = %s"
        self._execute_query(query, (comment_id,), commit=True)
        return True

    # --- Read-only Table Views ---
    def admin_get_all_user_courses(self):
        query = """
            SELECT uc.id, uc.user_id, u.username as user_username, uc.course_name, sc.course_description, uc.purchase_date
            FROM user_courses uc
            JOIN users u ON uc.user_id = u.id
            JOIN shop_courses sc ON uc.course_name = sc.course_name
            ORDER BY uc.purchase_date DESC
        """
        results = self._execute_query(query, fetch='all')
        if results is None: return None
        keys = ["id", "user_id", "user_username", "course_name", "course_description", "purchase_date"]
        return [dict(zip(keys, row)) for row in results]

    def admin_get_all_activities(self):
        query = "SELECT id, username, start_time, end_time, duration, yoga_pose FROM activities ORDER BY start_time DESC"
        results = self._execute_query(query, fetch='all')
        if results is None: return None
        keys = ["id", "username", "start_time", "end_time", "duration", "yoga_pose"]
        return [dict(zip(keys, row)) for row in results]

    def admin_get_all_friends(self):
        query = """
            SELECT f.id, f.user_id, u.username as user_username, f.friend_username 
            FROM friends f
            JOIN users u ON f.user_id = u.id
            ORDER BY f.user_id ASC, f.friend_username ASC
        """
        results = self._execute_query(query, fetch='all')
        if results is None: return None
        keys = ["id", "user_id", "user_username", "friend_username"]
        return [dict(zip(keys, row)) for row in results]

    def close(self):
        if self.conn:
            try:
                self.conn.close()
                print("Database connection closed.")
            except psycopg2.Error as e:
                print(f"Error closing database connection: {e}")
            finally:
                self.conn = None