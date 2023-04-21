DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS kanbans;

CREATE TABLE users (
    uid INTEGER PRIMARY KEY AUTOINCREMENT,
    nickname TEXT NOT NULL
);

CREATE TABLE kanbans (
    uid INTEGER,
    type TEXT NOT NULL,
    content TEXT NOT NULL,
    time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);