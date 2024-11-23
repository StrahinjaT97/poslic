CREATE DATABASE sportcontract;

CREATE TABLE LIGA (
  LigaId int PRIMARY KEY AUTO_INCREMENT,
  ImeNaDashboardu varchar(255) NOT NULL,
  ImeZaUpload varchar(255) NOT NULL,
  BucketName varchar(255) NOT NULL
);

CREATE TABLE DIVIZIJA (
  DivizijaId int PRIMARY KEY AUTO_INCREMENT,
  LigaId int NOT NULL,
  BucketName varchar(255)
);


CREATE TABLE SAJT(
  SajtId int PRIMARY KEY AUTO_INCREMENT,
  LigaId int NOT NULL,
  Url varchar(255) NOT NULL,
  Username varchar(255) NOT NULL,
  Password varchar(255) NOT NULL
);


CREATE TABLE DULTask(
  DULTaskId int PRIMARY KEY AUTO_INCREMENT,
  StatusId int NOT NULL DEFAULT 200,
  ErrorMessage varchar(255),
  TaskStartDateAndTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
  TaskEndDateAndTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
  LigaId int,
  DivizijaId int,
  HomeTeamId varchar(255),
  AwayTeamId varchar(255),
  GameDateAndTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);


CREATE TABLE DULTaskStatus(
	DULTaskStatusId int PRIMARY KEY AUTO_INCREMENT,
  Name ENUM('Not Started', 'Working', 'Success', 'Failure', 'File exists in Bucket') NOT NULL
);


ALTER TABLE DIVIZIJA
ADD FOREIGN KEY (LigaId) REFERENCES liga(LigaId);


ALTER TABLE DULTASK
ADD FOREIGN KEY (LigaId) REFERENCES LIGA(LigaId);
ALTER TABLE DULTASK
ADD FOREIGN KEY (DivizijaId) REFERENCES DIVIZIJA(DivizijaId);






