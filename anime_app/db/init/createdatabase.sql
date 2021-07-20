CREATE DATABASE anime_app;
\c anime_app

CREATE TABLE users(
    id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

INSERT INTO users VALUES(1, 'sample', 'sample@sample.com');
INSERT INTO users VALUES(2, 'test', 'test@test.com');
INSERT INTO users VALUES(3, 'app', 'app@app.com');
