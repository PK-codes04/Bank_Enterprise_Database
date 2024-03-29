create Database Tetsting;
Use Tetsting;
create table users (iduser varchar(20) NOT NULL,passuser varchar(20) NOT NULL);
create table users (iduser varchar(20) NOT NULL,passuser varchar(20) NOT NULL);	
create table mgmt (iduser varchar(20) NOT NULL,passuser varchar(20) NOT NULL);	
ALTER  TABLE management MODIFY COLUMN mgr_ssn varchar(20);
Select * from employee where  DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), start_date)), '%Y') + 1 = 10;
SELECT DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), start_date)), '%Y') + 1 FROM EMPLOYEE WHERE emp_ssn='8888';
CREATE EVENT event_name
  ON SCHEDULE
    EVERY 1 DAY
    STARTS (TIMESTAMP(CURRENT_DATE) + INTERVAL 1 DAY + INTERVAL 1 HOUR)
  DO
  Select * from employee where  DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), start_date)), '%Y') + 1 = 10;
  SHOW EVENTS;
select  * from employee where emp_ssn='8888';
select  * from customer;
select  * from account;
drop table account;
drop table depositor;
SET @@global.net_read_timeout=360;
INSERT INTO mgmt (emp_SSN, passuser)
VALUES ('123','bmsystem');
ALTER  TABLE account MODIFY COLUMN intrest_rate varchar(20);
CREATE TABLE bank (bank_id int NOT NULL ,bank_name varchar (20)NOT NULL,PRIMARY KEY(bank_id));
CREATE TABLE branch (bank_id int NOT NULL,branch_name varchar (40) NOT NULL,branch_city varchar (40) NOT NULL,foreign key(bank_id) references bank (bank_id),PRIMARY KEY(branch_name,bank_id));
CREATE TABLE employee (bank_id int NOT NULL,emp_SSN BIGINT NOT NULL,Fname varchar (20) NOT NULL,Lname varchar (20) NOT NULL,telephone_no varchar (20) NOT NULL,start_date date NOT NULL,foreign key(bank_id) references bank (bank_id),PRIMARY KEY(emp_SSN,bank_id));
CREATE TABLE management (emp_SSN BIGINT NOT NULL,mgr_ssn BIGINT,foreign key(mgr_ssn) references employee (emp_SSN),PRIMARY KEY(emp_SSN,mgr_ssn));
CREATE TABLE account (bank_id int NOT NULL,branch_name varchar (40) NOT NULL,account_no BIGINT NOT NULL,balance decimal(20,2) NOT NULL, account_type varchar (20) NOT NULL,intrest_rate varchar(20),overdraft varchar(20), foreign key(branch_name,bank_id) references branch (branch_name,bank_id),PRIMARY KEY(account_no,branch_name,bank_id));
CREATE TABLE customer (bank_id int NOT NULL,cust_SSN BIGINT NOT NULL,Fname varchar (20) NOT NULL,Lname varchar (20) NOT NULL,city varchar (20) NOT NULL,street varchar (20) NOT NULL, foreign key(bank_id) references bank (bank_id),PRIMARY KEY(cust_SSN,bank_id));
CREATE TABLE loan (bank_id int NOT NULL,branch_name varchar (40) NOT NULL,loan_no BIGINT NOT NULL,amount decimal(20,2) NOT NULL, loan_type varchar (20) NOT NULL,start_date date NOT NULL,end_date date NOT NULL,foreign key(branch_name,bank_id) references branch (branch_name,bank_id),PRIMARY KEY(loan_no,branch_name,bank_id));
CREATE TABLE payment (payment_no BIGINT NOT NULL,loan_no BIGINT NOT NULL,amount decimal(20,2) NOT NULL,payment_date date NOT NULL,foreign key(loan_no) references loan (loan_no),PRIMARY KEY(loan_no,payment_no));
CREATE TABLE transaction (transaction_no BIGINT NOT NULL,account_no BIGINT NOT NULL,amount decimal(20,2) NOT NULL,transaction_date date NOT NULL,transaction_type varchar (20) NOT NULL,foreign key(account_no) references account (account_no),PRIMARY KEY(transaction_no,account_no));
CREATE TABLE cust_banker (cust_SSN BIGINT NOT NULL,emp_SSN BIGINT NOT NULL,b_type varchar (20) NOT NULL, foreign key(cust_SSN) references customer (cust_SSN),foreign key(emp_SSN) references employee (emp_SSN),PRIMARY KEY(cust_SSN,emp_SSN));
CREATE TABLE depositor (cust_SSN BIGINT NOT NULL,account_no BIGINT NOT NULL,access_date date, foreign key(cust_SSN) references customer (cust_SSN),foreign key(account_no) references account (account_no),PRIMARY KEY(cust_SSN,account_no));
CREATE TABLE borrower (cust_SSN BIGINT NOT NULL,loan_no BIGINT NOT NULL, foreign key(cust_SSN) references customer (cust_SSN),foreign key(loan_no) references loan (loan_no),PRIMARY KEY(cust_SSN,loan_no));
CREATE TABLE branch_assets (branch_name varchar (40) NOT NULL,asset varchar (20) NOT NULL, foreign key(branch_name) references branch (branch_name),PRIMARY KEY(branch_name,asset));
CREATE TABLE emp_dependant (emp_SSN BIGINT NOT NULL,dependant_name varchar (20) NOT NULL, foreign key(emp_SSN) references employee (emp_SSN),PRIMARY KEY(emp_SSN,dependant_name));
desc bank;
desc branch;
desc employee;
desc management;
desc account;
desc customer;
desc loan;
desc payment;
desc transaction;
desc cust_banker;
desc depositor;
desc borrower;
desc branch_assets;
desc emp_dependant;