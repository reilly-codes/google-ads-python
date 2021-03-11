# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/resources/campaign_asset.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v6.proto.enums import asset_field_type_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_asset__field__type__pb2
from google.ads.google_ads.v6.proto.enums import asset_link_status_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_asset__link__status__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v6/resources/campaign_asset.proto',
  package='google.ads.googleads.v6.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v6.resourcesB\022CampaignAssetProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V6.Resources\312\002!Google\\Ads\\GoogleAds\\V6\\Resources\352\002%Google::Ads::GoogleAds::V6::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n6google/ads/googleads/v6/resources/campaign_asset.proto\x12!google.ads.googleads.v6.resources\x1a\x34google/ads/googleads/v6/enums/asset_field_type.proto\x1a\x35google/ads/googleads/v6/enums/asset_link_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\x9a\x04\n\rCampaignAsset\x12\x45\n\rresource_name\x18\x01 \x01(\tB.\xe0\x41\x05\xfa\x41(\n&googleads.googleapis.com/CampaignAsset\x12@\n\x08\x63\x61mpaign\x18\x06 \x01(\tB)\xe0\x41\x05\xfa\x41#\n!googleads.googleapis.com/CampaignH\x00\x88\x01\x01\x12:\n\x05\x61sset\x18\x07 \x01(\tB&\xe0\x41\x05\xfa\x41 \n\x1egoogleads.googleapis.com/AssetH\x01\x88\x01\x01\x12Y\n\nfield_type\x18\x04 \x01(\x0e\x32@.google.ads.googleads.v6.enums.AssetFieldTypeEnum.AssetFieldTypeB\x03\xe0\x41\x05\x12W\n\x06status\x18\x05 \x01(\x0e\x32\x42.google.ads.googleads.v6.enums.AssetLinkStatusEnum.AssetLinkStatusB\x03\xe0\x41\x03:y\xea\x41v\n&googleads.googleapis.com/CampaignAsset\x12Lcustomers/{customer_id}/campaignAssets/{campaign_id}~{asset_id}~{field_type}B\x0b\n\t_campaignB\x08\n\x06_assetB\xff\x01\n%com.google.ads.googleads.v6.resourcesB\x12\x43\x61mpaignAssetProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V6.Resources\xca\x02!Google\\Ads\\GoogleAds\\V6\\Resources\xea\x02%Google::Ads::GoogleAds::V6::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_asset__field__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_asset__link__status__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CAMPAIGNASSET = _descriptor.Descriptor(
  name='CampaignAsset',
  full_name='google.ads.googleads.v6.resources.CampaignAsset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.resources.CampaignAsset.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A(\n&googleads.googleapis.com/CampaignAsset', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='campaign', full_name='google.ads.googleads.v6.resources.CampaignAsset.campaign', index=1,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A#\n!googleads.googleapis.com/Campaign', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='asset', full_name='google.ads.googleads.v6.resources.CampaignAsset.asset', index=2,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A \n\036googleads.googleapis.com/Asset', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='field_type', full_name='google.ads.googleads.v6.resources.CampaignAsset.field_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v6.resources.CampaignAsset.status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352Av\n&googleads.googleapis.com/CampaignAsset\022Lcustomers/{customer_id}/campaignAssets/{campaign_id}~{asset_id}~{field_type}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_campaign', full_name='google.ads.googleads.v6.resources.CampaignAsset._campaign',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_asset', full_name='google.ads.googleads.v6.resources.CampaignAsset._asset',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=293,
  serialized_end=831,
)

_CAMPAIGNASSET.fields_by_name['field_type'].enum_type = google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_asset__field__type__pb2._ASSETFIELDTYPEENUM_ASSETFIELDTYPE
_CAMPAIGNASSET.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_asset__link__status__pb2._ASSETLINKSTATUSENUM_ASSETLINKSTATUS
_CAMPAIGNASSET.oneofs_by_name['_campaign'].fields.append(
  _CAMPAIGNASSET.fields_by_name['campaign'])
_CAMPAIGNASSET.fields_by_name['campaign'].containing_oneof = _CAMPAIGNASSET.oneofs_by_name['_campaign']
_CAMPAIGNASSET.oneofs_by_name['_asset'].fields.append(
  _CAMPAIGNASSET.fields_by_name['asset'])
_CAMPAIGNASSET.fields_by_name['asset'].containing_oneof = _CAMPAIGNASSET.oneofs_by_name['_asset']
DESCRIPTOR.message_types_by_name['CampaignAsset'] = _CAMPAIGNASSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CampaignAsset = _reflection.GeneratedProtocolMessageType('CampaignAsset', (_message.Message,), {
  'DESCRIPTOR' : _CAMPAIGNASSET,
  '__module__' : 'google.ads.googleads.v6.resources.campaign_asset_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.resources.CampaignAsset)
  })
_sym_db.RegisterMessage(CampaignAsset)


DESCRIPTOR._options = None
_CAMPAIGNASSET.fields_by_name['resource_name']._options = None
_CAMPAIGNASSET.fields_by_name['campaign']._options = None
_CAMPAIGNASSET.fields_by_name['asset']._options = None
_CAMPAIGNASSET.fields_by_name['field_type']._options = None
_CAMPAIGNASSET.fields_by_name['status']._options = None
_CAMPAIGNASSET._options = None
# @@protoc_insertion_point(module_scope)