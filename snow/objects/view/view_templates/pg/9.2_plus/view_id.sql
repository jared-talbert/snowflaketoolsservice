{#
 # pgAdmin 4 - Snowflake Tools
 #
 # Copyright (C) 2013 - 2017, The pgAdmin Development Team
 # This software is released under the Snowflake Licence
 #}
{# ===== Below will provide view id for last created view ===== #}
{% if data %}
SELECT c.oid, c.relname FROM pg_class c WHERE c.relname = '{{ data.name }}';
{% endif %}
