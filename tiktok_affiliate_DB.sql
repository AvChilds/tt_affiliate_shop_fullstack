CREATE DATABASE tiktok_affiliates;

USE tiktok_affiliates;

CREATE TABLE affiliates (
	id INT auto_increment,
    username VARCHAR (255),
    country VARCHAR (255),
    PRIMARY KEY (id)
    );

INSERT INTO affiliates
VALUES
(1, "mrshopper", "USA"),
(2, "missyhappy", "UK"),
(3, "wixandtix", "Spain"),
(4, "briggiefan", "USA"),
(5, "boocego", "USA"),
(6, "fridaygirl", "UK"),
(7, "polarishop", "Poland"),
(8, "artemisby", "UK")
;

CREATE TABLE videos (
	video_id INT AUTO_INCREMENT,
    affiliate_id INT,
    product_name VARCHAR(255) NOT NULL,
    views INT,
    commission_per_sale DECIMAL (5,2),
    no_of_sales INT,
    PRIMARY KEY (video_id),
    FOREIGN KEY (affiliate_id) REFERENCES affiliates(id)
    )
;

INSERT INTO videos
VALUES
(1, 2, "Phone Strap", 150, 0.30, 5),
(2, 1, "Super Vacuum Cleaner", 602, 3.50, 10),
(3, 1, "Pokemon Prismatic Pack", 1550, 2.55, 15),
(4, 4, "Love Rose Box", 255, 1.05, 2),
(5, 3, "Vox Mobilephone Holder", 456, 0.80, 65),
(6, 8, "Lorel Night Facial", 2235, 1.15, 75),
(7, 6, "Easyfit Wide Jeans", 660, 2.25, 32),
(8, 8, "Couple Night Out Cards", 155, 0.65, 12),
(9, 5, "Minsk Floor Sweep", 950, 1.35, 115),
(10, 7, "Grab Bluetooth Earphones", 2000, 2.00, 40)
;