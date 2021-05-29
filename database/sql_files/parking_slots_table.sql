DROP TABLE IF EXISTS Parking_Slots;

CREATE TABLE Parking_Slots (
  ID int NOT NULL,
  Lat_A decimal NOT NULL,
  Long_A decimal NOT NULL,
  Lat_B decimal NOT NULL,
  Long_B decimal NOT NULL,
  Street varchar(255) NOT NULL,
  Free boolean NOT NULL,
  Area decimal NOT NULL,
  Sum int NOT NULL,
  
  PRIMARY KEY (ID, Lat_A, Long_A, Lat_B, Long_B, Area)
);
