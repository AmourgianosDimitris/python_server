DROP TABLE IF EXISTS Types;

CREATE TABLE Types (
  ID int NOT NULL,
  Parking_ID int NOT NULL,
  Parking_Date date NOT NULL,
  Type varchar(5) NOT NULL,

  PRIMARY KEY (ID, Parking_ID, Parking_Date, Type),
  FOREIGN KEY (Parking_ID) REFERENCES Parking_Slots(ID)
);
