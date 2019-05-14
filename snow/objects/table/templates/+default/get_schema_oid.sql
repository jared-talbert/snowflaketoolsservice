{#
 # pgAdmin 4 - Snowflake Tools
 #
 # Copyright (C) 2013 - 2017, The pgAdmin Development Team
 # This software is released under the Snowflake Licence
 #}
{# ===== fetch new assigned schema oid ===== #}
SELECT
    c.relnamespace as scid
FROM
    pg_class c
WHERE
{% if tid %}
    c.oid = {{tid}}::oid;
{% else %}
    c.relname = {{tname|qtLiteral}}::text;
{% endif %}
