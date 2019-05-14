{#
 # pgAdmin 4 - Snowflake Tools
 #
 # Copyright (C) 2013 - 2017, The pgAdmin Development Team
 # This software is released under the Snowflake Licence
 #}
SELECT nsp.oid FROM pg_namespace nsp WHERE nsp.nspname = {{ schema|qtLiteral }};
