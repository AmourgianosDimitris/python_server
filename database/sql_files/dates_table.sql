DROP TABLE IF EXISTS Dates;

CREATE TABLE Dates (
  ID int NOT NULL,
  Parking_ID int NOT NULL,
  Parking_Date date NOT NULL,
  Total int NOT NULL,

  PRIMARY KEY (ID, Parking_ID, Parking_Date),
  FOREIGN KEY (Parking_ID) REFERENCES Parking_Slots(ID)
);
