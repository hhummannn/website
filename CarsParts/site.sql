CREATE TABLE prices (
  id serial PRIMARY KEY,
  uah float,
  usd float,
  eur float,
  UNIQUE (id)
);

CREATE TABLE models (
  id serial PRIMARY KEY,
  brand varchar,
  model varchar,
  UNIQUE (id)
);

CREATE TABLE parts (
  id serial PRIMARY KEY,
  model_id integer REFERENCES models (id),
  name varchar,
  description text,
  available integer,
  pricing integer,
  UNIQUE (id)
);

CREATE TABLE images (
  id serial PRIMARY KEY,
  image_name varchar,
  part_id integer REFERENCES parts (id),
  UNIQUE (id)
);

CREATE TABLE customers (
  id serial PRIMARY KEY,
  recipient_name varchar,
  recipient_address varchar,
  phone varchar,
  email varchar,
  UNIQUE (id)
);

CREATE TABLE orders (
  id serial PRIMARY KEY,
  order_number integer,
  customer_id integer REFERENCES customers (id),
  UNIQUE (id)
);

CREATE TABLE ordered_parts (
  id serial PRIMARY KEY,
  order_id integer REFERENCES orders (id),
  part_id integer REFERENCES parts (id),
  quantity integer,
  UNIQUE (id)
);

ALTER TABLE "parts" ADD FOREIGN KEY ("model_id") REFERENCES "models" ("id");

ALTER TABLE "parts" ADD FOREIGN KEY ("pricing") REFERENCES "prices" ("id");

ALTER TABLE "orders" ADD FOREIGN KEY ("customer_id") REFERENCES "customers" ("id");

ALTER TABLE "ordered_parts" ADD FOREIGN KEY ("order_id") REFERENCES "orders" ("id");

ALTER TABLE "ordered_parts" ADD FOREIGN KEY ("part_id") REFERENCES "parts" ("id");

ALTER TABLE "images" ADD FOREIGN KEY ("part_id") REFERENCES "parts" ("id");

INSERT INTO prices VALUES(1721.0,42.0,38.0);
INSERT INTO prices VALUES(5380.0,130.0,120.0);
INSERT INTO prices VALUES(3066.0,74.0,68.0);
INSERT INTO prices VALUES(540.0,13.0,12.0);
INSERT INTO prices VALUES(1660.0,40.0,37.0);
INSERT INTO prices VALUES(86,2.0,2.0);
INSERT INTO prices VALUES(8145,200.0,180.0);

INSERT INTO models VALUES('Toyota','Corolla');
INSERT INTO models VALUES('Toyota','Camry');
INSERT INTO models VALUES('Kia','Sportage');

INSERT INTO parts VALUES(1,'Cabin Filter','Part Number : 87139-YZZ34',10,1);
INSERT INTO parts VALUES(1,'Front Brake Pads','Part Number : 04465-F4010',25,2);
INSERT INTO parts VALUES(1,'Rear Brake Pads','Part Number : 04466-47101',25,3);
INSERT INTO parts VALUES(2,'Cabin Air Filter','Part Number : FDCAFM9',10,4);
INSERT INTO parts VALUES(2,'Ignition Coil Pack & Spark Plugs','Part Number : 90919-02266',10,5);
INSERT INTO parts VALUES(3,'Bumper Retainer','Part Number 865901W000',150,6);
INSERT INTO parts VALUES(3,'Service Kit','Kia Sportage Service Kit',5,7);

INSERT INTO images VALUES('toyota_corolla_cabin_filter_1.jpg',1);
INSERT INTO images VALUES('toyota_corolla_front_brake_pads_1.jpg',2);
INSERT INTO images VALUES('toyota_corolla_rear_brake_pads_1.jpg',3);
INSERT INTO images VALUES('toyota_camry_cabin_air_filter_1.jpg',4);
INSERT INTO images VALUES('toyota_camry_ignition_coil_pack_and_spark_plugs_1.jpg',5);
INSERT INTO images VALUES('kia_sportage_bumper_retainer_1.jpg',6);
INSERT INTO images VALUES('kia_sportage_service_kit_1.jpg',7);