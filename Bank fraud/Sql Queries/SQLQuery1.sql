
CREATE TABLE Dim_Customer (
    AccountID VARCHAR(50) PRIMARY KEY,
    Customer_Name VARCHAR(100),
    CustomerOccupation VARCHAR(100),
    TotalTransactions INT,
    PreviousFraudulentActivity BIT,  
    RiskValue INT                   
);


CREATE TABLE Dim_Merchant (
    MerchantID VARCHAR(50) PRIMARY KEY,
	MerchantCatagory VARCHAR(50)
);

CREATE TABLE Dim_Date (
    Date_ID INT IDENTITY(1,1) PRIMARY KEY ,
    FullDate DATE,
    Day INT,
    Month INT,
    Year INT,
);

CREATE TABLE Fact_Transactions (
    TransactionID VARCHAR(50) PRIMARY KEY,
    AccountID VARCHAR(50),
    MerchantID VARCHAR(50),
    Date_ID INT,
    TransactionAmount DECIMAL(18, 2),
    TransactionType VARCHAR(20),
    Channel VARCHAR(20),
    place VARCHAR(100),
    IP_Address VARCHAR(50),
    AccountBalance DECIMAL(18, 2),
    FraudLabel BIT,

    FOREIGN KEY (AccountID) REFERENCES Dim_Customer(AccountID),
    FOREIGN KEY (MerchantID) REFERENCES Dim_Merchant(MerchantID),
    FOREIGN KEY (Date_ID) REFERENCES Dim_Date(Date_ID)
);


CREATE TABLE Staging_Transactions (
    TransactionID VARCHAR(50),
    AccountID VARCHAR(50),
    MerchantID VARCHAR(50),
    [date] DATE,
    TransactionAmount DECIMAL(18, 2),
    TransactionType VARCHAR(20),
    Channel VARCHAR(20),
    place VARCHAR(100),
    IP_Address VARCHAR(50),
    AccountBalance DECIMAL(18, 2),
    FraudLabel BIT
);

