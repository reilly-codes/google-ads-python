# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/enums/lead_form_desired_intent.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v6/enums/lead_form_desired_intent.proto',
  package='google.ads.googleads.v6.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v6.enumsB\032LeadFormDesiredIntentProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V6.Enums\312\002\035Google\\Ads\\GoogleAds\\V6\\Enums\352\002!Google::Ads::GoogleAds::V6::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n<google/ads/googleads/v6/enums/lead_form_desired_intent.proto\x12\x1dgoogle.ads.googleads.v6.enums\x1a\x1cgoogle/api/annotations.proto\"s\n\x19LeadFormDesiredIntentEnum\"V\n\x15LeadFormDesiredIntent\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0e\n\nLOW_INTENT\x10\x02\x12\x0f\n\x0bHIGH_INTENT\x10\x03\x42\xef\x01\n!com.google.ads.googleads.v6.enumsB\x1aLeadFormDesiredIntentProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V6.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V6\\Enums\xea\x02!Google::Ads::GoogleAds::V6::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_LEADFORMDESIREDINTENTENUM_LEADFORMDESIREDINTENT = _descriptor.EnumDescriptor(
  name='LeadFormDesiredIntent',
  full_name='google.ads.googleads.v6.enums.LeadFormDesiredIntentEnum.LeadFormDesiredIntent',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOW_INTENT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HIGH_INTENT', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=154,
  serialized_end=240,
)
_sym_db.RegisterEnumDescriptor(_LEADFORMDESIREDINTENTENUM_LEADFORMDESIREDINTENT)


_LEADFORMDESIREDINTENTENUM = _descriptor.Descriptor(
  name='LeadFormDesiredIntentEnum',
  full_name='google.ads.googleads.v6.enums.LeadFormDesiredIntentEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LEADFORMDESIREDINTENTENUM_LEADFORMDESIREDINTENT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=240,
)

_LEADFORMDESIREDINTENTENUM_LEADFORMDESIREDINTENT.containing_type = _LEADFORMDESIREDINTENTENUM
DESCRIPTOR.message_types_by_name['LeadFormDesiredIntentEnum'] = _LEADFORMDESIREDINTENTENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LeadFormDesiredIntentEnum = _reflection.GeneratedProtocolMessageType('LeadFormDesiredIntentEnum', (_message.Message,), {
  'DESCRIPTOR' : _LEADFORMDESIREDINTENTENUM,
  '__module__' : 'google.ads.googleads.v6.enums.lead_form_desired_intent_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.enums.LeadFormDesiredIntentEnum)
  })
_sym_db.RegisterMessage(LeadFormDesiredIntentEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)