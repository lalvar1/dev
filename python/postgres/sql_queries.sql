SELECT 
	first_name, 
	last_name
FROM 
	customer
WHERE 
	first_name LIKE 'Bra%' AND
	first_name LIKE 'Bra_' AND				-- '_' matches only one character, '%' is a wildcard
	first_name ILIKE 'bra%' AND				-- same than like, but case insensitive
	last_name <> 'Motley' OR				-- not equal, why not NOT LIKE... 
	last_name in ('alvarez', 'gonzalez');

SELECT
	first_name,
	LENGTH(first_name) name_length
FROM 
	customer
WHERE 
	first_name LIKE 'A%' AND
	LENGTH(first_name) BETWEEN 3 AND 5
ORDER BY
	name_length;

---------------------------------------------------------------------------------------------------------------------


SELECT
   DISTINCT column_1, column_2
SELECT
   DISTINCT ON (column_1) column_alias,
   column_2
LIMIT n OFFSET m;		--offset to skip m rows
   
FETCH FIRST 5 ROW ONLY;  --the same than limit, but FETCH is sql-standard

---------------------------------------------------------------------------------------------------------------------

CREATE TABLE contacts(
    id SERIAL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(15),
    PRIMARY KEY (id)
);
INSERT INTO contacts(first_name, last_name, email, phone)
VALUES
    ('John','Doe','john.doe@example.com', NULL),
    ('Lily','Bush','lily.bush@example.com','(408-234-2764)');

SELECT
    id, first_name, last_name, email, phone
FROM
    contacts
WHERE
    phone IS NOT NULL;
---------------------------------------------------------------------------------------------------------------------

SELECT
    first_name || ' ' || last_name AS full_name
FROM
    contacts AS contacts_table_alias;			-- 'AS' is optional

SELECT
    contacts_table_alias.first_name || ' ' || contacts_table_alias.last_name AS full_name
FROM
    contacts contacts_table_alias;
---------------------------------------------------------------------------------------------------------------------
CREATE TABLE basket_a (
    id INT PRIMARY KEY,
    fruit VARCHAR (100) NOT NULL
);

CREATE TABLE basket_b (
    id INT PRIMARY KEY,
    fruit VARCHAR (100) NOT NULL
);

INSERT INTO basket_a (id, fruit)
VALUES
    (1, 'Apple'),
    (2, 'Orange'),
    (3, 'Banana'),
    (4, 'Cucumber');

INSERT INTO basket_b (id, fruit)
VALUES
    (1, 'Orange'),
    (2, 'Apple'),
    (3, 'Watermelon'),
    (4, 'Pear');
---------------------------------------------------------------------------------------------------------------------
INNER JOIN

SELECT
    a.id id_a,
    a.fruit fruit_a,
    b.id id_b,
    b.fruit fruit_b
FROM
    basket_a a
INNER JOIN basket_b b ON a.fruit = b.fruit;
---------------------------------------------------------------------------------------------------------------------
LEFT JOIN

SELECT
    a.id id_a,
    a.fruit fruit_a,
    b.id id_b,
    b.fruit fruit_b
FROM
    basket_a a
LEFT JOIN basket_b b ON a.fruit = b.fruit;
---------------------------------------------------------------------------------------------------------------------
LEFT JOIN, ONLY LEFT ROWS 
SELECT
    a.id id_a,
    a.fruit fruit_a,
    b.id id_b,
    b.fruit fruit_b
FROM
    basket_a a
LEFT JOIN basket_b b ON a.fruit = b.fruit
WHERE b.id IS NULL;
---------------------------------------------------------------------------------------------------------------------
IDEM RIGHT 
SELECT
    a.id id_a,
    a.fruit fruit_a,
    b.id id_b,
    b.fruit fruit_b
FROM
    basket_a a
RIGHT JOIN basket_b b ON a.fruit = b.fruit;

WHERE a.id IS NULL;
---------------------------------------------------------------------------------------------------------------------
FULL JOIN, if there is no match, the missing side contains null values
SELECT
    a.id id_a,
    a.fruit fruit_a,
    b.id id_b,
    b.fruit fruit_b
FROM
    basket_a a
FULL OUTER JOIN basket_b b ON a.fruit = b.fruit;

FULL JOIN, unique to both tables
SELECT
    a.id id_a,
    a.fruit fruit_a,
    b.id id_b,
    b.fruit fruit_b
FROM
    basket_a a
FULL JOIN basket_b b ON a.fruit = b.fruit
	WHERE a.id IS NULL OR b.id IS NULL;
---------------------------------------------------------------------------------------------------------------------
CREATE TABLE employee (
	employee_id INT PRIMARY KEY,
	first_name VARCHAR (255) NOT NULL,
	last_name VARCHAR (255) NOT NULL,
	manager_id INT,
	FOREIGN KEY (manager_id) 
	REFERENCES employee (employee_id) 
	ON DELETE CASCADE
);
INSERT INTO employee (
	employee_id,
	first_name,
	last_name,
	manager_id
)
VALUES
	(1, 'Windy', 'Hays', NULL),
	(2, 'Ava', 'Christensen', 1),
	(3, 'Hassan', 'Conner', 1),
	(4, 'Anna', 'Reeves', 2),
	(5, 'Sau', 'Norman', 2),
	(6, 'Kelsie', 'Hays', 3),
	(7, 'Tory', 'Goff', 3),
	(8, 'Salley', 'Lester', 3);

SELF JOIN 
SELECT
    e.first_name || ' ' || e.last_name employee,
    m .first_name || ' ' || m .last_name manager
FROM
    employee e
INNER JOIN employee m ON m .employee_id = e.manager_id
ORDER BY
    manager;

---------------------------------------------------------------------------------------------------------------------
CROSS JOIN, makes cartesian product of tables . There are 3 ways
SELECT * 
FROM T1
CROSS JOIN T2;

SELECT * 
FROM T1, T2;

SELECT *
FROM T1
INNER JOIN T2 ON TRUE;
---------------------------------------------------------------------------------------------------------------------
We often use the HAVING clause in conjunction with the GROUP BY clause to filter group rows that do not satisfy a specified condition.
SELECT
	customer_id,
	SUM (amount)
FROM
	payment
GROUP BY
	customer_id
HAVING
	SUM (amount) > 200;
---------------------------------------------------------------------------------------------------------------------
UNION. Both queries must return same number of columns with compatible data types
removes duplicates unless UNION ALL is used 
SELECT *
FROM
	sales2007q1
UNION
SELECT *
FROM
	sales2007q2;

---------------------------------------------------------------------------------------------------------------------
SELECT
	employee_id
FROM
	keys
INTERSECT
SELECT
        employee_id
FROM
	hipos
ORDER BY employee_id;
---------------------------------------------------------------------------------------------------------------------
GROUPING SETS 
SELECT
    brand,
    segment,
    SUM (quantity)
FROM
    sales
GROUP BY
    GROUPING SETS (
        (brand, segment),
        (brand),
        (segment),
        ()
    );
---------------------------------------------------------------------------------------------------------------------
SUBQUERIES
SELECT
	first_name,
	last_name
FROM
	customer
WHERE
	EXISTS (
		SELECT
			1
		FROM
			payment
		WHERE
			payment.customer_id = customer.customer_id
	);
	
SELECT
    title,
    category_id
FROM
    film
INNER JOIN film_category
        USING(film_id)
WHERE
    category_id IN(
        SELECT
            category_id
        FROM
            category
        WHERE
            NAME = 'Action'
            OR NAME = 'Drama'
    );

SELECT
    film_id,
    title,
    length
FROM
    film
WHERE
    length > ALL (
            SELECT
                ROUND(AVG (length),2)
            FROM
                film
            GROUP BY
                rating
    )
ORDER BY
    length;
---------------------------------------------------------------------------------------------------------------------
CTEs

WITH cte_film AS (
    SELECT 
        film_id, 
        title,
        (CASE 
            WHEN length < 30 THEN 'Short'
            WHEN length < 90 THEN 'Medium'
            ELSE 'Long'
        END) length    
    FROM
        film
)
SELECT
    film_id,
    title,
    length
FROM 
    cte_film
WHERE
    length = 'Long'
ORDER BY 
    title;

----------------------------------------------------------------------------------------------------------------
PRIMARY KEY
CREATE TABLE TABLE (
	column_1 data_type,
	column_2 data_type,
	… 
        PRIMARY KEY (column_1, column_2)
);


FOREIGN KEY
CREATE TABLE so_items (
  item_id INTEGER NOT NULL,	
  so_id INTEGER REFERENCES so_headers(id),
  product_id INTEGER,
  qty INTEGER,
  net_price numeric,
  PRIMARY KEY (item_id,so_id)
);

UNIQUE CONSTRAINT
CREATE TABLE person (
	id SERIAL  PRIMARY KEY,
	first_name VARCHAR (50),
	last_name  VARCHAR (50),
	email      VARCHAR (50),
        UNIQUE(email)
);
or
UNIQUE (first_name,last_name)

MORE CONSTRAINTS
CREATE TABLE invoice(
  id serial PRIMARY KEY,
  product_id int NOT NULL,
  qty numeric NOT NULL CHECK(qty > 0),
  net_price numeric CHECK(net_price > 0) 
);

----------------------------------------------------------------------------------------------------------------
unnest, expand array to a list of rows 
SELECT
	name,
	unnest(phones)
FROM
	contacts;
	
----------------------------------------------------------------------------------------------------------------
querying json
		'{ "customer": "Lily Bush", "items": {"product": "Diaper","qty": 24}}'
SELECT
	info ->> 'customer' AS customer,
	info -> 'items' ->> 'product' as product

----------------------------------------------------------------------------------------------------------------

window_function(arg1, arg2,..) OVER (
   [PARTITION BY partition_expression]
   [ORDER BY sort_expression [ASC | DESC] [NULLS {FIRST | LAST }]

SELECT
    wf1() OVER(PARTITION BY c1 ORDER BY c2),
    wf2() OVER(PARTITION BY c1 ORDER BY c2)
FROM table_name;