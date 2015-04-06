PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE rooms (id integer primary key autoincrement not null, creator_uuid text not null, accesskey text unique not null, date datetime not null default current_timestamp, name text default "",vote_id integer not null default 1 );
CREATE TABLE votes (id integer primary key autoincrement not null, voter_uuid text not null, room_id integer not null, vote_id integer not null, value integer not null, date datetime not null default current_timestamp);
CREATE TABLE names (id integer primary key autoincrement not null, uuid text unique not null, name text default "");
COMMIT;

