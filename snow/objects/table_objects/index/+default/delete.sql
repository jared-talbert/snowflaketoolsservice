{#
 # pgAdmin 4 - Snowflake Tools
 #
 # Copyright (C) 2013 - 2017, The pgAdmin Development Team
 # This software is released under the Snowflake Licence
 #}
DROP INDEX {{conn|qtIdent(data.nspname, data.name)}}{% if cascade %} cascade{% endif %};