create table etage(
    -> id int primary key auto_increment,
    -> name varchar (255),
    -> id_etage int,
    -> capacite int);

create table salles(
    -> id int primary key auto_increment,
    -> name varchar (255),
    -> id_etage int,
    -> capacite int);
