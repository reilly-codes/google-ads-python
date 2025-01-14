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


import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v18.errors",
    marshal="google.ads.googleads.v18",
    manifest={"CampaignConversionGoalErrorEnum",},
)


class CampaignConversionGoalErrorEnum(proto.Message):
    r"""Container for enum describing possible campaign conversion
    goal errors.

    """

    class CampaignConversionGoalError(proto.Enum):
        r"""Enum describing possible campaign conversion goal errors."""
        UNSPECIFIED = 0
        UNKNOWN = 1
        CANNOT_USE_CAMPAIGN_GOAL_FOR_SEARCH_ADS_360_MANAGED_CAMPAIGN = 2
        CANNOT_USE_STORE_SALE_GOAL_FOR_PERFORMANCE_MAX_CAMPAIGN = 3


__all__ = tuple(sorted(__protobuf__.manifest))