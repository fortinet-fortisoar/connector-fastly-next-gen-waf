## About the connector
Fastly Next-Gen WAF offers advanced web application protection with automated security measures, real-time monitoring, and rapid incident response. It provides robust defense by managing security policies, detecting threats, and enforcing rule sets to protect web applications.
<p>This document provides information about the Fastly Next-Gen WAF Connector, which facilitates automated interactions, with a Fastly Next-Gen WAF server using FortiSOAR&trade; playbooks. Add the Fastly Next-Gen WAF Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Fastly Next-Gen WAF.</p>

### Version information

Connector Version: 1.0.0

Authored By: Fortinet

Certified: No

## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-fastly-next-gen-waf</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Fastly Next-Gen WAF server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Fastly Next-Gen WAF server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Fastly Next-Gen WAF</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the URL of the Fastly Next-Gen WAF server to connect and perform automated operations. For example, <a href="https://dashboard.signalsciences.net">https://dashboard.signalsciences.net</a>
</td>
</tr><tr><td>Email ID</td><td>Specify the email ID of the user accessing the endpoint to connect and perform automated operations.
</td>
</tr><tr><td>Access Token</td><td>Specify the API key to access the endpoint to connect and perform automated operations.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector

The following automated operations can be included in playbooks, and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Site Allow List</td><td>Retrieves the allow list of IP addresses for the specified site and corporation.</td><td>get_site_allow_list <br/>Investigation</td></tr>
<tr><td>Add IP Address to Allow List</td><td>Adds an IP address to the allow list for the specified site and corporation.</td><td>add_ip_to_allow_list <br/>Investigation</td></tr>
<tr><td>Remove IP Address from Allow List</td><td>Removes an IP address from the allow list for the specified site and corporation using the IP address ID.</td><td>remove_ip_from_allow_list <br/>Investigation</td></tr>
<tr><td>Get Site Block List</td><td>Retrieves the block list of IP addresses for the specified site and corporation.</td><td>get_site_block_list <br/>Investigation</td></tr>
<tr><td>Add IP Address to Block List</td><td>Adds an IP address to the site's block list for the specified corporation.</td><td>add_ip_to_block_list <br/>Investigation</td></tr>
<tr><td>Remove IP Address from Block List</td><td>Removes an IP address from the block list for the specified site and corporation using the IP address ID.</td><td>remove_ip_from_block_list <br/>Investigation</td></tr>
<tr><td>Get All Site Lists</td><td>Retrieves both the allow lists and block lists of IP addresses for the specified site within the specified corporation.</td><td>get_all_site_lists <br/>Investigation</td></tr>
<tr><td>Get Site List Details</td><td>Retrieves the details of a site's list based on the specified List ID.</td><td>get_site_list_by_id <br/>Investigation</td></tr>
<tr><td>List Sites in Corporation</td><td>Retrieves a list of sites within the specified corporation.</td><td>list_sites_in_corp <br/>Investigation</td></tr>
<tr><td>List Corporations</td><td>Retrieves a list of corporations.</td><td>list_corps <br/>Investigation</td></tr>
<tr><td>List Alerts</td><td>Retrieves a list of alerts for the specified site within the specified corporation.</td><td>list_alerts <br/>Investigation</td></tr>
<tr><td>Get Alert Details</td><td>Retrieves detailed information about a specific alert for the specified site within the specified corporation.</td><td>get_alert_details <br/>Investigation</td></tr>
<tr><td>Update Alert</td><td>Updates an alert for the specified site within the specified corporation.</td><td>update_alert <br/>Investigation</td></tr>
<tr><td>List Events</td><td>Retrieves a list of events for the specified site within the specified corporation.</td><td>list_events <br/>Investigation</td></tr>
<tr><td>Get Event Details</td><td>Retrieves detailed information about a specific event for the specified site within the specified corporation.</td><td>get_event_details <br/>Investigation</td></tr>
<tr><td>Expire Event By ID</td><td>Marks a specific event as expired based on the provided event ID for the specified site within the specified corporation.</td><td>expire_event_by_id <br/>Management</td></tr>
</tbody></table>

### operation: Get Site Allow List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Corporation Name</td><td>Specify the corporation name whose site's allow list is to be retrieved.
</td></tr><tr><td>Site Name</td><td>Specify the site name whose allow list is to be retrieved.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": [
        {
            "id": "",
            "source": "",
            "expires": "",
            "note": "",
            "createdBy": "",
            "created": ""
        }
    ]
}</pre>
### operation: Add IP Address to Allow List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Corporation Name</td><td>Specify the corporation name whose site's allow list is to have the IP address added.
</td></tr><tr><td>Site Name</td><td>Specify the site name whose allow list is to have the IP address added.
</td></tr><tr><td>IP Address</td><td>Specify the IP address to be added to the site's allow list.
</td></tr><tr><td>Note</td><td>(Optional) Specify the note associated with the IP address being added to the allow list. Use this to provide additional context or information.
</td></tr><tr><td>Expiry Date</td><td>(Optional) Specify the datetime when the allow list entry should expire. Omit this field if the entry should not expire.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "source": "",
    "expires": "",
    "note": "",
    "createdBy": "",
    "created": ""
}</pre>
### operation: Remove IP Address from Allow List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Corporation Name</td><td>Specify the corporation name whose site's allow list is to be updated.
</td></tr><tr><td>Site Name</td><td>Specify the site name whose allow list is to be updated.
</td></tr><tr><td>IP Address ID</td><td>Specify the unique ID of the IP address to be removed from the site's allow list.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "status": "",
    "message": ""
}</pre>

### operation: Get Site Block List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Corporation Name</td><td>Specify the corporation name whose site's block list is to be retrieved.
</td></tr><tr><td>Site Name</td><td>Specify the site name whose block list is to be retrieved.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": [
        {
            "id": "",
            "source": "",
            "expires": "",
            "note": "",
            "createdBy": "",
            "created": ""
        }
    ]
}</pre>

### operation: Add IP Address to Block List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Corporation Name</td><td>Specify the corporation name whose site's block list is to have the IP address added.
</td></tr><tr><td>Site Name</td><td>Specify the site name whose block list is to have the IP address added.
</td></tr><tr><td>IP Address</td><td>Specify the IP address to be added to the site’s block list.
</td></tr><tr><td>Note</td><td>(Optional) Specify the note associated with the IP address being added to the block list. Use this to provide additional context or information.
</td></tr><tr><td>Expiry Date</td><td>(Optional) Specify the datetime when the block list entry should expire. Omit this field if the entry should not expire.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "source": "",
    "expires": "",
    "note": "",
    "createdBy": "",
    "created": ""
}</pre>
### operation: Remove IP Address from Block List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Corporation Name</td><td>Specify the corporation name whose site's block list is to be updated.
</td></tr><tr><td>Site Name</td><td>Specify the site name whose block list is to be updated.
</td></tr><tr><td>IP Address ID</td><td>Specify the unique ID of the IP address to be removed from the site's block list.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "status": "",
    "message": ""
}</pre>

### operation: Get All Site Lists
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Corporation Name</td><td>Specify the corporation name whose site's allow and block lists are to be retrieved.
</td></tr><tr><td>Site Name</td><td>Specify the site name whose allow and block lists are to be retrieved.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": [
        {
            "id": "",
            "name": "",
            "type": "",
            "description": "",
            "entries": [],
            "createdBy": "",
            "created": "",
            "updated": ""
        }
    ]
}</pre>

### operation: Get Site List Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Corporation Name</td><td>Specify the corporation name whose site list is to be retrieved.
</td></tr><tr><td>Site Name</td><td>Specify the site name whose list is to be retrieved.
</td></tr><tr><td>List ID</td><td>Specify the List ID of the site’s list to be retrieved.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "name": "",
    "type": "",
    "description": "",
    "entries": [],
    "createdBy": "",
    "created": "",
    "updated": ""
}</pre>

### operation: List Sites in Corporation
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Corporation Name</td><td>Specify the corporation shortname whose sites are to be listed.
</td></tr><tr><td>Site Name</td><td>(Optional) Specify a filter on site name or display name.
</td></tr><tr><td>Agent Level</td><td>(Optional) Select a filter on agent mode. You can choose from Off, Log and Block.
</td></tr><tr><td>Page</td><td>(Optional) Specify the page of the results to retrieve. Default is 1.
</td></tr><tr><td>Limit</td><td>(Optional) Specify the number of entries to be returned. Default is 10.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": [
        {
            "name": "",
            "displayName": "",
            "agentLevel": "",
            "blockHTTPCode": "",
            "blockDurationSeconds": "",
            "created": "",
            "whitelist": {
                "uri": ""
            },
            "blacklist": {
                "uri": ""
            },
            "events": {
                "uri": ""
            },
            "requests": {
                "uri": ""
            },
            "redactions": {
                "uri": ""
            },
            "suspiciousIPs": {
                "uri": ""
            },
            "monitors": {
                "uri": ""
            },
            "integrations": {
                "uri": ""
            },
            "headerLinks": {
                "uri": ""
            },
            "agents": {
                "uri": ""
            },
            "alerts": {
                "uri": ""
            },
            "analyticsEvents": {
                "uri": ""
            },
            "topAttacks": {
                "uri": ""
            },
            "members": {
                "uri": ""
            }
        }
    ]
}</pre>

### operation: List Corporations
#### Input parameters
None.

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": [
        {
            "name": "",
            "displayName": "",
            "smallIconURI": "",
            "created": "",
            "siteLimit": "",
            "sites": {
                "uri": ""
            },
            "authType": "",
            "sessionMaxAgeDashboard": ""
        }
    ]
}</pre>

### operation: List Alerts
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Corporation Name</td><td>Specify the corporation name whose site's alerts are to be listed.
</td></tr><tr><td>Site Name</td><td>Specify the site name whose alerts are to be listed.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": [
        {
            "id": "",
            "tagName": "",
            "longName": "",
            "type": "",
            "interval": "",
            "threshold": "",
            "skipNotifications": "",
            "enabled": "",
            "action": "",
            "fieldName": "",
            "createdBy": "",
            "created": "",
            "updated": ""
        }
    ]
}</pre>

### operation: Get Alert Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Corporation Name</td><td>Specify the corporation name whose site's alert details are to be retrieved.
</td></tr><tr><td>Site Name</td><td>Specify the site name whose alert details are to be retrieved.
</td></tr><tr><td>Alert ID</td><td>Specify the ID of the alert to retrieve details for.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "tagName": "",
    "longName": "",
    "type": "",
    "interval": "",
    "threshold": "",
    "skipNotifications": "",
    "enabled": "",
    "action": "",
    "fieldName": "",
    "createdBy": "",
    "created": "",
    "updated": ""
}</pre>

### operation: Update Alert
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Corporation Name</td><td>Specify the corporation name whose site's alert is to be updated.
</td></tr><tr><td>Site Name</td><td>Specify the site name whose alert is to be updated.
</td></tr><tr><td>Alert ID</td><td>Specify the ID of the alert to be updated.
</td></tr><tr><td>Long Name</td><td>(Optional) Specify a human-readable description of the alert. Must be between 3 and 25 characters.
</td></tr><tr><td>Tag Name</td><td>(Optional) Specify the name of the tag whose occurrences the alert is watching. Must match an existing tag.
</td></tr><tr><td>Interval</td><td>(Optional) Specify the number of minutes of past traffic to examine. Must be 1, 10, or 60.
</td></tr><tr><td>Threshold</td><td>(Optional) Specify the number of occurrences of the tag in the interval needed to trigger the alert. Must be between 1 and 10000.
</td></tr><tr><td>Block Duration Seconds</td><td>(Optional) Specify the number of seconds this alert is active.
</td></tr><tr><td>Enabled</td><td>(Optional) Specify a flag to toggle this alert.
</td></tr><tr><td>Action</td><td>(Optional) Specify what happens when the alert is triggered.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "siteId": "",
    "tagName": "",
    "interval": "",
    "threshold": "",
    "enabled": "",
    "action": "",
    "created": ""
}</pre>

### operation: List Events
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Corporation Name</td><td>Specify the corporation name whose site's events are to be listed.
</td></tr><tr><td>Site Name</td><td>Specify the site name whose events are to be listed.
</td></tr><tr><td>Status</td><td>(Optional) Specify a filter based on status. You can choose from Active and Expired.
</td></tr><tr><td>Action</td><td>(Optional) Specify a filter based on action. You can choose from are Flagged and Info.
</td></tr><tr><td>IP</td><td>(Optional) Specify a filter based on IP address. Minimum length is 7 characters, maximum length is 15 characters.
</td></tr><tr><td>Tag</td><td>(Optional) Specify a filter based on a tag. Minimum length is 3 characters, matching the pattern [a-zA-Z0-9_-]+.
</td></tr><tr><td>Since ID</td><td>(Optional) Specify the ID of the last object in the set to retrieve events created after this ID.
</td></tr><tr><td>Max ID</td><td>(Optional) Specify the ID of the last object in the set to retrieve events created before this ID.
</td></tr><tr><td>Start Time</td><td>(Optional) Specify the time to retrieve events created after the specified datetime.
</td></tr><tr><td>End Time</td><td>(Optional) Specify the time to retrieve events created before the specified datetime.
</td></tr><tr><td>Sort</td><td>(Optional) Specify the order to retrieve events, either Asc or Desc.
</td></tr><tr><td>Page</td><td>(Optional) Specify the page of the results to be retrieved. Each page is limited to 1,000 requests, with a maximum of 10,000 requests in total.
</td></tr><tr><td>Limit</td><td>(Optional) Specify the number of entries to be returned per page. Default is 100, with a maximum of 1000.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "totalCount": "",
    "next": {
        "uri": ""
    },
    "data": [
        {
            "id": "",
            "timestamp": "",
            "source": "",
            "remoteCountryCode": "",
            "remoteHostname": "",
            "userAgents": [],
            "action": "",
            "type": "",
            "reasons": {
                "SQLI": ""
            },
            "requestCount": "",
            "tagCount": "",
            "window": "",
            "expires": "",
            "expiredBy": ""
        }
    ]
}</pre>

### operation: Get Event Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Corporation Name</td><td>Specify the corporation name where the event occurred.
</td></tr><tr><td>Site Name</td><td>Specify the site name where the event occurred.
</td></tr><tr><td>Event ID</td><td>Specify the unique ID of the event to retrieve details for.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "timestamp": "",
    "source": "",
    "remoteCountryCode": "",
    "remoteHostname": "",
    "userAgents": [],
    "action": "",
    "type": "",
    "reasons": {
        "SQLI": ""
    },
    "requestCount": "",
    "tagCount": "",
    "window": "",
    "expires": "",
    "expiredBy": ""
}</pre>

### operation: Expire Event By ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Corporation Name</td><td>Specify the corporation name where the event is located.
</td></tr><tr><td>Site Name</td><td>Specify the site name where the event is located.
</td></tr><tr><td>Event ID</td><td>Specify the unique ID of the event to mark as expired.
</td></tr></tbody></table>
#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "timestamp": "",
    "source": "",
    "remoteCountryCode": "",
    "remoteHostname": "",
    "userAgents": [],
    "action": "",
    "type": "",
    "reasons": {
        "SQLI": ""
    },
    "requestCount": "",
    "tagCount": "",
    "window": "",
    "expires": "",
    "expiredBy": ""
}</pre>

## Included playbooks
The `Sample - fastly-next-gen-waf - 1.0.0` playbook collection comes bundled with the Fastly Next-Gen WAF connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Fastly Next-Gen WAF connector.

- Add IP Address to Allow List
- Add IP Address to Block List
- Expire Event By ID
- Get Alert Details
- Get All Site Lists
- Get Event Details
- Get Site Allow List
- Get Site Block List
- Get Site List Details
- List Alerts
- List Corporations
- List Events
- List Sites in Corporation
- Remove IP Address from Allow List
- Remove IP Address from Block List
- Update Alert

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
