CREATE DATABASE sportcontractDB;

CREATE TABLE LIGA (
  LigaId int PRIMARY KEY,
  Name varchar(255) NOT NULL,
  BucketName varchar(255) NOT NULL,
  FormatNazivFajla varchar(255) NOT NULL,
  SajtId int FOREIGN KEY REFERENCES SAJT(SajtId),
  UrlGuid varchar(255) NOT NULL
);

CREATE TABLE DIVIZIJA (
  DivizijaId int PRIMARY KEY,
  LigaId int FOREIGN KEY REFERENCES LIGA(LigaId),
  SajtId int FOREIGN KEY REFERENCES SAJT(SajtId),
  UrlGuid varchar(255) NOT NULL,
);

CREATE TABLE TIM (
  TimId int PRIMARY KEY,
  SiteName varchar(255),
  SajtId int FOREIGN KEY REFERENCES SAJT(SajtId),
  FileName varchar(255) NOT NULL
);

CREATE TABLE SAJT(
  SajtId int PRIMARY KEY,
  Url varchar(255) NOT NULL,
);

CREATE TABLE DULTask(
  DULTaskId int PRIMARY KEY,
  StatusId int NOT NULL DEFAULT 200,
  ErrorMessage varchar(65535),
  TaskStartDateAndTime DATETIME DEFAULT CURRENT_TIMESTAMP(),
  TaskEndDateAndTime DATETIME DEFAULT CURRENT_TIMESTAMP(),
  LigaId int FOREIGN KEY REFERENCES LIGA(LigaId),
  DivizijaId int FOREIGN KEY REFERENCES DIVIZIJA(DivizijaId),
  HomeTeamId varchar FOREIGN KEY REFERENCES TIM(TimId),
  AwayTeamId varchar FOREIGN KEY REFERENCES TIM(TimId),
  GameDateAndTime DATETIME DEFAULT CURRENT_TIMESTAMP(),
);

