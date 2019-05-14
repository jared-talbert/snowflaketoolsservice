{#
 # pgAdmin 4 - Snowflake Tools
 #
 # Copyright (C) 2013 - 2017, The pgAdmin Development Team
 # This software is released under the Snowflake Licence
 #}
SELECT ct.conindid AS oid
FROM pg_constraint ct
WHERE contype='x' AND
ct.conname = {{ name|qtLiteral }};