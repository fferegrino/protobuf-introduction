# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contacto.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='contacto.proto',
  package='agenda',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0e\x63ontacto.proto\x12\x06\x61genda\",\n\x08\x43ontacto\x12\x0e\n\x06nombre\x18\x01 \x01(\t\x12\x10\n\x08telefono\x18\x02 \x01(\tb\x06proto3')
)




_CONTACTO = _descriptor.Descriptor(
  name='Contacto',
  full_name='agenda.Contacto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nombre', full_name='agenda.Contacto.nombre', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='telefono', full_name='agenda.Contacto.telefono', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=70,
)

DESCRIPTOR.message_types_by_name['Contacto'] = _CONTACTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Contacto = _reflection.GeneratedProtocolMessageType('Contacto', (_message.Message,), dict(
  DESCRIPTOR = _CONTACTO,
  __module__ = 'contacto_pb2'
  # @@protoc_insertion_point(class_scope:agenda.Contacto)
  ))
_sym_db.RegisterMessage(Contacto)


# @@protoc_insertion_point(module_scope)
