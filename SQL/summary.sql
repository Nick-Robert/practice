-- Notes from https://www.youtube.com/watch?v=HXV3zeQKqGY&ab_channel=freeCodeCamp.org and my CSCE310 Notes

-- Some Basic SQL Datatypes:
    INT             -- Whole numbers
    DECIMAL(M, N)   -- Decimal numbers - Exact value (M = total digits, N = # after decimal)
    VARCHAR(1)      -- String of text of length 1
    BLOB            -- Binary Large Object, stores large data
    DATE            -- 'YYYY-MM-DD'
    TIMESTAMP       -- 'YYYY-MM-DD HH:MM:SS' - used for recording time

-- Comparison Operators
--  =       -- equals
--  <>      -- not equals
--  >       -- greater than
--  <       -- less than
--  >=      -- greater than or equal
--  <=      -- less than or equal
--  AND
--  OR

-- Basic Command Structure:
-- Tables
    CREATE TABLE table_name_here (
        attribute_name_1 datatype PRIMARY KEY,
        attribute_name_2 datatype,
        attribute_name_3 datatype,
    );

    DESCRIBE table_name_here;

    DROP TABLE table_name_here;

    ALTER TABLE table_name_here ADD attribute_name datatype;
    ALTER TABLE table_name_here DROP COLUMN attribute_name;

    SELECT * FROM table_name_here;

-- Inserting Data
    INSERT INTO table_name_here VALUES(..., ..., ...);
    INSERT INTO table_name_here(attribute_name_1, attribute_name_2) VALUES (..., ...);
    