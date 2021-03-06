# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SparkJob(Model):
    """SparkJob.

    :param state:
    :type state: str
    :param name:
    :type name: str
    :param submitter:
    :type submitter: str
    :param compute:
    :type compute: str
    :param spark_application_id:
    :type spark_application_id: str
    :param livy_id:
    :type livy_id: str
    :param timing:
    :type timing: list[str]
    :param spark_job_definition:
    :type spark_job_definition: str
    :param pipeline:
    :type pipeline: list[~azure.synapse.models.SparkJob]
    :param job_type:
    :type job_type: str
    :param submit_time:
    :type submit_time: datetime
    :param end_time:
    :type end_time: datetime
    :param queued_duration:
    :type queued_duration: str
    :param running_duration:
    :type running_duration: str
    :param total_duration:
    :type total_duration: str
    """

    _attribute_map = {
        'state': {'key': 'state', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'submitter': {'key': 'submitter', 'type': 'str'},
        'compute': {'key': 'compute', 'type': 'str'},
        'spark_application_id': {'key': 'sparkApplicationId', 'type': 'str'},
        'livy_id': {'key': 'livyId', 'type': 'str'},
        'timing': {'key': 'timing', 'type': '[str]'},
        'spark_job_definition': {'key': 'sparkJobDefinition', 'type': 'str'},
        'pipeline': {'key': 'pipeline', 'type': '[SparkJob]'},
        'job_type': {'key': 'jobType', 'type': 'str'},
        'submit_time': {'key': 'submitTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'queued_duration': {'key': 'queuedDuration', 'type': 'str'},
        'running_duration': {'key': 'runningDuration', 'type': 'str'},
        'total_duration': {'key': 'totalDuration', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SparkJob, self).__init__(**kwargs)
        self.state = kwargs.get('state', None)
        self.name = kwargs.get('name', None)
        self.submitter = kwargs.get('submitter', None)
        self.compute = kwargs.get('compute', None)
        self.spark_application_id = kwargs.get('spark_application_id', None)
        self.livy_id = kwargs.get('livy_id', None)
        self.timing = kwargs.get('timing', None)
        self.spark_job_definition = kwargs.get('spark_job_definition', None)
        self.pipeline = kwargs.get('pipeline', None)
        self.job_type = kwargs.get('job_type', None)
        self.submit_time = kwargs.get('submit_time', None)
        self.end_time = kwargs.get('end_time', None)
        self.queued_duration = kwargs.get('queued_duration', None)
        self.running_duration = kwargs.get('running_duration', None)
        self.total_duration = kwargs.get('total_duration', None)
