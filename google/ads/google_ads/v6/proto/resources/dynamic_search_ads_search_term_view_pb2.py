# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/resources/dynamic_search_ads_search_term_view.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v6/resources/dynamic_search_ads_search_term_view.proto',
  package='google.ads.googleads.v6.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v6.resourcesB#DynamicSearchAdsSearchTermViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V6.Resources\312\002!Google\\Ads\\GoogleAds\\V6\\Resources\352\002%Google::Ads::GoogleAds::V6::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nKgoogle/ads/googleads/v6/resources/dynamic_search_ads_search_term_view.proto\x12!google.ads.googleads.v6.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xd0\x05\n\x1e\x44ynamicSearchAdsSearchTermView\x12V\n\rresource_name\x18\x01 \x01(\tB?\xe0\x41\x03\xfa\x41\x39\n7googleads.googleapis.com/DynamicSearchAdsSearchTermView\x12\x1d\n\x0bsearch_term\x18\t \x01(\tB\x03\xe0\x41\x03H\x00\x88\x01\x01\x12\x1a\n\x08headline\x18\n \x01(\tB\x03\xe0\x41\x03H\x01\x88\x01\x01\x12\x1e\n\x0clanding_page\x18\x0b \x01(\tB\x03\xe0\x41\x03H\x02\x88\x01\x01\x12\x1a\n\x08page_url\x18\x0c \x01(\tB\x03\xe0\x41\x03H\x03\x88\x01\x01\x12&\n\x14has_negative_keyword\x18\r \x01(\x08\x42\x03\xe0\x41\x03H\x04\x88\x01\x01\x12&\n\x14has_matching_keyword\x18\x0e \x01(\x08\x42\x03\xe0\x41\x03H\x05\x88\x01\x01\x12\"\n\x10has_negative_url\x18\x0f \x01(\x08\x42\x03\xe0\x41\x03H\x06\x88\x01\x01:\xe8\x01\xea\x41\xe4\x01\n7googleads.googleapis.com/DynamicSearchAdsSearchTermView\x12\xa8\x01\x63ustomers/{customer_id}/dynamicSearchAdsSearchTermViews/{ad_group_id}~{search_term_fingerprint}~{headline_fingerprint}~{landing_page_fingerprint}~{page_url_fingerprint}B\x0e\n\x0c_search_termB\x0b\n\t_headlineB\x0f\n\r_landing_pageB\x0b\n\t_page_urlB\x17\n\x15_has_negative_keywordB\x17\n\x15_has_matching_keywordB\x13\n\x11_has_negative_urlB\x90\x02\n%com.google.ads.googleads.v6.resourcesB#DynamicSearchAdsSearchTermViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V6.Resources\xca\x02!Google\\Ads\\GoogleAds\\V6\\Resources\xea\x02%Google::Ads::GoogleAds::V6::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_DYNAMICSEARCHADSSEARCHTERMVIEW = _descriptor.Descriptor(
  name='DynamicSearchAdsSearchTermView',
  full_name='google.ads.googleads.v6.resources.DynamicSearchAdsSearchTermView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.resources.DynamicSearchAdsSearchTermView.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003\372A9\n7googleads.googleapis.com/DynamicSearchAdsSearchTermView', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='search_term', full_name='google.ads.googleads.v6.resources.DynamicSearchAdsSearchTermView.search_term', index=1,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='headline', full_name='google.ads.googleads.v6.resources.DynamicSearchAdsSearchTermView.headline', index=2,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='landing_page', full_name='google.ads.googleads.v6.resources.DynamicSearchAdsSearchTermView.landing_page', index=3,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_url', full_name='google.ads.googleads.v6.resources.DynamicSearchAdsSearchTermView.page_url', index=4,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='has_negative_keyword', full_name='google.ads.googleads.v6.resources.DynamicSearchAdsSearchTermView.has_negative_keyword', index=5,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='has_matching_keyword', full_name='google.ads.googleads.v6.resources.DynamicSearchAdsSearchTermView.has_matching_keyword', index=6,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='has_negative_url', full_name='google.ads.googleads.v6.resources.DynamicSearchAdsSearchTermView.has_negative_url', index=7,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352A\344\001\n7googleads.googleapis.com/DynamicSearchAdsSearchTermView\022\250\001customers/{customer_id}/dynamicSearchAdsSearchTermViews/{ad_group_id}~{search_term_fingerprint}~{headline_fingerprint}~{landing_page_fingerprint}~{page_url_fingerprint}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_search_term', full_name='google.ads.googleads.v6.resources.DynamicSearchAdsSearchTermView._search_term',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_headline', full_name='google.ads.googleads.v6.resources.DynamicSearchAdsSearchTermView._headline',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_landing_page', full_name='google.ads.googleads.v6.resources.DynamicSearchAdsSearchTermView._landing_page',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_page_url', full_name='google.ads.googleads.v6.resources.DynamicSearchAdsSearchTermView._page_url',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_has_negative_keyword', full_name='google.ads.googleads.v6.resources.DynamicSearchAdsSearchTermView._has_negative_keyword',
      index=4, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_has_matching_keyword', full_name='google.ads.googleads.v6.resources.DynamicSearchAdsSearchTermView._has_matching_keyword',
      index=5, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_has_negative_url', full_name='google.ads.googleads.v6.resources.DynamicSearchAdsSearchTermView._has_negative_url',
      index=6, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=205,
  serialized_end=925,
)

_DYNAMICSEARCHADSSEARCHTERMVIEW.oneofs_by_name['_search_term'].fields.append(
  _DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['search_term'])
_DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['search_term'].containing_oneof = _DYNAMICSEARCHADSSEARCHTERMVIEW.oneofs_by_name['_search_term']
_DYNAMICSEARCHADSSEARCHTERMVIEW.oneofs_by_name['_headline'].fields.append(
  _DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['headline'])
_DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['headline'].containing_oneof = _DYNAMICSEARCHADSSEARCHTERMVIEW.oneofs_by_name['_headline']
_DYNAMICSEARCHADSSEARCHTERMVIEW.oneofs_by_name['_landing_page'].fields.append(
  _DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['landing_page'])
_DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['landing_page'].containing_oneof = _DYNAMICSEARCHADSSEARCHTERMVIEW.oneofs_by_name['_landing_page']
_DYNAMICSEARCHADSSEARCHTERMVIEW.oneofs_by_name['_page_url'].fields.append(
  _DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['page_url'])
_DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['page_url'].containing_oneof = _DYNAMICSEARCHADSSEARCHTERMVIEW.oneofs_by_name['_page_url']
_DYNAMICSEARCHADSSEARCHTERMVIEW.oneofs_by_name['_has_negative_keyword'].fields.append(
  _DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['has_negative_keyword'])
_DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['has_negative_keyword'].containing_oneof = _DYNAMICSEARCHADSSEARCHTERMVIEW.oneofs_by_name['_has_negative_keyword']
_DYNAMICSEARCHADSSEARCHTERMVIEW.oneofs_by_name['_has_matching_keyword'].fields.append(
  _DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['has_matching_keyword'])
_DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['has_matching_keyword'].containing_oneof = _DYNAMICSEARCHADSSEARCHTERMVIEW.oneofs_by_name['_has_matching_keyword']
_DYNAMICSEARCHADSSEARCHTERMVIEW.oneofs_by_name['_has_negative_url'].fields.append(
  _DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['has_negative_url'])
_DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['has_negative_url'].containing_oneof = _DYNAMICSEARCHADSSEARCHTERMVIEW.oneofs_by_name['_has_negative_url']
DESCRIPTOR.message_types_by_name['DynamicSearchAdsSearchTermView'] = _DYNAMICSEARCHADSSEARCHTERMVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DynamicSearchAdsSearchTermView = _reflection.GeneratedProtocolMessageType('DynamicSearchAdsSearchTermView', (_message.Message,), {
  'DESCRIPTOR' : _DYNAMICSEARCHADSSEARCHTERMVIEW,
  '__module__' : 'google.ads.googleads.v6.resources.dynamic_search_ads_search_term_view_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.resources.DynamicSearchAdsSearchTermView)
  })
_sym_db.RegisterMessage(DynamicSearchAdsSearchTermView)


DESCRIPTOR._options = None
_DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['resource_name']._options = None
_DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['search_term']._options = None
_DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['headline']._options = None
_DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['landing_page']._options = None
_DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['page_url']._options = None
_DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['has_negative_keyword']._options = None
_DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['has_matching_keyword']._options = None
_DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['has_negative_url']._options = None
_DYNAMICSEARCHADSSEARCHTERMVIEW._options = None
# @@protoc_insertion_point(module_scope)