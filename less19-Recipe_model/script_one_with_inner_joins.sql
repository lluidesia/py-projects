
BEGIN;
INSERT INTO mydb.recipes (title, steps) VALUES('test5', 'test55');
INSERT INTO mydb.recipe_info (level, recipes_id) VALUES(2, last_insert_id());
COMMIT;


SELECT * FROM mydb.recipes LIMIT 1000;
SELECT title,steps FROM mydb.recipes LIMIT 3;
SELECT * FROM mydb.recipe_info LIMIT 1000;


SELECT * FROM mydb.recipes
INNER JOIN mydb.recipe_info
ON
mydb.recipes.id = mydb.recipe_info.recipes_id;







BEGIN;
INSERT INTO mydb.ingredients (ingredien_title) VALUES('ingrdnt 5');
INSERT INTO mydb.ingredient_info (article, carbs, ingredients_id) VALUES('artcl 5', 500, last_insert_id());
COMMIT;

SELECT * FROM mydb.ingredients LIMIT 1000;

SELECT * FROM mydb.ingredients
INNER JOIN (SELECT article,carbs,ingredients_id FROM mydb.ingredient_info) ingredient_info
ON
mydb.ingredients.id = mydb.ingredient_info.ingredients_id;




INSERT INTO mydb.cuisine (cuisine_title, cuisine_location) VALUES('Cuisine 5','Location 5');
SELECT * FROM mydb.cuisine LIMIT 1000;


INSERT INTO mydb.category (category_title, category_type) VALUES('Category 3',3);
SELECT * FROM mydb.category LIMIT 1000;


SELECT * FROM mydb.recipes
INNER JOIN mydb.recipe_info
ON
mydb.recipes.id = mydb.recipe_info.recipes_id;

SELECT * FROM mydb.recipes LIMIT 1000;

UPDATE mydb.recipes SET category_id = 1 WHERE id = 7;
UPDATE mydb.recipes SET cuisine_id = 4 WHERE id = 7;

DELETE FROM mydb.recipes WHERE id=1;

