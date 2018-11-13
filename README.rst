.. image:: https://travis-ci.com/jhigueras/wasupu-boinet-monitoring.svg?branch=master
    :target: https://travis-ci.com/jhigueras/wasupu-boinet-monitoring
Wasupu boinet monitoring tool
============================

This tool is used to monitor what's happening in a running boinet

Usage
-----

.. code:: console

    $ pip install .
    $ docker logs -f boinet | python -m boinet_monitoring balances
