DROP DATABASE IF EXISTS SQLAlchemy;

CREATE DATABASE SQLAlchemy;

\c SQLAlchemy

CREATE TABLE users
(
user_id SERIAL PRIMARY KEY,
user_first_name TEXT NOT NULL,
user_last_name TEXT NOT NULL,
image_url TEXT NOT NULL   
);

CREATE TABLE posts
(
post_id SERIAL PRIMARY KEY,
post_title TEXT NOT NULL,
post_content TEXT NOT NULL,
created_at TEXT NOT NULL,
Foreign Key (user_id) References users(id)  
);

CREATE TABLE post_tags
(
Foreign Key (post_id) References posts(id),
Foreign Key (tag_id) References tags(id)  
);

CREATE TABLE tags
(
tag_id SERIAL PRIMARY KEY,
tag_name TEXT NOT NULL,
tag_posts TEXT NOT NULL
);

INSERT INTO users
(user_id, user_first_name, user_last_name, image_url)
VALUES
('1', '', '', '');

INSERT INTO posts
(post_id, post_title, post_content, created_at, user_id)
VALUES
('1', '', '', '', '');

INSERT INTO post_tags
(post_id, tag_id)
VALUES
('', '');

INSERT INTO tags
(tag_id, tag_name, tag_posts)
VALUES
('1', '', '');