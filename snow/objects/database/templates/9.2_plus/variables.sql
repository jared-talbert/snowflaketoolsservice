{#
 # pgAdmin 4 - Snowflake Tools
 #
 # Copyright (C) 2013 - 2017, The pgAdmin Development Team
 # This software is released under the Snowflake Licence
 #}
SELECT
    name, vartype, min_val, max_val, enumvals
FROM pg_settings
WHERE context in ('user', 'superuser');
