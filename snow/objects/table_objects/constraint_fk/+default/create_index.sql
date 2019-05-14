{#
 # pgAdmin 4 - Snowflake Tools
 #
 # Copyright (C) 2013 - 2017, The pgAdmin Development Team
 # This software is released under the Snowflake Licence
 #}
{% if data.autoindex %}
CREATE INDEX {{ conn|qtIdent(data.coveringindex) }}
    ON {{ conn|qtIdent(data.schema, data.table) }}({% for columnobj in data.columns %}{% if loop.index != 1 %}
, {% endif %}{{ conn|qtIdent(columnobj.local_column)}}{% endfor %});
{% endif %}