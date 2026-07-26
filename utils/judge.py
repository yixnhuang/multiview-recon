import sqlite3
import os

# Database path
db_path = "database.db"  # Replace with the path to your database.db file

if not os.path.exists(db_path):
    print("Database file does not exist:", db_path)
    exit(1)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Query the number of keypoints in each image
cursor.execute("""
    SELECT name, rows
    FROM images
    JOIN (SELECT image_id, COUNT(*) AS rows FROM keypoints GROUP BY image_id) AS kp
    ON images.image_id = kp.image_id
""")
features = cursor.fetchall()

print("Number of keypoints in each image:")
for name, count in features:
    print(f"{name}: {count} keypoints")

# Query how many other images match each image
cursor.execute("""
    SELECT im1.name, COUNT(DISTINCT im2.id) as matched_images
    FROM matches AS m
    JOIN images AS im1 ON m.image_id1 = im1.image_id
    JOIN images AS im2 ON m.image_id2 = im2.image_id
    GROUP BY im1.name
""")
matches = cursor.fetchall()

print("\nNumber of matched images for each image:")
for name, matched_count in matches:
    print(f"{name}: {matched_count} matched images")
    
conn.close()
