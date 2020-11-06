DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS fitness_classes;
DROP TABLE IF EXISTS instructors;


CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    gender VARCHAR (255),
    age INT
);

CREATE TABLE fitness_classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    time VARCHAR (255),
    duration INT,
    class_type VARCHAR(255)
);

CREATE TABLE instructors (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255)
    -- fitness_class_id INT REFERENCES fitness_classes_id(id),
    -- member_id INT REFERENCES members(id)
);

