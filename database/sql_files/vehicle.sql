DROP TABLE IF EXISTS Parking_Slots;

CREATE TABLE Parking_Slots (
  ID int NOT NULL,
  Kind varchar(255) NOT NULL,
  Type varchar(255) NOT NULL,
  nickname varchar(255) NOT NULL,
  area decimal NOT NULL,

  PRIMARY KEY (ID, Lat_A, Long_A, Lat_B, Long_B, Area)
);
