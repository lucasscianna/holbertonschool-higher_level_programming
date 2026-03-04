-- Creates the table id_not_null on the MySQL server
-- The table has id (INT) with default value 1 and name (VARCHAR(256))
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);