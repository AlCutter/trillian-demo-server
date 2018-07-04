# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crypto/sigpb/sigpb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='crypto/sigpb/sigpb.proto',
  package='sigpb',
  syntax='proto3',
  serialized_pb=_b('\n\x18\x63rypto/sigpb/sigpb.proto\x12\x05sigpb\"\x8a\x02\n\x0f\x44igitallySigned\x12<\n\x0ehash_algorithm\x18\x01 \x01(\x0e\x32$.sigpb.DigitallySigned.HashAlgorithm\x12\x46\n\x13signature_algorithm\x18\x02 \x01(\x0e\x32).sigpb.DigitallySigned.SignatureAlgorithm\x12\x11\n\tsignature\x18\x03 \x01(\x0c\"%\n\rHashAlgorithm\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06SHA256\x10\x04\"7\n\x12SignatureAlgorithm\x12\r\n\tANONYMOUS\x10\x00\x12\x07\n\x03RSA\x10\x01\x12\t\n\x05\x45\x43\x44SA\x10\x03\x42)Z\'github.com/google/trillian/crypto/sigpbb\x06proto3')
)



_DIGITALLYSIGNED_HASHALGORITHM = _descriptor.EnumDescriptor(
  name='HashAlgorithm',
  full_name='sigpb.DigitallySigned.HashAlgorithm',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHA256', index=1, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=208,
  serialized_end=245,
)
_sym_db.RegisterEnumDescriptor(_DIGITALLYSIGNED_HASHALGORITHM)

_DIGITALLYSIGNED_SIGNATUREALGORITHM = _descriptor.EnumDescriptor(
  name='SignatureAlgorithm',
  full_name='sigpb.DigitallySigned.SignatureAlgorithm',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ANONYMOUS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RSA', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ECDSA', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=247,
  serialized_end=302,
)
_sym_db.RegisterEnumDescriptor(_DIGITALLYSIGNED_SIGNATUREALGORITHM)


_DIGITALLYSIGNED = _descriptor.Descriptor(
  name='DigitallySigned',
  full_name='sigpb.DigitallySigned',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash_algorithm', full_name='sigpb.DigitallySigned.hash_algorithm', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature_algorithm', full_name='sigpb.DigitallySigned.signature_algorithm', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='sigpb.DigitallySigned.signature', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DIGITALLYSIGNED_HASHALGORITHM,
    _DIGITALLYSIGNED_SIGNATUREALGORITHM,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=302,
)

_DIGITALLYSIGNED.fields_by_name['hash_algorithm'].enum_type = _DIGITALLYSIGNED_HASHALGORITHM
_DIGITALLYSIGNED.fields_by_name['signature_algorithm'].enum_type = _DIGITALLYSIGNED_SIGNATUREALGORITHM
_DIGITALLYSIGNED_HASHALGORITHM.containing_type = _DIGITALLYSIGNED
_DIGITALLYSIGNED_SIGNATUREALGORITHM.containing_type = _DIGITALLYSIGNED
DESCRIPTOR.message_types_by_name['DigitallySigned'] = _DIGITALLYSIGNED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DigitallySigned = _reflection.GeneratedProtocolMessageType('DigitallySigned', (_message.Message,), dict(
  DESCRIPTOR = _DIGITALLYSIGNED,
  __module__ = 'crypto.sigpb.sigpb_pb2'
  # @@protoc_insertion_point(class_scope:sigpb.DigitallySigned)
  ))
_sym_db.RegisterMessage(DigitallySigned)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\'github.com/google/trillian/crypto/sigpb'))
# @@protoc_insertion_point(module_scope)
