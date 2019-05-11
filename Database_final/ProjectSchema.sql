CREATE TABLE IDCodes(
State_Code INT,
County_Code INT,
State VARCHAR(255),
County VARCHAR(255)
);

CREATE TABLE Violent_Crimes(
State VARCHAR(255),
County VARCHAR(255),
Murder INT NULL,
Rape_Revised INT NULL,
Rape_Legacy INT NULL,
Robbery INT NULL,
Assault INT NULL,
PRIMARY KEY (State,County)
);

CREATE TABLE Property_crimes(
State VARCHAR(255),
County VARCHAR(255),
Burglary INT,
Larceny INT,
Vehicle INT,
Arson INT,
PRIMARY KEY (State,County)
);

CREATE TABLE MALE_Demos(
State VARCHAR(255),
County VARCHAR(255),
White_Only_MALE INT,
Black_Only_MALE INT,
American_Indian_Or_Alaskan_Only_MALE INT,
Asian_Only_MALE INT,
Hawaiian_Or_Pacfic_Islander_Only_MALE INT,
Two_Or_More_Races_MALE INT,
PRIMARY KEY (State,County)
);

CREATE TABLE FEMALE_Demos(
State VARCHAR(255),
County VARCHAR(255),
White_Only_FEMALE INT,
Black_Only_FEMALE INT,
American_Indian_Or_Alaskan_Only_FEMALE INT,
Asian_Only_FEMALE INT,
Hawaiian_Or_Pacfic_Islander_Only_FEMALE INT,
Two_Or_More_Races_FEMALE INT,
PRIMARY KEY (State,County)
);

CREATE TABLE Non_Hispanic_Demos(
State VARCHAR(255),
County VARCHAR(255),
Non_Hisp_White_Only_MALE INT,
Non_Hisp_White_Only_FEMALE INT,
Non_Hisp_Black_Only_MALE INT,
Non_Hisp_Black_Only_FEMALE INT,
Non_Hisp_American_Indian_Or_Alaskan_Only_MALE INT,
Non_Hisp_American_Indian_Or_Alaskan_Only_FEMALE INT,
Non_Hisp_Asian_Only_MALE INT,
Non_Hisp_Asia_Only_FEMALE INT,
Non_Hisp_Hawaiian_Or_Pacfic_Islander_Only_MALE INT,
Non_Hisp_Hawaiian_Or_Pacfic_Islander_Only_FEMALE INT,
Non_Hisp_Two_Or_More_Races_MALE INT,
Non_Hisp_Two_Or_More_Races_FEMALE INT,
PRIMARY KEY (State,County)
);

CREATE TABLE Hispanic_Demos(
State VARCHAR(255),
County VARCHAR(255),
Hisp_White_Only_MALE INT,
Hisp_White_Only_FEMALE INT,
Hisp_Black_Only_MALE INT,
Hisp_Black_Only_FEMALE INT,
Hisp_American_Indian_Or_Alaskan_Only_MALE INT,
Hisp_American_Indian_Or_Alaskan_Only_FEMALE INT,
Hisp_Asian_Only_MALE INT,
Hisp_Asia_Only_FEMALE INT,
Hisp_Hawaiian_Or_Pacfic_Islander_Only_MALE INT,
Hisp_Hawaiian_Or_Pacfic_Islander_Only_FEMALE INT,
Hisp_Two_Or_More_Races_MALE INT,
Hisp_Two_Or_More_Races_FEMALE INT,
PRIMARY KEY (State,County)
);
