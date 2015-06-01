drop database if exists python_blog;

create database python_blog;

use python_blog;

grant select, insert, update, delete on python_blog.* to 'www-data'@'localhost' identified by 'www-data';

create table user (
    `id` varchar(50) not null,
    `email` varchar(50) not null,
    `password` varchar(50) not null,
    `admin` bool not null,
    `name` varchar(50) not null,
    `image` varchar(500) not null,
    `create` real not null,
    unique key `idx_email` (`email`),
    key `idx_create` (`create`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table blog (
    `id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_image` varchar(500) not null,
    `name` varchar(50) not null,
    `summary` varchar(200) not null,
    `content` mediumtext not null,
    `create` real not null,
    key `idx_create` (`create`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table comment (
    `id` varchar(50) not null,
    `blog_id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_image` varchar(500) not null,
    `content` mediumtext not null,
    `create` real not null,
    key `idx_create` (`create`),
    primary key (`id`)
) engine=innodb default charset=utf8;