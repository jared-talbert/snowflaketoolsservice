{#
 # pgAdmin 4 - Snowflake Tools
 #
 # Copyright (C) 2013 - 2017, The pgAdmin Development Team
 # This software is released under the Snowflake Licence
 #}
SELECT
    ts.oid AS oid, spcname AS name, spcowner as owner
FROM
    pg_tablespace ts
{% if tsid %}
WHERE
    ts.oid={{ tsid|qtLiteral }}::OID
{% endif %}
ORDER BY name;
