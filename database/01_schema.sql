begin;

create table users
(
	id serial not null
		constraint users_pkey
			primary key,
	user_name text not null
		constraint users_user_name_key
			unique,
	password_hash text not null
);

create table activity
(
    id serial not null
        constraint activity_pkey
            primary key,
    name text not null
);

create table current_status
(
    id serial not null
        constraint current_status_pkey
            primary key,

    age integer,
    height numeric,
    weight numeric,
    body_fat numeric,
    user_id integer references users(id),
    activity_id integer references activity(id)
);
commit;