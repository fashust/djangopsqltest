CREATE FUNCTION funcname (argument-list)
  RETURNS return-type
AS $$
  # PL/Python function body
$$ LANGUAGE plpythonu;

CREATE FUNCTION pyreplace(x text)
  RETURNS text
AS $$
  return x.replace('123', '256')
$$ LANGUAGE plpythonu;

psqltest=# select * from pyreplace('123 123');
 pyreplace
-----------
 256 256
(1 row)


CREATE TABLE reservation  (room int, during tsrange);
INSERT INTO reservation VALUES (1, '[2015-01-31 14:30, 2015-01-31 15:30)');
