Public API
==============================================================================
.. contents::
    :depth: 1
    :local:


{%- for service_name, public_api_list in public_apis.items() %}

{{ service_name }}
------------------------------------------------------------------------------
{%- for public_api in public_api_list %}
- ``{{ public_api }}``
{%- endfor %}

{%- endfor %}
