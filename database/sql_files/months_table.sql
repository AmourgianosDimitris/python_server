DROP TABLE IF EXISTS Months;

CREATE TABLE Months (
  ID int NOT NULL,
  Parking_ID int NOT NULL,
  January int NOT NULL,
  February int NOT NULL,
  March int NOT NULL,
  April int NOT NULL,
  May int NOT NULL,
  June int NOT NULL,
  July int NOT NULL,
  August int NOT NULL,
  September int NOT NULL,
  October int NOT NULL,
  November int NOT NULL,
  December int NOT NULL,

  PRIMARY KEY (ID, Parking_ID),
  FOREIGN KEY (Parking_ID) REFERENCES Parking_Slots(ID)
);
