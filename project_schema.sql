DROP TABLE IF EXISTS contacts;
DROP TABLE IF EXISTS companies;

CREATE TABLE companies(
company_id SERIAL PRIMARY KEY,
company_name VARCHAR(100) NOT NULL UNIQUE, --required as we need to know what the company name is
service_type VARCHAR(100) NOT NULL, -- required because we need to know what service they are providing
address VARCHAR(100), 
reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO companies("company_name", "service_type", "address") VALUES
('EY', 'Auditing', 'Bangalore'),
('Amazon', 'Global Platform','Mumbai'),
('Digital Jena Network', 'Publicity and Advertising', 'Germany');

SELECT * FROM companies;

CREATE TABLE contacts(
contact_id SERIAL PRIMARY KEY,
company_id INT NOT NULL REFERENCES companies(company_id) ON DELETE CASCADE,-- ON DELETE CASCADE: chose because contact shouldnt be created
-- without a company because the said contacts table is specifically for contacts from the comapany, contacts dont mean nothing w/o knowing what company theyre from. and hence they cannot exist without a company. 
poc_name VARCHAR(100) NOT NULL,-- required as we need to know the employee's name
phone VARCHAR(100) NOT NULL UNIQUE, -- required as this is what the whole contact table is about
email VARCHAR(100) NOT NULL UNIQUE, -- same as above
designation VARCHAR(100),
reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO contacts("company_id","poc_name","phone","email","designation")
VALUES
(1,'Rahul U','98745XXXXX','Rahul@example.com','Partner'),
(1,'Anita V','76543XXXXX','Anita@example.com','Manager'),
(1,'Shiv P','98889XXXXX','Shiv@example.com','Consultant'),
(2,'Quintal P','92929XXXXX','Quintal@example.com','Manager'),
(2,'Jagdeesh S','992388XXXXX','Jagdeesh@example.com','Employee'),
(2,'Daniel D','97657XXXXX','Daniel@example.com','Employee');

SELECT * FROM contacts;
