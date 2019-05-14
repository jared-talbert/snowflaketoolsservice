{#
 # pgAdmin 4 - Snowflake Tools
 #
 # Copyright (C) 2013 - 2017, The pgAdmin Development Team
 # This software is released under the Snowflake Licence
 #}
SELECT
    rolname, rolcanlogin, rolcatupdate, rolsuper
FROM
    pg_roles
WHERE oid = {{ rid }}::OID
