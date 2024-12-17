Create database ChietDB;
use chietdb;

CREATE TABLE Customer (
  CustomerID SMALLINT UNSIGNED,
  FirstName VARCHAR(35),
  LastName VARCHAR(35),
  email VARCHAR(50),
  PRIMARY KEY (CustomerID)
);

describe Customer;

CREATE TABLE Restaurant (
  RestaurantID SMALLINT UNSIGNED,
  RestaurantName VARCHAR(35),
  Phone VARCHAR(20),
  Address VARCHAR(70),
  PRIMARY KEY (RestaurantID)
);

describe Restaurant;

CREATE TABLE Diet (
  DietID SMALLINT UNSIGNED,
  DietName VARCHAR(25),
  MenuItem VARCHAR(35),
  Res_ID SMALLINT UNSIGNED,
  PRIMARY KEY (DietID)
);

describe Diet;

INSERT INTO restaurant
VALUES (101,'Pita Inn', '630-799-0085', '1835 Abriter Court, Naperville, IL, 60563'),
       (102,'Panera Bread', '331-231-6165', '1620 N Route 59, Naperville, IL, 60563'),
       (103,'The Port of Peri Peri', '630-701-2193', '4151 McCoy Dr #153, Aurora, IL 60504'),
       (104,'JK Kabab', '630-778-5555', '572 Weston Ridge Dr., Suite 112, Naperville, IL 60563'),
       (105,'The Chicago Diner', '773-252-3211', '2333 N. Milwaukee Ave, Chicago, IL, 60647'),
       (106,'Urban Vegan', '773-404-1109', '1601-1603 W Montrose Ave, Chicago, IL, 60613'),
       (107,'True Food Kitchen', '630-716-3056', '105 Oakbrook Center, Oak Brook, IL 60523'),
       (108,'Chalavi & Main Pizza', '773-338-9640', '2839 W Touhy Ave, Chicago, IL 60645'),
       (109,'Mizrahi Grill', '847-831-1400', '215 Skokie Valley Rd, Highland Park, IL 60035'),
       (110,'Uncooked', '312-315-5552', '210 N Carpenter St Suite 140, Chicago, IL, 60607'),
       (111,'The Vegan Cafe', '815-838-4626', '928 S State St, Lockport, IL, 60441'),
       (112,'Manna Kitchen', '630-536-8328', '2801 Ogden Ave Ste 8 & 9, Lisle, IL, 60532'),
       (113,'Pa Lian Burmese', '331-716-7905', '254 E Geneva Rd, Wheaton, IL, 60187'),
       (114,'Beatrix', '312-583-0598', '23 E Jackson Blvd, Chicago, IL, 60604'),
       (115,'Shakou Naperville', '331-472-4955', '22 E Chicago Ave, Naperville, IL, 60540'),
       (116,'Original Soul Vegetarian', '773-224-0104', '203 E 75th St, Chicago, IL, 60619'),
       (117,'Wheats End Cafe', '773-770-3527', '2873 N Broadway, Chicago, IL, 60657'),
       (118,'Carols Garden', '630-260-0303', '515 S Schmale Rd, Carol Stream, IL, 60188'),
       (119,'Wilde Bar & Restaurant', '773-244-0404', '3130 N Broadway, Chicago, IL, 60657'),
       (120,'Chi Tea', '331-307-7916', '413 E Roosevelt Rd, Lombard, IL, 60148'),
       (121,'Al-Bawadi', '708-599-1999', '7216 W 87th St, Bridgeview, IL, 60455'),
       (122,'Shahi Nihari', '630-792-8839', '541 W North Ave, Villa Park, IL, 60181'),
       (123,'Hamachi Sushi Bar', '773-293-6904', '2801 W Howard St, Chicago, IL, 60645'),
       (124,'Evita Steakhouse', '773-463-8482', '6112 N Lincoln Ave, Chicago, IL, 60659'),
       (125,'Taboun Grill', '847-965-1818', '8808 Gross Point Rd, Skokie, IL, 60077');


SELECT * FROM restaurant;


INSERT INTO diet
VALUES (1, 'Vegetarian', 'Veggie Lunch Special', 101),
       (2, 'Vegetarian', 'Vegetarian Package', 101),
       (3, 'Vegetarian', 'Vegetarian Combiantion Plate', 101),
       (4, 'Vegetarian', 'Creamy Tomato Soup', 102),
       (5, 'Vegetarian', 'Mediterranean Veggie', 102),
       (6, 'Vegetarian', 'Greek Salad', 102),
       (7, 'Halal', 'The Sizzler', 103),
       (8, 'Halal', 'Chicken and Rice Bowl', 103),
       (9, 'Halal', 'Peri Costeletas', 103),
       (10, 'Halal', 'Chicken Seekh Kabab Wrap', 104),
       (11, 'Halal', 'Beef Chapli Kabab', 104),
       (12, 'Halal', 'Chilli Chicken Fried Rice', 104),
       (13, 'GlutenFree', 'Taco Salad', 105),
       (14, 'GlutenFree', 'Garden Salad', 105),
       (15, 'GlutenFree', 'Scrambled Tofu', 105),
       (16, 'Vegan', 'Grilled Veggi Dumpling', 106),       
       (17, 'Vegan', 'Tofu Satay', 106),
       (18, 'Vegan', 'Green Power Salad', 106),
       (19, 'Vegan', 'Stir-Fried Vegetable', 106),
       (20, 'Vegan', 'Spicy Noodle Dinner Combo', 106),
       (21, 'Vegan', 'Oatmeal with Strawberries & Pecans', 102),
       (22, 'Vegan', 'Ten Vegetable Soup', 102),
       (23,'Vegan', 'Peach & Blueberry Smoothie', 102),
       (24, 'GlutenFree', 'Spaghetti Squash Casserole', 107),
       (25, 'Vegan', 'Seasonal Ingredient Salad', 107),
       (26, 'Vegan', 'Ancient Grains Bowl', 107),
       (27, 'Vegan', 'Thai Basil Stir Fry', 105),
       (28, 'Kosher', 'Large Cheese Pizza', 108),
       (29, 'Kosher', 'Large Deep Dish Pizza', 108),
       (30, 'Kosher', 'Health Nut Salad', 108),
       (31, 'Kosher', 'Cream of Broccoli Soup', 108),
       (32, 'Kosher', 'Grilled Salmon Wrap', 108),
       (33, 'Kosher', 'IDF Eggplant Salad', 109),
       (34, 'Kosher', 'Falafel Sandwich', 109),
       (35, 'Kosher', 'Shawarma Sandwich', 109),
       (36, 'Kosher', 'Chicken Kabobs', 109),
       (37, 'Kosher', 'Jerusalem Mixed Grill', 109),
       (38, 'Vegan', 'cold brew overnight oats', 110),
       (39, 'Vegan', 'saffron curry noodle', 110),
       (40, 'Vegan', 'hummus bowl', 110),
       (41, 'Vegan', 'Creamy Alfredo', 111),
       (42, 'Vegan', 'Thai Pizza', 111),
       (43, 'Vegan', 'Loaded Burger Pizza', 111),
       (44, 'Vegan', 'Sum-Tam Soup', 113),
       (45, 'Vegan', 'Lehphat Htamin', 113),
       (46, 'Vegan', 'Kauk Swe Thoke', 113),
       (47, 'Vegatarian', 'ENLIGHTENED CAESAR', 114),
       (48, 'Vegatarian', 'MUSHROOM & QUINOA BURGER', 114),
       (49, 'Vegatarian', 'YUZU GINGER POKE BOWL', 114),
       (50, 'Vegatarian', 'Midori', 115),
       (51, 'Vegatarian', 'Secret Garden', 115),
       (52, 'Vegatarian', 'Veggie Futo', 115),
       (53, 'Vegatarian', 'Noodle Stir Kai', 116),
       (54, 'Vegatarian', 'Stir Fried Vegetables', 116),
       (55, 'Vegatarian', 'Down Home Greens', 116),
       (56, 'GlutenFree', 'Belgian Waffle', 117),
       (57, 'GlutenFree', 'Old World Panini', 117),
       (58, 'GlutenFree', 'Signature Popover', 117),
       (59, 'GlutenFree', 'Walnut and Apple Salad', 118),
       (60, 'GlutenFree', 'Golden Brown Pancakes', 118),
       (61, 'GlutenFree', 'Greek Omelette', 118),
       (62, 'GlutenFree', 'CLASSIC BURGER', 119),
       (63, 'GlutenFree', 'GRILLED SCOTTISH SALMON', 119),
       (64, 'GlutenFree', 'KNIFE & FORK GRILLED CAESAR SALAD', 119),
       (65, 'Halal', 'Big Bird Chicken Sandwich', 120),
       (66, 'Halal', 'Chi Tea Classic Beef Burger', 120),
       (67, 'Halal', 'Seasoned Fries', 120),
       (68, 'Halal', 'MEDITERRANEAN GREEK SALAD', 121),
       (69, 'Halal', 'LENTIL SOUP', 121),
       (70, 'Halal', 'FALAFIL SANDWICH', 121),
       (71, 'Halal', 'HAKKA NOODLES', 122),
       (72, 'Halal', 'CHICKEN MAKHNI', 122),
       (73, 'Halal', 'GYROS SANDWICH', 122),
       (74, 'Kosher', 'Bombay Salmon Sandwich', 123),
       (75, 'Kosher', 'Assorted Vegetable Tempura', 123),
       (76, 'Kosher', 'String Beans', 123),
       (77, 'Kosher', 'FISH TACOS', 124),
       (78, 'Kosher', 'THE IMPOSSIBLE BURGER', 124),
       (79, 'Kosher', 'PASTRAMI SALAD', 124),
       (80, 'Kosher', 'Moroccan Fish', 125),
       (81, 'Kosher', 'Falafel', 125),
       (82, 'Kosher', 'Moroccan Eggplant Salad', 125),
       (83, 'Vegan', 'Manna Burger', 112),
       (84, 'Vegan', 'Schnitzel Platter', 112),
       (85, 'Vegan', 'Smokey Chicago Chili', 112),
       (86, 'Halal', 'BEEF SEEKH KEBAB', 122);


SELECT * FROM diet;


INSERT INTO customer
VALUES (201,'Arwa', 'Afreen', 'arwaafreen@lewisu.edu'),
       (202,'Anjum', 'Shams', 'anjumshams@lewisu.edu'),
       (203,'Syed', 'Hassan', 'syedmhassaan@lewisu.edu'),
       (204,'Daniel', 'De Chiara', 'danielepdechiara@lewisu.edu');

SELECT * FROM customer;


CREATE VIEW Halal 
AS
SELECT DietName, MenuItem, RestaurantName, Phone, Address
FROM diet JOIN  restaurant 
ON Res_ID = RestaurantID
WHERE DietName = 'Halal';

SELECT * FROM Halal;


CREATE VIEW Kosher
AS
SELECT DietName, MenuItem, RestaurantName, Phone, Address
FROM diet JOIN  restaurant 
ON Res_ID = RestaurantID
WHERE DietName = 'Kosher';

SELECT * FROM Kosher;


CREATE VIEW Vegetarian
AS
SELECT DietName, MenuItem, RestaurantName, Phone, Address
FROM diet JOIN  restaurant 
ON Res_ID = RestaurantID
WHERE DietName = 'Vegetarian';


SELECT * FROM Vegetarian;

CREATE VIEW Vegan
AS
SELECT DietName, MenuItem, RestaurantName, Phone, Address
FROM diet JOIN  restaurant 
ON Res_ID = RestaurantID
WHERE DietName = 'Vegan';

SELECT * FROM Vegan;


CREATE VIEW GlutenFree
AS
SELECT DietName, MenuItem, RestaurantName, Phone, Address
FROM diet JOIN  restaurant 
ON Res_ID = RestaurantID
WHERE DietName = 'GlutenFree';

SELECT * FROM GlutenFree;



CREATE VIEW Chicago
AS
SELECT RestaurantName, Phone, Address, DietName, MenuItem
FROM restaurant JOIN diet 
ON RestaurantID = Res_ID
WHERE Address LIKE '%Chicago%';

SELECT * FROM Chicago;

CREATE VIEW Lombard
AS
SELECT RestaurantName, Phone, Address, DietName, MenuItem
FROM restaurant JOIN diet 
ON RestaurantID = Res_ID
WHERE Address LIKE '%Lombard%';

SELECT * FROM Lombard;

CREATE VIEW OakBrook
AS
SELECT RestaurantName, Phone, Address, DietName, MenuItem
FROM restaurant JOIN diet 
ON RestaurantID = Res_ID
WHERE Address LIKE '%Oak Brook%';

SELECT * FROM OakBrook;

CREATE VIEW Lockport
AS
SELECT RestaurantName, Phone, Address, DietName, MenuItem
FROM restaurant JOIN diet 
ON RestaurantID = Res_ID
WHERE Address LIKE '%Lockport%';

SELECT * FROM Lockport;

CREATE VIEW Lisle
AS
SELECT RestaurantName, Phone, Address, DietName, MenuItem
FROM restaurant JOIN diet 
ON RestaurantID = Res_ID
WHERE Address LIKE '%Lisle%';

SELECT * FROM Lisle;

CREATE VIEW Wheaton
AS
SELECT RestaurantName, Phone, Address, DietName, MenuItem
FROM restaurant JOIN diet 
ON RestaurantID = Res_ID
WHERE Address LIKE '%Wheaton%';

SELECT * FROM Wheaton;

CREATE VIEW Naperville
AS
SELECT RestaurantName, Phone, Address, DietName, MenuItem
FROM restaurant JOIN diet 
ON RestaurantID = Res_ID
WHERE Address LIKE '%Naperville%';

SELECT * FROM Naperville;

CREATE VIEW CarolStream
AS
SELECT RestaurantName, Phone, Address, DietName, MenuItem
FROM restaurant JOIN diet 
ON RestaurantID = Res_ID
WHERE Address LIKE '%Carol Stream%';

SELECT * FROM CarolStream;

CREATE VIEW VillaPark
AS
SELECT RestaurantName, Phone, Address, DietName, MenuItem
FROM restaurant JOIN diet 
ON RestaurantID = Res_ID
WHERE Address LIKE '%Villa Park%';

SELECT * FROM VillaPark;

CREATE VIEW Aurora
AS
SELECT RestaurantName, Phone, Address, DietName, MenuItem
FROM restaurant JOIN diet 
ON RestaurantID = Res_ID
WHERE Address LIKE '%Aurora%';

SELECT * FROM Aurora;

CREATE VIEW Bridgeview
AS
SELECT RestaurantName, Phone, Address, DietName, MenuItem
FROM restaurant JOIN diet 
ON RestaurantID = Res_ID
WHERE Address LIKE '%Bridgeview%';

SELECT * FROM Bridgeview;

CREATE VIEW HighlandPark
AS
SELECT RestaurantName, Phone, Address, DietName, MenuItem
FROM restaurant JOIN diet 
ON RestaurantID = Res_ID
WHERE Address LIKE '%Highland Park%';

SELECT * FROM HighlandPark;


CREATE VIEW Skokie
AS
SELECT RestaurantName, Phone, Address, DietName, MenuItem
FROM restaurant JOIN diet 
ON RestaurantID = Res_ID
WHERE Address LIKE '%Skokie%';

SELECT * FROM Skokie;