# Incident 001: Ubuntu Server VM Network Issue - DHCP and Netplan

## Summary

During the initial setup of the Ubuntu Server virtual machine, the system was unable to reach the internet. Commands such as `apt update` and `ping` failed because the VM did not have a valid IPv4 address or default gateway.

This issue was identified and resolved by reviewing the network interface configuration and enabling DHCP through Netplan.

## Environment

* Host Machine: Windows
* Virtualization Platform: VMware
* Guest OS: Ubuntu Server
* Network Adapter: NAT
* Network Interface: `ens33`

## Issue

The Ubuntu Server VM was unable to connect to external networks.

The following errors were observed:

```text
Network is unreachable
Temporary failure resolving 'archive.ubuntu.com'
```

The issue affected commands such as:

```bash
sudo apt update
ping 8.8.8.8
ping archive.ubuntu.com
```

## Investigation

The network interface was checked using:

```bash
ip a
```

The interface `ens33` was visible and marked as `UP`, but it did not have an IPv4 address assigned.

The routing table was checked using:

```bash
ip route
```

No default gateway was configured.

This confirmed that the VM had no active IPv4 network route.

## Root Cause

The `ens33` interface was not receiving an IPv4 address because DHCP was not properly enabled in the Netplan configuration.

Without DHCP, the VM could not obtain:

* IPv4 address
* Default gateway
* DNS configuration

## Resolution

The Netplan configuration file was edited:

```bash
sudo nano /etc/netplan/00-installer-config.yaml
```

The configuration was updated as follows:

```yaml
network:
  version: 2
  ethernets:
    ens33:
      dhcp4: true
      dhcp6: false
```

The configuration was then applied:

```bash
sudo netplan apply
```

After applying the configuration, the VM successfully received an IPv4 address.

Connectivity was validated using:

```bash
ip a
ip route
ping 8.8.8.8 -c 4
ping archive.ubuntu.com -c 4
```

After confirming network connectivity, package updates worked correctly:

```bash
sudo apt update
```

## Validation

The VM successfully obtained an IPv4 address:

```text
192.168.159.135
```

Internet connectivity and DNS resolution were restored.

## Lessons Learned

This issue reinforced the importance of checking the network stack step by step:

1. Verify the network interface.
2. Check if an IPv4 address is assigned.
3. Validate the default gateway.
4. Test external IP connectivity.
5. Test DNS resolution.
6. Review Netplan configuration.

## Application Support Relevance

This incident is a good example of basic Linux troubleshooting in an application support environment. Before investigating application-level failures, it is important to validate the underlying infrastructure, including networking, routing, and DNS resolution.

A missing IP address or default gateway can cause application deployments, package updates, database connections, monitoring tools, and CI/CD pipelines to fail.
