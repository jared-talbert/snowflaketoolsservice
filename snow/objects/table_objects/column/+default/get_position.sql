{#
 # pgAdmin 4 - Snowflake Tools
 #
 # Copyright (C) 2013 - 2017, The pgAdmin Development Team
 # This software is released under the Snowflake Licence
 #}
SELECT att.attnum
FROM pg_attribute att
    WHERE att.attrelid = {{tid}}::oid
    AND att.attname = {{data.name|qtLiteral}}
