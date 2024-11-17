CREATE DATABASE sportcontractDB;

CREATE TABLE LIGA (
  LigaId int PRIMARY KEY,
  Name varchar(255) NOT NULL,
  BucketName varchar(255) NOT NULL,
  FormatNazivFajla varchar(255) NOT NULL,
  SajtId int NOT NULL,
  CONSTRAINT SajtId FOREIGN KEY (SajtId) REFERENCES SAJT(SajtId),
  UrlGuid varchar(255) NOT NULL
);

CREATE TABLE DIVIZIJA (
  DivizijaId int PRIMARY KEY,
  LigaId int NOT NULL,
  SajtId int NOT NULL,
  CONSTRAINT LigaId FOREIGN KEY (LigaId) REFERENCES liga(LigaId),
  CONSTRAINT SatjId FOREIGN KEY (SajtId) REFERENCES sajt(SajtId),
  UrlGuid varchar(255) NOT NULL
);

CREATE TABLE TIM (
  TimId int PRIMARY KEY,
  SiteName varchar(255),
  SajtId int NOT NULL,
  FileName varchar(255) NOT NULL,
  CONSTRAINT SatjId FOREIGN KEY (SajtId) REFERENCES sajt(SajtId)
);

CREATE TABLE SAJT(
  SajtId int,
  Url varchar(255) NOT NULL,
  PRIMARY KEY (SajtId)
);



CREATE TABLE DULTask(
  DULTaskId int PRIMARY KEY,
  StatusId int NOT NULL DEFAULT 200,
  ErrorMessage varchar(65535),
  TaskStartDateAndTime DATETIME DEFAULT CURRENT_TIMESTAMP(),
  TaskEndDateAndTime DATETIME DEFAULT CURRENT_TIMESTAMP(),
  LigaId int,
  DivizijaId int,
  HomeTeamId varchar,
  AwayTeamId varchar,
  GameDateAndTime DATETIME DEFAULT CURRENT_TIMESTAMP(),
  CONSTRAINT LigaId FOREIGN KEY REFERENCES LIGA(LigaId),
  CONSTRAINT DivizijaId FOREIGN KEY REFERENCES DIVIZIJA(DivizijaId),
  CONSTRAINT HomeTeamId FOREIGN KEY REFERENCES TIM(TimId),
  CONSTRAINT AwayTeamId FOREIGN KEY REFERENCES TIM(TimId)
);









