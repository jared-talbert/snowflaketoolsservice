{#
 # pgAdmin 4 - Snowflake Tools
 #
 # Copyright (C) 2013 - 2017, The pgAdmin Development Team
 # This software is released under the Snowflake Licence
 #}
{### SQL to create tablespace object ###}
{% if data %}
CREATE TABLESPACE {{ conn|qtIdent(data.name) }}
{% if data.spcuser %}
  OWNER {{ conn|qtIdent(data.spcuser) }}
{% endif %}
  LOCATION {{ data.spclocation|qtLiteral }};

{% endif %}