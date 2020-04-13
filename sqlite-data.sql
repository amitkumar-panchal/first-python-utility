
drop table data;

create table data (
	id	    integer		    primary key autoincrement not null ,
	name	varchar(255)	not null,
	lei	    char(20)	    not null
);

create unique index idx_data on data (lei);