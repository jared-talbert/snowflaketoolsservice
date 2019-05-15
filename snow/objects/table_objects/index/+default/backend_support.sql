{#
 # pgAdmin 4 - Snowflake Tools
 #
 # Copyright (C) 2013 - 2017, The pgAdmin Development Team
 # This software is released under the Snowflake Licence
 #}
{#=============Checks if it is materialized view========#}
{% if vid %}
SELECT
    CASE WHEN c.relkind = 'm' THEN True ELSE False END As m_view
FROM
    pg_class c
WHERE
    c.oid = {{ vid }}::oid
{% endif %}