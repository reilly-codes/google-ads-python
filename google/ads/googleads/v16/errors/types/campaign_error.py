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
    package="google.ads.googleads.v16.errors",
    marshal="google.ads.googleads.v16",
    manifest={
        "CampaignErrorEnum",
    },
)


class CampaignErrorEnum(proto.Message):
    r"""Container for enum describing possible campaign errors."""

    class CampaignError(proto.Enum):
        r"""Enum describing possible campaign errors."""
        UNSPECIFIED = 0
        UNKNOWN = 1
        CANNOT_TARGET_CONTENT_NETWORK = 3
        CANNOT_TARGET_SEARCH_NETWORK = 4
        CANNOT_TARGET_SEARCH_NETWORK_WITHOUT_GOOGLE_SEARCH = 5
        CANNOT_TARGET_GOOGLE_SEARCH_FOR_CPM_CAMPAIGN = 6
        CAMPAIGN_MUST_TARGET_AT_LEAST_ONE_NETWORK = 7
        CANNOT_TARGET_PARTNER_SEARCH_NETWORK = 8
        CANNOT_TARGET_CONTENT_NETWORK_ONLY_WITH_CRITERIA_LEVEL_BIDDING_STRATEGY = (
            9
        )
        CAMPAIGN_DURATION_MUST_CONTAIN_ALL_RUNNABLE_TRIALS = 10
        CANNOT_MODIFY_FOR_TRIAL_CAMPAIGN = 11
        DUPLICATE_CAMPAIGN_NAME = 12
        INCOMPATIBLE_CAMPAIGN_FIELD = 13
        INVALID_CAMPAIGN_NAME = 14
        INVALID_AD_SERVING_OPTIMIZATION_STATUS = 15
        INVALID_TRACKING_URL = 16
        CANNOT_SET_BOTH_TRACKING_URL_TEMPLATE_AND_TRACKING_SETTING = 17
        MAX_IMPRESSIONS_NOT_IN_RANGE = 18
        TIME_UNIT_NOT_SUPPORTED = 19
        INVALID_OPERATION_IF_SERVING_STATUS_HAS_ENDED = 20
        BUDGET_CANNOT_BE_SHARED = 21
        CAMPAIGN_CANNOT_USE_SHARED_BUDGET = 22
        CANNOT_CHANGE_BUDGET_ON_CAMPAIGN_WITH_TRIALS = 23
        CAMPAIGN_LABEL_DOES_NOT_EXIST = 24
        CAMPAIGN_LABEL_ALREADY_EXISTS = 25
        MISSING_SHOPPING_SETTING = 26
        INVALID_SHOPPING_SALES_COUNTRY = 27
        ADVERTISING_CHANNEL_TYPE_NOT_AVAILABLE_FOR_ACCOUNT_TYPE = 31
        INVALID_ADVERTISING_CHANNEL_SUB_TYPE = 32
        AT_LEAST_ONE_CONVERSION_MUST_BE_SELECTED = 33
        CANNOT_SET_AD_ROTATION_MODE = 34
        CANNOT_MODIFY_START_DATE_IF_ALREADY_STARTED = 35
        CANNOT_SET_DATE_TO_PAST = 36
        MISSING_HOTEL_CUSTOMER_LINK = 37
        INVALID_HOTEL_CUSTOMER_LINK = 38
        MISSING_HOTEL_SETTING = 39
        CANNOT_USE_SHARED_CAMPAIGN_BUDGET_WHILE_PART_OF_CAMPAIGN_GROUP = 40
        APP_NOT_FOUND = 41
        SHOPPING_ENABLE_LOCAL_NOT_SUPPORTED_FOR_CAMPAIGN_TYPE = 42
        MERCHANT_NOT_ALLOWED_FOR_COMPARISON_LISTING_ADS = 43
        INSUFFICIENT_APP_INSTALLS_COUNT = 44
        SENSITIVE_CATEGORY_APP = 45
        HEC_AGREEMENT_REQUIRED = 46
        NOT_COMPATIBLE_WITH_VIEW_THROUGH_CONVERSION_OPTIMIZATION = 49
        INVALID_EXCLUDED_PARENT_ASSET_FIELD_TYPE = 48
        CANNOT_CREATE_APP_PRE_REGISTRATION_FOR_NON_ANDROID_APP = 50
        APP_NOT_AVAILABLE_TO_CREATE_APP_PRE_REGISTRATION_CAMPAIGN = 51
        INCOMPATIBLE_BUDGET_TYPE = 52
        LOCAL_SERVICES_DUPLICATE_CATEGORY_BID = 53
        LOCAL_SERVICES_INVALID_CATEGORY_BID = 54
        LOCAL_SERVICES_MISSING_CATEGORY_BID = 55
        INVALID_STATUS_CHANGE = 57
        MISSING_TRAVEL_CUSTOMER_LINK = 58
        INVALID_TRAVEL_CUSTOMER_LINK = 59
        INVALID_EXCLUDED_PARENT_ASSET_SET_TYPE = 62
        ASSET_SET_NOT_A_HOTEL_PROPERTY_ASSET_SET = 63
        HOTEL_PROPERTY_ASSET_SET_ONLY_FOR_PERFORMANCE_MAX_FOR_TRAVEL_GOALS = 64
        AVERAGE_DAILY_SPEND_TOO_HIGH = 65
        CANNOT_ATTACH_TO_REMOVED_CAMPAIGN_GROUP = 66
        CANNOT_ATTACH_TO_BIDDING_STRATEGY = 67
        CANNOT_CHANGE_BUDGET_PERIOD = 68
        NOT_ENOUGH_CONVERSIONS = 71
        CANNOT_SET_MORE_THAN_ONE_CONVERSION_ACTION = 72
        NOT_COMPATIBLE_WITH_BUDGET_TYPE = 73
        NOT_COMPATIBLE_WITH_UPLOAD_CLICKS_CONVERSION = 74
        APP_ID_MUST_MATCH_CONVERSION_ACTION_APP_ID = 76
        CONVERSION_ACTION_WITH_DOWNLOAD_CATEGORY_NOT_ALLOWED = 77
        CONVERSION_ACTION_WITH_DOWNLOAD_CATEGORY_REQUIRED = 78
        CONVERSION_TRACKING_NOT_ENABLED = 79
        NOT_COMPATIBLE_WITH_BIDDING_STRATEGY_TYPE = 80
        NOT_COMPATIBLE_WITH_GOOGLE_ATTRIBUTION_CONVERSIONS = 81
        CONVERSION_LAG_TOO_HIGH = 82
        NOT_LINKED_ADVERTISING_PARTNER = 83
        INVALID_NUMBER_OF_ADVERTISING_PARTNER_IDS = 84
        CANNOT_TARGET_DISPLAY_NETWORK_WITHOUT_YOUTUBE = 85
        CANNOT_LINK_TO_COMPARISON_SHOPPING_SERVICE_ACCOUNT = 86
        CANNOT_TARGET_NETWORK_FOR_COMPARISON_SHOPPING_SERVICE_LINKED_ACCOUNTS = (
            87
        )
        CANNOT_MODIFY_TEXT_ASSET_AUTOMATION_WITH_ENABLED_TRIAL = 88
        DYNAMIC_TEXT_ASSET_CANNOT_OPT_OUT_WITH_FINAL_URL_EXPANSION_OPT_IN = 89


__all__ = tuple(sorted(__protobuf__.manifest))
