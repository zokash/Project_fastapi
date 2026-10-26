-- queries in the project ( endpoints)

--adding a rollback so that no permanaent changes are made to the database

--1
EXPLAIN ANALYZE SELECT * FROM contacts WHERE contact_id = 10;

--2
EXPLAIN ANALYZE SELECT * FROM contacts WHERE company_id = 3 
ORDER BY contact_id;

--3
EXPLAIN ANALYZE SELECT * FROM contacts WHERE company_id = 3 
ORDER BY contact_id Limit 10;

--4
BEGIN;
EXPLAIN ANALYZE INSERT INTO contacts("company_id","poc_name","phone","email","designation")
VALUES (2,'suryansh','97345XXXXX','suryansh@example.com','HR');
ROLLBACK;

--5
BEGIN;
EXPLAIN ANALYZE DELETE FROM contacts WHERE contact_id = 122;
ROLLBACK;

--6
BEGIN;
EXPLAIN ANALYZE UPDATE contacts 
SET company_id = 1,
poc_name = 'Madhavan',
phone = '78787XXXXX',
email = 'Madhavan@example.com',
designation = 'IT'
WHERE contact_id = 6;
ROLLBACK;


--7
EXPLAIN ANALYZE SELECT * FROM companies ORDER BY company_id LIMIT 20;

--8
EXPLAIN ANALYZE SELECT * FROM companies ORDER BY company_id ;

--9
BEGIN;
EXPLAIN ANALYZE INSERT INTO companies("company_name","service_type","address")
VALUES('Bajaj','Electrical Appliances','XYZ Lane, ABC city, India');
ROLLBACK;

--query 2 improved
BEGIN;
CREATE INDEX idx_contacts_company_id_contact_id ON contacts (company_id,contact_id );
EXPLAIN ANALYZE SELECT * FROM contacts WHERE company_id = 3 
ORDER BY contact_id;
SET enable_bitmapscan = off;
EXPLAIN ANALYZE SELECT * FROM contacts WHERE company_id = 3 ORDER BY contact_id;
RESET enable_bitmapscan;
ROLLBACK;
