{#
 # pgAdmin 4 - Snowflake Tools
 #
 # Copyright (C) 2013 - 2017, The pgAdmin Development Team
 # This software is released under the Snowflake Licence
 #}
DROP TABLE {{conn|qtIdent(data.schema, data.name)}}{% if cascade %} CASCADE{% endif %};