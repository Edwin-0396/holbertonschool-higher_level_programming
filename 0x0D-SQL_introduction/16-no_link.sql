--  script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
select user, name FROM second_table WHERE name IS NOT NULL order by score DESC; 