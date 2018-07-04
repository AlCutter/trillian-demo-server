# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trillian_admin_api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import trillian_pb2 as trillian__pb2
from crypto.keyspb import keyspb_pb2 as crypto_dot_keyspb_dot_keyspb__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='trillian_admin_api.proto',
  package='trillian',
  syntax='proto3',
  serialized_pb=_b('\n\x18trillian_admin_api.proto\x12\x08trillian\x1a\x0etrillian.proto\x1a\x1a\x63rypto/keyspb/keyspb.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\"(\n\x10ListTreesRequest\x12\x14\n\x0cshow_deleted\x18\x01 \x01(\x08\"1\n\x11ListTreesResponse\x12\x1c\n\x04tree\x18\x01 \x03(\x0b\x32\x0e.trillian.Tree\"!\n\x0eGetTreeRequest\x12\x0f\n\x07tree_id\x18\x01 \x01(\x03\"Z\n\x11\x43reateTreeRequest\x12\x1c\n\x04tree\x18\x01 \x01(\x0b\x32\x0e.trillian.Tree\x12\'\n\x08key_spec\x18\x02 \x01(\x0b\x32\x15.keyspb.Specification\"b\n\x11UpdateTreeRequest\x12\x1c\n\x04tree\x18\x01 \x01(\x0b\x32\x0e.trillian.Tree\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"$\n\x11\x44\x65leteTreeRequest\x12\x0f\n\x07tree_id\x18\x01 \x01(\x03\"&\n\x13UndeleteTreeRequest\x12\x0f\n\x07tree_id\x18\x01 \x01(\x03\x32\xb8\x04\n\rTrillianAdmin\x12\x46\n\tListTrees\x12\x1a.trillian.ListTreesRequest\x1a\x1b.trillian.ListTreesResponse\"\x00\x12W\n\x07GetTree\x12\x18.trillian.GetTreeRequest\x1a\x0e.trillian.Tree\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1beta1/trees/{tree_id=*}\x12T\n\nCreateTree\x12\x1b.trillian.CreateTreeRequest\x1a\x0e.trillian.Tree\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/v1beta1/trees:\x01*\x12\x65\n\nUpdateTree\x12\x1b.trillian.UpdateTreeRequest\x1a\x0e.trillian.Tree\"*\x82\xd3\xe4\x93\x02$2\x1f/v1beta1/trees/{tree.tree_id=*}:\x01*\x12]\n\nDeleteTree\x12\x1b.trillian.DeleteTreeRequest\x1a\x0e.trillian.Tree\"\"\x82\xd3\xe4\x93\x02\x1c*\x1a/v1beta1/trees/{tree_id=*}\x12j\n\x0cUndeleteTree\x12\x1d.trillian.UndeleteTreeRequest\x1a\x0e.trillian.Tree\"+\x82\xd3\xe4\x93\x02%*#/v1beta1/trees/{tree_id=*}:undeleteBP\n\x19\x63om.google.trillian.protoB\x15TrillianAdminApiProtoP\x01Z\x1agithub.com/google/trillianb\x06proto3')
  ,
  dependencies=[trillian__pb2.DESCRIPTOR,crypto_dot_keyspb_dot_keyspb__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,])




_LISTTREESREQUEST = _descriptor.Descriptor(
  name='ListTreesRequest',
  full_name='trillian.ListTreesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='show_deleted', full_name='trillian.ListTreesRequest.show_deleted', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=146,
  serialized_end=186,
)


_LISTTREESRESPONSE = _descriptor.Descriptor(
  name='ListTreesResponse',
  full_name='trillian.ListTreesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tree', full_name='trillian.ListTreesResponse.tree', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=237,
)


_GETTREEREQUEST = _descriptor.Descriptor(
  name='GetTreeRequest',
  full_name='trillian.GetTreeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tree_id', full_name='trillian.GetTreeRequest.tree_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=239,
  serialized_end=272,
)


_CREATETREEREQUEST = _descriptor.Descriptor(
  name='CreateTreeRequest',
  full_name='trillian.CreateTreeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tree', full_name='trillian.CreateTreeRequest.tree', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key_spec', full_name='trillian.CreateTreeRequest.key_spec', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=274,
  serialized_end=364,
)


_UPDATETREEREQUEST = _descriptor.Descriptor(
  name='UpdateTreeRequest',
  full_name='trillian.UpdateTreeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tree', full_name='trillian.UpdateTreeRequest.tree', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='trillian.UpdateTreeRequest.update_mask', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=366,
  serialized_end=464,
)


_DELETETREEREQUEST = _descriptor.Descriptor(
  name='DeleteTreeRequest',
  full_name='trillian.DeleteTreeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tree_id', full_name='trillian.DeleteTreeRequest.tree_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=466,
  serialized_end=502,
)


_UNDELETETREEREQUEST = _descriptor.Descriptor(
  name='UndeleteTreeRequest',
  full_name='trillian.UndeleteTreeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tree_id', full_name='trillian.UndeleteTreeRequest.tree_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=504,
  serialized_end=542,
)

_LISTTREESRESPONSE.fields_by_name['tree'].message_type = trillian__pb2._TREE
_CREATETREEREQUEST.fields_by_name['tree'].message_type = trillian__pb2._TREE
_CREATETREEREQUEST.fields_by_name['key_spec'].message_type = crypto_dot_keyspb_dot_keyspb__pb2._SPECIFICATION
_UPDATETREEREQUEST.fields_by_name['tree'].message_type = trillian__pb2._TREE
_UPDATETREEREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
DESCRIPTOR.message_types_by_name['ListTreesRequest'] = _LISTTREESREQUEST
DESCRIPTOR.message_types_by_name['ListTreesResponse'] = _LISTTREESRESPONSE
DESCRIPTOR.message_types_by_name['GetTreeRequest'] = _GETTREEREQUEST
DESCRIPTOR.message_types_by_name['CreateTreeRequest'] = _CREATETREEREQUEST
DESCRIPTOR.message_types_by_name['UpdateTreeRequest'] = _UPDATETREEREQUEST
DESCRIPTOR.message_types_by_name['DeleteTreeRequest'] = _DELETETREEREQUEST
DESCRIPTOR.message_types_by_name['UndeleteTreeRequest'] = _UNDELETETREEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListTreesRequest = _reflection.GeneratedProtocolMessageType('ListTreesRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTTREESREQUEST,
  __module__ = 'trillian_admin_api_pb2'
  # @@protoc_insertion_point(class_scope:trillian.ListTreesRequest)
  ))
_sym_db.RegisterMessage(ListTreesRequest)

ListTreesResponse = _reflection.GeneratedProtocolMessageType('ListTreesResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTTREESRESPONSE,
  __module__ = 'trillian_admin_api_pb2'
  # @@protoc_insertion_point(class_scope:trillian.ListTreesResponse)
  ))
_sym_db.RegisterMessage(ListTreesResponse)

GetTreeRequest = _reflection.GeneratedProtocolMessageType('GetTreeRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETTREEREQUEST,
  __module__ = 'trillian_admin_api_pb2'
  # @@protoc_insertion_point(class_scope:trillian.GetTreeRequest)
  ))
_sym_db.RegisterMessage(GetTreeRequest)

CreateTreeRequest = _reflection.GeneratedProtocolMessageType('CreateTreeRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATETREEREQUEST,
  __module__ = 'trillian_admin_api_pb2'
  # @@protoc_insertion_point(class_scope:trillian.CreateTreeRequest)
  ))
_sym_db.RegisterMessage(CreateTreeRequest)

UpdateTreeRequest = _reflection.GeneratedProtocolMessageType('UpdateTreeRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATETREEREQUEST,
  __module__ = 'trillian_admin_api_pb2'
  # @@protoc_insertion_point(class_scope:trillian.UpdateTreeRequest)
  ))
_sym_db.RegisterMessage(UpdateTreeRequest)

DeleteTreeRequest = _reflection.GeneratedProtocolMessageType('DeleteTreeRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETETREEREQUEST,
  __module__ = 'trillian_admin_api_pb2'
  # @@protoc_insertion_point(class_scope:trillian.DeleteTreeRequest)
  ))
_sym_db.RegisterMessage(DeleteTreeRequest)

UndeleteTreeRequest = _reflection.GeneratedProtocolMessageType('UndeleteTreeRequest', (_message.Message,), dict(
  DESCRIPTOR = _UNDELETETREEREQUEST,
  __module__ = 'trillian_admin_api_pb2'
  # @@protoc_insertion_point(class_scope:trillian.UndeleteTreeRequest)
  ))
_sym_db.RegisterMessage(UndeleteTreeRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\031com.google.trillian.protoB\025TrillianAdminApiProtoP\001Z\032github.com/google/trillian'))

_TRILLIANADMIN = _descriptor.ServiceDescriptor(
  name='TrillianAdmin',
  full_name='trillian.TrillianAdmin',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=545,
  serialized_end=1113,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListTrees',
    full_name='trillian.TrillianAdmin.ListTrees',
    index=0,
    containing_service=None,
    input_type=_LISTTREESREQUEST,
    output_type=_LISTTREESRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTree',
    full_name='trillian.TrillianAdmin.GetTree',
    index=1,
    containing_service=None,
    input_type=_GETTREEREQUEST,
    output_type=trillian__pb2._TREE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\034\022\032/v1beta1/trees/{tree_id=*}')),
  ),
  _descriptor.MethodDescriptor(
    name='CreateTree',
    full_name='trillian.TrillianAdmin.CreateTree',
    index=2,
    containing_service=None,
    input_type=_CREATETREEREQUEST,
    output_type=trillian__pb2._TREE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\023\"\016/v1beta1/trees:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateTree',
    full_name='trillian.TrillianAdmin.UpdateTree',
    index=3,
    containing_service=None,
    input_type=_UPDATETREEREQUEST,
    output_type=trillian__pb2._TREE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002$2\037/v1beta1/trees/{tree.tree_id=*}:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteTree',
    full_name='trillian.TrillianAdmin.DeleteTree',
    index=4,
    containing_service=None,
    input_type=_DELETETREEREQUEST,
    output_type=trillian__pb2._TREE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\034*\032/v1beta1/trees/{tree_id=*}')),
  ),
  _descriptor.MethodDescriptor(
    name='UndeleteTree',
    full_name='trillian.TrillianAdmin.UndeleteTree',
    index=5,
    containing_service=None,
    input_type=_UNDELETETREEREQUEST,
    output_type=trillian__pb2._TREE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002%*#/v1beta1/trees/{tree_id=*}:undelete')),
  ),
])
_sym_db.RegisterServiceDescriptor(_TRILLIANADMIN)

DESCRIPTOR.services_by_name['TrillianAdmin'] = _TRILLIANADMIN

# @@protoc_insertion_point(module_scope)
