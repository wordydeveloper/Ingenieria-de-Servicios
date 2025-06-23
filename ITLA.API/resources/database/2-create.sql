create table if not exists usuario(
	usuario_id bigserial primary key,
	nombre varchar(250) not null,
	correo varchar(250) not null,
	clave varchar not null,
	estado varchar(2) not null,
	fecha_creacion timestamp not null default (now() at time zone 'EDT'),
	fecha_actualizacion timestamp null,
	
	constraint usuario_estado_ck
		check(estado in ('AC', 'IN'))
);