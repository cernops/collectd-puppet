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
     MaxRetention 21600
   </Plugin>

The `MaxRetention` setting represents, in seconds, for how long the value of
the metrics will be retained if there's no fresh data to publish during the
Collectd loop. Be aware that this setting depends on the global `Timeout`. For
instance, if you want a retention of 6 hours and the Collectd timeout is set to
2 then you'll have to halve value and set it to `(6*60*60)/2`.

Generated data
--------------

The plugin parses by default
``/opt/puppetlabs/puppet/cache/state/last_run_summary.yaml`` and
reports several single values extracted from there.

Take into account that this path has changed in Puppet7 and becomes
``/opt/puppetlabs/puppet/public/last_run_summary.yaml`` so adjust your
configuration accordingly depending on your Puppet version. This
default will be switched once Puppet6 reaches EOL (expected Feb 2023).

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

Distribution
------------

* `Pypy <https://pypi.org/project/collectd-puppet>`_.
* RHEL8/CentOS8 packages are available directly from
  `EPEL <https://fedoraproject.org/wiki/EPEL>`_
  (`Spec <https://src.fedoraproject.org/rpms/python-collectd_puppet/tree/master>`_).

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
