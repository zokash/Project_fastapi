INSERT INTO companies("company_name", "service_type", "address", "reg_date")
SELECT
	'Company ' || g,
	(ARRAY['IT', 'Finance','HR','Logistics','Healthcare'])[floor(random()*5)::int +1],
	(floor(random()*999)+1):: int || ' '
	||(ARRAY['MG Road', 'Park Street','Station Road','Defence Road','Allen Street'])[floor(random()*5):: int +1]
	|| ' '
	|| (ARRAY['Bangalore','Ahmedabad','Hyderabad','Chennai','New York','London'])[floor(random()*6):: int + 1],
	now() - random() * INTERVAL '5 years'
FROM generate_series(1,1000) as g;


SELECT min(company_id), max(company_id) FROM companies;

WITH ids AS (
	SELECT array_agg(company_id) AS arr FROM companies
)
INSERT INTO contacts("company_id","poc_name","phone","email","designation", "reg_date")
SELECT
	ids.arr[floor(random() * array_length(ids.arr, 1)) :: int +1],
	'Employee ' || g,
	( 9000000000 + g)::text,
	'employee'|| g|| '@example.com',
	(ARRAY['HR','Manager','Intern','Team Lead','Employee'])[floor(random()*5)::int +1],
	now() - random() * INTERVAL '5 years'
FROM generate_series(1,100000) as g, ids;


SELECT count(*) FROM companies;
SELECT count(*) FROM contacts;

ANALYZE companies;
ANALYZE contacts;
