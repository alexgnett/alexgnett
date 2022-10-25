SELECT count (*) from information_schema.tables where table_type = "base table"
SELECT name (*) from information_schema.tables where table_type = "base table"
SELECT * from users
SELECT * from grades
SELECT * FROM users, grades WHERE users.user_id = grades.user_id
