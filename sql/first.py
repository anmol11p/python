
#! 🟦 1. DDL – Data Definition Language
# Used to define / modify database structure (schema).
# They affect the structure, not the data.
# Auto-committed (once executed, can’t be rolled back).

# Command	Description	Example
# CREATE	Creates database objects (table, DB, view, etc.)	CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(50));
# ALTER	Modifies existing table structure	ALTER TABLE users ADD email VARCHAR(100);
# DROP	Deletes entire table / DB	DROP TABLE users;
# TRUNCATE	Removes all rows from table, keeps structure	TRUNCATE TABLE users;
# RENAME	Renames table	RENAME TABLE users TO customers;

#! 🟩 2. DML – Data Manipulation Language

# Used to manipulate data inside tables.
# These can be rolled back if inside a transaction.

# Command	Description	Example
# INSERT	Adds new records	INSERT INTO users (id, name) VALUES (1, 'Anmol');
# UPDATE	Modifies existing records	UPDATE users SET name='Pandey' WHERE id=1;
# DELETE	Removes records (based on condition)	DELETE FROM users WHERE id=1;

# 👉 CRUD operations correspond to:

# Create → INSERT

# Read → SELECT (DQL)

# Update → UPDATE

# Delete → DELETE

#! 🟨 3. DQL – Data Query Language

# Used to fetch / query data from database.

# Command	Description	Example
# SELECT	Retrieves data	SELECT * FROM users;

# 👉 SELECT can be combined with WHERE, ORDER BY, GROUP BY, JOIN, etc.

#! 🟧 4. TCL – Transaction Control Language

# Used to manage transactions — i.e. groups of DML operations.

# Command	Description	Example
# COMMIT	Saves all changes made in current transaction	COMMIT;
# ROLLBACK	Reverts changes since last commit	ROLLBACK;
# SAVEPOINT	Sets a point to roll back to	SAVEPOINT sp1;
# SET TRANSACTION	Starts a new transaction	SET TRANSACTION READ WRITE;


#! 🟥 5. DCL – Data Control Language

# Used to control access / permissions.

# Command	Description	Example
# GRANT	Gives user access rights	GRANT SELECT, INSERT ON users TO 'anmol'@'localhost';
# REVOKE	Removes access rights	REVOKE INSERT ON users FROM 'anmol'@'localhost';

# ✅ Summary Table:

# Category	Full Form	Purpose	Main Commands
# DDL	Data Definition Language	Define structure	CREATE, ALTER, DROP, TRUNCATE, RENAME
# DML	Data Manipulation Language	Manipulate data	INSERT, UPDATE, DELETE
# DQL	Data Query Language	Query data	SELECT
# TCL	Transaction Control Language	Manage transactions	COMMIT, ROLLBACK, SAVEPOINT
# DCL	Data Control Language	Manage permissions	GRANT, REVOKE



#?=========================constraint============================



#?  keys
#! 1. Primary Key - not null unique
#! 2. Foreing Key - Establishes a relationship between two tables.
#                 - It references the primary key of another table.     

#! 3. Unique Key - all values in a column (or group of a columns ) is unique

#! 4. Composite Key - A combination of two or more columns used to uniquely identify a record.
#                   - Used when no single column is unique by itself.
#                     primary key (user_id ,course_id)  


#!5. Candidate Key -  All columns that can be a primary key.
#                     From these, one is chosen as the primary key.


#!6. Alternate Key - A candidate key not selected as the primary key.
# student_id = Primary Key
# email = Alternate Key


#!7. Super Key - Any combination of columns that uniquely identifies a row.
# Every primary key is a super key, but not every super key is a primary key.





#? ========================crud============================= 
#* create

# create database leafnity
# create table user (id int not null unique,name varchar(50),salary int not null)
# insert into user  values(1,"anmol",20000),(1,"aman",20001)

#* read 
# select * from user 
# select * from user where name= "anmol"

#* update
# update user set name="anubhav" where name ="anmol"

#* delete
# delete from user where id =2

#? join 

# A JOIN in SQL is used to combine data from two or more tables based on a related column (usually a foreign key).

#? types of join 

#! 1. INNER JOIN

# 👉 Returns only matching records from both tables.

'''
select user.name,course.course_name 
from users 
inner join course 
on users.id=course.user_id
'''

#! 2. LEFT JOIN (or LEFT OUTER JOIN)
# 👉 Returns all rows from the left table (users),
# and the matching rows from the right (course).
# If no match → returns NULL.

'''
select user.name,cours.course_name 
from users
left join course 
on users.id=course.user_id
'''

# name	course_name
# Anmol	React
# Neha	Node.js
# Anmol	MySQL
#? Rahul	NULL  🧩 Rahul appears even though he has no course.


#! 3. RIGHT JOIN (or RIGHT OUTER JOIN)

# 👉 Returns all rows from the right table (course),
# and the matching rows from the left (users).

'''
select users.name,course.course_name
from users
right join course
on users.id=course.user_id
'''

'''
| name  | course_name |
| ----- | ----------- |
| Anmol | React       |
| Neha  | Node.js     |
| Anmol | MySQL       |
| NULL  | Docker      |

'''



#! 🧮 4. FULL OUTER JOIN

# 👉 Returns all rows when there is a match in either table.
# (If no match → shows NULLs for missing side)

# ⚠️ Not supported directly in MySQL — but you can emulate it using UNION:

'''
select users.name,course.course_name
from users
left join course 
on users.id=course.user_id
union
select users.name,course.course_name
from users
right join course 
on users.id=course.user_id
'''


#! 5. CROSS JOIN
'''
SELECT users.name, course.course_name
FROM users
CROSS JOIN course;
'''


#! 6. SELF JOIN

# 👉 When a table joins with itself — useful for hierarchical data.

# Example (employees table with manager_id):

'''
select e.name as employee,m.name as manager 

from employees e 

join employess m 

on e.manager_id =m.id
'''



#IMPORTANT THINGS IN SQL
'''
WHERE
ORDER BY --- sorting
LIMIT --- only give starting data (e.g limit 3 so it return only starting 3 data)
'''