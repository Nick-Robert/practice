-- More Basic Query Practice
    -- Find all employees
    SELECT * FROM employee;

    -- Find all clients
    SELECT * FROM client;

    -- Find all employees ordered by salary
    SELECT * 
    FROM employee
    ORDER BY salary DESC;

    -- Find all employees ordered by sex then name
    SELECT *
    FROM employee
    ORDER BY sex, first_name, last_name;

    -- Find the first 5 employees in the table
    SELECT *
    FROM employee
    LIMIT 5;

    -- Find the first and last names of all employees
    SELECT first_name, last_name
    FROM employee;

    -- Find the forename and the surnames of all employees
    SELECT first_name AS forename, last_name AS surname
    FROM employee;

    -- Find out all the different genders
    SELECT DISTINCT sex
    FROM employee;

    -- Find out all the different branch_ids
    SELECT DISTINCT branch_id
    FROM employee;



-- SQL Functions
    -- Find the number of employees
    SELECT COUNT(emp_id) AS Employee_Count
    FROM employee;

    -- Find the number of employees who have a supervisor
    SELECT COUNT(super_id) AS Supervised_Employee_Count
    FROM employee;

    -- Find the number of female employees born after 1970
    SELECT COUNT (emp_id) 
    FROM employee
    WHERE sex = 'F' AND birth_day > '1971-01-01';

    -- Find the average of all employee's salaries
    SELECT AVG(salary) 
    FROM employee
    WHERE sex = 'M';

    -- Find the sum of all employee's salaries
    SELECT SUM(salary)
    FROM employee;

    -- Aggregation (GROUP BY)
    -- Find out how many males and females there are
    SELECT COUNT(sex), sex
    FROM employee
    GROUP BY sex;

    -- Find the total sales of each salesman
    SELECT SUM(total_sales), emp_id
    FROM works_with
    GROUP BY emp_id;

    -- Find how much each client spent
    SELECT SUM(total_sales), client_id
    FROM works_with
    GROUP BY client_id;


-- Wildcards
-- % = any # characters, _ = one character
    -- Find any client's who are an LLC
    SELECT *
    FROM client
    WHERE client_name LIKE '%LLC';

    -- Find any branch suppliers who are in the label business
    SELECT *
    FROM branch_supplier
    WHERE supplier_name LIKE '% Label%';

    -- Find any employee born in October
    SELECT *
    FROM employee
    WHERE birth_day LIKE '____-10%';

    -- Find any clients who are schools
    SELECT *
    FROM client
    WHERE client_name LIKE '%school%';


-- Union
-- Combine the results of multiple SELECT statements into one
-- RULES:
--  1) Must have the same number of columns in each SELECT statement
--  2) Must have similar datatypes
    -- Find a list of employee, client, and branch names
    SELECT first_name AS Names
    FROM employee
    UNION
    SELECT client_name
    FROM client
    UNION
    SELECT branch_name
    FROM branch;

    -- Find a list of all clients and branch suppliers' names
    SELECT client_name, client.branch_id
    FROM client
    UNION
    SELECT supplier_name, branch_supplier.branch_id
    FROM branch_supplier;

    -- Find a list of all money spent or earned by the company
    SELECT total_sales
    FROM works_with
    UNION
    SELECT salary
    FROM employee;


-- Join
-- Combine rows from 2 or more tables based on a related column between them
-- Four different types:
--  1) Inner Join - Combines rows when they have the shared column in common
--  2) Left Join - Includes every row from the table on the "left" (the table mentioned first)
--  3) Right Join - Includes every row from the table on the "right" (the table mentioned last)
--  4) Full Outer Join - Includes every row (Left and Right together, cannot be done in MySQL)
    -- Find all branches and the names of their managers
    SELECT employee.emp_id, employee.first_name, branch.branch_name, branch.mgr_id
    FROM employee
    JOIN branch -- this is called an inner join
    ON employee.emp_id = branch.mgr_id;

    SELECT employee.emp_id, employee.first_name, branch.branch_name, branch.mgr_id
    FROM employee
    LEFT JOIN branch
    ON employee.emp_id = branch.mgr_id;

    SELECT employee.emp_id, employee.first_name, branch.branch_name, branch.mgr_id
    FROM employee
    RIGHT JOIN branch
    ON employee.emp_id = branch.mgr_id;

    -- SELECT employee.emp_id, employee.first_name, branch.branch_name, branch.mgr_id
    -- FROM employee
    -- FULL JOIN branch
    -- ON employee.emp_id = branch.mgr_id;


-- Nested Queries
-- A query where multiple SELECT statements are used to get specific information. Use the results of one SELECT statement to feed into another
    -- Find names of all employees who have sold over 30,000 to a single client
    SELECT employee.first_name, employee.last_name
    FROM employee
    WHERE employee.emp_id IN (
        SELECT works_with.emp_id
        FROM works_with
        WHERE works_with.total_sales > 30000
    );

    -- Find all clients who are handled by the branch that Michael Scott manages
    SELECT client.client_name
    FROM client
    WHERE client.branch_id IN (
        SELECT branch.branch_id
        FROM branch
        WHERE branch.mgr_id IN (
            SELECT employee.emp_id
            FROM employee
            WHERE employee.first_name = 'Michael' AND employee.last_name = 'Scott'
        )
    );


-- On Delete
-- Deleting entries in a table when they have foreign keys associated with them
-- ON DELETE SET NULL - 
--      When you delete the entry, then the foreign keys in other tables that referenced that   entry will be set to Null
-- ON DELETE SET CASCADE - 
--      When you delete the entry, then just delete the other rows that referenced it
-- Use set cascade when the foreign key is a real foreign key (when it's a primary key in another table) since primary keys cannot be NULL. If it isn't a real foreign key but just a reference, then you can use set null.

    -- Branch was made with this:
    CREATE TABLE branch (
    branch_id INT PRIMARY KEY,
    branch_name VARCHAR(40),
    mgr_id INT,
    mgr_start_date DATE,
    FOREIGN KEY(mgr_id) REFERENCES employee(emp_id) ON DELETE SET NULL
    );
    SELECT * FROM branch;
    SELECT * FROM employee;
    -- So, when Michael Scott is deleted, then Scranton's mgr_id will be NULL and super_ids will also be NULL in employee
    DELETE FROM employee
    WHERE emp_id = 102;

    -- Branch supplier was made like this:
    CREATE TABLE branch_supplier (
    branch_id INT,
    supplier_name VARCHAR(40),
    supply_type VARCHAR(40),
    PRIMARY KEY(branch_id, supplier_name),
    FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE CASCADE
    );
    -- So, when a branch is deleted, then it deletes the corresponding rows in branch_supplier 
    SELECT * FROM branch_supplier;
    DELETE FROM branch
    WHERE branch_id = 2;

-- Triggers
-- A block of SQL code that'll define a certain action that should happen when something else happens in the database
-- Cannot be done in PopSQL since need to change delimiter. Must use terminal.
-- Useful for logging changes and automating things
-- BEFORE/AFTER INSERT/UPDATE/DELETE

CREATE TABLE trigger_test (
    message VARCHAR(100)
);

SELECT * FROM trigger_test;

-- Examples
DELIMITER $$
CREATE
    TRIGGER my_trigger BEFORE INSERT
    ON employee
    FOR EACH ROW BEGIN
        INSERT INTO trigger_test VALUES('added new employee');
    END$$
DELIMITER ;

DELIMITER $$
CREATE
    TRIGGER my_trigger1 BEFORE INSERT
    ON employee
    FOR EACH ROW BEGIN
        INSERT INTO trigger_test VALUES(NEW.first_name);
    END$$
DELIMITER ;

INSERT INTO employee
VALUES(110, 'Kevin', 'Malone', '1978-02-19', 'M', 69000, 106, 3);

DELIMITER $$
CREATE
    TRIGGER my_trigger2 BEFORE INSERT
    ON employee
    FOR EACH ROW BEGIN
        IF NEW.sex = 'M' THEN
            INSERT INTO trigger_test VALUES('added male employee');
        ELSEIF NEW.sex = 'F' THEN
            INSERT INTO trigger_test VALUES('added female employee');
        ELSE
            INSERT INTO trigger_test VALUES('added other employee');
        END IF;
    END$$
DELIMITER ;

DROP TRIGGER my_trigger;
DROP TRIGGER my_trigger1;
DROP TRIGGER my_trigger2;
