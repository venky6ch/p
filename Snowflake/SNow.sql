

select * from information_schema.packages where language='python';

select * from information_schema.packages where language='python' and package_name in ('regex') ;


Use database interview;
use schema questions;

DECLARE
  counter INTEGER DEFAULT 0;
  maximum_count INTEGER default 5;
BEGIN
  FOR i IN 1 TO maximum_count DO
    counter := counter + 1;
  END FOR;
  RETURN counter;
END;


CREATE OR REPLACE PROCEDURE increment_counter()
RETURNS INTEGER
LANGUAGE SQL
AS
$$
DECLARE
  counter INTEGER DEFAULT 0;
  maximum_count INTEGER default 5;
BEGIN
  FOR i IN 1 TO maximum_count DO
    counter := counter + 1;
  END FOR;
  RETURN counter;
END;
$$;
