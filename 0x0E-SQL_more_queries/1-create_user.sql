-- Creates the MySQL server user user_0d_1
-- which has all privileges on the server
-- with password user_0d_1_pwd
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO user_od_1@localhost;