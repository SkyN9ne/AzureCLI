# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network watcher connection-monitor endpoint add",
    is_preview=True,
)
class Add(AAZCommand):
    """Add an endpoint to a connection monitor.

    :example: Add an external address as a destination endpoint
        az network watcher connection-monitor endpoint add --connection-monitor MyConnectionMonitor --location westus --name MyExternalEndpoint --address "bing.com" --dest-test-groups DefaultTestGroup --type ExternalAddress

    :example: Add an Azure VM as a source endpoint
        az network watcher connection-monitor endpoint add --connection-monitor MyConnectionMonitor --location westus --name MyVMEndpoint --resource-id MyVMResourceID --source-test-groups DefaultTestGroup --type AzureVM

    :example: Add a Subnet as a source endpoint with addresses excluded
        az network watcher connection-monitor endpoint add --connection-monitor MyConnectionMonitor --location westus --name MySubnetEndpoint --resource-id MySubnetID --source-test-groups DefaultTestGroup --type AzureSubnet --address-exclude 10.0.0.25 10.0.0.30 --coverage-level BelowAverage
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/networkwatchers/{}/connectionmonitors/{}", "2022-01-01", "properties.endpoints[]"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        self.SubresourceSelector(ctx=self.ctx, name="subresource")
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.connection_monitor = AAZStrArg(
            options=["--connection-monitor"],
            help="Connection monitor name.",
            required=True,
        )
        _args_schema.watcher_name = AAZStrArg(
            options=["--watcher-name"],
            help="The name of the Network Watcher resource.",
            required=True,
        )
        _args_schema.watcher_rg = AAZResourceGroupNameArg(
            options=["-g", "--watcher-rg"],
            help="Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.",
            required=True,
        )
        _args_schema.address = AAZStrArg(
            options=["--address"],
            help="Address of the connection monitor endpoint (IP or domain name).",
        )
        _args_schema.coverage_level = AAZStrArg(
            options=["--coverage-level"],
            help="Test coverage for the endpoint. Allowed values: AboveAverage, Average, BelowAverage, Default, Full, Low",
            enum={"AboveAverage": "AboveAverage", "Average": "Average", "BelowAverage": "BelowAverage", "Default": "Default", "Full": "Full", "Low": "Low"},
        )
        _args_schema.filter_items = AAZListArg(
            options=["--filter-items"],
            help="List of property=value pairs to define filter items. Property currently include: type, address. Property value of type supports 'AgentAddress' only now.",
        )
        _args_schema.filter_type = AAZStrArg(
            options=["--filter-type"],
            help="The behavior of the endpoint filter. Currently only 'Include' is supported.  Allowed values: Include.",
            enum={"Include": "Include"},
        )
        _args_schema.endpoint_name = AAZStrArg(
            options=["-n", "--name", "--endpoint-name"],
            help="The name of the connection monitor endpoint.",
            required=True,
        )
        _args_schema.resource_id = AAZStrArg(
            options=["--resource-id"],
            help="Resource ID of the connection monitor endpoint.",
        )
        _args_schema.scope_exclude = AAZListArg(
            options=["--scope-exclude"],
            help="List of items which needs to be excluded from the endpoint scope.",
        )
        _args_schema.scope_include = AAZListArg(
            options=["--scope-include"],
            help="List of items which needs to be included to the endpoint scope.",
        )
        _args_schema.type = AAZStrArg(
            options=["--type"],
            help="The endpoint type.  Allowed values: AzureArcVM, AzureSubnet, AzureVM, AzureVMSS, AzureVNet, ExternalAddress, MMAWorkspaceMachine, MMAWorkspaceNetwork.",
            enum={"AzureArcVM": "AzureArcVM", "AzureSubnet": "AzureSubnet", "AzureVM": "AzureVM", "AzureVMSS": "AzureVMSS", "AzureVNet": "AzureVNet", "ExternalAddress": "ExternalAddress", "MMAWorkspaceMachine": "MMAWorkspaceMachine", "MMAWorkspaceNetwork": "MMAWorkspaceNetwork"},
        )

        filter_items = cls._args_schema.filter_items
        filter_items.Element = AAZObjectArg()

        _element = cls._args_schema.filter_items.Element
        _element.address = AAZStrArg(
            options=["address"],
            help="The address of the filter item.",
        )
        _element.type = AAZStrArg(
            options=["type"],
            help="The type of item included in the filter. Currently only 'AgentAddress' is supported.",
            enum={"AgentAddress": "AgentAddress"},
        )

        scope_exclude = cls._args_schema.scope_exclude
        scope_exclude.Element = AAZObjectArg()

        _element = cls._args_schema.scope_exclude.Element
        _element.address = AAZStrArg(
            options=["address"],
            help="The address of the endpoint item. Supported types are IPv4/IPv6 subnet mask or IPv4/IPv6 IP address.",
        )

        scope_include = cls._args_schema.scope_include
        scope_include.Element = AAZObjectArg()

        _element = cls._args_schema.scope_include.Element
        _element.address = AAZStrArg(
            options=["address"],
            help="The address of the endpoint item. Supported types are IPv4/IPv6 subnet mask or IPv4/IPv6 IP address.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ConnectionMonitorsGet(ctx=self.ctx)()
        self.pre_instance_create()
        self.InstanceCreateByJson(ctx=self.ctx)()
        self.post_instance_create(self.ctx.selectors.subresource.required())
        yield self.ConnectionMonitorsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_create(self):
        pass

    @register_callback
    def post_instance_create(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.selectors.subresource.required(), client_flatten=True)
        return result

    class SubresourceSelector(AAZJsonSelector):

        def _get(self):
            result = self.ctx.vars.instance
            result = result.properties.endpoints
            filters = enumerate(result)
            filters = filter(
                lambda e: e[1].name == self.ctx.args.endpoint_name,
                filters
            )
            idx = next(filters)[0]
            return result[idx]

        def _set(self, value):
            result = self.ctx.vars.instance
            result = result.properties.endpoints
            filters = enumerate(result)
            filters = filter(
                lambda e: e[1].name == self.ctx.args.endpoint_name,
                filters
            )
            idx = next(filters, [len(result)])[0]
            result[idx] = value
            return

    class ConnectionMonitorsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "connectionMonitorName", self.ctx.args.connection_monitor,
                    required=True,
                ),
                **self.serialize_url_param(
                    "networkWatcherName", self.ctx.args.watcher_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.watcher_rg,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _AddHelper._build_schema_connection_monitor_result_read(cls._schema_on_200)

            return cls._schema_on_200

    class ConnectionMonitorsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "connectionMonitorName", self.ctx.args.connection_monitor,
                    required=True,
                ),
                **self.serialize_url_param(
                    "networkWatcherName", self.ctx.args.watcher_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.watcher_rg,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _AddHelper._build_schema_connection_monitor_result_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceCreateByJson(AAZJsonInstanceCreateOperation):

        def __call__(self, *args, **kwargs):
            self.ctx.selectors.subresource.set(self._create_instance())

        def _create_instance(self):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType
            )
            _builder.set_prop("address", AAZStrType, ".address")
            _builder.set_prop("coverageLevel", AAZStrType, ".coverage_level")
            _builder.set_prop("filter", AAZObjectType)
            _builder.set_prop("name", AAZStrType, ".endpoint_name", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("resourceId", AAZStrType, ".resource_id")
            _builder.set_prop("scope", AAZObjectType)
            _builder.set_prop("type", AAZStrType, ".type")

            filter = _builder.get(".filter")
            if filter is not None:
                filter.set_prop("items", AAZListType, ".filter_items")
                filter.set_prop("type", AAZStrType, ".filter_type")

            items = _builder.get(".filter.items")
            if items is not None:
                items.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".filter.items[]")
            if _elements is not None:
                _elements.set_prop("address", AAZStrType, ".address")
                _elements.set_prop("type", AAZStrType, ".type")

            scope = _builder.get(".scope")
            if scope is not None:
                scope.set_prop("exclude", AAZListType, ".scope_exclude")
                scope.set_prop("include", AAZListType, ".scope_include")

            exclude = _builder.get(".scope.exclude")
            if exclude is not None:
                exclude.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".scope.exclude[]")
            if _elements is not None:
                _elements.set_prop("address", AAZStrType, ".address")

            include = _builder.get(".scope.include")
            if include is not None:
                include.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".scope.include[]")
            if _elements is not None:
                _elements.set_prop("address", AAZStrType, ".address")

            return _instance_value


class _AddHelper:
    """Helper class for Add"""

    _schema_connection_monitor_endpoint_scope_item_read = None

    @classmethod
    def _build_schema_connection_monitor_endpoint_scope_item_read(cls, _schema):
        if cls._schema_connection_monitor_endpoint_scope_item_read is not None:
            _schema.address = cls._schema_connection_monitor_endpoint_scope_item_read.address
            return

        cls._schema_connection_monitor_endpoint_scope_item_read = _schema_connection_monitor_endpoint_scope_item_read = AAZObjectType()

        connection_monitor_endpoint_scope_item_read = _schema_connection_monitor_endpoint_scope_item_read
        connection_monitor_endpoint_scope_item_read.address = AAZStrType()

        _schema.address = cls._schema_connection_monitor_endpoint_scope_item_read.address

    _schema_connection_monitor_result_read = None

    @classmethod
    def _build_schema_connection_monitor_result_read(cls, _schema):
        if cls._schema_connection_monitor_result_read is not None:
            _schema.etag = cls._schema_connection_monitor_result_read.etag
            _schema.id = cls._schema_connection_monitor_result_read.id
            _schema.location = cls._schema_connection_monitor_result_read.location
            _schema.name = cls._schema_connection_monitor_result_read.name
            _schema.properties = cls._schema_connection_monitor_result_read.properties
            _schema.tags = cls._schema_connection_monitor_result_read.tags
            _schema.type = cls._schema_connection_monitor_result_read.type
            return

        cls._schema_connection_monitor_result_read = _schema_connection_monitor_result_read = AAZObjectType()

        connection_monitor_result_read = _schema_connection_monitor_result_read
        connection_monitor_result_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        connection_monitor_result_read.id = AAZStrType(
            flags={"read_only": True},
        )
        connection_monitor_result_read.location = AAZStrType()
        connection_monitor_result_read.name = AAZStrType(
            flags={"read_only": True},
        )
        connection_monitor_result_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        connection_monitor_result_read.tags = AAZDictType()
        connection_monitor_result_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_connection_monitor_result_read.properties
        properties.auto_start = AAZBoolType(
            serialized_name="autoStart",
        )
        properties.connection_monitor_type = AAZStrType(
            serialized_name="connectionMonitorType",
            flags={"read_only": True},
        )
        properties.destination = AAZObjectType()
        properties.endpoints = AAZListType()
        properties.monitoring_interval_in_seconds = AAZIntType(
            serialized_name="monitoringIntervalInSeconds",
        )
        properties.monitoring_status = AAZStrType(
            serialized_name="monitoringStatus",
            flags={"read_only": True},
        )
        properties.notes = AAZStrType()
        properties.outputs = AAZListType()
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.source = AAZObjectType()
        properties.start_time = AAZStrType(
            serialized_name="startTime",
            flags={"read_only": True},
        )
        properties.test_configurations = AAZListType(
            serialized_name="testConfigurations",
        )
        properties.test_groups = AAZListType(
            serialized_name="testGroups",
        )

        destination = _schema_connection_monitor_result_read.properties.destination
        destination.address = AAZStrType()
        destination.port = AAZIntType()
        destination.resource_id = AAZStrType(
            serialized_name="resourceId",
        )

        endpoints = _schema_connection_monitor_result_read.properties.endpoints
        endpoints.Element = AAZObjectType()

        _element = _schema_connection_monitor_result_read.properties.endpoints.Element
        _element.address = AAZStrType()
        _element.coverage_level = AAZStrType(
            serialized_name="coverageLevel",
        )
        _element.filter = AAZObjectType()
        _element.name = AAZStrType(
            flags={"required": True},
        )
        _element.resource_id = AAZStrType(
            serialized_name="resourceId",
        )
        _element.scope = AAZObjectType()
        _element.type = AAZStrType()

        filter = _schema_connection_monitor_result_read.properties.endpoints.Element.filter
        filter.items = AAZListType()
        filter.type = AAZStrType()

        items = _schema_connection_monitor_result_read.properties.endpoints.Element.filter.items
        items.Element = AAZObjectType()

        _element = _schema_connection_monitor_result_read.properties.endpoints.Element.filter.items.Element
        _element.address = AAZStrType()
        _element.type = AAZStrType()

        scope = _schema_connection_monitor_result_read.properties.endpoints.Element.scope
        scope.exclude = AAZListType()
        scope.include = AAZListType()

        exclude = _schema_connection_monitor_result_read.properties.endpoints.Element.scope.exclude
        exclude.Element = AAZObjectType()
        cls._build_schema_connection_monitor_endpoint_scope_item_read(exclude.Element)

        include = _schema_connection_monitor_result_read.properties.endpoints.Element.scope.include
        include.Element = AAZObjectType()
        cls._build_schema_connection_monitor_endpoint_scope_item_read(include.Element)

        outputs = _schema_connection_monitor_result_read.properties.outputs
        outputs.Element = AAZObjectType()

        _element = _schema_connection_monitor_result_read.properties.outputs.Element
        _element.type = AAZStrType()
        _element.workspace_settings = AAZObjectType(
            serialized_name="workspaceSettings",
        )

        workspace_settings = _schema_connection_monitor_result_read.properties.outputs.Element.workspace_settings
        workspace_settings.workspace_resource_id = AAZStrType(
            serialized_name="workspaceResourceId",
        )

        source = _schema_connection_monitor_result_read.properties.source
        source.port = AAZIntType()
        source.resource_id = AAZStrType(
            serialized_name="resourceId",
            flags={"required": True},
        )

        test_configurations = _schema_connection_monitor_result_read.properties.test_configurations
        test_configurations.Element = AAZObjectType()

        _element = _schema_connection_monitor_result_read.properties.test_configurations.Element
        _element.http_configuration = AAZObjectType(
            serialized_name="httpConfiguration",
        )
        _element.icmp_configuration = AAZObjectType(
            serialized_name="icmpConfiguration",
        )
        _element.name = AAZStrType(
            flags={"required": True},
        )
        _element.preferred_ip_version = AAZStrType(
            serialized_name="preferredIPVersion",
        )
        _element.protocol = AAZStrType(
            flags={"required": True},
        )
        _element.success_threshold = AAZObjectType(
            serialized_name="successThreshold",
        )
        _element.tcp_configuration = AAZObjectType(
            serialized_name="tcpConfiguration",
        )
        _element.test_frequency_sec = AAZIntType(
            serialized_name="testFrequencySec",
        )

        http_configuration = _schema_connection_monitor_result_read.properties.test_configurations.Element.http_configuration
        http_configuration.method = AAZStrType()
        http_configuration.path = AAZStrType()
        http_configuration.port = AAZIntType()
        http_configuration.prefer_https = AAZBoolType(
            serialized_name="preferHTTPS",
        )
        http_configuration.request_headers = AAZListType(
            serialized_name="requestHeaders",
        )
        http_configuration.valid_status_code_ranges = AAZListType(
            serialized_name="validStatusCodeRanges",
        )

        request_headers = _schema_connection_monitor_result_read.properties.test_configurations.Element.http_configuration.request_headers
        request_headers.Element = AAZObjectType()

        _element = _schema_connection_monitor_result_read.properties.test_configurations.Element.http_configuration.request_headers.Element
        _element.name = AAZStrType()
        _element.value = AAZStrType()

        valid_status_code_ranges = _schema_connection_monitor_result_read.properties.test_configurations.Element.http_configuration.valid_status_code_ranges
        valid_status_code_ranges.Element = AAZStrType()

        icmp_configuration = _schema_connection_monitor_result_read.properties.test_configurations.Element.icmp_configuration
        icmp_configuration.disable_trace_route = AAZBoolType(
            serialized_name="disableTraceRoute",
        )

        success_threshold = _schema_connection_monitor_result_read.properties.test_configurations.Element.success_threshold
        success_threshold.checks_failed_percent = AAZIntType(
            serialized_name="checksFailedPercent",
        )
        success_threshold.round_trip_time_ms = AAZFloatType(
            serialized_name="roundTripTimeMs",
        )

        tcp_configuration = _schema_connection_monitor_result_read.properties.test_configurations.Element.tcp_configuration
        tcp_configuration.destination_port_behavior = AAZStrType(
            serialized_name="destinationPortBehavior",
        )
        tcp_configuration.disable_trace_route = AAZBoolType(
            serialized_name="disableTraceRoute",
        )
        tcp_configuration.port = AAZIntType()

        test_groups = _schema_connection_monitor_result_read.properties.test_groups
        test_groups.Element = AAZObjectType()

        _element = _schema_connection_monitor_result_read.properties.test_groups.Element
        _element.destinations = AAZListType(
            flags={"required": True},
        )
        _element.disable = AAZBoolType()
        _element.name = AAZStrType(
            flags={"required": True},
        )
        _element.sources = AAZListType(
            flags={"required": True},
        )
        _element.test_configurations = AAZListType(
            serialized_name="testConfigurations",
            flags={"required": True},
        )

        destinations = _schema_connection_monitor_result_read.properties.test_groups.Element.destinations
        destinations.Element = AAZStrType()

        sources = _schema_connection_monitor_result_read.properties.test_groups.Element.sources
        sources.Element = AAZStrType()

        test_configurations = _schema_connection_monitor_result_read.properties.test_groups.Element.test_configurations
        test_configurations.Element = AAZStrType()

        tags = _schema_connection_monitor_result_read.tags
        tags.Element = AAZStrType()

        _schema.etag = cls._schema_connection_monitor_result_read.etag
        _schema.id = cls._schema_connection_monitor_result_read.id
        _schema.location = cls._schema_connection_monitor_result_read.location
        _schema.name = cls._schema_connection_monitor_result_read.name
        _schema.properties = cls._schema_connection_monitor_result_read.properties
        _schema.tags = cls._schema_connection_monitor_result_read.tags
        _schema.type = cls._schema_connection_monitor_result_read.type


__all__ = ["Add"]
