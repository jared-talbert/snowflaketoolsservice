{#
 # pgAdmin 4 - Snowflake Tools
 #
 # Copyright (C) 2013 - 2017, The pgAdmin Development Team
 # This software is released under the Snowflake Licence
 #}
{# ===== fetch schema name =====#}
SELECT
    nspname
FROM
    pg_namespace
WHERE
    oid = {{ scid }}::oid;
