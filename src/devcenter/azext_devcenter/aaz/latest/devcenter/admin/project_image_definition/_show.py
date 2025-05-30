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
    "devcenter admin project-image-definition show",
)
class Show(AAZCommand):
    """Get an Image Definition from the catalog

    :example: Get
        az devcenter admin project-image-definition show --catalog-name "CentralCatalog" --image-definition-name "DefaultDevImage" --project-name "DevProject" --resource-group "rg1"
    """

    _aaz_info = {
        "version": "2025-04-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.devcenter/projects/{}/catalogs/{}/imagedefinitions/{}", "2025-04-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.catalog_name = AAZStrArg(
            options=["--catalog-name"],
            help="The name of the Catalog.",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9-_.]{2,62}$",
                max_length=63,
                min_length=3,
            ),
        )
        _args_schema.image_definition_name = AAZStrArg(
            options=["-n", "--name", "--image-definition-name"],
            help="The name of the Image Definition.",
            required=True,
            id_part="child_name_2",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9-_.]{2,62}$",
                max_length=63,
                min_length=3,
            ),
        )
        _args_schema.project_name = AAZStrArg(
            options=["--project", "--project-name"],
            help="The name of the project. Use `az configure -d project=<project_name>` to configure a default.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9-_.]{2,62}$",
                max_length=63,
                min_length=3,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ProjectCatalogImageDefinitionsGetByProjectCatalog(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ProjectCatalogImageDefinitionsGetByProjectCatalog(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevCenter/projects/{projectName}/catalogs/{catalogName}/imageDefinitions/{imageDefinitionName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "catalogName", self.ctx.args.catalog_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "imageDefinitionName", self.ctx.args.image_definition_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "projectName", self.ctx.args.project_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
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
                    "api-version", "2025-04-01-preview",
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

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.active_image_reference = AAZObjectType(
                serialized_name="activeImageReference",
                flags={"read_only": True},
            )
            _ShowHelper._build_schema_image_reference_read(properties.active_image_reference)
            properties.auto_image_build = AAZStrType(
                serialized_name="autoImageBuild",
                flags={"read_only": True},
            )
            properties.extends = AAZObjectType()
            properties.file_url = AAZStrType(
                serialized_name="fileUrl",
                flags={"read_only": True},
            )
            properties.image_reference = AAZObjectType(
                serialized_name="imageReference",
            )
            _ShowHelper._build_schema_image_reference_read(properties.image_reference)
            properties.image_validation_error_details = AAZObjectType(
                serialized_name="imageValidationErrorDetails",
                flags={"read_only": True},
            )
            properties.image_validation_status = AAZStrType(
                serialized_name="imageValidationStatus",
                flags={"read_only": True},
            )
            properties.latest_build = AAZObjectType(
                serialized_name="latestBuild",
            )
            properties.tasks = AAZListType()
            properties.user_tasks = AAZListType(
                serialized_name="userTasks",
            )
            properties.validation_status = AAZStrType(
                serialized_name="validationStatus",
                flags={"read_only": True},
            )

            extends = cls._schema_on_200.properties.extends
            extends.image_definition = AAZStrType(
                serialized_name="imageDefinition",
                flags={"required": True},
            )
            extends.parameters = AAZListType()
            _ShowHelper._build_schema_definition_parameters_read(extends.parameters)

            image_validation_error_details = cls._schema_on_200.properties.image_validation_error_details
            image_validation_error_details.code = AAZStrType()
            image_validation_error_details.message = AAZStrType()

            latest_build = cls._schema_on_200.properties.latest_build
            latest_build.end_time = AAZStrType(
                serialized_name="endTime",
                flags={"read_only": True},
            )
            latest_build.name = AAZStrType(
                flags={"read_only": True},
            )
            latest_build.start_time = AAZStrType(
                serialized_name="startTime",
                flags={"read_only": True},
            )
            latest_build.status = AAZStrType(
                flags={"read_only": True},
            )

            tasks = cls._schema_on_200.properties.tasks
            tasks.Element = AAZObjectType()
            _ShowHelper._build_schema_customization_task_instance_read(tasks.Element)

            user_tasks = cls._schema_on_200.properties.user_tasks
            user_tasks.Element = AAZObjectType()
            _ShowHelper._build_schema_customization_task_instance_read(user_tasks.Element)

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_customization_task_instance_read = None

    @classmethod
    def _build_schema_customization_task_instance_read(cls, _schema):
        if cls._schema_customization_task_instance_read is not None:
            _schema.condition = cls._schema_customization_task_instance_read.condition
            _schema.display_name = cls._schema_customization_task_instance_read.display_name
            _schema.name = cls._schema_customization_task_instance_read.name
            _schema.parameters = cls._schema_customization_task_instance_read.parameters
            _schema.timeout_in_seconds = cls._schema_customization_task_instance_read.timeout_in_seconds
            return

        cls._schema_customization_task_instance_read = _schema_customization_task_instance_read = AAZObjectType()

        customization_task_instance_read = _schema_customization_task_instance_read
        customization_task_instance_read.condition = AAZStrType()
        customization_task_instance_read.display_name = AAZStrType(
            serialized_name="displayName",
        )
        customization_task_instance_read.name = AAZStrType(
            flags={"required": True},
        )
        customization_task_instance_read.parameters = AAZListType()
        cls._build_schema_definition_parameters_read(customization_task_instance_read.parameters)
        customization_task_instance_read.timeout_in_seconds = AAZIntType(
            serialized_name="timeoutInSeconds",
        )

        _schema.condition = cls._schema_customization_task_instance_read.condition
        _schema.display_name = cls._schema_customization_task_instance_read.display_name
        _schema.name = cls._schema_customization_task_instance_read.name
        _schema.parameters = cls._schema_customization_task_instance_read.parameters
        _schema.timeout_in_seconds = cls._schema_customization_task_instance_read.timeout_in_seconds

    _schema_definition_parameters_read = None

    @classmethod
    def _build_schema_definition_parameters_read(cls, _schema):
        if cls._schema_definition_parameters_read is not None:
            _schema.Element = cls._schema_definition_parameters_read.Element
            return

        cls._schema_definition_parameters_read = _schema_definition_parameters_read = AAZListType()

        definition_parameters_read = _schema_definition_parameters_read
        definition_parameters_read.Element = AAZObjectType()

        _element = _schema_definition_parameters_read.Element
        _element.name = AAZStrType(
            flags={"required": True},
        )
        _element.value = AAZStrType(
            flags={"required": True},
        )

        _schema.Element = cls._schema_definition_parameters_read.Element

    _schema_image_reference_read = None

    @classmethod
    def _build_schema_image_reference_read(cls, _schema):
        if cls._schema_image_reference_read is not None:
            _schema.exact_version = cls._schema_image_reference_read.exact_version
            _schema.id = cls._schema_image_reference_read.id
            return

        cls._schema_image_reference_read = _schema_image_reference_read = AAZObjectType()

        image_reference_read = _schema_image_reference_read
        image_reference_read.exact_version = AAZStrType(
            serialized_name="exactVersion",
            flags={"read_only": True},
        )
        image_reference_read.id = AAZStrType()

        _schema.exact_version = cls._schema_image_reference_read.exact_version
        _schema.id = cls._schema_image_reference_read.id


__all__ = ["Show"]
