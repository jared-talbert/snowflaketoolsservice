{#
 # pgAdmin 4 - Snowflake Tools
 #
 # Copyright (C) 2013 - 2017, The pgAdmin Development Team
 # This software is released under the Snowflake Licence
 #}
SELECT
    last_value,
    seqmin AS min_value,
    seqmax AS max_value,
    seqstart AS start_value,
    seqcache AS cache_value,
    seqcycle AS is_cycled,
    seqincrement AS increment_by,
    is_called
FROM pg_sequence, {{ conn|qtIdent(data.schema) }}.{{ conn|qtIdent(data.name) }}
WHERE seqrelid = '{{ conn|qtIdent(data.schema) }}.{{ conn|qtIdent(data.name) }}'::regclass
