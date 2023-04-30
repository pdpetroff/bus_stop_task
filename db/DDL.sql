CREATE USER bus_user WITH PASSWORD 'buspass';

CREATE DATABASE bus_database OWNER bus_user;

\c bus_database

CREATE TABLE bus_stops (
	id serial PRIMARY KEY,
	name VARCHAR ( 250 ) NOT NULL,
	location FLOAT[2] NOT NULL
);