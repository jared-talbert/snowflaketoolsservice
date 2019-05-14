{#
 # pgAdmin 4 - Snowflake Tools
 #
 # Copyright (C) 2013 - 2017, The pgAdmin Development Team
 # This software is released under the Snowflake Licence
 #}
DROP TRIGGER {{conn|qtIdent(data.name)}} ON {{conn|qtIdent(data.nspname, data.relname )}}{% if cascade %} CASCADE{% endif %};