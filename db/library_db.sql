
create database if not exists library_db;


USE library_db;

create table if not exists libro(
	libro_id INT NOT NULL auto_increment,
    titulo varchar(30) not null,
    autor varchar(75) not null,
    editorial varchar(30) not null,
    no_paginas int not null,
    genero_id VARCHAR(30) not null,
    cantidad int not null,
    disponible int not null,
    
    primary key(libro_id)
    
) ENGINE = INNODB;
    
create table if not exists usuario(
	usuario_id int not null auto_increment,
    nombre_completo varchar(75) not null,
    email varchar(30) not null,
    telefono varchar(10) not null,
    
    primary key (usuario_id)
) ENGINE = INNODB;

create table if not exists prestamo(
	prestamo_id int not null auto_increment,
    usuario_id int not null,
    libro_id int not null,
    fecha date,
    estatus ENUM('Pendiente', 'Entregado', 'Vencido'),
    
    primary key (prestamo_id),
    
    constraint fk_usuario foreign key (usuario_id)
		references usuario(usuario_id)
        on delete cascade
        on update cascade,
	
    constraint fk_libro foreign key(libro_id)
		references libro(libro_id)
        on delete cascade
        on update cascade
    
) ENGINE = INNODB;


