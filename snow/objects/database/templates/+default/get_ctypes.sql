{#
 # pgAdmin 4 - Snowflake Tools
 #
 # Copyright (C) 2013 - 2017, The pgAdmin Development Team
 # This software is released under the Snowflake Licence
 #}
SELECT DISTINCT(datctype) AS cname
FROM pg_database
UNION
SELECT DISTINCT(datcollate) AS cname
FROM pg_database