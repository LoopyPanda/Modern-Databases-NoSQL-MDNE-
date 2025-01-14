-- Create User Table
CREATE TABLE Users (
    UserID SERIAL PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Email VARCHAR(255) UNIQUE
);

-- Create House Table
CREATE TABLE House (
    HouseID SERIAL PRIMARY KEY,
    AddressLine1 VARCHAR(255),
    AddressLine2 VARCHAR(255),
    City VARCHAR(255)
);

-- Create HouseUser Table
CREATE TABLE HouseUser (
    UserType VARCHAR(50),
    HouseID INT,
    UserID INT,
    StartDate DATE,
    EndDate DATE,
    PRIMARY KEY (HouseID, UserID),
    FOREIGN KEY (HouseID) REFERENCES House(HouseID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Create Appliance Table
CREATE TABLE Appliance (
    ApplianceID SERIAL PRIMARY KEY,
    Name VARCHAR(255),
    HouseID INT,
    FOREIGN KEY (HouseID) REFERENCES House(HouseID)
);

-- Drop the existing foreign key constraints (if any)
ALTER TABLE HouseUser DROP CONSTRAINT IF EXISTS houseuser_houseid_fkey;
ALTER TABLE HouseUser DROP CONSTRAINT IF EXISTS houseuser_userid_fkey;

-- Add CASCADE on UPDATE and NO ACTION on DELETE for HouseID
ALTER TABLE HouseUser
ADD CONSTRAINT houseuser_houseid_fkey
FOREIGN KEY (HouseID) 
REFERENCES House(HouseID)
ON DELETE NO ACTION
ON UPDATE CASCADE;

-- Add CASCADE on UPDATE and NO ACTION on DELETE for UserID
ALTER TABLE HouseUser
ADD CONSTRAINT houseuser_userid_fkey
FOREIGN KEY (UserID)
REFERENCES Users(UserID)
ON DELETE NO ACTION
ON UPDATE CASCADE;

-- Drop the existing foreign key constraint (if any)
ALTER TABLE Appliance DROP CONSTRAINT IF EXISTS appliance_houseid_fkey;

-- Add CASCADE on UPDATE and NO ACTION on DELETE for HouseID
ALTER TABLE Appliance
ADD CONSTRAINT appliance_houseid_fkey
FOREIGN KEY (HouseID)
REFERENCES House(HouseID)
ON DELETE NO ACTION
ON UPDATE CASCADE;
