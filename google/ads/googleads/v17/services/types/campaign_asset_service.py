# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations

from typing import MutableSequence

import proto  # type: ignore

from google.ads.googleads.v17.enums.types import (
    response_content_type as gage_response_content_type,
)
from google.ads.googleads.v17.resources.types import (
    campaign_asset as gagr_campaign_asset,
)
from google.protobuf import field_mask_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v17.services",
    marshal="google.ads.googleads.v17",
    manifest={
        "MutateCampaignAssetsRequest",
        "CampaignAssetOperation",
        "MutateCampaignAssetsResponse",
        "MutateCampaignAssetResult",
    },
)


class MutateCampaignAssetsRequest(proto.Message):
    r"""Request message for
    [CampaignAssetService.MutateCampaignAssets][google.ads.googleads.v17.services.CampaignAssetService.MutateCampaignAssets].

    Attributes:
        customer_id (str):
            Required. The ID of the customer whose
            campaign assets are being modified.
        operations (MutableSequence[google.ads.googleads.v17.services.types.CampaignAssetOperation]):
            Required. The list of operations to perform
            on individual campaign assets.
        partial_failure (bool):
            If true, successful operations will be
            carried out and invalid operations will return
            errors. If false, all operations will be carried
            out in one transaction if and only if they are
            all valid. Default is false.
        validate_only (bool):
            If true, the request is validated but not
            executed. Only errors are returned, not results.
        response_content_type (google.ads.googleads.v17.enums.types.ResponseContentTypeEnum.ResponseContentType):
            The response content type setting. Determines
            whether the mutable resource or just the
            resource name should be returned post mutation.
    """

    customer_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    operations: MutableSequence["CampaignAssetOperation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CampaignAssetOperation",
    )
    partial_failure: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType = proto.Field(
        proto.ENUM,
        number=5,
        enum=gage_response_content_type.ResponseContentTypeEnum.ResponseContentType,
    )


class CampaignAssetOperation(proto.Message):
    r"""A single operation (create, update, remove) on a campaign
    asset.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            FieldMask that determines which resource
            fields are modified in an update.
        create (google.ads.googleads.v17.resources.types.CampaignAsset):
            Create operation: No resource name is
            expected for the new campaign asset.

            This field is a member of `oneof`_ ``operation``.
        update (google.ads.googleads.v17.resources.types.CampaignAsset):
            Update operation: The campaign asset is
            expected to have a valid resource name.

            This field is a member of `oneof`_ ``operation``.
        remove (str):
            Remove operation: A resource name for the removed campaign
            asset is expected, in this format:

            ``customers/{customer_id}/campaignAssets/{campaign_id}~{asset_id}~{field_type}``

            This field is a member of `oneof`_ ``operation``.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=4,
        message=field_mask_pb2.FieldMask,
    )
    create: gagr_campaign_asset.CampaignAsset = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="operation",
        message=gagr_campaign_asset.CampaignAsset,
    )
    update: gagr_campaign_asset.CampaignAsset = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="operation",
        message=gagr_campaign_asset.CampaignAsset,
    )
    remove: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="operation",
    )


class MutateCampaignAssetsResponse(proto.Message):
    r"""Response message for a campaign asset mutate.
    Attributes:
        partial_failure_error (google.rpc.status_pb2.Status):
            Errors that pertain to operation failures in the partial
            failure mode. Returned only when partial_failure = true and
            all errors occur inside the operations. If any errors occur
            outside the operations (for example, auth errors), we return
            an RPC level error.
        results (MutableSequence[google.ads.googleads.v17.services.types.MutateCampaignAssetResult]):
            All results for the mutate.
    """

    partial_failure_error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=1,
        message=status_pb2.Status,
    )
    results: MutableSequence["MutateCampaignAssetResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="MutateCampaignAssetResult",
    )


class MutateCampaignAssetResult(proto.Message):
    r"""The result for the campaign asset mutate.
    Attributes:
        resource_name (str):
            Returned for successful operations.
        campaign_asset (google.ads.googleads.v17.resources.types.CampaignAsset):
            The mutated campaign asset with only mutable fields after
            mutate. The field will only be returned when
            response_content_type is set to "MUTABLE_RESOURCE".
    """

    resource_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    campaign_asset: gagr_campaign_asset.CampaignAsset = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gagr_campaign_asset.CampaignAsset,
    )


__all__ = tuple(sorted(__protobuf__.manifest))