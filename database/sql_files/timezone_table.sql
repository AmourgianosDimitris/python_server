DROP TABLE IF EXISTS Months;

CREATE TABLE Months (
  ID int NOT NULL,
  Parking_ID int NOT NULL,
  Morning int NOT NULL,
  Noon int NOT NULL,
  Afternoon int NOT NULL,
  Night int NOT NULL,

  PRIMARY KEY (ID, Parking_ID),
  FOREIGN KEY (Parking_ID) REFERENCES Parking_Slots(ID)
);
