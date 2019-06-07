Collectd Plugin for Puppet
==========================

Configuration
-------------

.. code:: apache

   TypesDB "/usr/share/collectd/puppet_types.db"
   <LoadPlugin python>
     Globals true
   </LoadPlugin>

   <Plugin "python">
     LogTraces true
     Interactive false
     Import "puppet"
     PATH "/opt/puppetlabs/puppet/cache/state/last_run_summary.yaml"
   </Plugin>

Generated data
--------------

The plugin parses
``/opt/puppetlabs/puppet/cache/state/last_run_summary.yaml`` and reports
several single values extracted from there.

It will only send data if there has been a Puppet run after the last
time Collectd polled. This is monitored using a state file located in
``/var/lib/collectd/puppet.state``. To force a data point just delete
it.

These are the values that are currently being dispatched:

* puppet/boolean-compiled (flag denoting if the catalog compiled (1 or 0))
* puppet/seconds-config_retrieval
* puppet/seconds-total_time
* puppet/resources-changed
* puppet/resources-corrective_change
* puppet/resources-failed
* puppet/resources-failed_to_restart
* puppet/resources-out_of_sync
* puppet/resources-restarted
* puppet/resources-scheduled
* puppet/resources-skipped
* puppet/resources-total
* puppet/time_ref-last_run (epoch of last puppet run (seconds))

Authors
-------
Steve Traylen <steve.traylen@cern.ch>
Nacho Barrientos <nacho.barrientos@cern.ch>

Copyright
---------
2018 CERN

License
-------
Apache-II License

Development notes
-----------------

Don't forget to bump the ``schema_version`` if you modify the data format.
