{#
 # pgAdmin 4 - Snowflake Tools
 #
 # Copyright (C) 2013 - 2017, The pgAdmin Development Team
 # This software is released under the Snowflake Licence
 #}
{% if data %}
ALTER TABLE {{ conn|qtIdent(data.nspname, data.relname) }} DROP CONSTRAINT {{ conn|qtIdent(data.name) }};
{% endif %}
