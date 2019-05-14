{#
 # pgAdmin 4 - Snowflake Tools
 #
 # Copyright (C) 2013 - 2017, The pgAdmin Development Team
 # This software is released under the Snowflake Licence
 #}
ALTER TABLE {{ conn|qtIdent(data.schema, data.name) }}
    {% if is_enable_trigger == True %}ENABLE{% else %}DISABLE{% endif %} TRIGGER ALL;