{#
 # pgAdmin 4 - Snowflake Tools
 #
 # Copyright (C) 2013 - 2017, The pgAdmin Development Team
 # This software is released under the Snowflake Licence
 #}
SELECT nsp.nspname AS schema ,rel.relname AS table
FROM pg_class rel
    JOIN pg_namespace nsp
    ON rel.relnamespace = nsp.oid::oid
    WHERE rel.oid = {{tid}}::oid