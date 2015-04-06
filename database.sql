PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE rooms (id integer primary key autoincrement not null, creator_uuid text not null, accesskey text unique not null, date datetime not null default current_timestamp);
COMMIT;

