SELECT * FROM mydb.users;
SELECT * FROM mydb.user_info;
SELECT * FROM mydb.user_statistics;


#наповнити 5 записами всі створені таблиці.
BEGIN;
INSERT INTO mydb.users (name, surname, status) VALUES('name5', 'sur5', 'status5');
INSERT INTO mydb.user_info (year_of_birth, profession, date_signup, date_last_login, device, users_id) VALUES('2005.01.01', 'prof5', '05.02.02','05.02.03', 'device5', last_insert_id());
INSERT INTO mydb.user_statistics (recipes_added, recipes_liked, followers, following, users_id) VALUES(500, 510, 520,530, last_insert_id());
COMMIT;

#написати заипт для виведення консолідованих данних з таблиць users та user_info.
SELECT * FROM mydb.users
INNER JOIN mydb.user_info
ON
mydb.users.id = mydb.user_info.users_id;

#написати заипт для виведення консолідованих данних з таблиць users та  user_statistics
SELECT * FROM mydb.users
INNER JOIN mydb.user_statistics
ON
mydb.users.id = mydb.user_statistics.users_id;

 
#відредагувати довільний запис у таблиці user_info.
UPDATE mydb.user_info SET device='super' WHERE id_user_info=1;


#видалити довільний запис з таблиці users.
SET FOREIGN_KEY_CHECKS=0;
DELETE FROM mydb.users WHERE id=1;


#додати тип юзера (один до багатьох)
SELECT * FROM mydb.type;
INSERT INTO mydb.type (type_name) VALUE('type2');

#додати тип юзера до вже створених юзерів
UPDATE mydb.users SET type_id_type=2 WHERE id=5;



