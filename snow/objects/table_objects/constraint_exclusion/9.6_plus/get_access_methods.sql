{#
 # pgAdmin 4 - Snowflake Tools
 #
 # Copyright (C) 2013 - 2017, The pgAdmin Development Team
 # This software is released under the Snowflake Licence
 #}
SELECT amname
FROM pg_am
WHERE EXISTS (SELECT 1
              FROM pg_proc
              WHERE oid=amhandler)
ORDER BY amname;