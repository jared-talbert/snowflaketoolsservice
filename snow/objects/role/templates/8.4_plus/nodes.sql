{#
 # pgAdmin 4 - Snowflake Tools
 #
 # Copyright (C) 2013 - 2017, The pgAdmin Development Team
 # This software is released under the Snowflake Licence
 #}
SELECT
	r.oid, r.rolname as name, r.rolcanlogin, r.rolsuper
FROM
	pg_roles r
{% if rid %}
WHERE r.oid = {{ rid|qtLiteral }}::OID
{% endif %}
ORDER BY r.rolcanlogin, r.rolname
