-- сделать реакцию на удаление предка

CREATE TABLE [Job] --1
(
    [JobId] INT  PRIMARY KEY,
    [Name] VARCHAR(20) NOT NULL UNIQUE
)

CREATE TABLE [Workers] --3
(
    [WorkersId] INT PRIMARY KEY REFERENCES People,
    [JobId] INT REFERENCES Job(JobId) NOT NULL
)

CREATE TABLE [People] --2
(
    [PeopleId] INT PRIMARY KEY,
    [Name] VARCHAR(20) NOT NULL,
    [Surname] VARCHAR(20) NOT NULL,
    [Patronymic] VARCHAR(20) NOT NULL,
    [PhoneNumber] varchar(11) NOT NULL UNIQUE check()---check каждый символ на [0-9]
)

CREATE TABLE [Account] --4
(
    [AccountId] INT PRIMARY KEY REFERENCES People(PeopleId),
    [Name] VARCHAR(30) NOT NULL,
    [LastEntrance] DATE NOT NULL
)

CREATE TABLE [Account-Booking] -- 16
(
    [Account-BookingId] INT PRIMARY KEY,
    [AccountId] INT REFERENCES Account(AccountId) NOT NULL,
    [BookingId] INT REFERENCES Booking(BookingId) NOT NULL
)

CREATE TABLE [Address] --5
(
    [AddressId] INT PRIMARY KEY,
    [Name] VARCHAR(20) NOT NULL,
    [Number] VARCHAR(5) NOT NULL,
    [Floor] NUMERIC(2) NOT NULL -----SMALLINT
)

CREATE TABLE [Hall] --6
(
    [HallId] INT PRIMARY KEY,
    [AddressId] INT REFERENCES Address(AddressId) NOT NULL,
    [Name] VARCHAR (20) NOT NULL
)

CREATE TABLE [Cafe] --7
(
    [CafeId] INT  PRIMARY KEY,
    [HallId] INT REFERENCES Hall(HallId) NOT NULL,
    [Name] VARCHAR (20) NOT NULL
)

CREATE TABLE [GameSpot] --9
(
    [GameSpotId] INT  PRIMARY KEY,
    [HallId] INT REFERENCES Hall(HallId) NOT NULL,
    [ComputerId] INT REFERENCES Computer(ComputerId) NOT NULL,
    [Name] VARCHAR (20) NOT NULL
)

CREATE TABLE [Computer] --8
(
    [ComputerId] INT PRIMARY KEY,
    [Number] NUMERIC(7) NOT NULL UNIQUE
)

CREATE TABLE [Rate] --10
(
    [RateId] INT PRIMARY KEY,
    [Name] VARCHAR(20) NOT NULL,
    [Price] NUMERIC NOT NULL
)

CREATE TABLE [Discount] --11
(
    [DiscountId] INT PRIMARY KEY,
    [NameOfDiscount] VARCHAR(20) NOT NULL UNIQUE,
    [AmountOfDiscount] NUMERIC NOT NULL
)

CREATE TABLE [Booking] --12
(
    [BookingId] INT PRIMARY KEY,
    [ComputersId] INT REFERENCES Computers(ComputersId) NOT NULL,
    [RateId] INT REFERENCES Rate(RateId) NOT NULL,
    [DiscountId] INT REFERENCES Discount(RateId) NOT NULL,
    [Data] DATE NOT NULL,
    [Time] TIME NOT NULL
)

CREATE TABLE [Games] --13
(
    [GamesId] INT PRIMARY KEY,
    [Name] VARCHAR(20) NOT NULL UNIQUE
)

CREATE TABLE [Computer-Games] --14
(
    [Computer-GamesId] INT PRIMARY KEY,
    [ComputersId] INT REFERENCES Computers(ComputersId) NOT NULL,
    [GamesId] INT REFERENCES Games(GamesId) NOT NULL
)

CREATE TABLE [Tournirs] --15
(
    [TournirsId] INT PRIMARY KEY,
    [HallId] INT REFERENCES Hall(HallId) NOT NULL,
    [Prize] NUMERIC NOT NULL,
    [Data]  DATE NOT NULL
)

CREATE TABLE [Accounts-Tournirs]
(
    [TournirsId] INT  PRIMARY KEY REFERENCES Tournirs(TournirsId),
    [AccountsId] INT  PRIMARY KEY REFERENCES Accounts(AccountsId)
)