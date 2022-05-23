-- From https://www.youtube.com/watch?v=HXV3zeQKqGY&ab_channel=freeCodeCamp.org
-- Tables
CREATE TABLE student(
    student_id INT,
    name VARCHAR(20),
    major VARCHAR(20),
    PRIMARY KEY(student_id)
);

DESCRIBE student;

DROP TABLE student;

ALTER TABLE student ADD gpa DECIMAL(3, 2);
ALTER TABLE student DROP COLUMN gpa;

SELECT * FROM student;


-- Inserting Data
INSERT INTO student VALUES(1, 'Jack', 'Biology');
INSERT INTO student VALUES(2, 'Kate', 'Sociology');
INSERT INTO student(student_id, name) VALUES (3, 'Claire');
INSERT INTO student VALUES (4, 'Jack', 'Biology');
INSERT INTO student VALUES (5, 'Mike', 'Computer Science');

INSERT INTO student VALUES(3, NULL, 'Chemistry');

INSERT INTO student(name, major) VALUES('Jack', 'Biology');
INSERT INTO student(name, major) VALUES('Kate', 'Sociology');
INSERT INTO student(name, major) VALUES('Claire', NULL);


-- CONSTRAINTS
-- Shortlist:
--  NOT NULL
--  UNIQUE
--  DEFAULT value_here
--  AUTO_INCREMENT
CREATE TABLE student(
    student_id INT AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    major VARCHAR(20) DEFAULT 'undecided',
    PRIMARY KEY(student_id)
);


SELECT * FROM student;


-- UPDATE
UPDATE student
SET major = 'Chemistry'
WHERE student_id = 3;

UPDATE student
SET major = 'Bio'
WHERE major = 'Biology';

UPDATE student
SET major = 'Comp Sci'
WHERE student_id = 4;

UPDATE student
SET major = 'Biochemistry'
WHERE major = 'Bio' OR major = 'Chemistry';

UPDATE student
SET name = 'Tom', major = 'undecided'
WHERE student_id = 1;

UPDATE student
SET major = 'undecided';


-- DELETE
DELETE FROM student;

DELETE FROM student
WHERE student_id = 5;


-- QUERIES
SELECT * FROM student;

SELECT student.name, student.major
FROM student;

SELECT student.name, student.major
FROM student
ORDER BY name DESC; -- ASC by default

SELECT *
FROM student
ORDER BY major, student_id -- if major is the same, then order by student_id
LIMIT 2;

SELECT *
FROM student
WHERE name IN ('Claire', 'Kate', 'Mike');

