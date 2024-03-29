INSERT INTO bank (bank_id, bank_name)
VALUES ('1','Chase');
INSERT INTO branch (bank_id,branch_name,branch_city)
VALUES ('1','Chase-Arlington','Arlington');
INSERT INTO branch (bank_id,branch_name,branch_city)
VALUES ('1','Chase-Seattle','Seattle');
INSERT INTO employee (bank_id,emp_SSN,Fname,Lname,telephone_no,start_date)
VALUES ('1','111111111','Paul','Jose','9234567890','1999-12-31');
INSERT INTO employee (bank_id,emp_SSN,Fname,Lname,telephone_no,start_date)
VALUES ('1','111111112','William','Serena','1234567890','2012-11-06');
INSERT INTO employee (bank_id,emp_SSN,Fname,Lname,telephone_no,start_date)
VALUES ('1','101111112','Joe','Ray','7234567891','2012-11-19');
INSERT INTO employee (bank_id,emp_SSN,Fname,Lname,telephone_no,start_date)
VALUES ('1','101111113','Jay','Prichett','7234567891','2012-11-21');
INSERT INTO employee (bank_id,emp_SSN,Fname,Lname,telephone_no,start_date)
VALUES ('1','201111113','Gloria','Prichett','7234567881','2012-11-20');
INSERT INTO management (emp_SSN,mgr_ssn)
VALUES ('111111111','111111112');
INSERT INTO management (emp_SSN,mgr_ssn)
VALUES ('111111112','NA');
INSERT INTO management (emp_SSN,mgr_ssn)
VALUES ('101111112','101111113');
INSERT INTO management (emp_SSN,mgr_ssn)
VALUES ('101111113','NA');
INSERT INTO management (emp_SSN,mgr_ssn)
VALUES ('201111113','111111112');
INSERT INTO customer (bank_id,cust_SSN,Fname,Lname,city,street)
VALUES ('1','901111113','Joey','Tribiani','New York','Central Park');
INSERT INTO customer (bank_id,cust_SSN,Fname,Lname,city,street)
VALUES ('1','501151113','Ross','Geller','Vermont','1st Ave');
INSERT INTO customer (bank_id,cust_SSN,Fname,Lname,city,street)
VALUES ('1','801151113','Pheobe','Buffey','World','2nd Ave');
INSERT INTO customer (bank_id,cust_SSN,Fname,Lname,city,street)
VALUES ('1','891151113','Chandler','Bing','Tulsa','3rd Ave');
INSERT INTO account (bank_id,branch_name,account_no,balance,account_type,intrest_rate,overdraft)
VALUES ('1','Chase-Seattle','123456','705.2','savings','1.1','NA');
INSERT INTO account (bank_id,branch_name,account_no,balance,account_type,intrest_rate,overdraft)
VALUES ('1','Chase-Seattle','323459','500','checking','NA','100');
INSERT INTO account (bank_id,branch_name,account_no,balance,account_type,intrest_rate,overdraft)
VALUES ('1','Chase-Arlington','901234','10000','savings','9.1','NA');
INSERT INTO account (bank_id,branch_name,account_no,balance,account_type,intrest_rate,overdraft)
VALUES ('1','Chase-Arlington','401239','1000','checking','NA','200');
INSERT INTO loan (bank_id, branch_name,loan_no,amount,loan_type,start_date,end_date)
VALUES ('1','Chase-Seattle','87340','1000','Personal','2015-12-05','2025-12-05');
INSERT INTO loan (bank_id, branch_name,loan_no,amount,loan_type,start_date,end_date)
VALUES ('1','Chase-Seattle','234567','5000','Credit card','2020-11-05','2022-11-05');
INSERT INTO cust_banker (cust_SSN,emp_SSN,b_type)
VALUES ('901111113','111111111','personal banker');
INSERT INTO cust_banker (cust_SSN,emp_SSN,b_type)
VALUES ('901111113','111111111','loan officer');
INSERT INTO cust_banker (cust_SSN,emp_SSN,b_type)
VALUES ('501151113','101111112','personal banker');
INSERT INTO cust_banker (cust_SSN,emp_SSN,b_type)
VALUES ('501151113','101111112','loan officer');
INSERT INTO cust_banker (cust_SSN,emp_SSN,b_type)
VALUES ('801151113','111111111','personal banker');
INSERT INTO cust_banker (cust_SSN,emp_SSN,b_type)
VALUES ('891151113','201111113','personal banker');
INSERT INTO depositor (cust_SSN,account_no)
VALUES ('901111113','123456');
INSERT INTO depositor (cust_SSN,account_no)
VALUES ('501151113','323459');
INSERT INTO depositor (cust_SSN,account_no)
VALUES ('801151113','901234');
INSERT INTO depositor (cust_SSN,account_no)
VALUES ('891151113','401239');
INSERT INTO borrower (cust_SSN,loan_no)
VALUES ('901111113','87340');
INSERT INTO borrower (cust_SSN,loan_no)
VALUES ('501151113','234567');
INSERT INTO payment (loan_no,amount)
VALUES ('87340','123');
INSERT INTO payment (loan_no,amount)
VALUES ('234567','100');
INSERT INTO transaction (account_no,amount,transaction_type)
VALUES ('901234','100','Withdraw');
INSERT INTO transaction (account_no,amount,transaction_type)
VALUES ('401239','100','Deposit');
INSERT INTO branch_assets (branch_name,asset)
VALUES ('Chase-Arlington','Laptop');
INSERT INTO branch_assets (branch_name,asset)
VALUES ('Chase-Seattle','Laptop,Bike,Mobile');
INSERT INTO emp_dependant (emp_SSN,dependant_name)
VALUES ('111111111','Pranali');
INSERT INTO emp_dependant (emp_SSN,dependant_name)
VALUES ('111111112','Rachel');
INSERT INTO emp_dependant (emp_SSN,dependant_name)
VALUES ('111111112','Janice');
INSERT INTO emp_dependant (emp_SSN,dependant_name)
VALUES ('101111112','Judy');
INSERT INTO emp_dependant (emp_SSN,dependant_name)
VALUES ('101111113','Mike');
INSERT INTO emp_dependant (emp_SSN,dependant_name)
VALUES ('201111113','Andy');