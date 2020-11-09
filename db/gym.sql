
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS fitness_classes;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS instructors;



CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    gender VARCHAR (255),
    age INT
);

CREATE TABLE instructors (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255)
    -- fitness_classes_id INT REFERENCES fitness_classes_id(id),
);

CREATE TABLE fitness_classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    class_time VARCHAR (255),
    duration INT,
    class_type VARCHAR(255),
    instructor_id INT REFERENCES instructors(id)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id),
    fitness_class_id INT REFERENCES fitness_classes(id)
)



