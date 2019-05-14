{#
 # pgAdmin 4 - Snowflake Tools
 #
 # Copyright (C) 2013 - 2017, The pgAdmin Development Team
 # This software is released under the Snowflake Licence
 #}
SELECT opcname,  opcmethod
FROM pg_opclass
    WHERE opcmethod = {{oid}}::OID
    AND NOT opcdefault
    ORDER BY 1;