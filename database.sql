-- ============================================================================
-- E-VOTING SYSTEM USING BLOCKCHAIN TECHNOLOGY (2023–2024)
-- SQL Schema & Seed Data (MySQL & SQLite Compatible)
-- ============================================================================
-- Author:      Ateeq Bin Mubarak Wahlan (Roll No: 160920733003)
-- WahlanOS:    https://wahlanos.com ↗ | https://github.com/ateeq-wahlan
-- Institution: LIET (Osmania University)
-- Academic Yr: 2023–2024 (B.E. Computer Science & Engineering)
-- ============================================================================

CREATE DATABASE IF NOT EXISTS evoting;
USE evoting;

-- ----------------------------------------------------------------------------
-- 1. Core Electoral Roll & Party Registry Tables (`register` & `addparty`)
-- ----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS register (
    username VARCHAR(30) PRIMARY KEY,
    full_name VARCHAR(80) DEFAULT '',
    epic_id VARCHAR(30) DEFAULT '',
    password VARCHAR(64) NOT NULL,
    contact VARCHAR(15) NOT NULL,
    email VARCHAR(50) NOT NULL,
    address VARCHAR(100) NOT NULL,
    profile_image VARCHAR(180) DEFAULT 'https://randomuser.me/api/portraits/men/32.jpg',
    face_signature VARCHAR(64),
    registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS addparty (
    id INT PRIMARY KEY AUTO_INCREMENT,
    candidatename VARCHAR(50) NOT NULL,
    partyname VARCHAR(80) NOT NULL,
    areaname VARCHAR(100) NOT NULL,
    image VARCHAR(120) NOT NULL,
    party_code VARCHAR(16) NOT NULL,
    manifesto VARCHAR(255) DEFAULT ''
);

-- ----------------------------------------------------------------------------
-- 2. 3NF Normalized Relational Tables (`Voter`, `Election`, `Ballot`, `Voting`)
-- ----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS Voter (
    Voter_ID INT PRIMARY KEY AUTO_INCREMENT,
    Username VARCHAR(30) UNIQUE NOT NULL,
    Password VARCHAR(64) NOT NULL,
    Email VARCHAR(50) NOT NULL,
    Address VARCHAR(100) NOT NULL,
    Contact VARCHAR(15),
    Biometric_Hash VARCHAR(64)
);

CREATE TABLE IF NOT EXISTS Election (
    Election_ID INT PRIMARY KEY AUTO_INCREMENT,
    Election_Name VARCHAR(100) NOT NULL,
    Start_Date DATE NOT NULL,
    End_Date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS Ballot (
    Ballot_ID INT PRIMARY KEY AUTO_INCREMENT,
    Election_ID INT NOT NULL,
    Ballot_Title VARCHAR(100) NOT NULL,
    Ballot_Question VARCHAR(255) NOT NULL,
    FOREIGN KEY (Election_ID) REFERENCES Election(Election_ID)
);

CREATE TABLE IF NOT EXISTS Voting (
    Vote_ID INT PRIMARY KEY AUTO_INCREMENT,
    Voter_ID INT NOT NULL,
    Election_ID INT NOT NULL,
    Ballot_ID INT NOT NULL,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    Selected_Option VARCHAR(100) NOT NULL,
    Block_Index INT NOT NULL,
    Block_Hash VARCHAR(64) NOT NULL,
    Previous_Hash VARCHAR(64) NOT NULL,
    Homomorphic_Commitment VARCHAR(64) NOT NULL
);

-- ----------------------------------------------------------------------------
-- 3. Default National & Regional Party Roster (8 Parties + Official Symbols)
-- ----------------------------------------------------------------------------

INSERT INTO addparty (candidatename, partyname, areaname, image, party_code, manifesto) VALUES
('Rajeshwar Rao Deshmukh', 'Bharatiya Janata Party (BJP)', 'Jubilee Hills', 'static/parties/bjp.svg', 'BJP', 'Digital Infrastructure, Urban Mobility & Industrial Growth Corridors'),
('Dr. Ananya Reddy', 'Indian National Congress (INC)', 'Santosh Nagar', 'static/parties/inc.svg', 'INC', 'Universal Healthcare Access, Youth Employment & Civic Welfare'),
('Vikramaditya Sharma', 'Aam Aadmi Party (AAP)', 'Secunderabad', 'static/parties/aap.svg', 'AAP', 'Model Public Schools, Mohalla Clinics & Zero-Corruption Governance'),
('K. Chandrasekhar Goud', 'Bharat Rashtra Samithi (BRS)', 'Tolichowki', 'static/parties/brs.svg', 'BRS', 'IT Corridor Expansion, 24x7 Clean Water & Metro Connectivity'),
('Syed Zafarullah Quadri', 'All India Majlis-e-Ittehadul Muslimeen (AIMIM)', 'Charminar', 'static/parties/aimim.svg', 'AIMIM', 'Old City Heritage Renewal, Minority Education & Healthcare Centers'),
('Prabhakar Rao Ambedkar', 'Bahujan Samaj Party (BSP)', 'Mallepally', 'static/parties/bsp.svg', 'BSP', 'Social Justice, Equal Opportunity & Grassroots Empowerment'),
('Comrade Sitaramacharyulu', 'Communist Party of India (Marxist) (CPI-M)', 'Mehdipatnam', 'static/parties/cpim.svg', 'CPI-M', 'Labour Rights, Public Transport Subsidies & Affordable Housing'),
('None of the Above (NOTA)', 'NOTA — Official Electoral Option', 'All Constituencies', 'static/parties/nota.svg', 'NOTA', 'Constitutional Right to Reject All Listed Candidates');
