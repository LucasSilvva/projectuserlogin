create database sistema;
create table user(
id int auto_increment primary key,
nome varchar (255) not null,
senha varchar (10) not null,
email varchar (100) unique
);
alter table user add column senha varchar(10);