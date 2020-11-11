
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
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    class_type VARCHAR(255),
    instructor_id INT REFERENCES instructors(id) ON DELETE CASCADE
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    fitness_class_id INT REFERENCES fitness_classes(id) ON DELETE CASCADE
)



