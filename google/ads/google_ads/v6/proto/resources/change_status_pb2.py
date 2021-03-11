# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/resources/change_status.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v6.proto.enums import ad_type_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_ad__type__pb2
from google.ads.google_ads.v6.proto.enums import advertising_channel_sub_type_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_advertising__channel__sub__type__pb2
from google.ads.google_ads.v6.proto.enums import advertising_channel_type_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_advertising__channel__type__pb2
from google.ads.google_ads.v6.proto.enums import change_status_operation_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_change__status__operation__pb2
from google.ads.google_ads.v6.proto.enums import change_status_resource_type_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_change__status__resource__type__pb2
from google.ads.google_ads.v6.proto.enums import criterion_type_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_criterion__type__pb2
from google.ads.google_ads.v6.proto.enums import feed_origin_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_feed__origin__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v6/resources/change_status.proto',
  package='google.ads.googleads.v6.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v6.resourcesB\021ChangeStatusProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V6.Resources\312\002!Google\\Ads\\GoogleAds\\V6\\Resources\352\002%Google::Ads::GoogleAds::V6::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n5google/ads/googleads/v6/resources/change_status.proto\x12!google.ads.googleads.v6.resources\x1a+google/ads/googleads/v6/enums/ad_type.proto\x1a@google/ads/googleads/v6/enums/advertising_channel_sub_type.proto\x1a<google/ads/googleads/v6/enums/advertising_channel_type.proto\x1a;google/ads/googleads/v6/enums/change_status_operation.proto\x1a?google/ads/googleads/v6/enums/change_status_resource_type.proto\x1a\x32google/ads/googleads/v6/enums/criterion_type.proto\x1a/google/ads/googleads/v6/enums/feed_origin.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xe6\n\n\x0c\x43hangeStatus\x12\x44\n\rresource_name\x18\x01 \x01(\tB-\xe0\x41\x03\xfa\x41\'\n%googleads.googleapis.com/ChangeStatus\x12\'\n\x15last_change_date_time\x18\x18 \x01(\tB\x03\xe0\x41\x03H\x00\x88\x01\x01\x12p\n\rresource_type\x18\x04 \x01(\x0e\x32T.google.ads.googleads.v6.enums.ChangeStatusResourceTypeEnum.ChangeStatusResourceTypeB\x03\xe0\x41\x03\x12@\n\x08\x63\x61mpaign\x18\x11 \x01(\tB)\xe0\x41\x03\xfa\x41#\n!googleads.googleapis.com/CampaignH\x01\x88\x01\x01\x12?\n\x08\x61\x64_group\x18\x12 \x01(\tB(\xe0\x41\x03\xfa\x41\"\n googleads.googleapis.com/AdGroupH\x02\x88\x01\x01\x12l\n\x0fresource_status\x18\x08 \x01(\x0e\x32N.google.ads.googleads.v6.enums.ChangeStatusOperationEnum.ChangeStatusOperationB\x03\xe0\x41\x03\x12\x44\n\x0b\x61\x64_group_ad\x18\x19 \x01(\tB*\xe0\x41\x03\xfa\x41$\n\"googleads.googleapis.com/AdGroupAdH\x03\x88\x01\x01\x12R\n\x12\x61\x64_group_criterion\x18\x1a \x01(\tB1\xe0\x41\x03\xfa\x41+\n)googleads.googleapis.com/AdGroupCriterionH\x04\x88\x01\x01\x12S\n\x12\x63\x61mpaign_criterion\x18\x1b \x01(\tB2\xe0\x41\x03\xfa\x41,\n*googleads.googleapis.com/CampaignCriterionH\x05\x88\x01\x01\x12\x38\n\x04\x66\x65\x65\x64\x18\x1c \x01(\tB%\xe0\x41\x03\xfa\x41\x1f\n\x1dgoogleads.googleapis.com/FeedH\x06\x88\x01\x01\x12\x41\n\tfeed_item\x18\x1d \x01(\tB)\xe0\x41\x03\xfa\x41#\n!googleads.googleapis.com/FeedItemH\x07\x88\x01\x01\x12H\n\rad_group_feed\x18\x1e \x01(\tB,\xe0\x41\x03\xfa\x41&\n$googleads.googleapis.com/AdGroupFeedH\x08\x88\x01\x01\x12I\n\rcampaign_feed\x18\x1f \x01(\tB-\xe0\x41\x03\xfa\x41\'\n%googleads.googleapis.com/CampaignFeedH\t\x88\x01\x01\x12W\n\x15\x61\x64_group_bid_modifier\x18  \x01(\tB3\xe0\x41\x03\xfa\x41-\n+googleads.googleapis.com/AdGroupBidModifierH\n\x88\x01\x01:c\xea\x41`\n%googleads.googleapis.com/ChangeStatus\x12\x37\x63ustomers/{customer_id}/changeStatus/{change_status_id}B\x18\n\x16_last_change_date_timeB\x0b\n\t_campaignB\x0b\n\t_ad_groupB\x0e\n\x0c_ad_group_adB\x15\n\x13_ad_group_criterionB\x15\n\x13_campaign_criterionB\x07\n\x05_feedB\x0c\n\n_feed_itemB\x10\n\x0e_ad_group_feedB\x10\n\x0e_campaign_feedB\x18\n\x16_ad_group_bid_modifierB\xfe\x01\n%com.google.ads.googleads.v6.resourcesB\x11\x43hangeStatusProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V6.Resources\xca\x02!Google\\Ads\\GoogleAds\\V6\\Resources\xea\x02%Google::Ads::GoogleAds::V6::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_ad__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_advertising__channel__sub__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_advertising__channel__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_change__status__operation__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_change__status__resource__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_criterion__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_feed__origin__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CHANGESTATUS = _descriptor.Descriptor(
  name='ChangeStatus',
  full_name='google.ads.googleads.v6.resources.ChangeStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.resources.ChangeStatus.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003\372A\'\n%googleads.googleapis.com/ChangeStatus', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_change_date_time', full_name='google.ads.googleads.v6.resources.ChangeStatus.last_change_date_time', index=1,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_type', full_name='google.ads.googleads.v6.resources.ChangeStatus.resource_type', index=2,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='campaign', full_name='google.ads.googleads.v6.resources.ChangeStatus.campaign', index=3,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003\372A#\n!googleads.googleapis.com/Campaign', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ad_group', full_name='google.ads.googleads.v6.resources.ChangeStatus.ad_group', index=4,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003\372A\"\n googleads.googleapis.com/AdGroup', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_status', full_name='google.ads.googleads.v6.resources.ChangeStatus.resource_status', index=5,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ad_group_ad', full_name='google.ads.googleads.v6.resources.ChangeStatus.ad_group_ad', index=6,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003\372A$\n\"googleads.googleapis.com/AdGroupAd', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ad_group_criterion', full_name='google.ads.googleads.v6.resources.ChangeStatus.ad_group_criterion', index=7,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003\372A+\n)googleads.googleapis.com/AdGroupCriterion', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='campaign_criterion', full_name='google.ads.googleads.v6.resources.ChangeStatus.campaign_criterion', index=8,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003\372A,\n*googleads.googleapis.com/CampaignCriterion', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feed', full_name='google.ads.googleads.v6.resources.ChangeStatus.feed', index=9,
      number=28, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003\372A\037\n\035googleads.googleapis.com/Feed', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feed_item', full_name='google.ads.googleads.v6.resources.ChangeStatus.feed_item', index=10,
      number=29, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003\372A#\n!googleads.googleapis.com/FeedItem', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ad_group_feed', full_name='google.ads.googleads.v6.resources.ChangeStatus.ad_group_feed', index=11,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003\372A&\n$googleads.googleapis.com/AdGroupFeed', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='campaign_feed', full_name='google.ads.googleads.v6.resources.ChangeStatus.campaign_feed', index=12,
      number=31, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003\372A\'\n%googleads.googleapis.com/CampaignFeed', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ad_group_bid_modifier', full_name='google.ads.googleads.v6.resources.ChangeStatus.ad_group_bid_modifier', index=13,
      number=32, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003\372A-\n+googleads.googleapis.com/AdGroupBidModifier', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352A`\n%googleads.googleapis.com/ChangeStatus\0227customers/{customer_id}/changeStatus/{change_status_id}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_last_change_date_time', full_name='google.ads.googleads.v6.resources.ChangeStatus._last_change_date_time',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_campaign', full_name='google.ads.googleads.v6.resources.ChangeStatus._campaign',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_ad_group', full_name='google.ads.googleads.v6.resources.ChangeStatus._ad_group',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_ad_group_ad', full_name='google.ads.googleads.v6.resources.ChangeStatus._ad_group_ad',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_ad_group_criterion', full_name='google.ads.googleads.v6.resources.ChangeStatus._ad_group_criterion',
      index=4, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_campaign_criterion', full_name='google.ads.googleads.v6.resources.ChangeStatus._campaign_criterion',
      index=5, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_feed', full_name='google.ads.googleads.v6.resources.ChangeStatus._feed',
      index=6, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_feed_item', full_name='google.ads.googleads.v6.resources.ChangeStatus._feed_item',
      index=7, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_ad_group_feed', full_name='google.ads.googleads.v6.resources.ChangeStatus._ad_group_feed',
      index=8, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_campaign_feed', full_name='google.ads.googleads.v6.resources.ChangeStatus._campaign_feed',
      index=9, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_ad_group_bid_modifier', full_name='google.ads.googleads.v6.resources.ChangeStatus._ad_group_bid_modifier',
      index=10, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=583,
  serialized_end=1965,
)

_CHANGESTATUS.fields_by_name['resource_type'].enum_type = google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_change__status__resource__type__pb2._CHANGESTATUSRESOURCETYPEENUM_CHANGESTATUSRESOURCETYPE
_CHANGESTATUS.fields_by_name['resource_status'].enum_type = google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_change__status__operation__pb2._CHANGESTATUSOPERATIONENUM_CHANGESTATUSOPERATION
_CHANGESTATUS.oneofs_by_name['_last_change_date_time'].fields.append(
  _CHANGESTATUS.fields_by_name['last_change_date_time'])
_CHANGESTATUS.fields_by_name['last_change_date_time'].containing_oneof = _CHANGESTATUS.oneofs_by_name['_last_change_date_time']
_CHANGESTATUS.oneofs_by_name['_campaign'].fields.append(
  _CHANGESTATUS.fields_by_name['campaign'])
_CHANGESTATUS.fields_by_name['campaign'].containing_oneof = _CHANGESTATUS.oneofs_by_name['_campaign']
_CHANGESTATUS.oneofs_by_name['_ad_group'].fields.append(
  _CHANGESTATUS.fields_by_name['ad_group'])
_CHANGESTATUS.fields_by_name['ad_group'].containing_oneof = _CHANGESTATUS.oneofs_by_name['_ad_group']
_CHANGESTATUS.oneofs_by_name['_ad_group_ad'].fields.append(
  _CHANGESTATUS.fields_by_name['ad_group_ad'])
_CHANGESTATUS.fields_by_name['ad_group_ad'].containing_oneof = _CHANGESTATUS.oneofs_by_name['_ad_group_ad']
_CHANGESTATUS.oneofs_by_name['_ad_group_criterion'].fields.append(
  _CHANGESTATUS.fields_by_name['ad_group_criterion'])
_CHANGESTATUS.fields_by_name['ad_group_criterion'].containing_oneof = _CHANGESTATUS.oneofs_by_name['_ad_group_criterion']
_CHANGESTATUS.oneofs_by_name['_campaign_criterion'].fields.append(
  _CHANGESTATUS.fields_by_name['campaign_criterion'])
_CHANGESTATUS.fields_by_name['campaign_criterion'].containing_oneof = _CHANGESTATUS.oneofs_by_name['_campaign_criterion']
_CHANGESTATUS.oneofs_by_name['_feed'].fields.append(
  _CHANGESTATUS.fields_by_name['feed'])
_CHANGESTATUS.fields_by_name['feed'].containing_oneof = _CHANGESTATUS.oneofs_by_name['_feed']
_CHANGESTATUS.oneofs_by_name['_feed_item'].fields.append(
  _CHANGESTATUS.fields_by_name['feed_item'])
_CHANGESTATUS.fields_by_name['feed_item'].containing_oneof = _CHANGESTATUS.oneofs_by_name['_feed_item']
_CHANGESTATUS.oneofs_by_name['_ad_group_feed'].fields.append(
  _CHANGESTATUS.fields_by_name['ad_group_feed'])
_CHANGESTATUS.fields_by_name['ad_group_feed'].containing_oneof = _CHANGESTATUS.oneofs_by_name['_ad_group_feed']
_CHANGESTATUS.oneofs_by_name['_campaign_feed'].fields.append(
  _CHANGESTATUS.fields_by_name['campaign_feed'])
_CHANGESTATUS.fields_by_name['campaign_feed'].containing_oneof = _CHANGESTATUS.oneofs_by_name['_campaign_feed']
_CHANGESTATUS.oneofs_by_name['_ad_group_bid_modifier'].fields.append(
  _CHANGESTATUS.fields_by_name['ad_group_bid_modifier'])
_CHANGESTATUS.fields_by_name['ad_group_bid_modifier'].containing_oneof = _CHANGESTATUS.oneofs_by_name['_ad_group_bid_modifier']
DESCRIPTOR.message_types_by_name['ChangeStatus'] = _CHANGESTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChangeStatus = _reflection.GeneratedProtocolMessageType('ChangeStatus', (_message.Message,), {
  'DESCRIPTOR' : _CHANGESTATUS,
  '__module__' : 'google.ads.googleads.v6.resources.change_status_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.resources.ChangeStatus)
  })
_sym_db.RegisterMessage(ChangeStatus)


DESCRIPTOR._options = None
_CHANGESTATUS.fields_by_name['resource_name']._options = None
_CHANGESTATUS.fields_by_name['last_change_date_time']._options = None
_CHANGESTATUS.fields_by_name['resource_type']._options = None
_CHANGESTATUS.fields_by_name['campaign']._options = None
_CHANGESTATUS.fields_by_name['ad_group']._options = None
_CHANGESTATUS.fields_by_name['resource_status']._options = None
_CHANGESTATUS.fields_by_name['ad_group_ad']._options = None
_CHANGESTATUS.fields_by_name['ad_group_criterion']._options = None
_CHANGESTATUS.fields_by_name['campaign_criterion']._options = None
_CHANGESTATUS.fields_by_name['feed']._options = None
_CHANGESTATUS.fields_by_name['feed_item']._options = None
_CHANGESTATUS.fields_by_name['ad_group_feed']._options = None
_CHANGESTATUS.fields_by_name['campaign_feed']._options = None
_CHANGESTATUS.fields_by_name['ad_group_bid_modifier']._options = None
_CHANGESTATUS._options = None
# @@protoc_insertion_point(module_scope)