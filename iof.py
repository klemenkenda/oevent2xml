# .\iof.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:c5a3c5573096fea7c26dd5ce4d01ac4cdd133e1b
# Generated 2017-06-07 19:43:39.205882 by PyXB version 1.2.5 using Python 3.5.3.final.0
# Namespace http://www.orienteering.org/datastandard/3.0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:d69aca06-4ba8-11e7-9f69-bcc1f235ecf4')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.orienteering.org/datastandard/3.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 317, 12)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.Complete = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Complete', tag='Complete')
STD_ANON.Delta = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Delta', tag='Delta')
STD_ANON.Snapshot = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Snapshot', tag='Snapshot')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 485, 6)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.F = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='F', tag='F')
STD_ANON_.M = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='M', tag='M')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 657, 6)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.IOF = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='IOF', tag='IOF')
STD_ANON_2.IOFRegion = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='IOFRegion', tag='IOFRegion')
STD_ANON_2.NationalFederation = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='NationalFederation', tag='NationalFederation')
STD_ANON_2.NationalRegion = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='NationalRegion', tag='NationalRegion')
STD_ANON_2.Club = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Club', tag='Club')
STD_ANON_2.School = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='School', tag='School')
STD_ANON_2.Company = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Company', tag='Company')
STD_ANON_2.Military = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Military', tag='Military')
STD_ANON_2.Other = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: {http://www.orienteering.org/datastandard/3.0}EventForm
class EventForm (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EventForm')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 820, 2)
    _Documentation = None
EventForm._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EventForm, enum_prefix=None)
EventForm.Individual = EventForm._CF_enumeration.addEnumeration(unicode_value='Individual', tag='Individual')
EventForm.Team = EventForm._CF_enumeration.addEnumeration(unicode_value='Team', tag='Team')
EventForm.Relay = EventForm._CF_enumeration.addEnumeration(unicode_value='Relay', tag='Relay')
EventForm._InitializeFacetMap(EventForm._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'EventForm', EventForm)
_module_typeBindings.EventForm = EventForm

# Atomic simple type: {http://www.orienteering.org/datastandard/3.0}EventStatus
class EventStatus (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EventStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 828, 2)
    _Documentation = None
EventStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EventStatus, enum_prefix=None)
EventStatus.Planned = EventStatus._CF_enumeration.addEnumeration(unicode_value='Planned', tag='Planned')
EventStatus.Applied = EventStatus._CF_enumeration.addEnumeration(unicode_value='Applied', tag='Applied')
EventStatus.Proposed = EventStatus._CF_enumeration.addEnumeration(unicode_value='Proposed', tag='Proposed')
EventStatus.Sanctioned = EventStatus._CF_enumeration.addEnumeration(unicode_value='Sanctioned', tag='Sanctioned')
EventStatus.Canceled = EventStatus._CF_enumeration.addEnumeration(unicode_value='Canceled', tag='Canceled')
EventStatus.Rescheduled = EventStatus._CF_enumeration.addEnumeration(unicode_value='Rescheduled', tag='Rescheduled')
EventStatus._InitializeFacetMap(EventStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'EventStatus', EventStatus)
_module_typeBindings.EventStatus = EventStatus

# Atomic simple type: {http://www.orienteering.org/datastandard/3.0}EventClassification
class EventClassification (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EventClassification')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 965, 2)
    _Documentation = None
EventClassification._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EventClassification, enum_prefix=None)
EventClassification.International = EventClassification._CF_enumeration.addEnumeration(unicode_value='International', tag='International')
EventClassification.National = EventClassification._CF_enumeration.addEnumeration(unicode_value='National', tag='National')
EventClassification.Regional = EventClassification._CF_enumeration.addEnumeration(unicode_value='Regional', tag='Regional')
EventClassification.Local = EventClassification._CF_enumeration.addEnumeration(unicode_value='Local', tag='Local')
EventClassification.Club = EventClassification._CF_enumeration.addEnumeration(unicode_value='Club', tag='Club')
EventClassification._InitializeFacetMap(EventClassification._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'EventClassification', EventClassification)
_module_typeBindings.EventClassification = EventClassification

# Atomic simple type: {http://www.orienteering.org/datastandard/3.0}RaceDiscipline
class RaceDiscipline (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RaceDiscipline')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 975, 2)
    _Documentation = None
RaceDiscipline._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RaceDiscipline, enum_prefix=None)
RaceDiscipline.Sprint = RaceDiscipline._CF_enumeration.addEnumeration(unicode_value='Sprint', tag='Sprint')
RaceDiscipline.Middle = RaceDiscipline._CF_enumeration.addEnumeration(unicode_value='Middle', tag='Middle')
RaceDiscipline.Long = RaceDiscipline._CF_enumeration.addEnumeration(unicode_value='Long', tag='Long')
RaceDiscipline.Ultralong = RaceDiscipline._CF_enumeration.addEnumeration(unicode_value='Ultralong', tag='Ultralong')
RaceDiscipline.Other = RaceDiscipline._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
RaceDiscipline._InitializeFacetMap(RaceDiscipline._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RaceDiscipline', RaceDiscipline)
_module_typeBindings.RaceDiscipline = RaceDiscipline

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 989, 10)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.Website = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Website', tag='Website')
STD_ANON_3.StartList = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='StartList', tag='StartList')
STD_ANON_3.ResultList = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='ResultList', tag='ResultList')
STD_ANON_3.Other = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1181, 6)
    _Documentation = None
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_4, enum_prefix=None)
STD_ANON_4.B = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='B', tag='B')
STD_ANON_4.F = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='F', tag='F')
STD_ANON_4.M = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='M', tag='M')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration)
_module_typeBindings.STD_ANON_4 = STD_ANON_4

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1237, 6)
    _Documentation = None
STD_ANON_5._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_5, enum_prefix=None)
STD_ANON_5.Default = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='Default', tag='Default')
STD_ANON_5.Unordered = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='Unordered', tag='Unordered')
STD_ANON_5.UnorderedNoTimes = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='UnorderedNoTimes', tag='UnorderedNoTimes')
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_enumeration)
_module_typeBindings.STD_ANON_5 = STD_ANON_5

# Atomic simple type: {http://www.orienteering.org/datastandard/3.0}EventClassStatus
class EventClassStatus (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """
        The status of the class.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EventClassStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1285, 2)
    _Documentation = '\n        The status of the class.\n      '
EventClassStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EventClassStatus, enum_prefix=None)
EventClassStatus.Normal = EventClassStatus._CF_enumeration.addEnumeration(unicode_value='Normal', tag='Normal')
EventClassStatus.Divided = EventClassStatus._CF_enumeration.addEnumeration(unicode_value='Divided', tag='Divided')
EventClassStatus.Joined = EventClassStatus._CF_enumeration.addEnumeration(unicode_value='Joined', tag='Joined')
EventClassStatus.Invalidated = EventClassStatus._CF_enumeration.addEnumeration(unicode_value='Invalidated', tag='Invalidated')
EventClassStatus.InvalidatedNoFee = EventClassStatus._CF_enumeration.addEnumeration(unicode_value='InvalidatedNoFee', tag='InvalidatedNoFee')
EventClassStatus._InitializeFacetMap(EventClassStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'EventClassStatus', EventClassStatus)
_module_typeBindings.EventClassStatus = EventClassStatus

# Atomic simple type: {http://www.orienteering.org/datastandard/3.0}RaceClassStatus
class RaceClassStatus (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """
        The status of a certain race in the class.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RaceClassStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1330, 2)
    _Documentation = '\n        The status of a certain race in the class.\n      '
RaceClassStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RaceClassStatus, enum_prefix=None)
RaceClassStatus.StartTimesNotAllocated = RaceClassStatus._CF_enumeration.addEnumeration(unicode_value='StartTimesNotAllocated', tag='StartTimesNotAllocated')
RaceClassStatus.StartTimesAllocated = RaceClassStatus._CF_enumeration.addEnumeration(unicode_value='StartTimesAllocated', tag='StartTimesAllocated')
RaceClassStatus.NotUsed = RaceClassStatus._CF_enumeration.addEnumeration(unicode_value='NotUsed', tag='NotUsed')
RaceClassStatus.Completed = RaceClassStatus._CF_enumeration.addEnumeration(unicode_value='Completed', tag='Completed')
RaceClassStatus.Invalidated = RaceClassStatus._CF_enumeration.addEnumeration(unicode_value='Invalidated', tag='Invalidated')
RaceClassStatus.InvalidatedNoFee = RaceClassStatus._CF_enumeration.addEnumeration(unicode_value='InvalidatedNoFee', tag='InvalidatedNoFee')
RaceClassStatus._InitializeFacetMap(RaceClassStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RaceClassStatus', RaceClassStatus)
_module_typeBindings.RaceClassStatus = RaceClassStatus

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1542, 6)
    _Documentation = None
STD_ANON_6._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_6, enum_prefix=None)
STD_ANON_6.Normal = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='Normal', tag='Normal')
STD_ANON_6.Late = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='Late', tag='Late')
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_enumeration)
_module_typeBindings.STD_ANON_6 = STD_ANON_6

# Atomic simple type: [anonymous]
class STD_ANON_7 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1881, 6)
    _Documentation = None
STD_ANON_7._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_7, enum_prefix=None)
STD_ANON_7.Normal = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='Normal', tag='Normal')
STD_ANON_7.EarlyStart = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='EarlyStart', tag='EarlyStart')
STD_ANON_7.LateStart = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='LateStart', tag='LateStart')
STD_ANON_7.SeparatedFrom = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='SeparatedFrom', tag='SeparatedFrom')
STD_ANON_7.GroupedWith = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='GroupedWith', tag='GroupedWith')
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_enumeration)
_module_typeBindings.STD_ANON_7 = STD_ANON_7

# Atomic simple type: [anonymous]
class STD_ANON_8 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2713, 16)
    _Documentation = None
STD_ANON_8._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_8, enum_prefix=None)
STD_ANON_8.Leg = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='Leg', tag='Leg')
STD_ANON_8.Course = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='Course', tag='Course')
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_enumeration)
_module_typeBindings.STD_ANON_8 = STD_ANON_8

# Atomic simple type: [anonymous]
class STD_ANON_9 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2746, 16)
    _Documentation = None
STD_ANON_9._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_9, enum_prefix=None)
STD_ANON_9.Leg = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='Leg', tag='Leg')
STD_ANON_9.Course = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='Course', tag='Course')
STD_ANON_9._InitializeFacetMap(STD_ANON_9._CF_enumeration)
_module_typeBindings.STD_ANON_9 = STD_ANON_9

# Atomic simple type: {http://www.orienteering.org/datastandard/3.0}ResultStatus
class ResultStatus (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """
        The result status of the person or team at the time of the result generation.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResultStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2903, 2)
    _Documentation = '\n        The result status of the person or team at the time of the result generation.\n      '
ResultStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ResultStatus, enum_prefix=None)
ResultStatus.OK = ResultStatus._CF_enumeration.addEnumeration(unicode_value='OK', tag='OK')
ResultStatus.Finished = ResultStatus._CF_enumeration.addEnumeration(unicode_value='Finished', tag='Finished')
ResultStatus.MissingPunch = ResultStatus._CF_enumeration.addEnumeration(unicode_value='MissingPunch', tag='MissingPunch')
ResultStatus.Disqualified = ResultStatus._CF_enumeration.addEnumeration(unicode_value='Disqualified', tag='Disqualified')
ResultStatus.DidNotFinish = ResultStatus._CF_enumeration.addEnumeration(unicode_value='DidNotFinish', tag='DidNotFinish')
ResultStatus.Active = ResultStatus._CF_enumeration.addEnumeration(unicode_value='Active', tag='Active')
ResultStatus.Inactive = ResultStatus._CF_enumeration.addEnumeration(unicode_value='Inactive', tag='Inactive')
ResultStatus.OverTime = ResultStatus._CF_enumeration.addEnumeration(unicode_value='OverTime', tag='OverTime')
ResultStatus.SportingWithdrawal = ResultStatus._CF_enumeration.addEnumeration(unicode_value='SportingWithdrawal', tag='SportingWithdrawal')
ResultStatus.NotCompeting = ResultStatus._CF_enumeration.addEnumeration(unicode_value='NotCompeting', tag='NotCompeting')
ResultStatus.Moved = ResultStatus._CF_enumeration.addEnumeration(unicode_value='Moved', tag='Moved')
ResultStatus.MovedUp = ResultStatus._CF_enumeration.addEnumeration(unicode_value='MovedUp', tag='MovedUp')
ResultStatus.DidNotStart = ResultStatus._CF_enumeration.addEnumeration(unicode_value='DidNotStart', tag='DidNotStart')
ResultStatus.DidNotEnter = ResultStatus._CF_enumeration.addEnumeration(unicode_value='DidNotEnter', tag='DidNotEnter')
ResultStatus.Cancelled = ResultStatus._CF_enumeration.addEnumeration(unicode_value='Cancelled', tag='Cancelled')
ResultStatus._InitializeFacetMap(ResultStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ResultStatus', ResultStatus)
_module_typeBindings.ResultStatus = ResultStatus

# Atomic simple type: [anonymous]
class STD_ANON_10 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3091, 6)
    _Documentation = None
STD_ANON_10._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_10, enum_prefix=None)
STD_ANON_10.OK = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='OK', tag='OK')
STD_ANON_10.Missing = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='Missing', tag='Missing')
STD_ANON_10.Additional = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='Additional', tag='Additional')
STD_ANON_10._InitializeFacetMap(STD_ANON_10._CF_enumeration)
_module_typeBindings.STD_ANON_10 = STD_ANON_10

# Atomic simple type: [anonymous]
class STD_ANON_11 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3451, 6)
    _Documentation = None
STD_ANON_11._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_11, enum_prefix=None)
STD_ANON_11.px = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='px', tag='px')
STD_ANON_11.mm = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='mm', tag='mm')
STD_ANON_11._InitializeFacetMap(STD_ANON_11._CF_enumeration)
_module_typeBindings.STD_ANON_11 = STD_ANON_11

# Atomic simple type: [anonymous]
class STD_ANON_12 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3970, 6)
    _Documentation = None
STD_ANON_12._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_12, enum_prefix=None)
STD_ANON_12.None_ = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='None', tag='None_')
STD_ANON_12.TapedRoute = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='TapedRoute', tag='TapedRoute')
STD_ANON_12.FunnelTapedRoute = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='FunnelTapedRoute', tag='FunnelTapedRoute')
STD_ANON_12.MandatoryCrossingPoint = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='MandatoryCrossingPoint', tag='MandatoryCrossingPoint')
STD_ANON_12.MandatoryOutOfBoundsAreaPassage = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='MandatoryOutOfBoundsAreaPassage', tag='MandatoryOutOfBoundsAreaPassage')
STD_ANON_12._InitializeFacetMap(STD_ANON_12._CF_enumeration)
_module_typeBindings.STD_ANON_12 = STD_ANON_12

# Atomic simple type: {http://www.orienteering.org/datastandard/3.0}ControlType
class ControlType (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """
        The type of a control: (ordinary) control, start, finish, crossing point or end of marked route.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ControlType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3990, 2)
    _Documentation = '\n        The type of a control: (ordinary) control, start, finish, crossing point or end of marked route.\n      '
ControlType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ControlType, enum_prefix=None)
ControlType.Control = ControlType._CF_enumeration.addEnumeration(unicode_value='Control', tag='Control')
ControlType.Start = ControlType._CF_enumeration.addEnumeration(unicode_value='Start', tag='Start')
ControlType.Finish = ControlType._CF_enumeration.addEnumeration(unicode_value='Finish', tag='Finish')
ControlType.CrossingPoint = ControlType._CF_enumeration.addEnumeration(unicode_value='CrossingPoint', tag='CrossingPoint')
ControlType.EndOfMarkedRoute = ControlType._CF_enumeration.addEnumeration(unicode_value='EndOfMarkedRoute', tag='EndOfMarkedRoute')
ControlType._InitializeFacetMap(ControlType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ControlType', ControlType)
_module_typeBindings.ControlType = ControlType

# Atomic simple type: [anonymous]
class STD_ANON_13 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4241, 10)
    _Documentation = None
STD_ANON_13._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_13, enum_prefix=None)
STD_ANON_13.PhoneNumber = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='PhoneNumber', tag='PhoneNumber')
STD_ANON_13.MobilePhoneNumber = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='MobilePhoneNumber', tag='MobilePhoneNumber')
STD_ANON_13.FaxNumber = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='FaxNumber', tag='FaxNumber')
STD_ANON_13.EmailAddress = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='EmailAddress', tag='EmailAddress')
STD_ANON_13.WebAddress = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='WebAddress', tag='WebAddress')
STD_ANON_13.Other = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
STD_ANON_13._InitializeFacetMap(STD_ANON_13._CF_enumeration)
_module_typeBindings.STD_ANON_13 = STD_ANON_13

# Complex type {http://www.orienteering.org/datastandard/3.0}BaseMessageElement with content type EMPTY
class BaseMessageElement (pyxb.binding.basis.complexTypeDefinition):
    """
        The base message element that all message elements extend.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BaseMessageElement')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 33, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute iofVersion uses Python identifier iofVersion
    __iofVersion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'iofVersion'), 'iofVersion', '__httpwww_orienteering_orgdatastandard3_0_BaseMessageElement_iofVersion', pyxb.binding.datatypes.string, fixed=True, unicode_default='3.0', required=True)
    __iofVersion._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 39, 4)
    __iofVersion._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 39, 4)
    
    iofVersion = property(__iofVersion.value, __iofVersion.set, None, '\n          The version of the IOF Interface Standard that the file conforms to.\n        ')

    
    # Attribute createTime uses Python identifier createTime
    __createTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'createTime'), 'createTime', '__httpwww_orienteering_orgdatastandard3_0_BaseMessageElement_createTime', pyxb.binding.datatypes.dateTime)
    __createTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 46, 4)
    __createTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 46, 4)
    
    createTime = property(__createTime.value, __createTime.set, None, '\n          The time when the file was created.\n        ')

    
    # Attribute creator uses Python identifier creator
    __creator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'creator'), 'creator', '__httpwww_orienteering_orgdatastandard3_0_BaseMessageElement_creator', pyxb.binding.datatypes.string)
    __creator._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 53, 4)
    __creator._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 53, 4)
    
    creator = property(__creator.value, __creator.set, None, '\n          The name of the software that created the file.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __iofVersion.name() : __iofVersion,
        __createTime.name() : __createTime,
        __creator.name() : __creator
    })
_module_typeBindings.BaseMessageElement = BaseMessageElement
Namespace.addCategoryObject('typeBinding', 'BaseMessageElement', BaseMessageElement)


# Complex type {http://www.orienteering.org/datastandard/3.0}Id with content type SIMPLE
class Id (pyxb.binding.basis.complexTypeDefinition):
    """
        Identifier element, used extensively. The id should be known and common for both systems taking part in the data exchange.
      """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Id')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 432, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_orienteering_orgdatastandard3_0_Id_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 440, 8)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 440, 8)
    
    type = property(__type.value, __type.set, None, '\n              The issuer of the identity, e.g. World Ranking List.\n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.Id = Id
Namespace.addCategoryObject('typeBinding', 'Id', Id)


# Complex type {http://www.orienteering.org/datastandard/3.0}PersonName with content type ELEMENT_ONLY
class PersonName (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.orienteering.org/datastandard/3.0}PersonName with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PersonName')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 495, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Family uses Python identifier Family
    __Family = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Family'), 'Family', '__httpwww_orienteering_orgdatastandard3_0_PersonName_httpwww_orienteering_orgdatastandard3_0Family', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 497, 6), )

    
    Family = property(__Family.value, __Family.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Given uses Python identifier Given
    __Given = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Given'), 'Given', '__httpwww_orienteering_orgdatastandard3_0_PersonName_httpwww_orienteering_orgdatastandard3_0Given', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 498, 6), )

    
    Given = property(__Given.value, __Given.set, None, None)

    _ElementMap.update({
        __Family.name() : __Family,
        __Given.name() : __Given
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PersonName = PersonName
Namespace.addCategoryObject('typeBinding', 'PersonName', PersonName)


# Complex type {http://www.orienteering.org/datastandard/3.0}Competitor with content type ELEMENT_ONLY
class Competitor (pyxb.binding.basis.complexTypeDefinition):
    """
        Represents information about a person in a competition context, i.e. including organisation and control card.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Competitor')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 502, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Person uses Python identifier Person
    __Person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Person'), 'Person', '__httpwww_orienteering_orgdatastandard3_0_Competitor_httpwww_orienteering_orgdatastandard3_0Person', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 509, 6), )

    
    Person = property(__Person.value, __Person.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Organisation uses Python identifier Organisation
    __Organisation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), 'Organisation', '__httpwww_orienteering_orgdatastandard3_0_Competitor_httpwww_orienteering_orgdatastandard3_0Organisation', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 510, 6), )

    
    Organisation = property(__Organisation.value, __Organisation.set, None, '\n            The organisations that the person is member of.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ControlCard uses Python identifier ControlCard
    __ControlCard = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ControlCard'), 'ControlCard', '__httpwww_orienteering_orgdatastandard3_0_Competitor_httpwww_orienteering_orgdatastandard3_0ControlCard', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 517, 6), )

    
    ControlCard = property(__ControlCard.value, __ControlCard.set, None, '\n            The default control cards of the competitor.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Class uses Python identifier Class
    __Class = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Class'), 'Class', '__httpwww_orienteering_orgdatastandard3_0_Competitor_httpwww_orienteering_orgdatastandard3_0Class', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 524, 6), )

    
    Class = property(__Class.value, __Class.set, None, '\n            The default classes of the competitor.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Score uses Python identifier Score
    __Score = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Score'), 'Score', '__httpwww_orienteering_orgdatastandard3_0_Competitor_httpwww_orienteering_orgdatastandard3_0Score', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 531, 6), )

    
    Score = property(__Score.value, __Score.set, None, '\n            Any scores, e.g. ranking scores, for the person.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_Competitor_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 538, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_Competitor_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 546, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 546, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __Person.name() : __Person,
        __Organisation.name() : __Organisation,
        __ControlCard.name() : __ControlCard,
        __Class.name() : __Class,
        __Score.name() : __Score,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.Competitor = Competitor
Namespace.addCategoryObject('typeBinding', 'Competitor', Competitor)


# Complex type {http://www.orienteering.org/datastandard/3.0}ControlCard with content type SIMPLE
class ControlCard (pyxb.binding.basis.complexTypeDefinition):
    """
        The unique identifier of the control card, i.e. card number.
      """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ControlCard')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 549, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute punchingSystem uses Python identifier punchingSystem
    __punchingSystem = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'punchingSystem'), 'punchingSystem', '__httpwww_orienteering_orgdatastandard3_0_ControlCard_punchingSystem', pyxb.binding.datatypes.string)
    __punchingSystem._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 557, 8)
    __punchingSystem._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 557, 8)
    
    punchingSystem = property(__punchingSystem.value, __punchingSystem.set, None, "\n              The manufacturer of the punching system, e.g. 'SI' or 'Emit'.\n            ")

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_ControlCard_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 564, 8)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 564, 8)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __punchingSystem.name() : __punchingSystem,
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.ControlCard = ControlCard
Namespace.addCategoryObject('typeBinding', 'ControlCard', ControlCard)


# Complex type {http://www.orienteering.org/datastandard/3.0}Score with content type SIMPLE
class Score (pyxb.binding.basis.complexTypeDefinition):
    """
        The score earned in an event for some purpose, e.g. a ranking list. The 'type' attribute is used to specify which purpose.
      """
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Score')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 569, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.double
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_orienteering_orgdatastandard3_0_Score_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 577, 8)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 577, 8)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.Score = Score
Namespace.addCategoryObject('typeBinding', 'Score', Score)


# Complex type {http://www.orienteering.org/datastandard/3.0}Role with content type ELEMENT_ONLY
class Role (pyxb.binding.basis.complexTypeDefinition):
    """
        A role defines a connection between a person and some kind of task, responsibility or engagement, e.g. being a course setter at an event.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Role')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 674, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Person uses Python identifier Person
    __Person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Person'), 'Person', '__httpwww_orienteering_orgdatastandard3_0_Role_httpwww_orienteering_orgdatastandard3_0Person', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 681, 6), )

    
    Person = property(__Person.value, __Person.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_orienteering_orgdatastandard3_0_Role_type', pyxb.binding.datatypes.string, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 683, 4)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 683, 4)
    
    type = property(__type.value, __type.set, None, '\n          The type of role that the person has.\n        ')

    _ElementMap.update({
        __Person.name() : __Person
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.Role = Role
Namespace.addCategoryObject('typeBinding', 'Role', Role)


# Complex type {http://www.orienteering.org/datastandard/3.0}Event with content type ELEMENT_ONLY
class Event (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.orienteering.org/datastandard/3.0}Event with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Event')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 692, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__httpwww_orienteering_orgdatastandard3_0_Event_httpwww_orienteering_orgdatastandard3_0Id', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 694, 6), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httpwww_orienteering_orgdatastandard3_0_Event_httpwww_orienteering_orgdatastandard3_0Name', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 695, 6), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}StartTime uses Python identifier StartTime
    __StartTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartTime'), 'StartTime', '__httpwww_orienteering_orgdatastandard3_0_Event_httpwww_orienteering_orgdatastandard3_0StartTime', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 696, 6), )

    
    StartTime = property(__StartTime.value, __StartTime.set, None, '\n            The start time for the first starting competitor of the event. If the event contains multiple races, this is the start time for the first starting competitor of the first race.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}EndTime uses Python identifier EndTime
    __EndTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndTime'), 'EndTime', '__httpwww_orienteering_orgdatastandard3_0_Event_httpwww_orienteering_orgdatastandard3_0EndTime', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 703, 6), )

    
    EndTime = property(__EndTime.value, __EndTime.set, None, '\n            The expected finish time for the last finishing competitor of the event. If the event contains multiple races, this is the expected finish time for the last finishing competitor of the last race.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Status uses Python identifier Status
    __Status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Status'), 'Status', '__httpwww_orienteering_orgdatastandard3_0_Event_httpwww_orienteering_orgdatastandard3_0Status', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 710, 6), )

    
    Status = property(__Status.value, __Status.set, None, '\n            The status of the event. If the event is a multi-race event, and status is set per race, use the Status element of the Race element.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Classification uses Python identifier Classification
    __Classification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Classification'), 'Classification', '__httpwww_orienteering_orgdatastandard3_0_Event_httpwww_orienteering_orgdatastandard3_0Classification', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 717, 6), )

    
    Classification = property(__Classification.value, __Classification.set, None, '\n            The classification or level of the event. If the event is a multi-race event, and classification is set per race, use the Classification element of the Race element.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Form uses Python identifier Form
    __Form = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Form'), 'Form', '__httpwww_orienteering_orgdatastandard3_0_Event_httpwww_orienteering_orgdatastandard3_0Form', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 724, 6), )

    
    Form = property(__Form.value, __Form.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Organiser uses Python identifier Organiser
    __Organiser = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Organiser'), 'Organiser', '__httpwww_orienteering_orgdatastandard3_0_Event_httpwww_orienteering_orgdatastandard3_0Organiser', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 725, 6), )

    
    Organiser = property(__Organiser.value, __Organiser.set, None, '\n            The organisations that organise the event.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Official uses Python identifier Official
    __Official = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Official'), 'Official', '__httpwww_orienteering_orgdatastandard3_0_Event_httpwww_orienteering_orgdatastandard3_0Official', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 732, 6), )

    
    Official = property(__Official.value, __Official.set, None, '\n            The main officials of the event, e.g. course setter and event president.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Class uses Python identifier Class
    __Class = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Class'), 'Class', '__httpwww_orienteering_orgdatastandard3_0_Event_httpwww_orienteering_orgdatastandard3_0Class', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 739, 6), )

    
    Class = property(__Class.value, __Class.set, None, '\n            The classes that are available at the event.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Race uses Python identifier Race
    __Race = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Race'), 'Race', '__httpwww_orienteering_orgdatastandard3_0_Event_httpwww_orienteering_orgdatastandard3_0Race', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 746, 6), )

    
    Race = property(__Race.value, __Race.set, None, '\n            An event consists of a number of races. The number is equal to the number of times a competitor should start. Most events contain a single race, and this elemend could then be omitted.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}EntryReceiver uses Python identifier EntryReceiver
    __EntryReceiver = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EntryReceiver'), 'EntryReceiver', '__httpwww_orienteering_orgdatastandard3_0_Event_httpwww_orienteering_orgdatastandard3_0EntryReceiver', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 753, 6), )

    
    EntryReceiver = property(__EntryReceiver.value, __EntryReceiver.set, None, '\n            Address and contact information to the person or organisation which registers the entries for the event.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Service uses Python identifier Service
    __Service = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Service'), 'Service', '__httpwww_orienteering_orgdatastandard3_0_Event_httpwww_orienteering_orgdatastandard3_0Service', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 760, 6), )

    
    Service = property(__Service.value, __Service.set, None, '\n            The services available for the event, e.g. accomodation and transport.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Account uses Python identifier Account
    __Account = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Account'), 'Account', '__httpwww_orienteering_orgdatastandard3_0_Event_httpwww_orienteering_orgdatastandard3_0Account', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 767, 6), )

    
    Account = property(__Account.value, __Account.set, None, '\n            The bank account for the event.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'URL'), 'URL', '__httpwww_orienteering_orgdatastandard3_0_Event_httpwww_orienteering_orgdatastandard3_0URL', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 774, 6), )

    
    URL = property(__URL.value, __URL.set, None, '\n            URLs to various types of additional information regarding the event, e.g. event website or result list.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Information uses Python identifier Information
    __Information = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Information'), 'Information', '__httpwww_orienteering_orgdatastandard3_0_Event_httpwww_orienteering_orgdatastandard3_0Information', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 781, 6), )

    
    Information = property(__Information.value, __Information.set, None, '\n            Presents arbitrary data about the event, e.g. "Accommodation", "Local Attractions", and so on. Information present here should be defined well in advance of the event, in contrast to the \'News\' element.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Schedule uses Python identifier Schedule
    __Schedule = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Schedule'), 'Schedule', '__httpwww_orienteering_orgdatastandard3_0_Event_httpwww_orienteering_orgdatastandard3_0Schedule', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 788, 6), )

    
    Schedule = property(__Schedule.value, __Schedule.set, None, '\n            Defines the schedule of events that comprise the entire orienteering event, e.g. entry deadlines, banquet and social events, and awards ceremonies.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}News uses Python identifier News
    __News = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'News'), 'News', '__httpwww_orienteering_orgdatastandard3_0_Event_httpwww_orienteering_orgdatastandard3_0News', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 795, 6), )

    
    News = property(__News.value, __News.set, None, '\n            Presents "last minute information" about the event.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_Event_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 802, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_Event_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 810, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 810, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __Name.name() : __Name,
        __StartTime.name() : __StartTime,
        __EndTime.name() : __EndTime,
        __Status.name() : __Status,
        __Classification.name() : __Classification,
        __Form.name() : __Form,
        __Organiser.name() : __Organiser,
        __Official.name() : __Official,
        __Class.name() : __Class,
        __Race.name() : __Race,
        __EntryReceiver.name() : __EntryReceiver,
        __Service.name() : __Service,
        __Account.name() : __Account,
        __URL.name() : __URL,
        __Information.name() : __Information,
        __Schedule.name() : __Schedule,
        __News.name() : __News,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.Event = Event
Namespace.addCategoryObject('typeBinding', 'Event', Event)


# Complex type {http://www.orienteering.org/datastandard/3.0}EntryReceiver with content type ELEMENT_ONLY
class EntryReceiver (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.orienteering.org/datastandard/3.0}EntryReceiver with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EntryReceiver')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 813, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Address uses Python identifier Address
    __Address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Address'), 'Address', '__httpwww_orienteering_orgdatastandard3_0_EntryReceiver_httpwww_orienteering_orgdatastandard3_0Address', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 815, 6), )

    
    Address = property(__Address.value, __Address.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Contact uses Python identifier Contact
    __Contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Contact'), 'Contact', '__httpwww_orienteering_orgdatastandard3_0_EntryReceiver_httpwww_orienteering_orgdatastandard3_0Contact', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 816, 6), )

    
    Contact = property(__Contact.value, __Contact.set, None, None)

    _ElementMap.update({
        __Address.name() : __Address,
        __Contact.name() : __Contact
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.EntryReceiver = EntryReceiver
Namespace.addCategoryObject('typeBinding', 'EntryReceiver', EntryReceiver)


# Complex type {http://www.orienteering.org/datastandard/3.0}Race with content type ELEMENT_ONLY
class Race (pyxb.binding.basis.complexTypeDefinition):
    """
        An event consists of a number of races. The number is equal to the number of times a competitor should start.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Race')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 875, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}RaceNumber uses Python identifier RaceNumber
    __RaceNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RaceNumber'), 'RaceNumber', '__httpwww_orienteering_orgdatastandard3_0_Race_httpwww_orienteering_orgdatastandard3_0RaceNumber', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 882, 6), )

    
    RaceNumber = property(__RaceNumber.value, __RaceNumber.set, None, '\n            The ordinal number of the race in the multi-race event, starting at 1.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httpwww_orienteering_orgdatastandard3_0_Race_httpwww_orienteering_orgdatastandard3_0Name', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 889, 6), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}StartTime uses Python identifier StartTime
    __StartTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartTime'), 'StartTime', '__httpwww_orienteering_orgdatastandard3_0_Race_httpwww_orienteering_orgdatastandard3_0StartTime', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 890, 6), )

    
    StartTime = property(__StartTime.value, __StartTime.set, None, '\n            The start time for the first starting competitor of the race.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}EndTime uses Python identifier EndTime
    __EndTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndTime'), 'EndTime', '__httpwww_orienteering_orgdatastandard3_0_Race_httpwww_orienteering_orgdatastandard3_0EndTime', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 897, 6), )

    
    EndTime = property(__EndTime.value, __EndTime.set, None, '\n            The time when the finish closes.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Status uses Python identifier Status
    __Status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Status'), 'Status', '__httpwww_orienteering_orgdatastandard3_0_Race_httpwww_orienteering_orgdatastandard3_0Status', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 904, 6), )

    
    Status = property(__Status.value, __Status.set, None, '\n            The status of the race. This element overrides the Status element of the parent Event element.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Classification uses Python identifier Classification
    __Classification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Classification'), 'Classification', '__httpwww_orienteering_orgdatastandard3_0_Race_httpwww_orienteering_orgdatastandard3_0Classification', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 911, 6), )

    
    Classification = property(__Classification.value, __Classification.set, None, '\n            The classification or level of the race. This element overrides the Classification element of the parent Event element.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Position uses Python identifier Position
    __Position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Position'), 'Position', '__httpwww_orienteering_orgdatastandard3_0_Race_httpwww_orienteering_orgdatastandard3_0Position', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 918, 6), )

    
    Position = property(__Position.value, __Position.set, None, '\n            The geographical location of the arena.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Discipline uses Python identifier Discipline
    __Discipline = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Discipline'), 'Discipline', '__httpwww_orienteering_orgdatastandard3_0_Race_httpwww_orienteering_orgdatastandard3_0Discipline', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 925, 6), )

    
    Discipline = property(__Discipline.value, __Discipline.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Organiser uses Python identifier Organiser
    __Organiser = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Organiser'), 'Organiser', '__httpwww_orienteering_orgdatastandard3_0_Race_httpwww_orienteering_orgdatastandard3_0Organiser', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 926, 6), )

    
    Organiser = property(__Organiser.value, __Organiser.set, None, '\n            The organisations that organise the event.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Official uses Python identifier Official
    __Official = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Official'), 'Official', '__httpwww_orienteering_orgdatastandard3_0_Race_httpwww_orienteering_orgdatastandard3_0Official', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 933, 6), )

    
    Official = property(__Official.value, __Official.set, None, '\n            The main officials of the event, e.g. course setter and event president.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Service uses Python identifier Service
    __Service = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Service'), 'Service', '__httpwww_orienteering_orgdatastandard3_0_Race_httpwww_orienteering_orgdatastandard3_0Service', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 940, 6), )

    
    Service = property(__Service.value, __Service.set, None, '\n            The services available for the race, e.g. accomodation and transport.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'URL'), 'URL', '__httpwww_orienteering_orgdatastandard3_0_Race_httpwww_orienteering_orgdatastandard3_0URL', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 947, 6), )

    
    URL = property(__URL.value, __URL.set, None, '\n            URLs to various types of additional information regarding the event, e.g. event website or result list.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_Race_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 954, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_Race_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 962, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 962, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __RaceNumber.name() : __RaceNumber,
        __Name.name() : __Name,
        __StartTime.name() : __StartTime,
        __EndTime.name() : __EndTime,
        __Status.name() : __Status,
        __Classification.name() : __Classification,
        __Position.name() : __Position,
        __Discipline.name() : __Discipline,
        __Organiser.name() : __Organiser,
        __Official.name() : __Official,
        __Service.name() : __Service,
        __URL.name() : __URL,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.Race = Race
Namespace.addCategoryObject('typeBinding', 'Race', Race)


# Complex type {http://www.orienteering.org/datastandard/3.0}Schedule with content type ELEMENT_ONLY
class Schedule (pyxb.binding.basis.complexTypeDefinition):
    """
        Defines the schedule of sub-events that comprise the entire orienteering event, e.g. banquets, social events and awards ceremonies.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Schedule')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1002, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}StartTime uses Python identifier StartTime
    __StartTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartTime'), 'StartTime', '__httpwww_orienteering_orgdatastandard3_0_Schedule_httpwww_orienteering_orgdatastandard3_0StartTime', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1009, 6), )

    
    StartTime = property(__StartTime.value, __StartTime.set, None, '\n            The start time of the sub-event.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}EndTime uses Python identifier EndTime
    __EndTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndTime'), 'EndTime', '__httpwww_orienteering_orgdatastandard3_0_Schedule_httpwww_orienteering_orgdatastandard3_0EndTime', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1016, 6), )

    
    EndTime = property(__EndTime.value, __EndTime.set, None, '\n            The end time of the sub-event.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httpwww_orienteering_orgdatastandard3_0_Schedule_httpwww_orienteering_orgdatastandard3_0Name', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1023, 6), )

    
    Name = property(__Name.value, __Name.set, None, '\n            The name or title of the sub-event.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Venue uses Python identifier Venue
    __Venue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Venue'), 'Venue', '__httpwww_orienteering_orgdatastandard3_0_Schedule_httpwww_orienteering_orgdatastandard3_0Venue', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1030, 6), )

    
    Venue = property(__Venue.value, __Venue.set, None, '\n            The name of the place where the sub-event occurs.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Position uses Python identifier Position
    __Position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Position'), 'Position', '__httpwww_orienteering_orgdatastandard3_0_Schedule_httpwww_orienteering_orgdatastandard3_0Position', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1037, 6), )

    
    Position = property(__Position.value, __Position.set, None, '\n            The geographical position of the sub-event.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Details uses Python identifier Details
    __Details = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Details'), 'Details', '__httpwww_orienteering_orgdatastandard3_0_Schedule_httpwww_orienteering_orgdatastandard3_0Details', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1044, 6), )

    
    Details = property(__Details.value, __Details.set, None, '\n            Any extra information about the sub-event.\n          ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_Schedule_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1052, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1052, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __StartTime.name() : __StartTime,
        __EndTime.name() : __EndTime,
        __Name.name() : __Name,
        __Venue.name() : __Venue,
        __Position.name() : __Position,
        __Details.name() : __Details
    })
    _AttributeMap.update({
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.Schedule = Schedule
Namespace.addCategoryObject('typeBinding', 'Schedule', Schedule)


# Complex type {http://www.orienteering.org/datastandard/3.0}InformationItem with content type ELEMENT_ONLY
class InformationItem (pyxb.binding.basis.complexTypeDefinition):
    """
        Defines a general-purpose information object containing a title and content.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InformationItem')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1055, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Title uses Python identifier Title
    __Title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Title'), 'Title', '__httpwww_orienteering_orgdatastandard3_0_InformationItem_httpwww_orienteering_orgdatastandard3_0Title', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1062, 6), )

    
    Title = property(__Title.value, __Title.set, None, '\n            A short summary of the information.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Content uses Python identifier Content
    __Content = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Content'), 'Content', '__httpwww_orienteering_orgdatastandard3_0_InformationItem_httpwww_orienteering_orgdatastandard3_0Content', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1069, 6), )

    
    Content = property(__Content.value, __Content.set, None, '\n            The information in detailed form.\n          ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_InformationItem_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1077, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1077, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __Title.name() : __Title,
        __Content.name() : __Content
    })
    _AttributeMap.update({
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.InformationItem = InformationItem
Namespace.addCategoryObject('typeBinding', 'InformationItem', InformationItem)


# Complex type {http://www.orienteering.org/datastandard/3.0}ClassType with content type ELEMENT_ONLY
class ClassType (pyxb.binding.basis.complexTypeDefinition):
    """
        Defines a class type, which is used to group classes in categories.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ClassType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1266, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__httpwww_orienteering_orgdatastandard3_0_ClassType_httpwww_orienteering_orgdatastandard3_0Id', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1273, 6), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httpwww_orienteering_orgdatastandard3_0_ClassType_httpwww_orienteering_orgdatastandard3_0Name', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1274, 6), )

    
    Name = property(__Name.value, __Name.set, None, '\n            The name of the class type.\n          ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_ClassType_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1282, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1282, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __Name.name() : __Name
    })
    _AttributeMap.update({
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.ClassType = ClassType
Namespace.addCategoryObject('typeBinding', 'ClassType', ClassType)


# Complex type {http://www.orienteering.org/datastandard/3.0}RaceClass with content type ELEMENT_ONLY
class RaceClass (pyxb.binding.basis.complexTypeDefinition):
    """
        Information about a class with respect to a race.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RaceClass')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1382, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}PunchingSystem uses Python identifier PunchingSystem
    __PunchingSystem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PunchingSystem'), 'PunchingSystem', '__httpwww_orienteering_orgdatastandard3_0_RaceClass_httpwww_orienteering_orgdatastandard3_0PunchingSystem', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1389, 6), )

    
    PunchingSystem = property(__PunchingSystem.value, __PunchingSystem.set, None, '\n            The punching system used for the class at the race. Multiple punching systems can be specified, e.g. one for punch checking and another for timing.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}TeamFee uses Python identifier TeamFee
    __TeamFee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TeamFee'), 'TeamFee', '__httpwww_orienteering_orgdatastandard3_0_RaceClass_httpwww_orienteering_orgdatastandard3_0TeamFee', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1396, 6), )

    
    TeamFee = property(__TeamFee.value, __TeamFee.set, None, '\n            The entry fees for a team as a whole taking part in this class. Use the Fee element to specify a fee for an individual competitor in the team. Use the TeamFee subelement of the Class element to specify a fee on event level.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Fee uses Python identifier Fee
    __Fee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Fee'), 'Fee', '__httpwww_orienteering_orgdatastandard3_0_RaceClass_httpwww_orienteering_orgdatastandard3_0Fee', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1403, 6), )

    
    Fee = property(__Fee.value, __Fee.set, None, '\n            The entry fees for an individual competitor taking part in the race class. Use the TeamFee element to specify a fee for the team as a whole. Use the Fee subelement of the Class element to specify a fee on event level.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}FirstStart uses Python identifier FirstStart
    __FirstStart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FirstStart'), 'FirstStart', '__httpwww_orienteering_orgdatastandard3_0_RaceClass_httpwww_orienteering_orgdatastandard3_0FirstStart', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1410, 6), )

    
    FirstStart = property(__FirstStart.value, __FirstStart.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Status uses Python identifier Status
    __Status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Status'), 'Status', '__httpwww_orienteering_orgdatastandard3_0_RaceClass_httpwww_orienteering_orgdatastandard3_0Status', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1411, 6), )

    
    Status = property(__Status.value, __Status.set, None, '\n            The status of the race, e.g. if results should be considered invalid due to misplaced constrols.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Course uses Python identifier Course
    __Course = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Course'), 'Course', '__httpwww_orienteering_orgdatastandard3_0_RaceClass_httpwww_orienteering_orgdatastandard3_0Course', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1418, 6), )

    
    Course = property(__Course.value, __Course.set, None, '\n            The courses assigned to this class. For a mass-start event or a relay event, there are usually multiple courses per class due to the usage of spreading methods.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}OnlineControl uses Python identifier OnlineControl
    __OnlineControl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OnlineControl'), 'OnlineControl', '__httpwww_orienteering_orgdatastandard3_0_RaceClass_httpwww_orienteering_orgdatastandard3_0OnlineControl', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1425, 6), )

    
    OnlineControl = property(__OnlineControl.value, __OnlineControl.set, None, '\n            The controls that are online controls for this class.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_RaceClass_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1432, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute raceNumber uses Python identifier raceNumber
    __raceNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'raceNumber'), 'raceNumber', '__httpwww_orienteering_orgdatastandard3_0_RaceClass_raceNumber', pyxb.binding.datatypes.integer)
    __raceNumber._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1440, 4)
    __raceNumber._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1440, 4)
    
    raceNumber = property(__raceNumber.value, __raceNumber.set, None, '\n          The ordinal number of the race that the information belongs to for a multi-race event, starting at 1.\n        ')

    
    # Attribute maxNumberOfCompetitors uses Python identifier maxNumberOfCompetitors
    __maxNumberOfCompetitors = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'maxNumberOfCompetitors'), 'maxNumberOfCompetitors', '__httpwww_orienteering_orgdatastandard3_0_RaceClass_maxNumberOfCompetitors', pyxb.binding.datatypes.integer)
    __maxNumberOfCompetitors._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1447, 4)
    __maxNumberOfCompetitors._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1447, 4)
    
    maxNumberOfCompetitors = property(__maxNumberOfCompetitors.value, __maxNumberOfCompetitors.set, None, '\n          The maximum number of competitors that are allowed to take part in the race class. A competitor corresponds to a person (if an individual event) or a team (if a team or relay event). This attribute overrides the maxNumberOfCompetitors attribute in the Class element.\n        ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_RaceClass_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1454, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1454, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __PunchingSystem.name() : __PunchingSystem,
        __TeamFee.name() : __TeamFee,
        __Fee.name() : __Fee,
        __FirstStart.name() : __FirstStart,
        __Status.name() : __Status,
        __Course.name() : __Course,
        __OnlineControl.name() : __OnlineControl,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __raceNumber.name() : __raceNumber,
        __maxNumberOfCompetitors.name() : __maxNumberOfCompetitors,
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.RaceClass = RaceClass
Namespace.addCategoryObject('typeBinding', 'RaceClass', RaceClass)


# Complex type {http://www.orienteering.org/datastandard/3.0}AssignedFee with content type ELEMENT_ONLY
class AssignedFee (pyxb.binding.basis.complexTypeDefinition):
    """
        Contains information about a fee that has been assigned to a competitor or a team, and the amount that has been paid.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AssignedFee')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1564, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Fee uses Python identifier Fee
    __Fee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Fee'), 'Fee', '__httpwww_orienteering_orgdatastandard3_0_AssignedFee_httpwww_orienteering_orgdatastandard3_0Fee', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1571, 6), )

    
    Fee = property(__Fee.value, __Fee.set, None, '\n            The fee that has been assigned to the competitor or the team.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}PaidAmount uses Python identifier PaidAmount
    __PaidAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PaidAmount'), 'PaidAmount', '__httpwww_orienteering_orgdatastandard3_0_AssignedFee_httpwww_orienteering_orgdatastandard3_0PaidAmount', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1578, 6), )

    
    PaidAmount = property(__PaidAmount.value, __PaidAmount.set, None, '\n            The amount that has been paid, optionally including currency code.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_AssignedFee_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1585, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_AssignedFee_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1593, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1593, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __Fee.name() : __Fee,
        __PaidAmount.name() : __PaidAmount,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.AssignedFee = AssignedFee
Namespace.addCategoryObject('typeBinding', 'AssignedFee', AssignedFee)


# Complex type {http://www.orienteering.org/datastandard/3.0}Amount with content type SIMPLE
class Amount (pyxb.binding.basis.complexTypeDefinition):
    """
        Defines a monetary amount.
      """
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Amount')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1596, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.decimal
    
    # Attribute currency uses Python identifier currency
    __currency = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'currency'), 'currency', '__httpwww_orienteering_orgdatastandard3_0_Amount_currency', pyxb.binding.datatypes.string)
    __currency._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1604, 8)
    __currency._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1604, 8)
    
    currency = property(__currency.value, __currency.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __currency.name() : __currency
    })
_module_typeBindings.Amount = Amount
Namespace.addCategoryObject('typeBinding', 'Amount', Amount)


# Complex type {http://www.orienteering.org/datastandard/3.0}PersonEntry with content type ELEMENT_ONLY
class PersonEntry (pyxb.binding.basis.complexTypeDefinition):
    """
        Defines an event entry for a person.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PersonEntry')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1609, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__httpwww_orienteering_orgdatastandard3_0_PersonEntry_httpwww_orienteering_orgdatastandard3_0Id', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1616, 6), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Person uses Python identifier Person
    __Person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Person'), 'Person', '__httpwww_orienteering_orgdatastandard3_0_PersonEntry_httpwww_orienteering_orgdatastandard3_0Person', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1617, 6), )

    
    Person = property(__Person.value, __Person.set, None, '\n            The person that is entered.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Organisation uses Python identifier Organisation
    __Organisation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), 'Organisation', '__httpwww_orienteering_orgdatastandard3_0_PersonEntry_httpwww_orienteering_orgdatastandard3_0Organisation', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1624, 6), )

    
    Organisation = property(__Organisation.value, __Organisation.set, None, '\n            The organisation that the person represents at the event.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ControlCard uses Python identifier ControlCard
    __ControlCard = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ControlCard'), 'ControlCard', '__httpwww_orienteering_orgdatastandard3_0_PersonEntry_httpwww_orienteering_orgdatastandard3_0ControlCard', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1631, 6), )

    
    ControlCard = property(__ControlCard.value, __ControlCard.set, None, '\n            Information about the control cards (punching cards) that the person uses at the event. Multiple control cards can be specified, e.g. one for punch checking and another for timing.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Score uses Python identifier Score
    __Score = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Score'), 'Score', '__httpwww_orienteering_orgdatastandard3_0_PersonEntry_httpwww_orienteering_orgdatastandard3_0Score', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1638, 6), )

    
    Score = property(__Score.value, __Score.set, None, '\n            Any score that is submitted together with the entry, e.g. World Ranking points.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Class uses Python identifier Class
    __Class = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Class'), 'Class', '__httpwww_orienteering_orgdatastandard3_0_PersonEntry_httpwww_orienteering_orgdatastandard3_0Class', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1645, 6), )

    
    Class = property(__Class.value, __Class.set, None, '\n            The class(es) the person wants to take part in. Multiple classes may be provided in order of preference in scenarios where the number of competitors are limited in some classes.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}RaceNumber uses Python identifier RaceNumber
    __RaceNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RaceNumber'), 'RaceNumber', '__httpwww_orienteering_orgdatastandard3_0_PersonEntry_httpwww_orienteering_orgdatastandard3_0RaceNumber', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1652, 6), )

    
    RaceNumber = property(__RaceNumber.value, __RaceNumber.set, None, '\n            The ordinal numbers of the races that the person is taking part in, starting at 1. If not specified, the person takes part in all races.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}AssignedFee uses Python identifier AssignedFee
    __AssignedFee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee'), 'AssignedFee', '__httpwww_orienteering_orgdatastandard3_0_PersonEntry_httpwww_orienteering_orgdatastandard3_0AssignedFee', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1659, 6), )

    
    AssignedFee = property(__AssignedFee.value, __AssignedFee.set, None, '\n            The fees that the person has to pay when entering the event. In a multi-race event, there is usually one element for each race.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ServiceRequest uses Python identifier ServiceRequest
    __ServiceRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest'), 'ServiceRequest', '__httpwww_orienteering_orgdatastandard3_0_PersonEntry_httpwww_orienteering_orgdatastandard3_0ServiceRequest', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1666, 6), )

    
    ServiceRequest = property(__ServiceRequest.value, __ServiceRequest.set, None, '\n            Defines the services requested by the person.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}StartTimeAllocationRequest uses Python identifier StartTimeAllocationRequest
    __StartTimeAllocationRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartTimeAllocationRequest'), 'StartTimeAllocationRequest', '__httpwww_orienteering_orgdatastandard3_0_PersonEntry_httpwww_orienteering_orgdatastandard3_0StartTimeAllocationRequest', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1673, 6), )

    
    StartTimeAllocationRequest = property(__StartTimeAllocationRequest.value, __StartTimeAllocationRequest.set, None, '\n            Any special preferences regarding start time that has to be taken into consideration when making the start list draw.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}EntryTime uses Python identifier EntryTime
    __EntryTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EntryTime'), 'EntryTime', '__httpwww_orienteering_orgdatastandard3_0_PersonEntry_httpwww_orienteering_orgdatastandard3_0EntryTime', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1680, 6), )

    
    EntryTime = property(__EntryTime.value, __EntryTime.set, None, '\n            The time when the entry was first submitted.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_PersonEntry_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1687, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_PersonEntry_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1695, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1695, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __Person.name() : __Person,
        __Organisation.name() : __Organisation,
        __ControlCard.name() : __ControlCard,
        __Score.name() : __Score,
        __Class.name() : __Class,
        __RaceNumber.name() : __RaceNumber,
        __AssignedFee.name() : __AssignedFee,
        __ServiceRequest.name() : __ServiceRequest,
        __StartTimeAllocationRequest.name() : __StartTimeAllocationRequest,
        __EntryTime.name() : __EntryTime,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.PersonEntry = PersonEntry
Namespace.addCategoryObject('typeBinding', 'PersonEntry', PersonEntry)


# Complex type {http://www.orienteering.org/datastandard/3.0}TeamEntry with content type ELEMENT_ONLY
class TeamEntry (pyxb.binding.basis.complexTypeDefinition):
    """
        Defines an event entry for a team.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TeamEntry')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1698, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__httpwww_orienteering_orgdatastandard3_0_TeamEntry_httpwww_orienteering_orgdatastandard3_0Id', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1705, 6), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httpwww_orienteering_orgdatastandard3_0_TeamEntry_httpwww_orienteering_orgdatastandard3_0Name', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1706, 6), )

    
    Name = property(__Name.value, __Name.set, None, '\n            The name of the team. If a relay, this is probably the name of the club optionally followed by a sequence number to distinguish teams from the same club in a class.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Organisation uses Python identifier Organisation
    __Organisation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), 'Organisation', '__httpwww_orienteering_orgdatastandard3_0_TeamEntry_httpwww_orienteering_orgdatastandard3_0Organisation', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1713, 6), )

    
    Organisation = property(__Organisation.value, __Organisation.set, None, '\n            The organisation(s) that the team represents.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}TeamEntryPerson uses Python identifier TeamEntryPerson
    __TeamEntryPerson = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TeamEntryPerson'), 'TeamEntryPerson', '__httpwww_orienteering_orgdatastandard3_0_TeamEntry_httpwww_orienteering_orgdatastandard3_0TeamEntryPerson', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1720, 6), )

    
    TeamEntryPerson = property(__TeamEntryPerson.value, __TeamEntryPerson.set, None, '\n            The persons that make up the team.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Class uses Python identifier Class
    __Class = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Class'), 'Class', '__httpwww_orienteering_orgdatastandard3_0_TeamEntry_httpwww_orienteering_orgdatastandard3_0Class', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1727, 6), )

    
    Class = property(__Class.value, __Class.set, None, '\n            The class(es) the team wants to take part in. Multiple classes may be provided in order of preference in scenarios where the number of competitors are limited in some classes.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Race uses Python identifier Race
    __Race = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Race'), 'Race', '__httpwww_orienteering_orgdatastandard3_0_TeamEntry_httpwww_orienteering_orgdatastandard3_0Race', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1734, 6), )

    
    Race = property(__Race.value, __Race.set, None, '\n            The numbers of the races that the team is taking part in. If not specified, team person takes part in all races.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}AssignedFee uses Python identifier AssignedFee
    __AssignedFee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee'), 'AssignedFee', '__httpwww_orienteering_orgdatastandard3_0_TeamEntry_httpwww_orienteering_orgdatastandard3_0AssignedFee', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1741, 6), )

    
    AssignedFee = property(__AssignedFee.value, __AssignedFee.set, None, '\n            The fees that the team as a whole has to pay when entering the event. In a multi-race event, there is usually one element for each race. If there are differentated fees for the team members, specify them in the TeamEntryPerson elements.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ServiceRequest uses Python identifier ServiceRequest
    __ServiceRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest'), 'ServiceRequest', '__httpwww_orienteering_orgdatastandard3_0_TeamEntry_httpwww_orienteering_orgdatastandard3_0ServiceRequest', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1748, 6), )

    
    ServiceRequest = property(__ServiceRequest.value, __ServiceRequest.set, None, '\n            Defines the services requested by the team.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}StartTimeAllocationRequest uses Python identifier StartTimeAllocationRequest
    __StartTimeAllocationRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartTimeAllocationRequest'), 'StartTimeAllocationRequest', '__httpwww_orienteering_orgdatastandard3_0_TeamEntry_httpwww_orienteering_orgdatastandard3_0StartTimeAllocationRequest', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1755, 6), )

    
    StartTimeAllocationRequest = property(__StartTimeAllocationRequest.value, __StartTimeAllocationRequest.set, None, '\n            Any special preferences regarding start time that has to be taken into consideration when making the start list draw.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ContactInformation uses Python identifier ContactInformation
    __ContactInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ContactInformation'), 'ContactInformation', '__httpwww_orienteering_orgdatastandard3_0_TeamEntry_httpwww_orienteering_orgdatastandard3_0ContactInformation', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1762, 6), )

    
    ContactInformation = property(__ContactInformation.value, __ContactInformation.set, None, '\n            Contact information (name and e.g. mobile phone number) to a team leader or coach, expressed as plain text.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}EntryTime uses Python identifier EntryTime
    __EntryTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EntryTime'), 'EntryTime', '__httpwww_orienteering_orgdatastandard3_0_TeamEntry_httpwww_orienteering_orgdatastandard3_0EntryTime', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1769, 6), )

    
    EntryTime = property(__EntryTime.value, __EntryTime.set, None, '\n            The time when the entry was first submitted.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_TeamEntry_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1776, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_TeamEntry_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1784, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1784, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __Name.name() : __Name,
        __Organisation.name() : __Organisation,
        __TeamEntryPerson.name() : __TeamEntryPerson,
        __Class.name() : __Class,
        __Race.name() : __Race,
        __AssignedFee.name() : __AssignedFee,
        __ServiceRequest.name() : __ServiceRequest,
        __StartTimeAllocationRequest.name() : __StartTimeAllocationRequest,
        __ContactInformation.name() : __ContactInformation,
        __EntryTime.name() : __EntryTime,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.TeamEntry = TeamEntry
Namespace.addCategoryObject('typeBinding', 'TeamEntry', TeamEntry)


# Complex type {http://www.orienteering.org/datastandard/3.0}TeamEntryPerson with content type ELEMENT_ONLY
class TeamEntryPerson (pyxb.binding.basis.complexTypeDefinition):
    """
        Defines a person that is part of a team entry.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TeamEntryPerson')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1787, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Person uses Python identifier Person
    __Person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Person'), 'Person', '__httpwww_orienteering_orgdatastandard3_0_TeamEntryPerson_httpwww_orienteering_orgdatastandard3_0Person', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1794, 6), )

    
    Person = property(__Person.value, __Person.set, None, '\n            The person. Omit if the person is not known at the moment, but for example the control card is known.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Organisation uses Python identifier Organisation
    __Organisation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), 'Organisation', '__httpwww_orienteering_orgdatastandard3_0_TeamEntryPerson_httpwww_orienteering_orgdatastandard3_0Organisation', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1801, 6), )

    
    Organisation = property(__Organisation.value, __Organisation.set, None, '\n            The organisation that the person represent. Omit if this is the same as the organsiation given in the TeamEntry element.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Leg uses Python identifier Leg
    __Leg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Leg'), 'Leg', '__httpwww_orienteering_orgdatastandard3_0_TeamEntryPerson_httpwww_orienteering_orgdatastandard3_0Leg', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1808, 6), )

    
    Leg = property(__Leg.value, __Leg.set, None, '\n            For relay entries, the number of the leg that this person is taking part in.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}LegOrder uses Python identifier LegOrder
    __LegOrder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LegOrder'), 'LegOrder', '__httpwww_orienteering_orgdatastandard3_0_TeamEntryPerson_httpwww_orienteering_orgdatastandard3_0LegOrder', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1815, 6), )

    
    LegOrder = property(__LegOrder.value, __LegOrder.set, None, "\n            Defines the person's starting order within a team at a parallel relay leg.\n          ")

    
    # Element {http://www.orienteering.org/datastandard/3.0}ControlCard uses Python identifier ControlCard
    __ControlCard = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ControlCard'), 'ControlCard', '__httpwww_orienteering_orgdatastandard3_0_TeamEntryPerson_httpwww_orienteering_orgdatastandard3_0ControlCard', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1822, 6), )

    
    ControlCard = property(__ControlCard.value, __ControlCard.set, None, '\n            Information about the control cards (punching cards) that the person uses at the event. Multiple control cards can be specified, e.g. one for punch checking and another for timing.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Score uses Python identifier Score
    __Score = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Score'), 'Score', '__httpwww_orienteering_orgdatastandard3_0_TeamEntryPerson_httpwww_orienteering_orgdatastandard3_0Score', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1829, 6), )

    
    Score = property(__Score.value, __Score.set, None, '\n            Any score that is submitted together with the entry, e.g. World Ranking points.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}AssignedFee uses Python identifier AssignedFee
    __AssignedFee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee'), 'AssignedFee', '__httpwww_orienteering_orgdatastandard3_0_TeamEntryPerson_httpwww_orienteering_orgdatastandard3_0AssignedFee', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1836, 6), )

    
    AssignedFee = property(__AssignedFee.value, __AssignedFee.set, None, '\n            The fees that this particular person has to pay when entering the event. In a multi-race event, there is usually one element for each race. Fees assigned to the team as a whole should be defined in the TeamEntry element.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_TeamEntryPerson_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1843, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    _ElementMap.update({
        __Person.name() : __Person,
        __Organisation.name() : __Organisation,
        __Leg.name() : __Leg,
        __LegOrder.name() : __LegOrder,
        __ControlCard.name() : __ControlCard,
        __Score.name() : __Score,
        __AssignedFee.name() : __AssignedFee,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TeamEntryPerson = TeamEntryPerson
Namespace.addCategoryObject('typeBinding', 'TeamEntryPerson', TeamEntryPerson)


# Complex type {http://www.orienteering.org/datastandard/3.0}ClassStart with content type ELEMENT_ONLY
class ClassStart (pyxb.binding.basis.complexTypeDefinition):
    """
        The start list of a single class containing either individual start times or team start times.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ClassStart')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1923, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Class uses Python identifier Class
    __Class = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Class'), 'Class', '__httpwww_orienteering_orgdatastandard3_0_ClassStart_httpwww_orienteering_orgdatastandard3_0Class', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1930, 6), )

    
    Class = property(__Class.value, __Class.set, None, '\n            The class that the start list belongs to.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Course uses Python identifier Course
    __Course = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Course'), 'Course', '__httpwww_orienteering_orgdatastandard3_0_ClassStart_httpwww_orienteering_orgdatastandard3_0Course', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1937, 6), )

    
    Course = property(__Course.value, __Course.set, None, '\n            Defines the course assigned to the class. If courses are unique per competitor, use PersonStart/Course or TeamStart/TeamMemberStart/Course instead. One element per race.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}StartName uses Python identifier StartName
    __StartName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartName'), 'StartName', '__httpwww_orienteering_orgdatastandard3_0_ClassStart_httpwww_orienteering_orgdatastandard3_0StartName', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1944, 6), )

    
    StartName = property(__StartName.value, __StartName.set, None, '\n            Defines the name of the start place (e.g. Start 1), if the race has multiple start places. One element per race.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}PersonStart uses Python identifier PersonStart
    __PersonStart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PersonStart'), 'PersonStart', '__httpwww_orienteering_orgdatastandard3_0_ClassStart_httpwww_orienteering_orgdatastandard3_0PersonStart', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1951, 6), )

    
    PersonStart = property(__PersonStart.value, __PersonStart.set, None, '\n            Start times for individual competitors in the class.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}TeamStart uses Python identifier TeamStart
    __TeamStart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TeamStart'), 'TeamStart', '__httpwww_orienteering_orgdatastandard3_0_ClassStart_httpwww_orienteering_orgdatastandard3_0TeamStart', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1958, 6), )

    
    TeamStart = property(__TeamStart.value, __TeamStart.set, None, '\n            Start times for teams in the class.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_ClassStart_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1965, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute timeResolution uses Python identifier timeResolution
    __timeResolution = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'timeResolution'), 'timeResolution', '__httpwww_orienteering_orgdatastandard3_0_ClassStart_timeResolution', pyxb.binding.datatypes.double, unicode_default='1')
    __timeResolution._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1973, 4)
    __timeResolution._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1973, 4)
    
    timeResolution = property(__timeResolution.value, __timeResolution.set, None, '\n          The time resolution of the start times, normally 1. For tenths of a second, use 0.1.\n        ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_ClassStart_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1980, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1980, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __Class.name() : __Class,
        __Course.name() : __Course,
        __StartName.name() : __StartName,
        __PersonStart.name() : __PersonStart,
        __TeamStart.name() : __TeamStart,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __timeResolution.name() : __timeResolution,
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.ClassStart = ClassStart
Namespace.addCategoryObject('typeBinding', 'ClassStart', ClassStart)


# Complex type {http://www.orienteering.org/datastandard/3.0}StartName with content type SIMPLE
class StartName (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.orienteering.org/datastandard/3.0}StartName with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StartName')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1983, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute raceNumber uses Python identifier raceNumber
    __raceNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'raceNumber'), 'raceNumber', '__httpwww_orienteering_orgdatastandard3_0_StartName_raceNumber', pyxb.binding.datatypes.integer)
    __raceNumber._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1991, 8)
    __raceNumber._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1991, 8)
    
    raceNumber = property(__raceNumber.value, __raceNumber.set, None, '\n              The ordinal number of the race that the information belongs to for a multi-race event, starting at 1.\n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __raceNumber.name() : __raceNumber
    })
_module_typeBindings.StartName = StartName
Namespace.addCategoryObject('typeBinding', 'StartName', StartName)


# Complex type {http://www.orienteering.org/datastandard/3.0}PersonStart with content type ELEMENT_ONLY
class PersonStart (pyxb.binding.basis.complexTypeDefinition):
    """
        Start information for an individual competitor, including e.g. start time and bib number.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PersonStart')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2002, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}EntryId uses Python identifier EntryId
    __EntryId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EntryId'), 'EntryId', '__httpwww_orienteering_orgdatastandard3_0_PersonStart_httpwww_orienteering_orgdatastandard3_0EntryId', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2009, 6), )

    
    EntryId = property(__EntryId.value, __EntryId.set, None, "\n            The id corresponding to this person's entry in an EntryList.\n          ")

    
    # Element {http://www.orienteering.org/datastandard/3.0}Person uses Python identifier Person
    __Person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Person'), 'Person', '__httpwww_orienteering_orgdatastandard3_0_PersonStart_httpwww_orienteering_orgdatastandard3_0Person', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2016, 6), )

    
    Person = property(__Person.value, __Person.set, None, '\n            The person that the start time belongs to. Omit if there is no person assigned to the start time, e.g. a vacant person.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Organisation uses Python identifier Organisation
    __Organisation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), 'Organisation', '__httpwww_orienteering_orgdatastandard3_0_PersonStart_httpwww_orienteering_orgdatastandard3_0Organisation', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2023, 6), )

    
    Organisation = property(__Organisation.value, __Organisation.set, None, '\n            The organisation that the person is representing at the event.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Start uses Python identifier Start
    __Start = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Start'), 'Start', '__httpwww_orienteering_orgdatastandard3_0_PersonStart_httpwww_orienteering_orgdatastandard3_0Start', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2030, 6), )

    
    Start = property(__Start.value, __Start.set, None, '\n            The core start information for the person; one element per race in the event.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_PersonStart_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2037, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_PersonStart_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2045, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2045, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __EntryId.name() : __EntryId,
        __Person.name() : __Person,
        __Organisation.name() : __Organisation,
        __Start.name() : __Start,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.PersonStart = PersonStart
Namespace.addCategoryObject('typeBinding', 'PersonStart', PersonStart)


# Complex type {http://www.orienteering.org/datastandard/3.0}PersonRaceStart with content type ELEMENT_ONLY
class PersonRaceStart (pyxb.binding.basis.complexTypeDefinition):
    """
        Start information for a person in a race.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PersonRaceStart')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2048, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}BibNumber uses Python identifier BibNumber
    __BibNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BibNumber'), 'BibNumber', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceStart_httpwww_orienteering_orgdatastandard3_0BibNumber', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2055, 6), )

    
    BibNumber = property(__BibNumber.value, __BibNumber.set, None, '\n            The bib number that the person is wearing.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}StartTime uses Python identifier StartTime
    __StartTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartTime'), 'StartTime', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceStart_httpwww_orienteering_orgdatastandard3_0StartTime', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2062, 6), )

    
    StartTime = property(__StartTime.value, __StartTime.set, None, '\n            The time when the person starts.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Course uses Python identifier Course
    __Course = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Course'), 'Course', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceStart_httpwww_orienteering_orgdatastandard3_0Course', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2069, 6), )

    
    Course = property(__Course.value, __Course.set, None, '\n            Defines the course assigned to the person.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ControlCard uses Python identifier ControlCard
    __ControlCard = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ControlCard'), 'ControlCard', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceStart_httpwww_orienteering_orgdatastandard3_0ControlCard', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2076, 6), )

    
    ControlCard = property(__ControlCard.value, __ControlCard.set, None, '\n            Defines the control cards assigned to the person. Multiple control cards can be specified, e.g. one for punch checking and another for timing.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}AssignedFee uses Python identifier AssignedFee
    __AssignedFee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee'), 'AssignedFee', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceStart_httpwww_orienteering_orgdatastandard3_0AssignedFee', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2083, 6), )

    
    AssignedFee = property(__AssignedFee.value, __AssignedFee.set, None, '\n            Defines the fees that the person has been assigned.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ServiceRequest uses Python identifier ServiceRequest
    __ServiceRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest'), 'ServiceRequest', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceStart_httpwww_orienteering_orgdatastandard3_0ServiceRequest', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2090, 6), )

    
    ServiceRequest = property(__ServiceRequest.value, __ServiceRequest.set, None, '\n            Defines the services requested by the person.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceStart_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2097, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute raceNumber uses Python identifier raceNumber
    __raceNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'raceNumber'), 'raceNumber', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceStart_raceNumber', pyxb.binding.datatypes.integer)
    __raceNumber._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2105, 4)
    __raceNumber._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2105, 4)
    
    raceNumber = property(__raceNumber.value, __raceNumber.set, None, '\n          The ordinal number of the race that the information belongs to for a multi-race event, starting at 1.\n        ')

    _ElementMap.update({
        __BibNumber.name() : __BibNumber,
        __StartTime.name() : __StartTime,
        __Course.name() : __Course,
        __ControlCard.name() : __ControlCard,
        __AssignedFee.name() : __AssignedFee,
        __ServiceRequest.name() : __ServiceRequest,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __raceNumber.name() : __raceNumber
    })
_module_typeBindings.PersonRaceStart = PersonRaceStart
Namespace.addCategoryObject('typeBinding', 'PersonRaceStart', PersonRaceStart)


# Complex type {http://www.orienteering.org/datastandard/3.0}TeamStart with content type ELEMENT_ONLY
class TeamStart (pyxb.binding.basis.complexTypeDefinition):
    """
        Start information for a team, including e.g. team name, start times and bib numbers.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TeamStart')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2114, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}EntryId uses Python identifier EntryId
    __EntryId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EntryId'), 'EntryId', '__httpwww_orienteering_orgdatastandard3_0_TeamStart_httpwww_orienteering_orgdatastandard3_0EntryId', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2121, 6), )

    
    EntryId = property(__EntryId.value, __EntryId.set, None, "\n            The id corresponding to this team's entry in an EntryList.\n          ")

    
    # Element {http://www.orienteering.org/datastandard/3.0}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httpwww_orienteering_orgdatastandard3_0_TeamStart_httpwww_orienteering_orgdatastandard3_0Name', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2128, 6), )

    
    Name = property(__Name.value, __Name.set, None, '\n            The name of the team, e.g. organisation name and team number for a relay team. Omit if the team name is not know, e.g. a vacant team.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Organisation uses Python identifier Organisation
    __Organisation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), 'Organisation', '__httpwww_orienteering_orgdatastandard3_0_TeamStart_httpwww_orienteering_orgdatastandard3_0Organisation', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2135, 6), )

    
    Organisation = property(__Organisation.value, __Organisation.set, None, '\n            The organisation(s) the team is representing.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}BibNumber uses Python identifier BibNumber
    __BibNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BibNumber'), 'BibNumber', '__httpwww_orienteering_orgdatastandard3_0_TeamStart_httpwww_orienteering_orgdatastandard3_0BibNumber', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2142, 6), )

    
    BibNumber = property(__BibNumber.value, __BibNumber.set, None, '\n            The bib number that the members of the team are wearing. If each team member has a unique bib number, use the BibNumber of the TeamMemberStart element.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}TeamMemberStart uses Python identifier TeamMemberStart
    __TeamMemberStart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TeamMemberStart'), 'TeamMemberStart', '__httpwww_orienteering_orgdatastandard3_0_TeamStart_httpwww_orienteering_orgdatastandard3_0TeamMemberStart', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2149, 6), )

    
    TeamMemberStart = property(__TeamMemberStart.value, __TeamMemberStart.set, None, '\n            Information about the start times for the team members. One element per relay leg must be included, even if the team has not assigned any team member to the leg.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}AssignedFee uses Python identifier AssignedFee
    __AssignedFee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee'), 'AssignedFee', '__httpwww_orienteering_orgdatastandard3_0_TeamStart_httpwww_orienteering_orgdatastandard3_0AssignedFee', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2156, 6), )

    
    AssignedFee = property(__AssignedFee.value, __AssignedFee.set, None, '\n            Defines the fees that the team has been assigned.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ServiceRequest uses Python identifier ServiceRequest
    __ServiceRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest'), 'ServiceRequest', '__httpwww_orienteering_orgdatastandard3_0_TeamStart_httpwww_orienteering_orgdatastandard3_0ServiceRequest', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2163, 6), )

    
    ServiceRequest = property(__ServiceRequest.value, __ServiceRequest.set, None, '\n            Defines the services requested by the team.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_TeamStart_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2170, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_TeamStart_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2178, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2178, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __EntryId.name() : __EntryId,
        __Name.name() : __Name,
        __Organisation.name() : __Organisation,
        __BibNumber.name() : __BibNumber,
        __TeamMemberStart.name() : __TeamMemberStart,
        __AssignedFee.name() : __AssignedFee,
        __ServiceRequest.name() : __ServiceRequest,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.TeamStart = TeamStart
Namespace.addCategoryObject('typeBinding', 'TeamStart', TeamStart)


# Complex type {http://www.orienteering.org/datastandard/3.0}TeamMemberStart with content type ELEMENT_ONLY
class TeamMemberStart (pyxb.binding.basis.complexTypeDefinition):
    """
        Start information for an individual competitor, including e.g. start time and bib number.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TeamMemberStart')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2181, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}EntryId uses Python identifier EntryId
    __EntryId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EntryId'), 'EntryId', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberStart_httpwww_orienteering_orgdatastandard3_0EntryId', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2188, 6), )

    
    EntryId = property(__EntryId.value, __EntryId.set, None, "\n            The id corresponding to this team member's entry in an EntryList.\n          ")

    
    # Element {http://www.orienteering.org/datastandard/3.0}Person uses Python identifier Person
    __Person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Person'), 'Person', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberStart_httpwww_orienteering_orgdatastandard3_0Person', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2195, 6), )

    
    Person = property(__Person.value, __Person.set, None, '\n            The team member that the start time belongs to.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Organisation uses Python identifier Organisation
    __Organisation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), 'Organisation', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberStart_httpwww_orienteering_orgdatastandard3_0Organisation', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2202, 6), )

    
    Organisation = property(__Organisation.value, __Organisation.set, None, '\n            The organisation that the team member is representing at the event.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Start uses Python identifier Start
    __Start = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Start'), 'Start', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberStart_httpwww_orienteering_orgdatastandard3_0Start', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2209, 6), )

    
    Start = property(__Start.value, __Start.set, None, '\n            The core start information for the team member; one element per race in the event.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberStart_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2216, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberStart_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2224, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2224, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __EntryId.name() : __EntryId,
        __Person.name() : __Person,
        __Organisation.name() : __Organisation,
        __Start.name() : __Start,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.TeamMemberStart = TeamMemberStart
Namespace.addCategoryObject('typeBinding', 'TeamMemberStart', TeamMemberStart)


# Complex type {http://www.orienteering.org/datastandard/3.0}TeamMemberRaceStart with content type ELEMENT_ONLY
class TeamMemberRaceStart (pyxb.binding.basis.complexTypeDefinition):
    """
        Start information for a team member in a race.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TeamMemberRaceStart')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2227, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Leg uses Python identifier Leg
    __Leg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Leg'), 'Leg', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceStart_httpwww_orienteering_orgdatastandard3_0Leg', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2234, 6), )

    
    Leg = property(__Leg.value, __Leg.set, None, '\n            In case of a relay, this is the number of the leg that the team member takes part in.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}LegOrder uses Python identifier LegOrder
    __LegOrder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LegOrder'), 'LegOrder', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceStart_httpwww_orienteering_orgdatastandard3_0LegOrder', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2241, 6), )

    
    LegOrder = property(__LegOrder.value, __LegOrder.set, None, "\n            In case of a relay with parallel legs, this defines the team member's starting order of the leg within the team.\n          ")

    
    # Element {http://www.orienteering.org/datastandard/3.0}BibNumber uses Python identifier BibNumber
    __BibNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BibNumber'), 'BibNumber', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceStart_httpwww_orienteering_orgdatastandard3_0BibNumber', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2248, 6), )

    
    BibNumber = property(__BibNumber.value, __BibNumber.set, None, '\n            The bib number that the team member is wearing.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}StartTime uses Python identifier StartTime
    __StartTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartTime'), 'StartTime', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceStart_httpwww_orienteering_orgdatastandard3_0StartTime', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2255, 6), )

    
    StartTime = property(__StartTime.value, __StartTime.set, None, '\n            The time when the team member starts.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Course uses Python identifier Course
    __Course = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Course'), 'Course', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceStart_httpwww_orienteering_orgdatastandard3_0Course', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2262, 6), )

    
    Course = property(__Course.value, __Course.set, None, '\n            Defines the course assigned to the team member.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ControlCard uses Python identifier ControlCard
    __ControlCard = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ControlCard'), 'ControlCard', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceStart_httpwww_orienteering_orgdatastandard3_0ControlCard', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2269, 6), )

    
    ControlCard = property(__ControlCard.value, __ControlCard.set, None, '\n            Defines the control card assigned to the team member. Multiple control cards can be specified, e.g. one for punch checking and another for timing.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}AssignedFee uses Python identifier AssignedFee
    __AssignedFee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee'), 'AssignedFee', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceStart_httpwww_orienteering_orgdatastandard3_0AssignedFee', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2276, 6), )

    
    AssignedFee = property(__AssignedFee.value, __AssignedFee.set, None, '\n            Defines the fees that the team member has been assigned.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ServiceRequest uses Python identifier ServiceRequest
    __ServiceRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest'), 'ServiceRequest', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceStart_httpwww_orienteering_orgdatastandard3_0ServiceRequest', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2283, 6), )

    
    ServiceRequest = property(__ServiceRequest.value, __ServiceRequest.set, None, '\n            Defines the services requested by the team member.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceStart_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2290, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute raceNumber uses Python identifier raceNumber
    __raceNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'raceNumber'), 'raceNumber', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceStart_raceNumber', pyxb.binding.datatypes.integer)
    __raceNumber._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2298, 4)
    __raceNumber._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2298, 4)
    
    raceNumber = property(__raceNumber.value, __raceNumber.set, None, '\n          The ordinal number of the race that the information belongs to for a multi-race event, starting at 1.\n        ')

    _ElementMap.update({
        __Leg.name() : __Leg,
        __LegOrder.name() : __LegOrder,
        __BibNumber.name() : __BibNumber,
        __StartTime.name() : __StartTime,
        __Course.name() : __Course,
        __ControlCard.name() : __ControlCard,
        __AssignedFee.name() : __AssignedFee,
        __ServiceRequest.name() : __ServiceRequest,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __raceNumber.name() : __raceNumber
    })
_module_typeBindings.TeamMemberRaceStart = TeamMemberRaceStart
Namespace.addCategoryObject('typeBinding', 'TeamMemberRaceStart', TeamMemberRaceStart)


# Complex type {http://www.orienteering.org/datastandard/3.0}ClassResult with content type ELEMENT_ONLY
class ClassResult (pyxb.binding.basis.complexTypeDefinition):
    """
        The result list for a single class containing either individual results or team results.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ClassResult')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2307, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Class uses Python identifier Class
    __Class = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Class'), 'Class', '__httpwww_orienteering_orgdatastandard3_0_ClassResult_httpwww_orienteering_orgdatastandard3_0Class', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2314, 6), )

    
    Class = property(__Class.value, __Class.set, None, '\n            The class that the result list belongs to.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Course uses Python identifier Course
    __Course = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Course'), 'Course', '__httpwww_orienteering_orgdatastandard3_0_ClassResult_httpwww_orienteering_orgdatastandard3_0Course', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2321, 6), )

    
    Course = property(__Course.value, __Course.set, None, '\n            Defines the course assigned to the class. If courses are unique per competitor, use PersonResult/Course or TeamResult/TeamMemberResult/Course instead. One element per race.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}PersonResult uses Python identifier PersonResult
    __PersonResult = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PersonResult'), 'PersonResult', '__httpwww_orienteering_orgdatastandard3_0_ClassResult_httpwww_orienteering_orgdatastandard3_0PersonResult', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2328, 6), )

    
    PersonResult = property(__PersonResult.value, __PersonResult.set, None, '\n            Results for individual competitors in the class.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}TeamResult uses Python identifier TeamResult
    __TeamResult = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TeamResult'), 'TeamResult', '__httpwww_orienteering_orgdatastandard3_0_ClassResult_httpwww_orienteering_orgdatastandard3_0TeamResult', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2335, 6), )

    
    TeamResult = property(__TeamResult.value, __TeamResult.set, None, '\n            Results for teams in the class.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_ClassResult_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2342, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute timeResolution uses Python identifier timeResolution
    __timeResolution = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'timeResolution'), 'timeResolution', '__httpwww_orienteering_orgdatastandard3_0_ClassResult_timeResolution', pyxb.binding.datatypes.double, unicode_default='1')
    __timeResolution._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2350, 4)
    __timeResolution._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2350, 4)
    
    timeResolution = property(__timeResolution.value, __timeResolution.set, None, '\n          The time resolution of the results, normally 1. For tenths of a second, use 0.1.\n        ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_ClassResult_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2357, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2357, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __Class.name() : __Class,
        __Course.name() : __Course,
        __PersonResult.name() : __PersonResult,
        __TeamResult.name() : __TeamResult,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __timeResolution.name() : __timeResolution,
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.ClassResult = ClassResult
Namespace.addCategoryObject('typeBinding', 'ClassResult', ClassResult)


# Complex type {http://www.orienteering.org/datastandard/3.0}PersonResult with content type ELEMENT_ONLY
class PersonResult (pyxb.binding.basis.complexTypeDefinition):
    """
        Result information for an individual competitor, including e.g. result status, place, finish time, and split times.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PersonResult')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2360, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}EntryId uses Python identifier EntryId
    __EntryId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EntryId'), 'EntryId', '__httpwww_orienteering_orgdatastandard3_0_PersonResult_httpwww_orienteering_orgdatastandard3_0EntryId', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2367, 6), )

    
    EntryId = property(__EntryId.value, __EntryId.set, None, "\n            The id corresponding to this person's entry in an EntryList.\n          ")

    
    # Element {http://www.orienteering.org/datastandard/3.0}Person uses Python identifier Person
    __Person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Person'), 'Person', '__httpwww_orienteering_orgdatastandard3_0_PersonResult_httpwww_orienteering_orgdatastandard3_0Person', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2374, 6), )

    
    Person = property(__Person.value, __Person.set, None, '\n            The person that the result belongs to.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Organisation uses Python identifier Organisation
    __Organisation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), 'Organisation', '__httpwww_orienteering_orgdatastandard3_0_PersonResult_httpwww_orienteering_orgdatastandard3_0Organisation', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2381, 6), )

    
    Organisation = property(__Organisation.value, __Organisation.set, None, '\n            The organisation that the person is representing at the event.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Result uses Python identifier Result
    __Result = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Result'), 'Result', '__httpwww_orienteering_orgdatastandard3_0_PersonResult_httpwww_orienteering_orgdatastandard3_0Result', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2388, 6), )

    
    Result = property(__Result.value, __Result.set, None, '\n            The core result information for the person; one element per race in the event.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_PersonResult_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2395, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_PersonResult_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2403, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2403, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __EntryId.name() : __EntryId,
        __Person.name() : __Person,
        __Organisation.name() : __Organisation,
        __Result.name() : __Result,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.PersonResult = PersonResult
Namespace.addCategoryObject('typeBinding', 'PersonResult', PersonResult)


# Complex type {http://www.orienteering.org/datastandard/3.0}PersonRaceResult with content type ELEMENT_ONLY
class PersonRaceResult (pyxb.binding.basis.complexTypeDefinition):
    """
        Result information for a person in a race.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PersonRaceResult')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2406, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}BibNumber uses Python identifier BibNumber
    __BibNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BibNumber'), 'BibNumber', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceResult_httpwww_orienteering_orgdatastandard3_0BibNumber', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2413, 6), )

    
    BibNumber = property(__BibNumber.value, __BibNumber.set, None, '\n            The bib number that the person that the result belongs to is wearing.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}StartTime uses Python identifier StartTime
    __StartTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartTime'), 'StartTime', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceResult_httpwww_orienteering_orgdatastandard3_0StartTime', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2420, 6), )

    
    StartTime = property(__StartTime.value, __StartTime.set, None, '\n            The time when the person that the result belongs to started, expressed in ISO 8601 format.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}FinishTime uses Python identifier FinishTime
    __FinishTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FinishTime'), 'FinishTime', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceResult_httpwww_orienteering_orgdatastandard3_0FinishTime', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2427, 6), )

    
    FinishTime = property(__FinishTime.value, __FinishTime.set, None, '\n            The time when the person that the result belongs to finished, expressed in ISO 8601 format.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Time uses Python identifier Time
    __Time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Time'), 'Time', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceResult_httpwww_orienteering_orgdatastandard3_0Time', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2434, 6), )

    
    Time = property(__Time.value, __Time.set, None, '\n            The time, in seconds, that is shown in the result list. Fractions of seconds (e.g. 258.7) may be used if the time resolution is higher than one second.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}TimeBehind uses Python identifier TimeBehind
    __TimeBehind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TimeBehind'), 'TimeBehind', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceResult_httpwww_orienteering_orgdatastandard3_0TimeBehind', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2441, 6), )

    
    TimeBehind = property(__TimeBehind.value, __TimeBehind.set, None, '\n            The time, in seconds, that the the person is behind the winner. Fractions of seconds (e.g. 258.7) may be used if the time resolution is higher than one second.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Position uses Python identifier Position
    __Position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Position'), 'Position', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceResult_httpwww_orienteering_orgdatastandard3_0Position', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2448, 6), )

    
    Position = property(__Position.value, __Position.set, None, '\n            The position in the result list for the person that the result belongs to. This element should only be present when the Status element is set to OK.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Status uses Python identifier Status
    __Status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Status'), 'Status', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceResult_httpwww_orienteering_orgdatastandard3_0Status', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2455, 6), )

    
    Status = property(__Status.value, __Status.set, None, '\n            The status of the result.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Score uses Python identifier Score
    __Score = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Score'), 'Score', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceResult_httpwww_orienteering_orgdatastandard3_0Score', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2462, 6), )

    
    Score = property(__Score.value, __Score.set, None, '\n            Any scores that are attached to the result, e.g. World Ranking points.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}OverallResult uses Python identifier OverallResult
    __OverallResult = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OverallResult'), 'OverallResult', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceResult_httpwww_orienteering_orgdatastandard3_0OverallResult', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2469, 6), )

    
    OverallResult = property(__OverallResult.value, __OverallResult.set, None, '\n            Holds the overall result for the person after the current race for a multi-race event.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Course uses Python identifier Course
    __Course = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Course'), 'Course', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceResult_httpwww_orienteering_orgdatastandard3_0Course', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2476, 6), )

    
    Course = property(__Course.value, __Course.set, None, '\n            Defines the course assigned to the person.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}SplitTime uses Python identifier SplitTime
    __SplitTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SplitTime'), 'SplitTime', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceResult_httpwww_orienteering_orgdatastandard3_0SplitTime', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2483, 6), )

    
    SplitTime = property(__SplitTime.value, __SplitTime.set, None, "\n            Contains the times at each control of the course. Each control of the competitor's course (if known) has to be defined in a SplitTime element, even if the control has not been punched or if the competitor has not started. Start and finish times must not be present as SplitTime elements.\n          ")

    
    # Element {http://www.orienteering.org/datastandard/3.0}ControlAnswer uses Python identifier ControlAnswer
    __ControlAnswer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ControlAnswer'), 'ControlAnswer', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceResult_httpwww_orienteering_orgdatastandard3_0ControlAnswer', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2490, 6), )

    
    ControlAnswer = property(__ControlAnswer.value, __ControlAnswer.set, None, '\n            Defines the answer for a trail-O control.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Route uses Python identifier Route
    __Route = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Route'), 'Route', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceResult_httpwww_orienteering_orgdatastandard3_0Route', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2497, 6), )

    
    Route = property(__Route.value, __Route.set, None, "\n            Defines the person's route recorded by a tracking device.\n          ")

    
    # Element {http://www.orienteering.org/datastandard/3.0}ControlCard uses Python identifier ControlCard
    __ControlCard = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ControlCard'), 'ControlCard', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceResult_httpwww_orienteering_orgdatastandard3_0ControlCard', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2504, 6), )

    
    ControlCard = property(__ControlCard.value, __ControlCard.set, None, '\n            Defines the control card assigned to the person. Multiple control cards can be specified, e.g. one for punch checking and another for timing.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}AssignedFee uses Python identifier AssignedFee
    __AssignedFee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee'), 'AssignedFee', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceResult_httpwww_orienteering_orgdatastandard3_0AssignedFee', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2511, 6), )

    
    AssignedFee = property(__AssignedFee.value, __AssignedFee.set, None, '\n            Defines the fees that the person has been assigned.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ServiceRequest uses Python identifier ServiceRequest
    __ServiceRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest'), 'ServiceRequest', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceResult_httpwww_orienteering_orgdatastandard3_0ServiceRequest', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2518, 6), )

    
    ServiceRequest = property(__ServiceRequest.value, __ServiceRequest.set, None, '\n            Defines the services requested by the person.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceResult_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2525, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute raceNumber uses Python identifier raceNumber
    __raceNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'raceNumber'), 'raceNumber', '__httpwww_orienteering_orgdatastandard3_0_PersonRaceResult_raceNumber', pyxb.binding.datatypes.integer)
    __raceNumber._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2533, 4)
    __raceNumber._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2533, 4)
    
    raceNumber = property(__raceNumber.value, __raceNumber.set, None, '\n          The ordinal number of the race that the information belongs to for a multi-race event, starting at 1.\n        ')

    _ElementMap.update({
        __BibNumber.name() : __BibNumber,
        __StartTime.name() : __StartTime,
        __FinishTime.name() : __FinishTime,
        __Time.name() : __Time,
        __TimeBehind.name() : __TimeBehind,
        __Position.name() : __Position,
        __Status.name() : __Status,
        __Score.name() : __Score,
        __OverallResult.name() : __OverallResult,
        __Course.name() : __Course,
        __SplitTime.name() : __SplitTime,
        __ControlAnswer.name() : __ControlAnswer,
        __Route.name() : __Route,
        __ControlCard.name() : __ControlCard,
        __AssignedFee.name() : __AssignedFee,
        __ServiceRequest.name() : __ServiceRequest,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __raceNumber.name() : __raceNumber
    })
_module_typeBindings.PersonRaceResult = PersonRaceResult
Namespace.addCategoryObject('typeBinding', 'PersonRaceResult', PersonRaceResult)


# Complex type {http://www.orienteering.org/datastandard/3.0}TeamResult with content type ELEMENT_ONLY
class TeamResult (pyxb.binding.basis.complexTypeDefinition):
    """
        Result information for a team, including e.g. result status, place, finish time and individual times for the team members.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TeamResult')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2542, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}EntryId uses Python identifier EntryId
    __EntryId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EntryId'), 'EntryId', '__httpwww_orienteering_orgdatastandard3_0_TeamResult_httpwww_orienteering_orgdatastandard3_0EntryId', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2549, 6), )

    
    EntryId = property(__EntryId.value, __EntryId.set, None, "\n            The id corresponding to this team's entry in an EntryList.\n          ")

    
    # Element {http://www.orienteering.org/datastandard/3.0}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httpwww_orienteering_orgdatastandard3_0_TeamResult_httpwww_orienteering_orgdatastandard3_0Name', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2556, 6), )

    
    Name = property(__Name.value, __Name.set, None, '\n            The name of the team, e.g. organisation name and team number for a relay team.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Organisation uses Python identifier Organisation
    __Organisation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), 'Organisation', '__httpwww_orienteering_orgdatastandard3_0_TeamResult_httpwww_orienteering_orgdatastandard3_0Organisation', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2563, 6), )

    
    Organisation = property(__Organisation.value, __Organisation.set, None, '\n            The organisation(s) the team is representing.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}BibNumber uses Python identifier BibNumber
    __BibNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BibNumber'), 'BibNumber', '__httpwww_orienteering_orgdatastandard3_0_TeamResult_httpwww_orienteering_orgdatastandard3_0BibNumber', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2570, 6), )

    
    BibNumber = property(__BibNumber.value, __BibNumber.set, None, '\n            The bib number that the members of the team are wearing. If each team member has a unique bib number, use the BibNumber of the TeamMemberStart element.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}TeamMemberResult uses Python identifier TeamMemberResult
    __TeamMemberResult = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TeamMemberResult'), 'TeamMemberResult', '__httpwww_orienteering_orgdatastandard3_0_TeamResult_httpwww_orienteering_orgdatastandard3_0TeamMemberResult', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2577, 6), )

    
    TeamMemberResult = property(__TeamMemberResult.value, __TeamMemberResult.set, None, '\n            Defines the result information for each team member. One element per relay leg must be included, even if the team has not assigned any team member to the leg, with exception for delta results.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}AssignedFee uses Python identifier AssignedFee
    __AssignedFee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee'), 'AssignedFee', '__httpwww_orienteering_orgdatastandard3_0_TeamResult_httpwww_orienteering_orgdatastandard3_0AssignedFee', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2584, 6), )

    
    AssignedFee = property(__AssignedFee.value, __AssignedFee.set, None, '\n            Defines the fees that the team has been assigned.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ServiceRequest uses Python identifier ServiceRequest
    __ServiceRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest'), 'ServiceRequest', '__httpwww_orienteering_orgdatastandard3_0_TeamResult_httpwww_orienteering_orgdatastandard3_0ServiceRequest', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2591, 6), )

    
    ServiceRequest = property(__ServiceRequest.value, __ServiceRequest.set, None, '\n            Defines the services requested by the team.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_TeamResult_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2598, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    _ElementMap.update({
        __EntryId.name() : __EntryId,
        __Name.name() : __Name,
        __Organisation.name() : __Organisation,
        __BibNumber.name() : __BibNumber,
        __TeamMemberResult.name() : __TeamMemberResult,
        __AssignedFee.name() : __AssignedFee,
        __ServiceRequest.name() : __ServiceRequest,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TeamResult = TeamResult
Namespace.addCategoryObject('typeBinding', 'TeamResult', TeamResult)


# Complex type {http://www.orienteering.org/datastandard/3.0}TeamMemberResult with content type ELEMENT_ONLY
class TeamMemberResult (pyxb.binding.basis.complexTypeDefinition):
    """
        Result information for a team member, including e.g. result status, place, finish time, and split times.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TeamMemberResult')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2608, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}EntryId uses Python identifier EntryId
    __EntryId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EntryId'), 'EntryId', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberResult_httpwww_orienteering_orgdatastandard3_0EntryId', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2615, 6), )

    
    EntryId = property(__EntryId.value, __EntryId.set, None, "\n            The id corresponding to this team member's entry in an EntryList.\n          ")

    
    # Element {http://www.orienteering.org/datastandard/3.0}Person uses Python identifier Person
    __Person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Person'), 'Person', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberResult_httpwww_orienteering_orgdatastandard3_0Person', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2622, 6), )

    
    Person = property(__Person.value, __Person.set, None, '\n            The team member that the result belongs to. If a relay team is missing a team member, omit this element.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Organisation uses Python identifier Organisation
    __Organisation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), 'Organisation', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberResult_httpwww_orienteering_orgdatastandard3_0Organisation', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2629, 6), )

    
    Organisation = property(__Organisation.value, __Organisation.set, None, '\n            The organisation that the team member is representing at the event.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Result uses Python identifier Result
    __Result = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Result'), 'Result', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberResult_httpwww_orienteering_orgdatastandard3_0Result', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2636, 6), )

    
    Result = property(__Result.value, __Result.set, None, '\n            The core result information for the person; one element per race in the event.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberResult_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2643, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberResult_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2651, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2651, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __EntryId.name() : __EntryId,
        __Person.name() : __Person,
        __Organisation.name() : __Organisation,
        __Result.name() : __Result,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.TeamMemberResult = TeamMemberResult
Namespace.addCategoryObject('typeBinding', 'TeamMemberResult', TeamMemberResult)


# Complex type {http://www.orienteering.org/datastandard/3.0}TeamMemberRaceResult with content type ELEMENT_ONLY
class TeamMemberRaceResult (pyxb.binding.basis.complexTypeDefinition):
    """
        Result information for a person in a race.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TeamMemberRaceResult')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2654, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Leg uses Python identifier Leg
    __Leg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Leg'), 'Leg', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceResult_httpwww_orienteering_orgdatastandard3_0Leg', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2661, 6), )

    
    Leg = property(__Leg.value, __Leg.set, None, '\n            In case of a relay, this is the number of the leg that the team member takes part in.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}LegOrder uses Python identifier LegOrder
    __LegOrder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LegOrder'), 'LegOrder', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceResult_httpwww_orienteering_orgdatastandard3_0LegOrder', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2668, 6), )

    
    LegOrder = property(__LegOrder.value, __LegOrder.set, None, "\n            In case of a relay with parallel legs, this defines the team member's starting order of the leg within the team.\n          ")

    
    # Element {http://www.orienteering.org/datastandard/3.0}BibNumber uses Python identifier BibNumber
    __BibNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BibNumber'), 'BibNumber', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceResult_httpwww_orienteering_orgdatastandard3_0BibNumber', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2675, 6), )

    
    BibNumber = property(__BibNumber.value, __BibNumber.set, None, '\n            The bib number that the team member that the result belongs to is wearing.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}StartTime uses Python identifier StartTime
    __StartTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartTime'), 'StartTime', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceResult_httpwww_orienteering_orgdatastandard3_0StartTime', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2682, 6), )

    
    StartTime = property(__StartTime.value, __StartTime.set, None, '\n            The time when the team member that the result belongs to started, expressed in ISO 8601 format.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}FinishTime uses Python identifier FinishTime
    __FinishTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FinishTime'), 'FinishTime', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceResult_httpwww_orienteering_orgdatastandard3_0FinishTime', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2689, 6), )

    
    FinishTime = property(__FinishTime.value, __FinishTime.set, None, '\n            The time when the team member that the result belongs to finished, expressed in ISO 8601 format.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Time uses Python identifier Time
    __Time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Time'), 'Time', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceResult_httpwww_orienteering_orgdatastandard3_0Time', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2696, 6), )

    
    Time = property(__Time.value, __Time.set, None, '\n            The time, in seconds, that is shown in the result list. Fractions of seconds (e.g. 258.7) may be used if the time resolution is higher than one second.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}TimeBehind uses Python identifier TimeBehind
    __TimeBehind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TimeBehind'), 'TimeBehind', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceResult_httpwww_orienteering_orgdatastandard3_0TimeBehind', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2703, 6), )

    
    TimeBehind = property(__TimeBehind.value, __TimeBehind.set, None, '\n            The time, in seconds, that the the team member is behind the winner. Fractions of seconds (e.g. 258.7) may be used if the time resolution is higher than one second.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Position uses Python identifier Position
    __Position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Position'), 'Position', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceResult_httpwww_orienteering_orgdatastandard3_0Position', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2736, 6), )

    
    Position = property(__Position.value, __Position.set, None, '\n            The position in the result list for the person that the result belongs to. This element should only be present when the Status element is set to OK.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Status uses Python identifier Status
    __Status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Status'), 'Status', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceResult_httpwww_orienteering_orgdatastandard3_0Status', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2769, 6), )

    
    Status = property(__Status.value, __Status.set, None, '\n            The status of the result.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Score uses Python identifier Score
    __Score = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Score'), 'Score', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceResult_httpwww_orienteering_orgdatastandard3_0Score', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2776, 6), )

    
    Score = property(__Score.value, __Score.set, None, '\n            Any scores that are attached to the result, e.g. World Ranking points.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}OverallResult uses Python identifier OverallResult
    __OverallResult = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OverallResult'), 'OverallResult', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceResult_httpwww_orienteering_orgdatastandard3_0OverallResult', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2783, 6), )

    
    OverallResult = property(__OverallResult.value, __OverallResult.set, None, '\n            Holds the result after the current leg for the team.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Course uses Python identifier Course
    __Course = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Course'), 'Course', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceResult_httpwww_orienteering_orgdatastandard3_0Course', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2790, 6), )

    
    Course = property(__Course.value, __Course.set, None, '\n            Defines the course assigned to the person.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}SplitTime uses Python identifier SplitTime
    __SplitTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SplitTime'), 'SplitTime', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceResult_httpwww_orienteering_orgdatastandard3_0SplitTime', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2797, 6), )

    
    SplitTime = property(__SplitTime.value, __SplitTime.set, None, "\n            Contains the times at each control of the course. Each control of the team member's course has to be defined in a SplitTime element, even if the control has not been punched. Start and finish times must not be present as SplitTime elements.\n          ")

    
    # Element {http://www.orienteering.org/datastandard/3.0}ControlAnswer uses Python identifier ControlAnswer
    __ControlAnswer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ControlAnswer'), 'ControlAnswer', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceResult_httpwww_orienteering_orgdatastandard3_0ControlAnswer', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2804, 6), )

    
    ControlAnswer = property(__ControlAnswer.value, __ControlAnswer.set, None, '\n            Defines the answer for a trail-O control.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Route uses Python identifier Route
    __Route = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Route'), 'Route', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceResult_httpwww_orienteering_orgdatastandard3_0Route', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2811, 6), )

    
    Route = property(__Route.value, __Route.set, None, "\n            Defines the person's route recorded by a tracking device.\n          ")

    
    # Element {http://www.orienteering.org/datastandard/3.0}ControlCard uses Python identifier ControlCard
    __ControlCard = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ControlCard'), 'ControlCard', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceResult_httpwww_orienteering_orgdatastandard3_0ControlCard', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2818, 6), )

    
    ControlCard = property(__ControlCard.value, __ControlCard.set, None, '\n            Defines the control card assigned to the person. Multiple control cards can be specified, e.g. one for punch checking and another for timing.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}AssignedFee uses Python identifier AssignedFee
    __AssignedFee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee'), 'AssignedFee', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceResult_httpwww_orienteering_orgdatastandard3_0AssignedFee', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2825, 6), )

    
    AssignedFee = property(__AssignedFee.value, __AssignedFee.set, None, '\n            Defines the fees that the team member has been assigned.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ServiceRequest uses Python identifier ServiceRequest
    __ServiceRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest'), 'ServiceRequest', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceResult_httpwww_orienteering_orgdatastandard3_0ServiceRequest', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2832, 6), )

    
    ServiceRequest = property(__ServiceRequest.value, __ServiceRequest.set, None, '\n            Defines the services requested by the team member.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceResult_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2839, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute raceNumber uses Python identifier raceNumber
    __raceNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'raceNumber'), 'raceNumber', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberRaceResult_raceNumber', pyxb.binding.datatypes.integer)
    __raceNumber._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2847, 4)
    __raceNumber._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2847, 4)
    
    raceNumber = property(__raceNumber.value, __raceNumber.set, None, '\n          The ordinal number of the race that the information belongs to for a multi-race event, starting at 1.\n        ')

    _ElementMap.update({
        __Leg.name() : __Leg,
        __LegOrder.name() : __LegOrder,
        __BibNumber.name() : __BibNumber,
        __StartTime.name() : __StartTime,
        __FinishTime.name() : __FinishTime,
        __Time.name() : __Time,
        __TimeBehind.name() : __TimeBehind,
        __Position.name() : __Position,
        __Status.name() : __Status,
        __Score.name() : __Score,
        __OverallResult.name() : __OverallResult,
        __Course.name() : __Course,
        __SplitTime.name() : __SplitTime,
        __ControlAnswer.name() : __ControlAnswer,
        __Route.name() : __Route,
        __ControlCard.name() : __ControlCard,
        __AssignedFee.name() : __AssignedFee,
        __ServiceRequest.name() : __ServiceRequest,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __raceNumber.name() : __raceNumber
    })
_module_typeBindings.TeamMemberRaceResult = TeamMemberRaceResult
Namespace.addCategoryObject('typeBinding', 'TeamMemberRaceResult', TeamMemberRaceResult)


# Complex type {http://www.orienteering.org/datastandard/3.0}OverallResult with content type ELEMENT_ONLY
class OverallResult (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.orienteering.org/datastandard/3.0}OverallResult with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OverallResult')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2856, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Time uses Python identifier Time
    __Time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Time'), 'Time', '__httpwww_orienteering_orgdatastandard3_0_OverallResult_httpwww_orienteering_orgdatastandard3_0Time', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2858, 6), )

    
    Time = property(__Time.value, __Time.set, None, '\n            The time, in seconds, that is shown in the result list. Fractions of seconds (e.g. 258.7) may be used if the time resolution is higher than one second.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}TimeBehind uses Python identifier TimeBehind
    __TimeBehind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TimeBehind'), 'TimeBehind', '__httpwww_orienteering_orgdatastandard3_0_OverallResult_httpwww_orienteering_orgdatastandard3_0TimeBehind', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2865, 6), )

    
    TimeBehind = property(__TimeBehind.value, __TimeBehind.set, None, '\n            The time, in seconds, that the the person or team is behind the leader or winner. Fractions of seconds (e.g. 258.7) may be used if the time resolution is higher than one second.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Position uses Python identifier Position
    __Position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Position'), 'Position', '__httpwww_orienteering_orgdatastandard3_0_OverallResult_httpwww_orienteering_orgdatastandard3_0Position', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2872, 6), )

    
    Position = property(__Position.value, __Position.set, None, '\n            The position in the result list for the person or team that the result belongs to. This element should only be present when the Status element is set to OK.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Status uses Python identifier Status
    __Status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Status'), 'Status', '__httpwww_orienteering_orgdatastandard3_0_OverallResult_httpwww_orienteering_orgdatastandard3_0Status', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2879, 6), )

    
    Status = property(__Status.value, __Status.set, None, '\n            The status of the result.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Score uses Python identifier Score
    __Score = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Score'), 'Score', '__httpwww_orienteering_orgdatastandard3_0_OverallResult_httpwww_orienteering_orgdatastandard3_0Score', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2886, 6), )

    
    Score = property(__Score.value, __Score.set, None, '\n            Any scores that are attached to the result, e.g. World Ranking points.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_OverallResult_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2893, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    _ElementMap.update({
        __Time.name() : __Time,
        __TimeBehind.name() : __TimeBehind,
        __Position.name() : __Position,
        __Status.name() : __Status,
        __Score.name() : __Score,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OverallResult = OverallResult
Namespace.addCategoryObject('typeBinding', 'OverallResult', OverallResult)


# Complex type {http://www.orienteering.org/datastandard/3.0}ControlAnswer with content type ELEMENT_ONLY
class ControlAnswer (pyxb.binding.basis.complexTypeDefinition):
    """
        Defines the the selected answer, the correct answer and the time used on a Trail-O control.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ControlAnswer')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3018, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Answer uses Python identifier Answer
    __Answer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Answer'), 'Answer', '__httpwww_orienteering_orgdatastandard3_0_ControlAnswer_httpwww_orienteering_orgdatastandard3_0Answer', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3025, 6), )

    
    Answer = property(__Answer.value, __Answer.set, None, '\n            The answer that the competitor selected. If the competitor did not give any answer, use an empty string.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}CorrectAnswer uses Python identifier CorrectAnswer
    __CorrectAnswer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CorrectAnswer'), 'CorrectAnswer', '__httpwww_orienteering_orgdatastandard3_0_ControlAnswer_httpwww_orienteering_orgdatastandard3_0CorrectAnswer', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3032, 6), )

    
    CorrectAnswer = property(__CorrectAnswer.value, __CorrectAnswer.set, None, '\n            The correct answer. If no answer is correct, use an empty string.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Time uses Python identifier Time
    __Time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Time'), 'Time', '__httpwww_orienteering_orgdatastandard3_0_ControlAnswer_httpwww_orienteering_orgdatastandard3_0Time', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3039, 6), )

    
    Time = property(__Time.value, __Time.set, None, '\n            The time in seconds used to give the answer, in case of a timed control. Fractions of seconds (e.g. 258.7) may be used if the time resolution is higher than one second.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_ControlAnswer_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3046, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    _ElementMap.update({
        __Answer.name() : __Answer,
        __CorrectAnswer.name() : __CorrectAnswer,
        __Time.name() : __Time,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ControlAnswer = ControlAnswer
Namespace.addCategoryObject('typeBinding', 'ControlAnswer', ControlAnswer)


# Complex type {http://www.orienteering.org/datastandard/3.0}Route with content type SIMPLE
class Route (pyxb.binding.basis.complexTypeDefinition):
    """
        Defines a route, i.e. a number of geographical positions (waypoints) describing a competitor's navigation throughout a course.

        As routes contain large amounts of information, a compact storage format is utilized to keep the overall file size small. A route is stored as a base64-encoded byte sequence of waypoints. A waypoint is represented as described below. All multi-byte data types are stored in big-endian byte order (most significant byte first). Typically, a one-hour route with one-second waypoint recording interval occupies around 20 kilobytes.


        Waypoint header byte
        ====================
        Each waypoint byte sequence starts with a waypoint header byte:
        Waypoint header byte, bit 1: Waypoint type. 0 for normal waypoint, 1 for interruption waypoint. An interruption waypoint is a waypoint that is the last waypoint before an interruption in the route occurs, e.g. due to a satellite signal receiving failure. The last waypoint of a route should be a normal waypoint, not an interruption waypoint.
        Waypoint header byte, bits 2 and 3: Time storage mode. For a description of the time storage modes, see below.
        Bit 2   Bit 3   Time storage mode
        0      0      full storage mode (6 bytes)
        1      0      milliseconds delta storage mode (2 bytes)
        0      1      seconds delta storage mode (1 byte)
        Waypoint header byte, bits 4 and 5: Position storage mode (latitude, longitude, and altitude (if present)). For a description of the position storage modes, see below.
        Bit 4   Bit 5   Position storage mode
        0      0      full storage mode (4 + 4 (+ 3) bytes for latitude, longitude and altitude (if present))
        1      0      big delta delta storage mode (2 + 2 (+ 1) bytes)
        0      1      small delta storage mode (1 + 1 (+ 1) bytes)
        Waypoint header byte, bit 6: Altitude presence. 0 if an altitude value is not present, 1 if it is present.
        Waypoint header byte, bit 7: Unused, always 0.
        Waypoint header byte, bit 8: Unused, always 0.


        Time byte sequence
        ==================
        After the waypoint byte comes the time byte sequence. Depending on the time storage mode defined in the waypoint header, the time byte sequence is either 6 bytes (full), 2 bytes (milliseconds delta) or 1 byte (seconds delta) long.

        Full storage mode
        -----------------
        The following 6 bytes are an unsigned 48-bit integer defining the waypoint's time as the number of milliseconds (1/1000 seconds) since January 1, 1900, 00:00:00 UTC.

        Milliseconds delta storage mode
        -------------------------------
        The following 2 bytes are an unsigned 16-bit integer defining the waypoint's time as the number of milliseconds to add to the last waypoint's time.

        Seconds delta storage mode
        --------------------------
        The following byte is an unsigned 8-bit integer defining the waypoint's time as the number of seconds to add to the last waypoint's time. This storage mody can only be used when the difference to the last waypoint's time is an integer value.

        Consequently:
        - seconds delta storage mode is used when the waypoint's time is less than 256 seconds later than the last waypoint's time, and the difference between the times is an integer value.
        - milliseconds delta storage mode is used when the waypoint's time is less than 65.536 seconds later than the last waypoint's time
        - otherwise, full storage mode is used
        The time of the first waypoint of a route is always stored in full storage mode.


        Position byte sequence
        ======================
        Next, the position byte sequence appears: latitude, longitude and (if present) altitude bytes. Depending on the position storage mode defined in the waypoint header, the position byte sequence is either 4 + 4 (+ 3) bytes (full), 2 + 2 (+ 1) bytes (big delta) or 1 + 1 (+ 1) bytes (small delta) long.

        Full storage mode
        -----------------
        The first 4 bytes are a signed 32-bit integer defining the waypoint's latitude as microdegrees (1/1000000 degrees) relative to the equator. A negative value implies a latitude south of the equator. A microdegree is approximately equivalent to 0.1 meters.
        The following 4 bytes are a signed 32-bit integer defining the waypoint's latitude as microdegrees (1/1000000 degrees) relative to the Greenwich meridian. A negative value implies a longitude west of the Greenwich meridian. A microdegree is approximately equivalent to 0.1 meters at the equator and infinitely small at the poles.
        If the altitude presence bit in the waypoint header bit is set to 1, the following 3 bytes are a signed 24-bit integer defining the waypoint's altitude as decimeters (1/10 meters) relative to the sea level.

        Big delta storage mode
        ----------------------
        The first 2 bytes are a signed 16-bit integer defining the waypoint's latitude as the number of microdegrees to add to the last waypoint's latitude.
        The following 2 bytes are a signed 16-bit integer defining the waypoint's longitude as the number of microdegrees to add to the last waypoint's longitude.
        If the altitude presence bit in the waypoint header bit is set to 1, the following byte is a signed 8-bit integer defining the waypoint's altitude as the number of decimeters to add to the last waypoint's altitude.

        Small delta storage mode
        ----------------------
        The first byte is a signed 8-bit integer defining the waypoint's latitude as the number of microdegrees to add to the last waypoint's latitude.
        The following byte is a signed 8-bit integer defining the waypoint's longitude as the number of microdegrees to add to the last waypoint's longitude.
        If the altitude presence bit in the waypoint header bit is set to 1, the following byte is a signed 8-bit integer defining the waypoint's altitude as the number of decimeters to add to the last waypoint's altitude.

        Consequently:
        - small delta storage mode is used when the waypoint's latitude and longitude is within -0.000128 to 0.000127 degrees from the last waypoint's latitude, and when the altitude is not present or is within -12.8 to 12.7 meters from the last waypoint's altitude
        - big delta storage mode is used when the waypoint's latitude and longitude is within -0.032768 to 0.032767 degrees from the last waypoint's latitude, and when the altitude is not present or is within -12.8 to 12.7 meters from the last waypoint's altitude
        - otherwise, full storage mode is used
        The position of the first waypoint of a route is always stored in full storage mode.

        Code libraries for reading and writing route data are found at http://www.orienteering.org/datastandard/3.0/Libraries.zip.
      """
    _TypeDefinition = pyxb.binding.datatypes.base64Binary
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Route')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3119, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.base64Binary
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Route = Route
Namespace.addCategoryObject('typeBinding', 'Route', Route)


# Complex type {http://www.orienteering.org/datastandard/3.0}Leg with content type ELEMENT_ONLY
class Leg (pyxb.binding.basis.complexTypeDefinition):
    """
        Defines extra information for a relay leg.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Leg')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3205, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httpwww_orienteering_orgdatastandard3_0_Leg_httpwww_orienteering_orgdatastandard3_0Name', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3212, 6), )

    
    Name = property(__Name.value, __Name.set, None, '\n            The name of the leg, if not sequentially named.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_Leg_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3219, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute minNumberOfCompetitors uses Python identifier minNumberOfCompetitors
    __minNumberOfCompetitors = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'minNumberOfCompetitors'), 'minNumberOfCompetitors', '__httpwww_orienteering_orgdatastandard3_0_Leg_minNumberOfCompetitors', pyxb.binding.datatypes.integer, unicode_default='1')
    __minNumberOfCompetitors._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3227, 4)
    __minNumberOfCompetitors._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3227, 4)
    
    minNumberOfCompetitors = property(__minNumberOfCompetitors.value, __minNumberOfCompetitors.set, None, '\n          The minimum number of competitors in case of a parallel leg.\n        ')

    
    # Attribute maxNumberOfCompetitors uses Python identifier maxNumberOfCompetitors
    __maxNumberOfCompetitors = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'maxNumberOfCompetitors'), 'maxNumberOfCompetitors', '__httpwww_orienteering_orgdatastandard3_0_Leg_maxNumberOfCompetitors', pyxb.binding.datatypes.integer, unicode_default='1')
    __maxNumberOfCompetitors._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3234, 4)
    __maxNumberOfCompetitors._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3234, 4)
    
    maxNumberOfCompetitors = property(__maxNumberOfCompetitors.value, __maxNumberOfCompetitors.set, None, '\n          The maximum number of competitors in case of a parallel leg.\n        ')

    _ElementMap.update({
        __Name.name() : __Name,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __minNumberOfCompetitors.name() : __minNumberOfCompetitors,
        __maxNumberOfCompetitors.name() : __maxNumberOfCompetitors
    })
_module_typeBindings.Leg = Leg
Namespace.addCategoryObject('typeBinding', 'Leg', Leg)


# Complex type {http://www.orienteering.org/datastandard/3.0}GeoPosition with content type EMPTY
class GeoPosition (pyxb.binding.basis.complexTypeDefinition):
    """
        Defines a geographical position, e.g. of a control.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GeoPosition')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3303, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute lng uses Python identifier lng
    __lng = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lng'), 'lng', '__httpwww_orienteering_orgdatastandard3_0_GeoPosition_lng', pyxb.binding.datatypes.double, required=True)
    __lng._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3309, 4)
    __lng._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3309, 4)
    
    lng = property(__lng.value, __lng.set, None, '\n          The longitude.\n        ')

    
    # Attribute lat uses Python identifier lat
    __lat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lat'), 'lat', '__httpwww_orienteering_orgdatastandard3_0_GeoPosition_lat', pyxb.binding.datatypes.double, required=True)
    __lat._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3316, 4)
    __lat._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3316, 4)
    
    lat = property(__lat.value, __lat.set, None, '\n          The latitude.\n        ')

    
    # Attribute alt uses Python identifier alt
    __alt = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'alt'), 'alt', '__httpwww_orienteering_orgdatastandard3_0_GeoPosition_alt', pyxb.binding.datatypes.double)
    __alt._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3323, 4)
    __alt._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3323, 4)
    
    alt = property(__alt.value, __alt.set, None, '\n          The altitude (elevation above sea level), in meters.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lng.name() : __lng,
        __lat.name() : __lat,
        __alt.name() : __alt
    })
_module_typeBindings.GeoPosition = GeoPosition
Namespace.addCategoryObject('typeBinding', 'GeoPosition', GeoPosition)


# Complex type {http://www.orienteering.org/datastandard/3.0}Map with content type ELEMENT_ONLY
class Map (pyxb.binding.basis.complexTypeDefinition):
    """
        Map information, used in course setting software with regard to the "real" map.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Map')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3332, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__httpwww_orienteering_orgdatastandard3_0_Map_httpwww_orienteering_orgdatastandard3_0Id', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3339, 6), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Image uses Python identifier Image
    __Image = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Image'), 'Image', '__httpwww_orienteering_orgdatastandard3_0_Map_httpwww_orienteering_orgdatastandard3_0Image', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3340, 6), )

    
    Image = property(__Image.value, __Image.set, None, '\n            The map image.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Scale uses Python identifier Scale
    __Scale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Scale'), 'Scale', '__httpwww_orienteering_orgdatastandard3_0_Map_httpwww_orienteering_orgdatastandard3_0Scale', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3347, 6), )

    
    Scale = property(__Scale.value, __Scale.set, None, '\n            The denominator of the scale of the map. 1:15000 should be represented as 15000.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}MapPositionTopLeft uses Python identifier MapPositionTopLeft
    __MapPositionTopLeft = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MapPositionTopLeft'), 'MapPositionTopLeft', '__httpwww_orienteering_orgdatastandard3_0_Map_httpwww_orienteering_orgdatastandard3_0MapPositionTopLeft', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3354, 6), )

    
    MapPositionTopLeft = property(__MapPositionTopLeft.value, __MapPositionTopLeft.set, None, "\n            The position of the map's top left corner given in the map's coordinate system, usually (0, 0).\n          ")

    
    # Element {http://www.orienteering.org/datastandard/3.0}MapPositionBottomRight uses Python identifier MapPositionBottomRight
    __MapPositionBottomRight = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MapPositionBottomRight'), 'MapPositionBottomRight', '__httpwww_orienteering_orgdatastandard3_0_Map_httpwww_orienteering_orgdatastandard3_0MapPositionBottomRight', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3361, 6), )

    
    MapPositionBottomRight = property(__MapPositionBottomRight.value, __MapPositionBottomRight.set, None, "\n            The position of the map's bottom right corner given in the map's coordinate system.\n          ")

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_Map_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3368, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    _ElementMap.update({
        __Id.name() : __Id,
        __Image.name() : __Image,
        __Scale.name() : __Scale,
        __MapPositionTopLeft.name() : __MapPositionTopLeft,
        __MapPositionBottomRight.name() : __MapPositionBottomRight,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Map = Map
Namespace.addCategoryObject('typeBinding', 'Map', Map)


# Complex type {http://www.orienteering.org/datastandard/3.0}Image with content type SIMPLE
class Image (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.orienteering.org/datastandard/3.0}Image with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.base64Binary
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Image')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3378, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.base64Binary
    
    # Attribute url uses Python identifier url
    __url = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'url'), 'url', '__httpwww_orienteering_orgdatastandard3_0_Image_url', pyxb.binding.datatypes.string)
    __url._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3386, 8)
    __url._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3386, 8)
    
    url = property(__url.value, __url.set, None, '\n              The url to the image if it is stored externally (i.e. not as base64-encoded binary data).\n            ')

    
    # Attribute mediaType uses Python identifier mediaType
    __mediaType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mediaType'), 'mediaType', '__httpwww_orienteering_orgdatastandard3_0_Image_mediaType', pyxb.binding.datatypes.string, required=True)
    __mediaType._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3393, 8)
    __mediaType._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3393, 8)
    
    mediaType = property(__mediaType.value, __mediaType.set, None, '\n              The type of the image file, e.g. image/jpeg. Refer to http://en.wikipedia.org/wiki/Internet_media_type#Type_image for available media types.\n            ')

    
    # Attribute width uses Python identifier width
    __width = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'width'), 'width', '__httpwww_orienteering_orgdatastandard3_0_Image_width', pyxb.binding.datatypes.integer)
    __width._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3400, 8)
    __width._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3400, 8)
    
    width = property(__width.value, __width.set, None, '\n              The width of the image in pixels.\n            ')

    
    # Attribute height uses Python identifier height
    __height = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'height'), 'height', '__httpwww_orienteering_orgdatastandard3_0_Image_height', pyxb.binding.datatypes.integer)
    __height._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3407, 8)
    __height._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3407, 8)
    
    height = property(__height.value, __height.set, None, '\n              The height of the image in pixels.\n            ')

    
    # Attribute resolution uses Python identifier resolution
    __resolution = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'resolution'), 'resolution', '__httpwww_orienteering_orgdatastandard3_0_Image_resolution', pyxb.binding.datatypes.double)
    __resolution._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3414, 8)
    __resolution._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3414, 8)
    
    resolution = property(__resolution.value, __resolution.set, None, '\n              The resolution of the image in dpi.\n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __url.name() : __url,
        __mediaType.name() : __mediaType,
        __width.name() : __width,
        __height.name() : __height,
        __resolution.name() : __resolution
    })
_module_typeBindings.Image = Image
Namespace.addCategoryObject('typeBinding', 'Image', Image)


# Complex type {http://www.orienteering.org/datastandard/3.0}RaceCourseData with content type ELEMENT_ONLY
class RaceCourseData (pyxb.binding.basis.complexTypeDefinition):
    """
        This element defines all the control and course information for a race.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RaceCourseData')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3472, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Map uses Python identifier Map
    __Map = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Map'), 'Map', '__httpwww_orienteering_orgdatastandard3_0_RaceCourseData_httpwww_orienteering_orgdatastandard3_0Map', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3479, 6), )

    
    Map = property(__Map.value, __Map.set, None, '\n            The map(s) used in this race. Usually just one map, but different courses may use different scales and/or areas.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Control uses Python identifier Control
    __Control = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Control'), 'Control', '__httpwww_orienteering_orgdatastandard3_0_RaceCourseData_httpwww_orienteering_orgdatastandard3_0Control', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3486, 6), )

    
    Control = property(__Control.value, __Control.set, None, '\n            All controls of the race.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Course uses Python identifier Course
    __Course = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Course'), 'Course', '__httpwww_orienteering_orgdatastandard3_0_RaceCourseData_httpwww_orienteering_orgdatastandard3_0Course', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3493, 6), )

    
    Course = property(__Course.value, __Course.set, None, '\n            All courses of the race.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ClassCourseAssignment uses Python identifier ClassCourseAssignment
    __ClassCourseAssignment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ClassCourseAssignment'), 'ClassCourseAssignment', '__httpwww_orienteering_orgdatastandard3_0_RaceCourseData_httpwww_orienteering_orgdatastandard3_0ClassCourseAssignment', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3500, 6), )

    
    ClassCourseAssignment = property(__ClassCourseAssignment.value, __ClassCourseAssignment.set, None, '\n            The assignment of courses to classes.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}PersonCourseAssignment uses Python identifier PersonCourseAssignment
    __PersonCourseAssignment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PersonCourseAssignment'), 'PersonCourseAssignment', '__httpwww_orienteering_orgdatastandard3_0_RaceCourseData_httpwww_orienteering_orgdatastandard3_0PersonCourseAssignment', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3507, 6), )

    
    PersonCourseAssignment = property(__PersonCourseAssignment.value, __PersonCourseAssignment.set, None, '\n            The assignment of courses to individual competitors.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}TeamCourseAssignment uses Python identifier TeamCourseAssignment
    __TeamCourseAssignment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TeamCourseAssignment'), 'TeamCourseAssignment', '__httpwww_orienteering_orgdatastandard3_0_RaceCourseData_httpwww_orienteering_orgdatastandard3_0TeamCourseAssignment', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3514, 6), )

    
    TeamCourseAssignment = property(__TeamCourseAssignment.value, __TeamCourseAssignment.set, None, '\n            The assignment of courses to relay team members teams.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_RaceCourseData_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3521, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute raceNumber uses Python identifier raceNumber
    __raceNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'raceNumber'), 'raceNumber', '__httpwww_orienteering_orgdatastandard3_0_RaceCourseData_raceNumber', pyxb.binding.datatypes.integer)
    __raceNumber._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3529, 4)
    __raceNumber._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3529, 4)
    
    raceNumber = property(__raceNumber.value, __raceNumber.set, None, '\n          The ordinal number of the race that the information belongs to for a multi-race event, starting at 1.\n        ')

    _ElementMap.update({
        __Map.name() : __Map,
        __Control.name() : __Control,
        __Course.name() : __Course,
        __ClassCourseAssignment.name() : __ClassCourseAssignment,
        __PersonCourseAssignment.name() : __PersonCourseAssignment,
        __TeamCourseAssignment.name() : __TeamCourseAssignment,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __raceNumber.name() : __raceNumber
    })
_module_typeBindings.RaceCourseData = RaceCourseData
Namespace.addCategoryObject('typeBinding', 'RaceCourseData', RaceCourseData)


# Complex type {http://www.orienteering.org/datastandard/3.0}ClassCourseAssignment with content type ELEMENT_ONLY
class ClassCourseAssignment (pyxb.binding.basis.complexTypeDefinition):
    """
        Element that connects a course with a class. Courses should be present in the RaceCourseData element and are matched on course name and/or course family. Classes are matched by 1) Id, 2) Name.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ClassCourseAssignment')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3538, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}ClassId uses Python identifier ClassId
    __ClassId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ClassId'), 'ClassId', '__httpwww_orienteering_orgdatastandard3_0_ClassCourseAssignment_httpwww_orienteering_orgdatastandard3_0ClassId', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3545, 6), )

    
    ClassId = property(__ClassId.value, __ClassId.set, None, '\n            The id of the class.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ClassName uses Python identifier ClassName
    __ClassName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ClassName'), 'ClassName', '__httpwww_orienteering_orgdatastandard3_0_ClassCourseAssignment_httpwww_orienteering_orgdatastandard3_0ClassName', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3552, 6), )

    
    ClassName = property(__ClassName.value, __ClassName.set, None, '\n            The name of the class.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}AllowedOnLeg uses Python identifier AllowedOnLeg
    __AllowedOnLeg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AllowedOnLeg'), 'AllowedOnLeg', '__httpwww_orienteering_orgdatastandard3_0_ClassCourseAssignment_httpwww_orienteering_orgdatastandard3_0AllowedOnLeg', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3559, 6), )

    
    AllowedOnLeg = property(__AllowedOnLeg.value, __AllowedOnLeg.set, None, '\n            The legs that the course can be assigned to in a relay class. This element can be omitted for individual classes.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}CourseName uses Python identifier CourseName
    __CourseName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CourseName'), 'CourseName', '__httpwww_orienteering_orgdatastandard3_0_ClassCourseAssignment_httpwww_orienteering_orgdatastandard3_0CourseName', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3566, 6), )

    
    CourseName = property(__CourseName.value, __CourseName.set, None, '\n            The name of the course.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}CourseFamily uses Python identifier CourseFamily
    __CourseFamily = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CourseFamily'), 'CourseFamily', '__httpwww_orienteering_orgdatastandard3_0_ClassCourseAssignment_httpwww_orienteering_orgdatastandard3_0CourseFamily', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3573, 6), )

    
    CourseFamily = property(__CourseFamily.value, __CourseFamily.set, None, '\n            The family or group of forked courses that the course is part of.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_ClassCourseAssignment_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3580, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute numberOfCompetitors uses Python identifier numberOfCompetitors
    __numberOfCompetitors = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'numberOfCompetitors'), 'numberOfCompetitors', '__httpwww_orienteering_orgdatastandard3_0_ClassCourseAssignment_numberOfCompetitors', pyxb.binding.datatypes.integer)
    __numberOfCompetitors._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3588, 4)
    __numberOfCompetitors._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3588, 4)
    
    numberOfCompetitors = property(__numberOfCompetitors.value, __numberOfCompetitors.set, None, '\n          The number of competitors in the class. A competitor corresponds to a person (if an individual event) or a team (if a team or relay event).\n        ')

    _ElementMap.update({
        __ClassId.name() : __ClassId,
        __ClassName.name() : __ClassName,
        __AllowedOnLeg.name() : __AllowedOnLeg,
        __CourseName.name() : __CourseName,
        __CourseFamily.name() : __CourseFamily,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __numberOfCompetitors.name() : __numberOfCompetitors
    })
_module_typeBindings.ClassCourseAssignment = ClassCourseAssignment
Namespace.addCategoryObject('typeBinding', 'ClassCourseAssignment', ClassCourseAssignment)


# Complex type {http://www.orienteering.org/datastandard/3.0}PersonCourseAssignment with content type ELEMENT_ONLY
class PersonCourseAssignment (pyxb.binding.basis.complexTypeDefinition):
    """
        Element that connects a course with an individual competitor. Courses should be present in the RaceCourseData element and are matched on course name and/or course family. Persons are matched by 1) BibNumber, 2) EntryId.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PersonCourseAssignment')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3597, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}EntryId uses Python identifier EntryId
    __EntryId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EntryId'), 'EntryId', '__httpwww_orienteering_orgdatastandard3_0_PersonCourseAssignment_httpwww_orienteering_orgdatastandard3_0EntryId', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3604, 6), )

    
    EntryId = property(__EntryId.value, __EntryId.set, None, "\n            The id corresponding to this person's entry in an EntryList.\n          ")

    
    # Element {http://www.orienteering.org/datastandard/3.0}BibNumber uses Python identifier BibNumber
    __BibNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BibNumber'), 'BibNumber', '__httpwww_orienteering_orgdatastandard3_0_PersonCourseAssignment_httpwww_orienteering_orgdatastandard3_0BibNumber', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3611, 6), )

    
    BibNumber = property(__BibNumber.value, __BibNumber.set, None, '\n            The bib number of the person.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}PersonName uses Python identifier PersonName
    __PersonName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PersonName'), 'PersonName', '__httpwww_orienteering_orgdatastandard3_0_PersonCourseAssignment_httpwww_orienteering_orgdatastandard3_0PersonName', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3618, 6), )

    
    PersonName = property(__PersonName.value, __PersonName.set, None, '\n            The name of the person.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ClassName uses Python identifier ClassName
    __ClassName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ClassName'), 'ClassName', '__httpwww_orienteering_orgdatastandard3_0_PersonCourseAssignment_httpwww_orienteering_orgdatastandard3_0ClassName', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3625, 6), )

    
    ClassName = property(__ClassName.value, __ClassName.set, None, '\n            The name of the class that the person belongs to.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}CourseName uses Python identifier CourseName
    __CourseName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CourseName'), 'CourseName', '__httpwww_orienteering_orgdatastandard3_0_PersonCourseAssignment_httpwww_orienteering_orgdatastandard3_0CourseName', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3632, 6), )

    
    CourseName = property(__CourseName.value, __CourseName.set, None, '\n            The name of the course.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}CourseFamily uses Python identifier CourseFamily
    __CourseFamily = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CourseFamily'), 'CourseFamily', '__httpwww_orienteering_orgdatastandard3_0_PersonCourseAssignment_httpwww_orienteering_orgdatastandard3_0CourseFamily', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3639, 6), )

    
    CourseFamily = property(__CourseFamily.value, __CourseFamily.set, None, '\n            The family or group of forked courses that the course is part of.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_PersonCourseAssignment_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3646, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    _ElementMap.update({
        __EntryId.name() : __EntryId,
        __BibNumber.name() : __BibNumber,
        __PersonName.name() : __PersonName,
        __ClassName.name() : __ClassName,
        __CourseName.name() : __CourseName,
        __CourseFamily.name() : __CourseFamily,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PersonCourseAssignment = PersonCourseAssignment
Namespace.addCategoryObject('typeBinding', 'PersonCourseAssignment', PersonCourseAssignment)


# Complex type {http://www.orienteering.org/datastandard/3.0}TeamCourseAssignment with content type ELEMENT_ONLY
class TeamCourseAssignment (pyxb.binding.basis.complexTypeDefinition):
    """
        Element that connects a number of team members in a relay team to a number of courses. Teams are matched by 1) BibNumber, 2) TeamName+ClassName.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TeamCourseAssignment')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3656, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}BibNumber uses Python identifier BibNumber
    __BibNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BibNumber'), 'BibNumber', '__httpwww_orienteering_orgdatastandard3_0_TeamCourseAssignment_httpwww_orienteering_orgdatastandard3_0BibNumber', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3663, 6), )

    
    BibNumber = property(__BibNumber.value, __BibNumber.set, None, '\n            The bib number of the team.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}TeamName uses Python identifier TeamName
    __TeamName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TeamName'), 'TeamName', '__httpwww_orienteering_orgdatastandard3_0_TeamCourseAssignment_httpwww_orienteering_orgdatastandard3_0TeamName', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3670, 6), )

    
    TeamName = property(__TeamName.value, __TeamName.set, None, '\n            The name of the team.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ClassName uses Python identifier ClassName
    __ClassName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ClassName'), 'ClassName', '__httpwww_orienteering_orgdatastandard3_0_TeamCourseAssignment_httpwww_orienteering_orgdatastandard3_0ClassName', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3677, 6), )

    
    ClassName = property(__ClassName.value, __ClassName.set, None, '\n            The name of the class that the team belongs to.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}TeamMemberCourseAssignment uses Python identifier TeamMemberCourseAssignment
    __TeamMemberCourseAssignment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TeamMemberCourseAssignment'), 'TeamMemberCourseAssignment', '__httpwww_orienteering_orgdatastandard3_0_TeamCourseAssignment_httpwww_orienteering_orgdatastandard3_0TeamMemberCourseAssignment', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3684, 6), )

    
    TeamMemberCourseAssignment = property(__TeamMemberCourseAssignment.value, __TeamMemberCourseAssignment.set, None, '\n            The assignment of courses to team members.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_TeamCourseAssignment_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3691, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    _ElementMap.update({
        __BibNumber.name() : __BibNumber,
        __TeamName.name() : __TeamName,
        __ClassName.name() : __ClassName,
        __TeamMemberCourseAssignment.name() : __TeamMemberCourseAssignment,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TeamCourseAssignment = TeamCourseAssignment
Namespace.addCategoryObject('typeBinding', 'TeamCourseAssignment', TeamCourseAssignment)


# Complex type {http://www.orienteering.org/datastandard/3.0}TeamMemberCourseAssignment with content type ELEMENT_ONLY
class TeamMemberCourseAssignment (pyxb.binding.basis.complexTypeDefinition):
    """
        Element that connects a course with a relay team member. Courses should be present in the RaceCourseData element and are matched on course name and/or course family. Team members are matched by 1) BibNumber, 2) Leg and LegOrder, 3) EntryId.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TeamMemberCourseAssignment')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3701, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}EntryId uses Python identifier EntryId
    __EntryId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EntryId'), 'EntryId', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberCourseAssignment_httpwww_orienteering_orgdatastandard3_0EntryId', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3708, 6), )

    
    EntryId = property(__EntryId.value, __EntryId.set, None, "\n            The id corresponding to this person's entry in an EntryList.\n          ")

    
    # Element {http://www.orienteering.org/datastandard/3.0}BibNumber uses Python identifier BibNumber
    __BibNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BibNumber'), 'BibNumber', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberCourseAssignment_httpwww_orienteering_orgdatastandard3_0BibNumber', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3715, 6), )

    
    BibNumber = property(__BibNumber.value, __BibNumber.set, None, '\n            The bib number of the person or the team that the person belongs to. Omit if the bib number is specified in the TeamCourseAssignment element.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Leg uses Python identifier Leg
    __Leg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Leg'), 'Leg', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberCourseAssignment_httpwww_orienteering_orgdatastandard3_0Leg', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3722, 6), )

    
    Leg = property(__Leg.value, __Leg.set, None, '\n            For relay entries, the number of the leg that the person is taking part in.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}LegOrder uses Python identifier LegOrder
    __LegOrder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LegOrder'), 'LegOrder', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberCourseAssignment_httpwww_orienteering_orgdatastandard3_0LegOrder', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3729, 6), )

    
    LegOrder = property(__LegOrder.value, __LegOrder.set, None, "\n            Defines the person's starting order within a team at a parallel relay leg.\n          ")

    
    # Element {http://www.orienteering.org/datastandard/3.0}TeamMemberName uses Python identifier TeamMemberName
    __TeamMemberName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TeamMemberName'), 'TeamMemberName', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberCourseAssignment_httpwww_orienteering_orgdatastandard3_0TeamMemberName', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3736, 6), )

    
    TeamMemberName = property(__TeamMemberName.value, __TeamMemberName.set, None, '\n            The name of the person.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}CourseName uses Python identifier CourseName
    __CourseName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CourseName'), 'CourseName', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberCourseAssignment_httpwww_orienteering_orgdatastandard3_0CourseName', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3743, 6), )

    
    CourseName = property(__CourseName.value, __CourseName.set, None, '\n            The name of the course.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}CourseFamily uses Python identifier CourseFamily
    __CourseFamily = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CourseFamily'), 'CourseFamily', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberCourseAssignment_httpwww_orienteering_orgdatastandard3_0CourseFamily', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3750, 6), )

    
    CourseFamily = property(__CourseFamily.value, __CourseFamily.set, None, '\n            The family or group of forked courses that the course is part of.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_TeamMemberCourseAssignment_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3757, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    _ElementMap.update({
        __EntryId.name() : __EntryId,
        __BibNumber.name() : __BibNumber,
        __Leg.name() : __Leg,
        __LegOrder.name() : __LegOrder,
        __TeamMemberName.name() : __TeamMemberName,
        __CourseName.name() : __CourseName,
        __CourseFamily.name() : __CourseFamily,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TeamMemberCourseAssignment = TeamMemberCourseAssignment
Namespace.addCategoryObject('typeBinding', 'TeamMemberCourseAssignment', TeamMemberCourseAssignment)


# Complex type {http://www.orienteering.org/datastandard/3.0}Course with content type ELEMENT_ONLY
class Course (pyxb.binding.basis.complexTypeDefinition):
    """
        Defines a course, i.e. a number of controls including start and finish.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Course')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3767, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__httpwww_orienteering_orgdatastandard3_0_Course_httpwww_orienteering_orgdatastandard3_0Id', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3774, 6), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httpwww_orienteering_orgdatastandard3_0_Course_httpwww_orienteering_orgdatastandard3_0Name', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3775, 6), )

    
    Name = property(__Name.value, __Name.set, None, '\n            The name of the course.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}CourseFamily uses Python identifier CourseFamily
    __CourseFamily = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CourseFamily'), 'CourseFamily', '__httpwww_orienteering_orgdatastandard3_0_Course_httpwww_orienteering_orgdatastandard3_0CourseFamily', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3782, 6), )

    
    CourseFamily = property(__CourseFamily.value, __CourseFamily.set, None, '\n            The family or group of forked courses that the course is part of.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Length uses Python identifier Length
    __Length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Length'), 'Length', '__httpwww_orienteering_orgdatastandard3_0_Course_httpwww_orienteering_orgdatastandard3_0Length', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3789, 6), )

    
    Length = property(__Length.value, __Length.set, None, '\n            The length of the course, in meters.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Climb uses Python identifier Climb
    __Climb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Climb'), 'Climb', '__httpwww_orienteering_orgdatastandard3_0_Course_httpwww_orienteering_orgdatastandard3_0Climb', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3796, 6), )

    
    Climb = property(__Climb.value, __Climb.set, None, '\n            The climb of the course, in meters, along the expected best route choice.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}CourseControl uses Python identifier CourseControl
    __CourseControl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CourseControl'), 'CourseControl', '__httpwww_orienteering_orgdatastandard3_0_Course_httpwww_orienteering_orgdatastandard3_0CourseControl', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3803, 6), )

    
    CourseControl = property(__CourseControl.value, __CourseControl.set, None, '\n            The controls, including start and finish, that the course is made up of.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}MapId uses Python identifier MapId
    __MapId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MapId'), 'MapId', '__httpwww_orienteering_orgdatastandard3_0_Course_httpwww_orienteering_orgdatastandard3_0MapId', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3810, 6), )

    
    MapId = property(__MapId.value, __MapId.set, None, '\n            The id of the map used for this course.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_Course_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3817, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute numberOfCompetitors uses Python identifier numberOfCompetitors
    __numberOfCompetitors = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'numberOfCompetitors'), 'numberOfCompetitors', '__httpwww_orienteering_orgdatastandard3_0_Course_numberOfCompetitors', pyxb.binding.datatypes.integer)
    __numberOfCompetitors._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3825, 4)
    __numberOfCompetitors._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3825, 4)
    
    numberOfCompetitors = property(__numberOfCompetitors.value, __numberOfCompetitors.set, None, '\n          The number of competitors that this course has been assigned to.\n        ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_Course_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3832, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3832, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __Name.name() : __Name,
        __CourseFamily.name() : __CourseFamily,
        __Length.name() : __Length,
        __Climb.name() : __Climb,
        __CourseControl.name() : __CourseControl,
        __MapId.name() : __MapId,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __numberOfCompetitors.name() : __numberOfCompetitors,
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.Course = Course
Namespace.addCategoryObject('typeBinding', 'Course', Course)


# Complex type {http://www.orienteering.org/datastandard/3.0}SimpleCourse with content type ELEMENT_ONLY
class SimpleCourse (pyxb.binding.basis.complexTypeDefinition):
    """
        Defines a course, excluding controls.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleCourse')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3835, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__httpwww_orienteering_orgdatastandard3_0_SimpleCourse_httpwww_orienteering_orgdatastandard3_0Id', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3842, 6), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httpwww_orienteering_orgdatastandard3_0_SimpleCourse_httpwww_orienteering_orgdatastandard3_0Name', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3843, 6), )

    
    Name = property(__Name.value, __Name.set, None, '\n            The name of the course.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}CourseFamily uses Python identifier CourseFamily
    __CourseFamily = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CourseFamily'), 'CourseFamily', '__httpwww_orienteering_orgdatastandard3_0_SimpleCourse_httpwww_orienteering_orgdatastandard3_0CourseFamily', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3850, 6), )

    
    CourseFamily = property(__CourseFamily.value, __CourseFamily.set, None, '\n            The family or group of forked courses that the course is part of.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Length uses Python identifier Length
    __Length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Length'), 'Length', '__httpwww_orienteering_orgdatastandard3_0_SimpleCourse_httpwww_orienteering_orgdatastandard3_0Length', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3857, 6), )

    
    Length = property(__Length.value, __Length.set, None, '\n            The length of the course, in meters.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Climb uses Python identifier Climb
    __Climb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Climb'), 'Climb', '__httpwww_orienteering_orgdatastandard3_0_SimpleCourse_httpwww_orienteering_orgdatastandard3_0Climb', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3864, 6), )

    
    Climb = property(__Climb.value, __Climb.set, None, '\n            The climb of the course, in meters, along the expected best route choice.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}NumberOfControls uses Python identifier NumberOfControls
    __NumberOfControls = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumberOfControls'), 'NumberOfControls', '__httpwww_orienteering_orgdatastandard3_0_SimpleCourse_httpwww_orienteering_orgdatastandard3_0NumberOfControls', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3871, 6), )

    
    NumberOfControls = property(__NumberOfControls.value, __NumberOfControls.set, None, '\n            The number of controls in the course, excluding start and finish.\n          ')

    _ElementMap.update({
        __Id.name() : __Id,
        __Name.name() : __Name,
        __CourseFamily.name() : __CourseFamily,
        __Length.name() : __Length,
        __Climb.name() : __Climb,
        __NumberOfControls.name() : __NumberOfControls
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SimpleCourse = SimpleCourse
Namespace.addCategoryObject('typeBinding', 'SimpleCourse', SimpleCourse)


# Complex type {http://www.orienteering.org/datastandard/3.0}Service with content type ELEMENT_ONLY
class Service (pyxb.binding.basis.complexTypeDefinition):
    """
        Defines a general purpose service request, e.g. for rental card or accomodation.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Service')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4005, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__httpwww_orienteering_orgdatastandard3_0_Service_httpwww_orienteering_orgdatastandard3_0Id', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4012, 6), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httpwww_orienteering_orgdatastandard3_0_Service_httpwww_orienteering_orgdatastandard3_0Name', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4013, 6), )

    
    Name = property(__Name.value, __Name.set, None, '\n            The name of the service.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Fee uses Python identifier Fee
    __Fee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Fee'), 'Fee', '__httpwww_orienteering_orgdatastandard3_0_Service_httpwww_orienteering_orgdatastandard3_0Fee', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4020, 6), )

    
    Fee = property(__Fee.value, __Fee.set, None, '\n            The fees attached to this service.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Description'), 'Description', '__httpwww_orienteering_orgdatastandard3_0_Service_httpwww_orienteering_orgdatastandard3_0Description', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4027, 6), )

    
    Description = property(__Description.value, __Description.set, None, '\n            A further description of the service than the Name element gives.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}MaxNumber uses Python identifier MaxNumber
    __MaxNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MaxNumber'), 'MaxNumber', '__httpwww_orienteering_orgdatastandard3_0_Service_httpwww_orienteering_orgdatastandard3_0MaxNumber', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4034, 6), )

    
    MaxNumber = property(__MaxNumber.value, __MaxNumber.set, None, '\n            The maximum number of instances of this service that are available. Omit this element if there is no such limit.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}RequestedNumber uses Python identifier RequestedNumber
    __RequestedNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RequestedNumber'), 'RequestedNumber', '__httpwww_orienteering_orgdatastandard3_0_Service_httpwww_orienteering_orgdatastandard3_0RequestedNumber', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4041, 6), )

    
    RequestedNumber = property(__RequestedNumber.value, __RequestedNumber.set, None, '\n            The number of instances of this service that has been requested.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_Service_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4048, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_orienteering_orgdatastandard3_0_Service_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4056, 4)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4056, 4)
    
    type = property(__type.value, __type.set, None, '\n          Used to mark special services, e.g. rental cards whose fees that are to be used in entry scenarios.\n        ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_Service_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4063, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4063, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __Name.name() : __Name,
        __Fee.name() : __Fee,
        __Description.name() : __Description,
        __MaxNumber.name() : __MaxNumber,
        __RequestedNumber.name() : __RequestedNumber,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __type.name() : __type,
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.Service = Service
Namespace.addCategoryObject('typeBinding', 'Service', Service)


# Complex type {http://www.orienteering.org/datastandard/3.0}OrganisationServiceRequest with content type ELEMENT_ONLY
class OrganisationServiceRequest (pyxb.binding.basis.complexTypeDefinition):
    """
        Service requests made by an organisation.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrganisationServiceRequest')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4066, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Organisation uses Python identifier Organisation
    __Organisation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), 'Organisation', '__httpwww_orienteering_orgdatastandard3_0_OrganisationServiceRequest_httpwww_orienteering_orgdatastandard3_0Organisation', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4073, 6), )

    
    Organisation = property(__Organisation.value, __Organisation.set, None, '\n            The organisation that made the requests.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ServiceRequest uses Python identifier ServiceRequest
    __ServiceRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest'), 'ServiceRequest', '__httpwww_orienteering_orgdatastandard3_0_OrganisationServiceRequest_httpwww_orienteering_orgdatastandard3_0ServiceRequest', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4080, 6), )

    
    ServiceRequest = property(__ServiceRequest.value, __ServiceRequest.set, None, '\n            The service requests that the organisation made.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}PersonServiceRequest uses Python identifier PersonServiceRequest
    __PersonServiceRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PersonServiceRequest'), 'PersonServiceRequest', '__httpwww_orienteering_orgdatastandard3_0_OrganisationServiceRequest_httpwww_orienteering_orgdatastandard3_0PersonServiceRequest', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4087, 6), )

    
    PersonServiceRequest = property(__PersonServiceRequest.value, __PersonServiceRequest.set, None, '\n            The service requests made by persons representing the organisation.\n          ')

    _ElementMap.update({
        __Organisation.name() : __Organisation,
        __ServiceRequest.name() : __ServiceRequest,
        __PersonServiceRequest.name() : __PersonServiceRequest
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OrganisationServiceRequest = OrganisationServiceRequest
Namespace.addCategoryObject('typeBinding', 'OrganisationServiceRequest', OrganisationServiceRequest)


# Complex type {http://www.orienteering.org/datastandard/3.0}PersonServiceRequest with content type ELEMENT_ONLY
class PersonServiceRequest (pyxb.binding.basis.complexTypeDefinition):
    """
        Service requests made by a person.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PersonServiceRequest')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4097, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Person uses Python identifier Person
    __Person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Person'), 'Person', '__httpwww_orienteering_orgdatastandard3_0_PersonServiceRequest_httpwww_orienteering_orgdatastandard3_0Person', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4104, 6), )

    
    Person = property(__Person.value, __Person.set, None, '\n            The person that made the requests.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ServiceRequest uses Python identifier ServiceRequest
    __ServiceRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest'), 'ServiceRequest', '__httpwww_orienteering_orgdatastandard3_0_PersonServiceRequest_httpwww_orienteering_orgdatastandard3_0ServiceRequest', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4111, 6), )

    
    ServiceRequest = property(__ServiceRequest.value, __ServiceRequest.set, None, '\n            The service requests.\n          ')

    _ElementMap.update({
        __Person.name() : __Person,
        __ServiceRequest.name() : __ServiceRequest
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PersonServiceRequest = PersonServiceRequest
Namespace.addCategoryObject('typeBinding', 'PersonServiceRequest', PersonServiceRequest)


# Complex type {http://www.orienteering.org/datastandard/3.0}ServiceRequest with content type ELEMENT_ONLY
class ServiceRequest (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.orienteering.org/datastandard/3.0}ServiceRequest with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4121, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__httpwww_orienteering_orgdatastandard3_0_ServiceRequest_httpwww_orienteering_orgdatastandard3_0Id', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4123, 6), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Service uses Python identifier Service
    __Service = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Service'), 'Service', '__httpwww_orienteering_orgdatastandard3_0_ServiceRequest_httpwww_orienteering_orgdatastandard3_0Service', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4124, 6), )

    
    Service = property(__Service.value, __Service.set, None, '\n            The service that is requested.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}RequestedQuantity uses Python identifier RequestedQuantity
    __RequestedQuantity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RequestedQuantity'), 'RequestedQuantity', '__httpwww_orienteering_orgdatastandard3_0_ServiceRequest_httpwww_orienteering_orgdatastandard3_0RequestedQuantity', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4131, 6), )

    
    RequestedQuantity = property(__RequestedQuantity.value, __RequestedQuantity.set, None, '\n            The quantity (number of instances) of the service that is requested.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}DeliveredQuantity uses Python identifier DeliveredQuantity
    __DeliveredQuantity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DeliveredQuantity'), 'DeliveredQuantity', '__httpwww_orienteering_orgdatastandard3_0_ServiceRequest_httpwww_orienteering_orgdatastandard3_0DeliveredQuantity', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4138, 6), )

    
    DeliveredQuantity = property(__DeliveredQuantity.value, __DeliveredQuantity.set, None, '\n            The quantity (number of instances) of the service that has been delivered. Can differ from RequestedQuantity when the available number of instances of a service is limited.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Comment'), 'Comment', '__httpwww_orienteering_orgdatastandard3_0_ServiceRequest_httpwww_orienteering_orgdatastandard3_0Comment', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4145, 6), )

    
    Comment = property(__Comment.value, __Comment.set, None, '\n            Any extra information or comment attached to the service request.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}AssignedFee uses Python identifier AssignedFee
    __AssignedFee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee'), 'AssignedFee', '__httpwww_orienteering_orgdatastandard3_0_ServiceRequest_httpwww_orienteering_orgdatastandard3_0AssignedFee', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4152, 6), )

    
    AssignedFee = property(__AssignedFee.value, __AssignedFee.set, None, '\n            The fees related to this service request.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_ServiceRequest_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4159, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_ServiceRequest_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4167, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4167, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __Service.name() : __Service,
        __RequestedQuantity.name() : __RequestedQuantity,
        __DeliveredQuantity.name() : __DeliveredQuantity,
        __Comment.name() : __Comment,
        __AssignedFee.name() : __AssignedFee,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.ServiceRequest = ServiceRequest
Namespace.addCategoryObject('typeBinding', 'ServiceRequest', ServiceRequest)


# Complex type {http://www.orienteering.org/datastandard/3.0}Account with content type SIMPLE
class Account (pyxb.binding.basis.complexTypeDefinition):
    """
        The bank account of an organisation or an event.
      """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Account')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4170, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_orienteering_orgdatastandard3_0_Account_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4178, 8)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4178, 8)
    
    type = property(__type.value, __type.set, None, '\n              The account type.\n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.Account = Account
Namespace.addCategoryObject('typeBinding', 'Account', Account)


# Complex type {http://www.orienteering.org/datastandard/3.0}Address with content type ELEMENT_ONLY
class Address (pyxb.binding.basis.complexTypeDefinition):
    """
        The postal address of a person or organisation.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Address')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4189, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}CareOf uses Python identifier CareOf
    __CareOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CareOf'), 'CareOf', '__httpwww_orienteering_orgdatastandard3_0_Address_httpwww_orienteering_orgdatastandard3_0CareOf', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4196, 6), )

    
    CareOf = property(__CareOf.value, __CareOf.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Street uses Python identifier Street
    __Street = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Street'), 'Street', '__httpwww_orienteering_orgdatastandard3_0_Address_httpwww_orienteering_orgdatastandard3_0Street', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4197, 6), )

    
    Street = property(__Street.value, __Street.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}ZipCode uses Python identifier ZipCode
    __ZipCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ZipCode'), 'ZipCode', '__httpwww_orienteering_orgdatastandard3_0_Address_httpwww_orienteering_orgdatastandard3_0ZipCode', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4198, 6), )

    
    ZipCode = property(__ZipCode.value, __ZipCode.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}City uses Python identifier City
    __City = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'City'), 'City', '__httpwww_orienteering_orgdatastandard3_0_Address_httpwww_orienteering_orgdatastandard3_0City', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4199, 6), )

    
    City = property(__City.value, __City.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}State uses Python identifier State
    __State = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'State'), 'State', '__httpwww_orienteering_orgdatastandard3_0_Address_httpwww_orienteering_orgdatastandard3_0State', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4200, 6), )

    
    State = property(__State.value, __State.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Country uses Python identifier Country
    __Country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Country'), 'Country', '__httpwww_orienteering_orgdatastandard3_0_Address_httpwww_orienteering_orgdatastandard3_0Country', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4201, 6), )

    
    Country = property(__Country.value, __Country.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_orienteering_orgdatastandard3_0_Address_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4203, 4)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4203, 4)
    
    type = property(__type.value, __type.set, None, '\n          The address type, e.g. visitor address or invoice address.\n        ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_Address_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4210, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4210, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __CareOf.name() : __CareOf,
        __Street.name() : __Street,
        __ZipCode.name() : __ZipCode,
        __City.name() : __City,
        __State.name() : __State,
        __Country.name() : __Country
    })
    _AttributeMap.update({
        __type.name() : __type,
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.Address = Address
Namespace.addCategoryObject('typeBinding', 'Address', Address)


# Complex type {http://www.orienteering.org/datastandard/3.0}Country with content type SIMPLE
class Country (pyxb.binding.basis.complexTypeDefinition):
    """
        Defines the name of the country.
      """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Country')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4213, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code'), 'code', '__httpwww_orienteering_orgdatastandard3_0_Country_code', pyxb.binding.datatypes.string, required=True)
    __code._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4221, 8)
    __code._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4221, 8)
    
    code = property(__code.value, __code.set, None, "\n              The International Olympic Committee's 3-letter code of the country as stated in http://en.wikipedia.org/wiki/List_of_IOC_country_codes. Note that several of the IOC codes are different from the standard ISO 3166-1 alpha-3 codes.\n            ")

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __code.name() : __code
    })
_module_typeBindings.Country = Country
Namespace.addCategoryObject('typeBinding', 'Country', Country)


# Complex type {http://www.orienteering.org/datastandard/3.0}DateAndOptionalTime with content type ELEMENT_ONLY
class DateAndOptionalTime (pyxb.binding.basis.complexTypeDefinition):
    """
        Defines a point in time which either is known by date and time, or just by date. May be used for event dates, when the event date is decided before the time of the first start.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DateAndOptionalTime')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4257, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Date uses Python identifier Date
    __Date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Date'), 'Date', '__httpwww_orienteering_orgdatastandard3_0_DateAndOptionalTime_httpwww_orienteering_orgdatastandard3_0Date', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4264, 6), )

    
    Date = property(__Date.value, __Date.set, None, '\n            The date part, expressed in ISO 8601 format.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Time uses Python identifier Time
    __Time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Time'), 'Time', '__httpwww_orienteering_orgdatastandard3_0_DateAndOptionalTime_httpwww_orienteering_orgdatastandard3_0Time', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4271, 6), )

    
    Time = property(__Time.value, __Time.set, None, '\n            The time part, expressed in ISO 8601 format.\n          ')

    _ElementMap.update({
        __Date.name() : __Date,
        __Time.name() : __Time
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DateAndOptionalTime = DateAndOptionalTime
Namespace.addCategoryObject('typeBinding', 'DateAndOptionalTime', DateAndOptionalTime)


# Complex type {http://www.orienteering.org/datastandard/3.0}LanguageString with content type SIMPLE
class LanguageString (pyxb.binding.basis.complexTypeDefinition):
    """
        Defines a text that is given in a particular language.
      """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LanguageString')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4281, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute language uses Python identifier language
    __language = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'language'), 'language', '__httpwww_orienteering_orgdatastandard3_0_LanguageString_language', pyxb.binding.datatypes.string)
    __language._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4289, 8)
    __language._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4289, 8)
    
    language = property(__language.value, __language.set, None, '\n              The ISO 639-1 two-letter code of the language as stated in http://www.loc.gov/standards/iso639-2/php/code_list.php.\n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __language.name() : __language
    })
_module_typeBindings.LanguageString = LanguageString
Namespace.addCategoryObject('typeBinding', 'LanguageString', LanguageString)


# Complex type {http://www.orienteering.org/datastandard/3.0}Extensions with content type ELEMENT_ONLY
class Extensions (pyxb.binding.basis.complexTypeDefinition):
    """
        Container element that is used to add custom elements from other schemas.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Extensions')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4300, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Extensions = Extensions
Namespace.addCategoryObject('typeBinding', 'Extensions', Extensions)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (BaseMessageElement):
    """
        A list of competitors. This is used to exchange a "brutto" list of possible competitors. This should not be used to exchange entries; use EntryList instead.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 71, 4)
    _ElementMap = BaseMessageElement._ElementMap.copy()
    _AttributeMap = BaseMessageElement._AttributeMap.copy()
    # Base type is BaseMessageElement
    
    # Element {http://www.orienteering.org/datastandard/3.0}Competitor uses Python identifier Competitor
    __Competitor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Competitor'), 'Competitor', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_httpwww_orienteering_orgdatastandard3_0Competitor', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 75, 12), )

    
    Competitor = property(__Competitor.value, __Competitor.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 76, 12), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n                  Container element for custom elements from other schemas.\n                ')

    
    # Attribute iofVersion inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    
    # Attribute createTime inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    
    # Attribute creator inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    _ElementMap.update({
        __Competitor.name() : __Competitor,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (BaseMessageElement):
    """
        A list of organisations, including address and contact information.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 95, 4)
    _ElementMap = BaseMessageElement._ElementMap.copy()
    _AttributeMap = BaseMessageElement._AttributeMap.copy()
    # Base type is BaseMessageElement
    
    # Element {http://www.orienteering.org/datastandard/3.0}Organisation uses Python identifier Organisation
    __Organisation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), 'Organisation', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON__httpwww_orienteering_orgdatastandard3_0Organisation', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 99, 12), )

    
    Organisation = property(__Organisation.value, __Organisation.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON__httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 100, 12), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n                  Container element for custom elements from other schemas.\n                ')

    
    # Attribute iofVersion inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    
    # Attribute createTime inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    
    # Attribute creator inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    _ElementMap.update({
        __Organisation.name() : __Organisation,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (BaseMessageElement):
    """
        A list of events. This can be used to exchange fixtures.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 119, 4)
    _ElementMap = BaseMessageElement._ElementMap.copy()
    _AttributeMap = BaseMessageElement._AttributeMap.copy()
    # Base type is BaseMessageElement
    
    # Element {http://www.orienteering.org/datastandard/3.0}Event uses Python identifier Event
    __Event = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Event'), 'Event', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_2_httpwww_orienteering_orgdatastandard3_0Event', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 123, 12), )

    
    Event = property(__Event.value, __Event.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_2_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 124, 12), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n                  Container element for custom elements from other schemas.\n                ')

    
    # Attribute iofVersion inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    
    # Attribute createTime inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    
    # Attribute creator inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    _ElementMap.update({
        __Event.name() : __Event,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (BaseMessageElement):
    """
        A list of classes.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 143, 4)
    _ElementMap = BaseMessageElement._ElementMap.copy()
    _AttributeMap = BaseMessageElement._AttributeMap.copy()
    # Base type is BaseMessageElement
    
    # Element {http://www.orienteering.org/datastandard/3.0}Class uses Python identifier Class
    __Class = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Class'), 'Class', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_3_httpwww_orienteering_orgdatastandard3_0Class', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 147, 12), )

    
    Class = property(__Class.value, __Class.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_3_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 148, 12), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n                  Container element for custom elements from other schemas.\n                ')

    
    # Attribute iofVersion inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    
    # Attribute createTime inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    
    # Attribute creator inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    _ElementMap.update({
        __Class.name() : __Class,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (BaseMessageElement):
    """
        A list of persons and/or teams which are registered for a particular event.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 167, 4)
    _ElementMap = BaseMessageElement._ElementMap.copy()
    _AttributeMap = BaseMessageElement._AttributeMap.copy()
    # Base type is BaseMessageElement
    
    # Element {http://www.orienteering.org/datastandard/3.0}Event uses Python identifier Event
    __Event = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Event'), 'Event', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_4_httpwww_orienteering_orgdatastandard3_0Event', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 171, 12), )

    
    Event = property(__Event.value, __Event.set, None, '\n                  The event that the entry list belongs to.\n                ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}TeamEntry uses Python identifier TeamEntry
    __TeamEntry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TeamEntry'), 'TeamEntry', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_4_httpwww_orienteering_orgdatastandard3_0TeamEntry', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 178, 12), )

    
    TeamEntry = property(__TeamEntry.value, __TeamEntry.set, None, '\n                  The teams registered for the event.\n                ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}PersonEntry uses Python identifier PersonEntry
    __PersonEntry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PersonEntry'), 'PersonEntry', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_4_httpwww_orienteering_orgdatastandard3_0PersonEntry', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 185, 12), )

    
    PersonEntry = property(__PersonEntry.value, __PersonEntry.set, None, '\n                  The individual competitors registered for the event.\n                ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_4_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 192, 12), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n                  Container element for custom elements from other schemas.\n                ')

    
    # Attribute iofVersion inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    
    # Attribute createTime inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    
    # Attribute creator inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    _ElementMap.update({
        __Event.name() : __Event,
        __TeamEntry.name() : __TeamEntry,
        __PersonEntry.name() : __PersonEntry,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (BaseMessageElement):
    """
        This element defines all the control and course information for an event or race. Used when transferring courses from course-setting software to event administration software.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 211, 4)
    _ElementMap = BaseMessageElement._ElementMap.copy()
    _AttributeMap = BaseMessageElement._AttributeMap.copy()
    # Base type is BaseMessageElement
    
    # Element {http://www.orienteering.org/datastandard/3.0}Event uses Python identifier Event
    __Event = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Event'), 'Event', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_5_httpwww_orienteering_orgdatastandard3_0Event', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 215, 12), )

    
    Event = property(__Event.value, __Event.set, None, '\n                  The event that the course data belongs to.\n                ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}RaceCourseData uses Python identifier RaceCourseData
    __RaceCourseData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RaceCourseData'), 'RaceCourseData', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_5_httpwww_orienteering_orgdatastandard3_0RaceCourseData', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 222, 12), )

    
    RaceCourseData = property(__RaceCourseData.value, __RaceCourseData.set, None, '\n                  The course data for each race; one element per race in the event.\n                ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_5_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 229, 12), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n                  Container element for custom elements from other schemas.\n                ')

    
    # Attribute iofVersion inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    
    # Attribute createTime inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    
    # Attribute creator inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    _ElementMap.update({
        __Event.name() : __Event,
        __RaceCourseData.name() : __RaceCourseData,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (BaseMessageElement):
    """
        Contains information about the start lists for the classes in an event.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 248, 4)
    _ElementMap = BaseMessageElement._ElementMap.copy()
    _AttributeMap = BaseMessageElement._AttributeMap.copy()
    # Base type is BaseMessageElement
    
    # Element {http://www.orienteering.org/datastandard/3.0}Event uses Python identifier Event
    __Event = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Event'), 'Event', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_6_httpwww_orienteering_orgdatastandard3_0Event', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 252, 12), )

    
    Event = property(__Event.value, __Event.set, None, '\n                  The event that the start lists belong to.\n                ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ClassStart uses Python identifier ClassStart
    __ClassStart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ClassStart'), 'ClassStart', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_6_httpwww_orienteering_orgdatastandard3_0ClassStart', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 259, 12), )

    
    ClassStart = property(__ClassStart.value, __ClassStart.set, None, '\n                  Start lists for the classes in the event.\n                ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_6_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 266, 12), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n                  Container element for custom elements from other schemas.\n                ')

    
    # Attribute iofVersion inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    
    # Attribute createTime inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    
    # Attribute creator inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    _ElementMap.update({
        __Event.name() : __Event,
        __ClassStart.name() : __ClassStart,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (BaseMessageElement):
    """
        Contains information about the result lists for the classes in an event.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 285, 4)
    _ElementMap = BaseMessageElement._ElementMap.copy()
    _AttributeMap = BaseMessageElement._AttributeMap.copy()
    # Base type is BaseMessageElement
    
    # Element {http://www.orienteering.org/datastandard/3.0}Event uses Python identifier Event
    __Event = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Event'), 'Event', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_7_httpwww_orienteering_orgdatastandard3_0Event', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 289, 12), )

    
    Event = property(__Event.value, __Event.set, None, '\n                  The event that the result lists belong to.\n                ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ClassResult uses Python identifier ClassResult
    __ClassResult = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ClassResult'), 'ClassResult', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_7_httpwww_orienteering_orgdatastandard3_0ClassResult', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 296, 12), )

    
    ClassResult = property(__ClassResult.value, __ClassResult.set, None, '\n                  Result lists for the classes in the event.\n                ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_7_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 303, 12), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n                  Container element for custom elements from other schemas.\n                ')

    
    # Attribute iofVersion inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    
    # Attribute createTime inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    
    # Attribute creator inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'status'), 'status', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_7_status', _module_typeBindings.STD_ANON, unicode_default='Complete')
    __status._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 311, 10)
    __status._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 311, 10)
    
    status = property(__status.value, __status.set, None, '\n                The status of the result list.\n              ')

    _ElementMap.update({
        __Event.name() : __Event,
        __ClassResult.name() : __ClassResult,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __status.name() : __status
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (BaseMessageElement):
    """
        A list of service requests.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 354, 4)
    _ElementMap = BaseMessageElement._ElementMap.copy()
    _AttributeMap = BaseMessageElement._AttributeMap.copy()
    # Base type is BaseMessageElement
    
    # Element {http://www.orienteering.org/datastandard/3.0}Event uses Python identifier Event
    __Event = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Event'), 'Event', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_8_httpwww_orienteering_orgdatastandard3_0Event', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 358, 12), )

    
    Event = property(__Event.value, __Event.set, None, '\n                  The event that the service requests are valid for.\n                ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}OrganisationServiceRequest uses Python identifier OrganisationServiceRequest
    __OrganisationServiceRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OrganisationServiceRequest'), 'OrganisationServiceRequest', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_8_httpwww_orienteering_orgdatastandard3_0OrganisationServiceRequest', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 365, 12), )

    
    OrganisationServiceRequest = property(__OrganisationServiceRequest.value, __OrganisationServiceRequest.set, None, '\n                  Service requests made by organisations.\n                ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}PersonServiceRequest uses Python identifier PersonServiceRequest
    __PersonServiceRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PersonServiceRequest'), 'PersonServiceRequest', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_8_httpwww_orienteering_orgdatastandard3_0PersonServiceRequest', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 372, 12), )

    
    PersonServiceRequest = property(__PersonServiceRequest.value, __PersonServiceRequest.set, None, '\n                  Service requests made by persons.\n                ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_8_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 379, 12), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n                  Container element for custom elements from other schemas.\n                ')

    
    # Attribute iofVersion inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    
    # Attribute createTime inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    
    # Attribute creator inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    _ElementMap.update({
        __Event.name() : __Event,
        __OrganisationServiceRequest.name() : __OrganisationServiceRequest,
        __PersonServiceRequest.name() : __PersonServiceRequest,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (BaseMessageElement):
    """
        Defines control card ownership, e.g. for rental control card handling purposes.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 398, 4)
    _ElementMap = BaseMessageElement._ElementMap.copy()
    _AttributeMap = BaseMessageElement._AttributeMap.copy()
    # Base type is BaseMessageElement
    
    # Element {http://www.orienteering.org/datastandard/3.0}Owner uses Python identifier Owner
    __Owner = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Owner'), 'Owner', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_9_httpwww_orienteering_orgdatastandard3_0Owner', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 402, 12), )

    
    Owner = property(__Owner.value, __Owner.set, None, '\n                  The owner of the control cards.\n                ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ControlCard uses Python identifier ControlCard
    __ControlCard = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ControlCard'), 'ControlCard', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_9_httpwww_orienteering_orgdatastandard3_0ControlCard', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 409, 12), )

    
    ControlCard = property(__ControlCard.value, __ControlCard.set, None, '\n                  The control cards.\n                ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_9_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 416, 12), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n                  Container element for custom elements from other schemas.\n                ')

    
    # Attribute iofVersion inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    
    # Attribute createTime inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    
    # Attribute creator inherited from {http://www.orienteering.org/datastandard/3.0}BaseMessageElement
    _ElementMap.update({
        __Owner.name() : __Owner,
        __ControlCard.name() : __ControlCard,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type {http://www.orienteering.org/datastandard/3.0}Person with content type ELEMENT_ONLY
class Person (pyxb.binding.basis.complexTypeDefinition):
    """
        Represents a person. This could either be a competitor (see the Competitor element) or contact persons in an organisation (see the Organisation element).
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Person')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 451, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__httpwww_orienteering_orgdatastandard3_0_Person_httpwww_orienteering_orgdatastandard3_0Id', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 458, 6), )

    
    Id = property(__Id.value, __Id.set, None, '\n            The identifier of the person. Multiple identifiers can be included, e.g. when there is both a World Ranking Event identifier and a national database identifier for the person.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httpwww_orienteering_orgdatastandard3_0_Person_httpwww_orienteering_orgdatastandard3_0Name', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 465, 6), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}BirthDate uses Python identifier BirthDate
    __BirthDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BirthDate'), 'BirthDate', '__httpwww_orienteering_orgdatastandard3_0_Person_httpwww_orienteering_orgdatastandard3_0BirthDate', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 466, 6), )

    
    BirthDate = property(__BirthDate.value, __BirthDate.set, None, '\n            The date when the person was born, expressed in ISO 8601 format.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Nationality uses Python identifier Nationality
    __Nationality = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nationality'), 'Nationality', '__httpwww_orienteering_orgdatastandard3_0_Person_httpwww_orienteering_orgdatastandard3_0Nationality', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 473, 6), )

    
    Nationality = property(__Nationality.value, __Nationality.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Address uses Python identifier Address
    __Address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Address'), 'Address', '__httpwww_orienteering_orgdatastandard3_0_Person_httpwww_orienteering_orgdatastandard3_0Address', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 474, 6), )

    
    Address = property(__Address.value, __Address.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Contact uses Python identifier Contact
    __Contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Contact'), 'Contact', '__httpwww_orienteering_orgdatastandard3_0_Person_httpwww_orienteering_orgdatastandard3_0Contact', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 475, 6), )

    
    Contact = property(__Contact.value, __Contact.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_Person_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 476, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute sex uses Python identifier sex
    __sex = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sex'), 'sex', '__httpwww_orienteering_orgdatastandard3_0_Person_sex', _module_typeBindings.STD_ANON_)
    __sex._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 484, 4)
    __sex._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 484, 4)
    
    sex = property(__sex.value, __sex.set, None, None)

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_Person_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 492, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 492, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __Name.name() : __Name,
        __BirthDate.name() : __BirthDate,
        __Nationality.name() : __Nationality,
        __Address.name() : __Address,
        __Contact.name() : __Contact,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __sex.name() : __sex,
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.Person = Person
Namespace.addCategoryObject('typeBinding', 'Person', Person)


# Complex type {http://www.orienteering.org/datastandard/3.0}Organisation with content type ELEMENT_ONLY
class Organisation (pyxb.binding.basis.complexTypeDefinition):
    """
        Information about an organisation, i.e. address, contact person(s) etc. An organisation is a general term including federations, clubs, etc.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Organisation')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 582, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__httpwww_orienteering_orgdatastandard3_0_Organisation_httpwww_orienteering_orgdatastandard3_0Id', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 589, 6), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httpwww_orienteering_orgdatastandard3_0_Organisation_httpwww_orienteering_orgdatastandard3_0Name', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 590, 6), )

    
    Name = property(__Name.value, __Name.set, None, '\n            The full name of the organisation.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ShortName uses Python identifier ShortName
    __ShortName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ShortName'), 'ShortName', '__httpwww_orienteering_orgdatastandard3_0_Organisation_httpwww_orienteering_orgdatastandard3_0ShortName', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 597, 6), )

    
    ShortName = property(__ShortName.value, __ShortName.set, None, '\n            The short (abbreviated) name of the organisation.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}MediaName uses Python identifier MediaName
    __MediaName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MediaName'), 'MediaName', '__httpwww_orienteering_orgdatastandard3_0_Organisation_httpwww_orienteering_orgdatastandard3_0MediaName', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 604, 6), )

    
    MediaName = property(__MediaName.value, __MediaName.set, None, '\n            The name of the organisation as appearing in result lists targeted to media.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ParentOrganisationId uses Python identifier ParentOrganisationId
    __ParentOrganisationId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ParentOrganisationId'), 'ParentOrganisationId', '__httpwww_orienteering_orgdatastandard3_0_Organisation_httpwww_orienteering_orgdatastandard3_0ParentOrganisationId', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 611, 6), )

    
    ParentOrganisationId = property(__ParentOrganisationId.value, __ParentOrganisationId.set, None, '\n            The id of the parent of this organisation, e.g. a regional organisation for a club.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Country uses Python identifier Country
    __Country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Country'), 'Country', '__httpwww_orienteering_orgdatastandard3_0_Organisation_httpwww_orienteering_orgdatastandard3_0Country', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 618, 6), )

    
    Country = property(__Country.value, __Country.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Address uses Python identifier Address
    __Address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Address'), 'Address', '__httpwww_orienteering_orgdatastandard3_0_Organisation_httpwww_orienteering_orgdatastandard3_0Address', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 619, 6), )

    
    Address = property(__Address.value, __Address.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Contact uses Python identifier Contact
    __Contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Contact'), 'Contact', '__httpwww_orienteering_orgdatastandard3_0_Organisation_httpwww_orienteering_orgdatastandard3_0Contact', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 620, 6), )

    
    Contact = property(__Contact.value, __Contact.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Position uses Python identifier Position
    __Position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Position'), 'Position', '__httpwww_orienteering_orgdatastandard3_0_Organisation_httpwww_orienteering_orgdatastandard3_0Position', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 621, 6), )

    
    Position = property(__Position.value, __Position.set, None, '\n            The geographical location of the organisation, e.g. a city center, an office or a club house.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Account uses Python identifier Account
    __Account = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Account'), 'Account', '__httpwww_orienteering_orgdatastandard3_0_Organisation_httpwww_orienteering_orgdatastandard3_0Account', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 628, 6), )

    
    Account = property(__Account.value, __Account.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Role uses Python identifier Role
    __Role = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Role'), 'Role', '__httpwww_orienteering_orgdatastandard3_0_Organisation_httpwww_orienteering_orgdatastandard3_0Role', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 629, 6), )

    
    Role = property(__Role.value, __Role.set, None, '\n            Persons having certain roles within the organisation, e.g. chairman, secretary, and treasurer.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Logotype uses Python identifier Logotype
    __Logotype = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Logotype'), 'Logotype', '__httpwww_orienteering_orgdatastandard3_0_Organisation_httpwww_orienteering_orgdatastandard3_0Logotype', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 636, 6), )

    
    Logotype = property(__Logotype.value, __Logotype.set, None, '\n            The logotype for the organisation. Multiple logotypes may be included; in this case, make sure to include width and height attributes.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_Organisation_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 643, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_orienteering_orgdatastandard3_0_Organisation_type', _module_typeBindings.STD_ANON_2)
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 651, 4)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 651, 4)
    
    type = property(__type.value, __type.set, None, '\n          The hierarchical level or type of an organisation.\n        ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_Organisation_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 671, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 671, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __Name.name() : __Name,
        __ShortName.name() : __ShortName,
        __MediaName.name() : __MediaName,
        __ParentOrganisationId.name() : __ParentOrganisationId,
        __Country.name() : __Country,
        __Address.name() : __Address,
        __Contact.name() : __Contact,
        __Position.name() : __Position,
        __Account.name() : __Account,
        __Role.name() : __Role,
        __Logotype.name() : __Logotype,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __type.name() : __type,
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.Organisation = Organisation
Namespace.addCategoryObject('typeBinding', 'Organisation', Organisation)


# Complex type {http://www.orienteering.org/datastandard/3.0}EventURL with content type SIMPLE
class EventURL (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.orienteering.org/datastandard/3.0}EventURL with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EventURL')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 985, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_orienteering_orgdatastandard3_0_EventURL_type', _module_typeBindings.STD_ANON_3, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 988, 8)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 988, 8)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.EventURL = EventURL
Namespace.addCategoryObject('typeBinding', 'EventURL', EventURL)


# Complex type {http://www.orienteering.org/datastandard/3.0}Class with content type ELEMENT_ONLY
class Class (pyxb.binding.basis.complexTypeDefinition):
    """
        Defines a class in an event.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Class')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1080, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__httpwww_orienteering_orgdatastandard3_0_Class_httpwww_orienteering_orgdatastandard3_0Id', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1087, 6), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httpwww_orienteering_orgdatastandard3_0_Class_httpwww_orienteering_orgdatastandard3_0Name', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1088, 6), )

    
    Name = property(__Name.value, __Name.set, None, '\n            The name of the class.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ShortName uses Python identifier ShortName
    __ShortName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ShortName'), 'ShortName', '__httpwww_orienteering_orgdatastandard3_0_Class_httpwww_orienteering_orgdatastandard3_0ShortName', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1095, 6), )

    
    ShortName = property(__ShortName.value, __ShortName.set, None, '\n            The abbreviated name of a class, used when space is limited.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ClassType uses Python identifier ClassType
    __ClassType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ClassType'), 'ClassType', '__httpwww_orienteering_orgdatastandard3_0_Class_httpwww_orienteering_orgdatastandard3_0ClassType', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1102, 6), )

    
    ClassType = property(__ClassType.value, __ClassType.set, None, '\n            The class type(s) for the class.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Leg uses Python identifier Leg
    __Leg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Leg'), 'Leg', '__httpwww_orienteering_orgdatastandard3_0_Class_httpwww_orienteering_orgdatastandard3_0Leg', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1109, 6), )

    
    Leg = property(__Leg.value, __Leg.set, None, '\n            Information about the legs, if the class is a relay class. One Leg element per leg must be present.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}TeamFee uses Python identifier TeamFee
    __TeamFee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TeamFee'), 'TeamFee', '__httpwww_orienteering_orgdatastandard3_0_Class_httpwww_orienteering_orgdatastandard3_0TeamFee', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1116, 6), )

    
    TeamFee = property(__TeamFee.value, __TeamFee.set, None, '\n            The entry fees for a team as a whole taking part in this class. Use the Fee element to specify a fee for an individual competitor in the team. Use the TeamFee subelement of the RaceClass element to specify a fee on race level.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Fee uses Python identifier Fee
    __Fee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Fee'), 'Fee', '__httpwww_orienteering_orgdatastandard3_0_Class_httpwww_orienteering_orgdatastandard3_0Fee', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1123, 6), )

    
    Fee = property(__Fee.value, __Fee.set, None, '\n            The entry fees for an individual competitor taking part in the class. Use the TeamFee element to specify a fee for the team as a whole. Use the Fee subelement of the RaceClass element to specify a fee on race level.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Status uses Python identifier Status
    __Status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Status'), 'Status', '__httpwww_orienteering_orgdatastandard3_0_Class_httpwww_orienteering_orgdatastandard3_0Status', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1130, 6), )

    
    Status = property(__Status.value, __Status.set, None, '\n            The overall status of the class, e.g. if overall results should be considered invalid due to misplaced controls.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}RaceClass uses Python identifier RaceClass
    __RaceClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RaceClass'), 'RaceClass', '__httpwww_orienteering_orgdatastandard3_0_Class_httpwww_orienteering_orgdatastandard3_0RaceClass', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1137, 6), )

    
    RaceClass = property(__RaceClass.value, __RaceClass.set, None, '\n            Race-specific information for the class, e.g. course(s) assigned to the class.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}TooFewEntriesSubstituteClass uses Python identifier TooFewEntriesSubstituteClass
    __TooFewEntriesSubstituteClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TooFewEntriesSubstituteClass'), 'TooFewEntriesSubstituteClass', '__httpwww_orienteering_orgdatastandard3_0_Class_httpwww_orienteering_orgdatastandard3_0TooFewEntriesSubstituteClass', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1144, 6), )

    
    TooFewEntriesSubstituteClass = property(__TooFewEntriesSubstituteClass.value, __TooFewEntriesSubstituteClass.set, None, '\n            The class that competitors in this class should be transferred to if there are too few entries in this class.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}TooManyEntriesSubstituteClass uses Python identifier TooManyEntriesSubstituteClass
    __TooManyEntriesSubstituteClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TooManyEntriesSubstituteClass'), 'TooManyEntriesSubstituteClass', '__httpwww_orienteering_orgdatastandard3_0_Class_httpwww_orienteering_orgdatastandard3_0TooManyEntriesSubstituteClass', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1151, 6), )

    
    TooManyEntriesSubstituteClass = property(__TooManyEntriesSubstituteClass.value, __TooManyEntriesSubstituteClass.set, None, '\n            The class that competitors that are not qualified (e.g. due to too low ranking) should be transferred to if there are too many entries in this class.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_Class_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1158, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute minAge uses Python identifier minAge
    __minAge = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'minAge'), 'minAge', '__httpwww_orienteering_orgdatastandard3_0_Class_minAge', pyxb.binding.datatypes.integer)
    __minAge._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1166, 4)
    __minAge._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1166, 4)
    
    minAge = property(__minAge.value, __minAge.set, None, '\n          The lowest allowed age for a competitor taking part in the class.\n        ')

    
    # Attribute maxAge uses Python identifier maxAge
    __maxAge = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'maxAge'), 'maxAge', '__httpwww_orienteering_orgdatastandard3_0_Class_maxAge', pyxb.binding.datatypes.integer)
    __maxAge._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1173, 4)
    __maxAge._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1173, 4)
    
    maxAge = property(__maxAge.value, __maxAge.set, None, '\n          The highest allowed age for a competitor taking part in the class.\n        ')

    
    # Attribute sex uses Python identifier sex
    __sex = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sex'), 'sex', '__httpwww_orienteering_orgdatastandard3_0_Class_sex', _module_typeBindings.STD_ANON_4, unicode_default='B')
    __sex._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1180, 4)
    __sex._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1180, 4)
    
    sex = property(__sex.value, __sex.set, None, None)

    
    # Attribute minNumberOfTeamMembers uses Python identifier minNumberOfTeamMembers
    __minNumberOfTeamMembers = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'minNumberOfTeamMembers'), 'minNumberOfTeamMembers', '__httpwww_orienteering_orgdatastandard3_0_Class_minNumberOfTeamMembers', pyxb.binding.datatypes.integer, unicode_default='1')
    __minNumberOfTeamMembers._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1189, 4)
    __minNumberOfTeamMembers._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1189, 4)
    
    minNumberOfTeamMembers = property(__minNumberOfTeamMembers.value, __minNumberOfTeamMembers.set, None, '\n          The minimum number of members in a team taking part in the class, if the class is a team class.\n        ')

    
    # Attribute maxNumberOfTeamMembers uses Python identifier maxNumberOfTeamMembers
    __maxNumberOfTeamMembers = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'maxNumberOfTeamMembers'), 'maxNumberOfTeamMembers', '__httpwww_orienteering_orgdatastandard3_0_Class_maxNumberOfTeamMembers', pyxb.binding.datatypes.integer, unicode_default='1')
    __maxNumberOfTeamMembers._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1196, 4)
    __maxNumberOfTeamMembers._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1196, 4)
    
    maxNumberOfTeamMembers = property(__maxNumberOfTeamMembers.value, __maxNumberOfTeamMembers.set, None, '\n          The maximum number of members in a team taking part in the class, if the class is a team class.\n        ')

    
    # Attribute minTeamAge uses Python identifier minTeamAge
    __minTeamAge = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'minTeamAge'), 'minTeamAge', '__httpwww_orienteering_orgdatastandard3_0_Class_minTeamAge', pyxb.binding.datatypes.integer)
    __minTeamAge._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1203, 4)
    __minTeamAge._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1203, 4)
    
    minTeamAge = property(__minTeamAge.value, __minTeamAge.set, None, '\n          The lowest allowed age sum of the team members for a team taking part in the class.\n        ')

    
    # Attribute maxTeamAge uses Python identifier maxTeamAge
    __maxTeamAge = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'maxTeamAge'), 'maxTeamAge', '__httpwww_orienteering_orgdatastandard3_0_Class_maxTeamAge', pyxb.binding.datatypes.integer)
    __maxTeamAge._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1210, 4)
    __maxTeamAge._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1210, 4)
    
    maxTeamAge = property(__maxTeamAge.value, __maxTeamAge.set, None, '\n          The highest allowed age sum of the team members for a team taking part in the class.\n        ')

    
    # Attribute numberOfCompetitors uses Python identifier numberOfCompetitors
    __numberOfCompetitors = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'numberOfCompetitors'), 'numberOfCompetitors', '__httpwww_orienteering_orgdatastandard3_0_Class_numberOfCompetitors', pyxb.binding.datatypes.integer)
    __numberOfCompetitors._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1217, 4)
    __numberOfCompetitors._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1217, 4)
    
    numberOfCompetitors = property(__numberOfCompetitors.value, __numberOfCompetitors.set, None, '\n          The number of competitors in the class. A competitor corresponds to a person (if an individual event) or a team (if a team or relay event).\n        ')

    
    # Attribute maxNumberOfCompetitors uses Python identifier maxNumberOfCompetitors
    __maxNumberOfCompetitors = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'maxNumberOfCompetitors'), 'maxNumberOfCompetitors', '__httpwww_orienteering_orgdatastandard3_0_Class_maxNumberOfCompetitors', pyxb.binding.datatypes.integer)
    __maxNumberOfCompetitors._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1224, 4)
    __maxNumberOfCompetitors._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1224, 4)
    
    maxNumberOfCompetitors = property(__maxNumberOfCompetitors.value, __maxNumberOfCompetitors.set, None, '\n          The maximum number of competitors that are allowed to take part in the class. A competitor corresponds to a person (if an individual event) or a team (if a team or relay event). If the maximum number of competitors varies between races in a multi-day event, use the maxNumberOfCompetitors attribute in the RaceClass element.\n        ')

    
    # Attribute resultListMode uses Python identifier resultListMode
    __resultListMode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'resultListMode'), 'resultListMode', '__httpwww_orienteering_orgdatastandard3_0_Class_resultListMode', _module_typeBindings.STD_ANON_5, unicode_default='Default')
    __resultListMode._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1231, 4)
    __resultListMode._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1231, 4)
    
    resultListMode = property(__resultListMode.value, __resultListMode.set, None, '\n          Defines the kind of information to include in the result list, and how to sort it. For example, the result list of a beginner\'s class may include just "finished" or "did not finish" instead of the actual times.\n        ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_Class_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1263, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1263, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __Name.name() : __Name,
        __ShortName.name() : __ShortName,
        __ClassType.name() : __ClassType,
        __Leg.name() : __Leg,
        __TeamFee.name() : __TeamFee,
        __Fee.name() : __Fee,
        __Status.name() : __Status,
        __RaceClass.name() : __RaceClass,
        __TooFewEntriesSubstituteClass.name() : __TooFewEntriesSubstituteClass,
        __TooManyEntriesSubstituteClass.name() : __TooManyEntriesSubstituteClass,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __minAge.name() : __minAge,
        __maxAge.name() : __maxAge,
        __sex.name() : __sex,
        __minNumberOfTeamMembers.name() : __minNumberOfTeamMembers,
        __maxNumberOfTeamMembers.name() : __maxNumberOfTeamMembers,
        __minTeamAge.name() : __minTeamAge,
        __maxTeamAge.name() : __maxTeamAge,
        __numberOfCompetitors.name() : __numberOfCompetitors,
        __maxNumberOfCompetitors.name() : __maxNumberOfCompetitors,
        __resultListMode.name() : __resultListMode,
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.Class = Class
Namespace.addCategoryObject('typeBinding', 'Class', Class)


# Complex type {http://www.orienteering.org/datastandard/3.0}Fee with content type ELEMENT_ONLY
class Fee (pyxb.binding.basis.complexTypeDefinition):
    """
        A fee that applies when entering a class at a race or ordering a service.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Fee')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1457, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__httpwww_orienteering_orgdatastandard3_0_Fee_httpwww_orienteering_orgdatastandard3_0Id', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1464, 6), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://www.orienteering.org/datastandard/3.0}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httpwww_orienteering_orgdatastandard3_0_Fee_httpwww_orienteering_orgdatastandard3_0Name', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1465, 6), )

    
    Name = property(__Name.value, __Name.set, None, "\n            A describing name of the fee, e.g. 'Late entry fee'.\n          ")

    
    # Element {http://www.orienteering.org/datastandard/3.0}Amount uses Python identifier Amount
    __Amount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Amount'), 'Amount', '__httpwww_orienteering_orgdatastandard3_0_Fee_httpwww_orienteering_orgdatastandard3_0Amount', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1472, 6), )

    
    Amount = property(__Amount.value, __Amount.set, None, '\n            The fee amount, optionally including currency code. This element must not be present if a Percentage element exists.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}TaxableAmount uses Python identifier TaxableAmount
    __TaxableAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TaxableAmount'), 'TaxableAmount', '__httpwww_orienteering_orgdatastandard3_0_Fee_httpwww_orienteering_orgdatastandard3_0TaxableAmount', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1479, 6), )

    
    TaxableAmount = property(__TaxableAmount.value, __TaxableAmount.set, None, '\n            The fee amount that is taxable, i.e. considered when calculating taxes for an event. This element must not be present if a Percentage element exists, or if an Amount element does not exist.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Percentage uses Python identifier Percentage
    __Percentage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Percentage'), 'Percentage', '__httpwww_orienteering_orgdatastandard3_0_Fee_httpwww_orienteering_orgdatastandard3_0Percentage', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1486, 6), )

    
    Percentage = property(__Percentage.value, __Percentage.set, None, '\n            The percentage to increase or decrease already existing fees in a fee list with. This element must not be present if an Amount element exists.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}TaxablePercentage uses Python identifier TaxablePercentage
    __TaxablePercentage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TaxablePercentage'), 'TaxablePercentage', '__httpwww_orienteering_orgdatastandard3_0_Fee_httpwww_orienteering_orgdatastandard3_0TaxablePercentage', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1493, 6), )

    
    TaxablePercentage = property(__TaxablePercentage.value, __TaxablePercentage.set, None, '\n            The percentage to increase or decrease already existing taxable fees in a fee list with. This element must not be present if an Amount element exists, or if a Percentage element does not exist.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ValidFromTime uses Python identifier ValidFromTime
    __ValidFromTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValidFromTime'), 'ValidFromTime', '__httpwww_orienteering_orgdatastandard3_0_Fee_httpwww_orienteering_orgdatastandard3_0ValidFromTime', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1500, 6), )

    
    ValidFromTime = property(__ValidFromTime.value, __ValidFromTime.set, None, '\n            The time when the fee takes effect.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ValidToTime uses Python identifier ValidToTime
    __ValidToTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValidToTime'), 'ValidToTime', '__httpwww_orienteering_orgdatastandard3_0_Fee_httpwww_orienteering_orgdatastandard3_0ValidToTime', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1507, 6), )

    
    ValidToTime = property(__ValidToTime.value, __ValidToTime.set, None, '\n            The time when the fee expires.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}FromDateOfBirth uses Python identifier FromDateOfBirth
    __FromDateOfBirth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FromDateOfBirth'), 'FromDateOfBirth', '__httpwww_orienteering_orgdatastandard3_0_Fee_httpwww_orienteering_orgdatastandard3_0FromDateOfBirth', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1514, 6), )

    
    FromDateOfBirth = property(__FromDateOfBirth.value, __FromDateOfBirth.set, None, '\n            The start of the birth date interval that the fee should be applied to. Omit if no lower birth date restriction.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}ToDateOfBirth uses Python identifier ToDateOfBirth
    __ToDateOfBirth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ToDateOfBirth'), 'ToDateOfBirth', '__httpwww_orienteering_orgdatastandard3_0_Fee_httpwww_orienteering_orgdatastandard3_0ToDateOfBirth', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1521, 6), )

    
    ToDateOfBirth = property(__ToDateOfBirth.value, __ToDateOfBirth.set, None, '\n            The end of the birth date interval that the fee should be applied to. Omit if no upper birth date restriction.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_Fee_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1528, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_orienteering_orgdatastandard3_0_Fee_type', _module_typeBindings.STD_ANON_6, unicode_default='Normal')
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1536, 4)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1536, 4)
    
    type = property(__type.value, __type.set, None, '\n          The type of fee.\n        ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_Fee_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1561, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1561, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __Name.name() : __Name,
        __Amount.name() : __Amount,
        __TaxableAmount.name() : __TaxableAmount,
        __Percentage.name() : __Percentage,
        __TaxablePercentage.name() : __TaxablePercentage,
        __ValidFromTime.name() : __ValidFromTime,
        __ValidToTime.name() : __ValidToTime,
        __FromDateOfBirth.name() : __FromDateOfBirth,
        __ToDateOfBirth.name() : __ToDateOfBirth,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __type.name() : __type,
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.Fee = Fee
Namespace.addCategoryObject('typeBinding', 'Fee', Fee)


# Complex type {http://www.orienteering.org/datastandard/3.0}StartTimeAllocationRequest with content type ELEMENT_ONLY
class StartTimeAllocationRequest (pyxb.binding.basis.complexTypeDefinition):
    """
        Used to state start time allocation requests. It consists of a possible reference Organisation or Person and the allocation request, e.g. late start or grouped with the reference Organisation/Person. This way it is possible to state requests to the event organizer so that e.g. all members of an organisation has start times close to each other - or parents have start times far from each other. It is totally up to the event software and organizers whether they will support such requests.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StartTimeAllocationRequest')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1853, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Organisation uses Python identifier Organisation
    __Organisation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), 'Organisation', '__httpwww_orienteering_orgdatastandard3_0_StartTimeAllocationRequest_httpwww_orienteering_orgdatastandard3_0Organisation', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1860, 6), )

    
    Organisation = property(__Organisation.value, __Organisation.set, None, '\n            The reference organisation for the start time allocation request.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Person uses Python identifier Person
    __Person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Person'), 'Person', '__httpwww_orienteering_orgdatastandard3_0_StartTimeAllocationRequest_httpwww_orienteering_orgdatastandard3_0Person', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1867, 6), )

    
    Person = property(__Person.value, __Person.set, None, '\n            The reference person for the start time allocation request.\n          ')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_orienteering_orgdatastandard3_0_StartTimeAllocationRequest_type', _module_typeBindings.STD_ANON_7, unicode_default='Normal')
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1875, 4)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1875, 4)
    
    type = property(__type.value, __type.set, None, '\n          The type of start time allocation request.\n        ')

    _ElementMap.update({
        __Organisation.name() : __Organisation,
        __Person.name() : __Person
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.StartTimeAllocationRequest = StartTimeAllocationRequest
Namespace.addCategoryObject('typeBinding', 'StartTimeAllocationRequest', StartTimeAllocationRequest)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """
            The time, in seconds, that the the team member is behind the winner. Fractions of seconds (e.g. 258.7) may be used if the time resolution is higher than one second.
          """
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2709, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.double
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_10_type', _module_typeBindings.STD_ANON_8, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2712, 14)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2712, 14)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.CTD_ANON_10 = CTD_ANON_10


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """
            The position in the result list for the person that the result belongs to. This element should only be present when the Status element is set to OK.
          """
    _TypeDefinition = pyxb.binding.datatypes.integer
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2742, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.integer
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_orienteering_orgdatastandard3_0_CTD_ANON_11_type', _module_typeBindings.STD_ANON_9, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2745, 14)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2745, 14)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.CTD_ANON_11 = CTD_ANON_11


# Complex type {http://www.orienteering.org/datastandard/3.0}SplitTime with content type ELEMENT_ONLY
class SplitTime (pyxb.binding.basis.complexTypeDefinition):
    """
        Defines a split time at a control.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SplitTime')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3056, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}ControlCode uses Python identifier ControlCode
    __ControlCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ControlCode'), 'ControlCode', '__httpwww_orienteering_orgdatastandard3_0_SplitTime_httpwww_orienteering_orgdatastandard3_0ControlCode', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3063, 6), )

    
    ControlCode = property(__ControlCode.value, __ControlCode.set, None, '\n            The code of the control.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Time uses Python identifier Time
    __Time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Time'), 'Time', '__httpwww_orienteering_orgdatastandard3_0_SplitTime_httpwww_orienteering_orgdatastandard3_0Time', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3070, 6), )

    
    Time = property(__Time.value, __Time.set, None, '\n            The time, in seconds, elapsed from start to punching the control. Fractions of seconds (e.g. 258.7) may be used if the time resolution is higher than one second.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_SplitTime_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3077, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'status'), 'status', '__httpwww_orienteering_orgdatastandard3_0_SplitTime_status', _module_typeBindings.STD_ANON_10, unicode_default='OK')
    __status._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3085, 4)
    __status._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3085, 4)
    
    status = property(__status.value, __status.set, None, '\n          The status of the split time.\n        ')

    _ElementMap.update({
        __ControlCode.name() : __ControlCode,
        __Time.name() : __Time,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __status.name() : __status
    })
_module_typeBindings.SplitTime = SplitTime
Namespace.addCategoryObject('typeBinding', 'SplitTime', SplitTime)


# Complex type {http://www.orienteering.org/datastandard/3.0}Control with content type ELEMENT_ONLY
class Control (pyxb.binding.basis.complexTypeDefinition):
    """
        Defines a control, without any relationship to a particular course.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Control')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3243, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__httpwww_orienteering_orgdatastandard3_0_Control_httpwww_orienteering_orgdatastandard3_0Id', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3250, 6), )

    
    Id = property(__Id.value, __Id.set, None, '\n            The code of the control.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}PunchingUnitId uses Python identifier PunchingUnitId
    __PunchingUnitId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PunchingUnitId'), 'PunchingUnitId', '__httpwww_orienteering_orgdatastandard3_0_Control_httpwww_orienteering_orgdatastandard3_0PunchingUnitId', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3257, 6), )

    
    PunchingUnitId = property(__PunchingUnitId.value, __PunchingUnitId.set, None, '\n            If the control has multiple punching units with separate codes, specify all these codes using elements of this kind. Omit this element if there is a single punching unit whose code is the same as the control code.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httpwww_orienteering_orgdatastandard3_0_Control_httpwww_orienteering_orgdatastandard3_0Name', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3264, 6), )

    
    Name = property(__Name.value, __Name.set, None, "\n            The name of the control, used for e.g. online controls ('spectator control', 'prewarning').\n          ")

    
    # Element {http://www.orienteering.org/datastandard/3.0}Position uses Python identifier Position
    __Position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Position'), 'Position', '__httpwww_orienteering_orgdatastandard3_0_Control_httpwww_orienteering_orgdatastandard3_0Position', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3271, 6), )

    
    Position = property(__Position.value, __Position.set, None, '\n            The geographical position of the control.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}MapPosition uses Python identifier MapPosition
    __MapPosition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MapPosition'), 'MapPosition', '__httpwww_orienteering_orgdatastandard3_0_Control_httpwww_orienteering_orgdatastandard3_0MapPosition', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3278, 6), )

    
    MapPosition = property(__MapPosition.value, __MapPosition.set, None, "\n            The position of the control according to tha map's coordinate system.\n          ")

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_Control_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3285, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_orienteering_orgdatastandard3_0_Control_type', _module_typeBindings.ControlType, unicode_default='Control')
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3293, 4)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3293, 4)
    
    type = property(__type.value, __type.set, None, '\n          The type of the control: (ordinary) control, start, finish, crossing point or end of marked route. This attribute can be overridden on the CourseControl level.\n        ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_Control_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3300, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3300, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __PunchingUnitId.name() : __PunchingUnitId,
        __Name.name() : __Name,
        __Position.name() : __Position,
        __MapPosition.name() : __MapPosition,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __type.name() : __type,
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.Control = Control
Namespace.addCategoryObject('typeBinding', 'Control', Control)


# Complex type {http://www.orienteering.org/datastandard/3.0}MapPosition with content type EMPTY
class MapPosition (pyxb.binding.basis.complexTypeDefinition):
    """
        Defines a position in a map's coordinate system.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MapPosition')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3425, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute x uses Python identifier x
    __x = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'x'), 'x', '__httpwww_orienteering_orgdatastandard3_0_MapPosition_x', pyxb.binding.datatypes.double, required=True)
    __x._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3431, 4)
    __x._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3431, 4)
    
    x = property(__x.value, __x.set, None, '\n          The number of units right of the center of the coordinate system.\n        ')

    
    # Attribute y uses Python identifier y
    __y = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'y'), 'y', '__httpwww_orienteering_orgdatastandard3_0_MapPosition_y', pyxb.binding.datatypes.double, required=True)
    __y._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3438, 4)
    __y._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3438, 4)
    
    y = property(__y.value, __y.set, None, '\n          The number of units below the center of the coordinate system.\n        ')

    
    # Attribute unit uses Python identifier unit
    __unit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unit'), 'unit', '__httpwww_orienteering_orgdatastandard3_0_MapPosition_unit', _module_typeBindings.STD_ANON_11, unicode_default='mm')
    __unit._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3445, 4)
    __unit._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3445, 4)
    
    unit = property(__unit.value, __unit.set, None, '\n          The type of unit used.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __x.name() : __x,
        __y.name() : __y,
        __unit.name() : __unit
    })
_module_typeBindings.MapPosition = MapPosition
Namespace.addCategoryObject('typeBinding', 'MapPosition', MapPosition)


# Complex type {http://www.orienteering.org/datastandard/3.0}SimpleRaceCourse with content type ELEMENT_ONLY
class SimpleRaceCourse (SimpleCourse):
    """
        Defines a course for a certain race, excluding controls.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleRaceCourse')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3881, 2)
    _ElementMap = SimpleCourse._ElementMap.copy()
    _AttributeMap = SimpleCourse._AttributeMap.copy()
    # Base type is SimpleCourse
    
    # Element Id ({http://www.orienteering.org/datastandard/3.0}Id) inherited from {http://www.orienteering.org/datastandard/3.0}SimpleCourse
    
    # Element Name ({http://www.orienteering.org/datastandard/3.0}Name) inherited from {http://www.orienteering.org/datastandard/3.0}SimpleCourse
    
    # Element CourseFamily ({http://www.orienteering.org/datastandard/3.0}CourseFamily) inherited from {http://www.orienteering.org/datastandard/3.0}SimpleCourse
    
    # Element Length ({http://www.orienteering.org/datastandard/3.0}Length) inherited from {http://www.orienteering.org/datastandard/3.0}SimpleCourse
    
    # Element Climb ({http://www.orienteering.org/datastandard/3.0}Climb) inherited from {http://www.orienteering.org/datastandard/3.0}SimpleCourse
    
    # Element NumberOfControls ({http://www.orienteering.org/datastandard/3.0}NumberOfControls) inherited from {http://www.orienteering.org/datastandard/3.0}SimpleCourse
    
    # Attribute raceNumber uses Python identifier raceNumber
    __raceNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'raceNumber'), 'raceNumber', '__httpwww_orienteering_orgdatastandard3_0_SimpleRaceCourse_raceNumber', pyxb.binding.datatypes.integer)
    __raceNumber._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3889, 8)
    __raceNumber._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3889, 8)
    
    raceNumber = property(__raceNumber.value, __raceNumber.set, None, '\n              The ordinal number of the race that the information belongs to for a multi-race event, starting at 1.\n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __raceNumber.name() : __raceNumber
    })
_module_typeBindings.SimpleRaceCourse = SimpleRaceCourse
Namespace.addCategoryObject('typeBinding', 'SimpleRaceCourse', SimpleRaceCourse)


# Complex type {http://www.orienteering.org/datastandard/3.0}CourseControl with content type ELEMENT_ONLY
class CourseControl (pyxb.binding.basis.complexTypeDefinition):
    """
        A control included in a particular course.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CourseControl')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3900, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.orienteering.org/datastandard/3.0}Control uses Python identifier Control
    __Control = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Control'), 'Control', '__httpwww_orienteering_orgdatastandard3_0_CourseControl_httpwww_orienteering_orgdatastandard3_0Control', True, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3907, 6), )

    
    Control = property(__Control.value, __Control.set, None, '\n            The code(s) of the control(s), without course-specific information. Specifying multiple control codes means that the competitor is required to punch one of the controls, but not all of them.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}MapText uses Python identifier MapText
    __MapText = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MapText'), 'MapText', '__httpwww_orienteering_orgdatastandard3_0_CourseControl_httpwww_orienteering_orgdatastandard3_0MapText', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3914, 6), )

    
    MapText = property(__MapText.value, __MapText.set, None, '\n            Indicates the text shown next to the control circle, i.e. the control number.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}MapTextPosition uses Python identifier MapTextPosition
    __MapTextPosition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MapTextPosition'), 'MapTextPosition', '__httpwww_orienteering_orgdatastandard3_0_CourseControl_httpwww_orienteering_orgdatastandard3_0MapTextPosition', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3921, 6), )

    
    MapTextPosition = property(__MapTextPosition.value, __MapTextPosition.set, None, '\n            Indicates the position of the center of the text relative to the center of the control circle.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}LegLength uses Python identifier LegLength
    __LegLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LegLength'), 'LegLength', '__httpwww_orienteering_orgdatastandard3_0_CourseControl_httpwww_orienteering_orgdatastandard3_0LegLength', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3928, 6), )

    
    LegLength = property(__LegLength.value, __LegLength.set, None, '\n            The length in meters from the previous control on the course. For starts, this length may refer to the distance from the time start to the start flag.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Score uses Python identifier Score
    __Score = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Score'), 'Score', '__httpwww_orienteering_orgdatastandard3_0_CourseControl_httpwww_orienteering_orgdatastandard3_0Score', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3935, 6), )

    
    Score = property(__Score.value, __Score.set, None, '\n            The score of the control in score-O events.\n          ')

    
    # Element {http://www.orienteering.org/datastandard/3.0}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httpwww_orienteering_orgdatastandard3_0_CourseControl_httpwww_orienteering_orgdatastandard3_0Extensions', False, pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3942, 6), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, '\n            Container element for custom elements from other schemas.\n          ')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_orienteering_orgdatastandard3_0_CourseControl_type', _module_typeBindings.ControlType)
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3950, 4)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3950, 4)
    
    type = property(__type.value, __type.set, None, "\n          The type of the control: (ordinary) control, start, finish, crossing point or end of marked route. If this attribute is specified, it overrides the corresponding Control's type.\n        ")

    
    # Attribute randomOrder uses Python identifier randomOrder
    __randomOrder = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'randomOrder'), 'randomOrder', '__httpwww_orienteering_orgdatastandard3_0_CourseControl_randomOrder', pyxb.binding.datatypes.boolean, unicode_default='false')
    __randomOrder._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3957, 4)
    __randomOrder._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3957, 4)
    
    randomOrder = property(__randomOrder.value, __randomOrder.set, None, '\n          Non-broken sequences of course controls having randomOrder set to true can be visited in an arbitrary order.\n        ')

    
    # Attribute specialInstruction uses Python identifier specialInstruction
    __specialInstruction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'specialInstruction'), 'specialInstruction', '__httpwww_orienteering_orgdatastandard3_0_CourseControl_specialInstruction', _module_typeBindings.STD_ANON_12, unicode_default='None')
    __specialInstruction._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3964, 4)
    __specialInstruction._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3964, 4)
    
    specialInstruction = property(__specialInstruction.value, __specialInstruction.set, None, '\n          Any special instruction applied at the control, see http://orienteering.org/wp-content/uploads/2010/12/Control-Descriptions-2004-symbols-only.pdf, page 15.\n        ')

    
    # Attribute tapedRouteLength uses Python identifier tapedRouteLength
    __tapedRouteLength = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tapedRouteLength'), 'tapedRouteLength', '__httpwww_orienteering_orgdatastandard3_0_CourseControl_tapedRouteLength', pyxb.binding.datatypes.double)
    __tapedRouteLength._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3980, 4)
    __tapedRouteLength._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3980, 4)
    
    tapedRouteLength = property(__tapedRouteLength.value, __tapedRouteLength.set, None, '\n          The length of the taped route in meters. Only to be specified if specialInstruction is TapedRoute or FunnelTapedRoute and if different from the value specified in LegLength element, i.e. when Special Instruction 13.1 is used.\n        ')

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_CourseControl_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3987, 4)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3987, 4)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        __Control.name() : __Control,
        __MapText.name() : __MapText,
        __MapTextPosition.name() : __MapTextPosition,
        __LegLength.name() : __LegLength,
        __Score.name() : __Score,
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __type.name() : __type,
        __randomOrder.name() : __randomOrder,
        __specialInstruction.name() : __specialInstruction,
        __tapedRouteLength.name() : __tapedRouteLength,
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.CourseControl = CourseControl
Namespace.addCategoryObject('typeBinding', 'CourseControl', CourseControl)


# Complex type {http://www.orienteering.org/datastandard/3.0}Contact with content type SIMPLE
class Contact (pyxb.binding.basis.complexTypeDefinition):
    """
        Contact information for a person, organisation or other entity.
      """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Contact')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4232, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_orienteering_orgdatastandard3_0_Contact_type', _module_typeBindings.STD_ANON_13, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4240, 8)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4240, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute modifyTime uses Python identifier modifyTime
    __modifyTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifyTime'), 'modifyTime', '__httpwww_orienteering_orgdatastandard3_0_Contact_modifyTime', pyxb.binding.datatypes.dateTime)
    __modifyTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4252, 8)
    __modifyTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4252, 8)
    
    modifyTime = property(__modifyTime.value, __modifyTime.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __modifyTime.name() : __modifyTime
    })
_module_typeBindings.Contact = Contact
Namespace.addCategoryObject('typeBinding', 'Contact', Contact)


CompetitorList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CompetitorList'), CTD_ANON, documentation='\n        A list of competitors. This is used to exchange a "brutto" list of possible competitors. This should not be used to exchange entries; use EntryList instead.\n      ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 65, 2))
Namespace.addCategoryObject('elementBinding', CompetitorList.name().localName(), CompetitorList)

OrganisationList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OrganisationList'), CTD_ANON_, documentation='\n        A list of organisations, including address and contact information.\n      ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 89, 2))
Namespace.addCategoryObject('elementBinding', OrganisationList.name().localName(), OrganisationList)

EventList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EventList'), CTD_ANON_2, documentation='\n        A list of events. This can be used to exchange fixtures.\n      ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 113, 2))
Namespace.addCategoryObject('elementBinding', EventList.name().localName(), EventList)

ClassList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClassList'), CTD_ANON_3, documentation='\n        A list of classes.\n      ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 137, 2))
Namespace.addCategoryObject('elementBinding', ClassList.name().localName(), ClassList)

EntryList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EntryList'), CTD_ANON_4, documentation='\n        A list of persons and/or teams which are registered for a particular event.\n      ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 161, 2))
Namespace.addCategoryObject('elementBinding', EntryList.name().localName(), EntryList)

CourseData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CourseData'), CTD_ANON_5, documentation='\n        This element defines all the control and course information for an event or race. Used when transferring courses from course-setting software to event administration software.\n      ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 205, 2))
Namespace.addCategoryObject('elementBinding', CourseData.name().localName(), CourseData)

StartList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartList'), CTD_ANON_6, documentation='\n        Contains information about the start lists for the classes in an event.\n      ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 242, 2))
Namespace.addCategoryObject('elementBinding', StartList.name().localName(), StartList)

ResultList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResultList'), CTD_ANON_7, documentation='\n        Contains information about the result lists for the classes in an event.\n      ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 279, 2))
Namespace.addCategoryObject('elementBinding', ResultList.name().localName(), ResultList)

ServiceRequestList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequestList'), CTD_ANON_8, documentation='\n        A list of service requests.\n      ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 348, 2))
Namespace.addCategoryObject('elementBinding', ServiceRequestList.name().localName(), ServiceRequestList)

ControlCardList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlCardList'), CTD_ANON_9, documentation='\n        Defines control card ownership, e.g. for rental control card handling purposes.\n      ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 392, 2))
Namespace.addCategoryObject('elementBinding', ControlCardList.name().localName(), ControlCardList)



PersonName._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Family'), pyxb.binding.datatypes.string, scope=PersonName, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 497, 6)))

PersonName._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Given'), pyxb.binding.datatypes.string, scope=PersonName, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 498, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PersonName._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Family')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 497, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PersonName._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Given')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 498, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PersonName._Automaton = _BuildAutomaton()




Competitor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Person'), Person, scope=Competitor, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 509, 6)))

Competitor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), Organisation, scope=Competitor, documentation='\n            The organisations that the person is member of.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 510, 6)))

Competitor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlCard'), ControlCard, scope=Competitor, documentation='\n            The default control cards of the competitor.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 517, 6)))

Competitor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Class'), Class, scope=Competitor, documentation='\n            The default classes of the competitor.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 524, 6)))

Competitor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Score'), Score, scope=Competitor, documentation='\n            Any scores, e.g. ranking scores, for the person.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 531, 6)))

Competitor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=Competitor, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 538, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 510, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 517, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 524, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 531, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 538, 6))
    counters.add(cc_4)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Competitor._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Person')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 509, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Competitor._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Organisation')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 510, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Competitor._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ControlCard')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 517, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Competitor._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Class')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 524, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Competitor._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Score')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 531, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Competitor._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 538, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Competitor._Automaton = _BuildAutomaton_()




Role._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Person'), Person, scope=Role, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 681, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Role._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Person')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 681, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Role._Automaton = _BuildAutomaton_2()




Event._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Id, scope=Event, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 694, 6)))

Event._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), pyxb.binding.datatypes.string, scope=Event, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 695, 6)))

Event._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartTime'), DateAndOptionalTime, scope=Event, documentation='\n            The start time for the first starting competitor of the event. If the event contains multiple races, this is the start time for the first starting competitor of the first race.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 696, 6)))

Event._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndTime'), DateAndOptionalTime, scope=Event, documentation='\n            The expected finish time for the last finishing competitor of the event. If the event contains multiple races, this is the expected finish time for the last finishing competitor of the last race.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 703, 6)))

Event._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Status'), EventStatus, scope=Event, documentation='\n            The status of the event. If the event is a multi-race event, and status is set per race, use the Status element of the Race element.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 710, 6)))

Event._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Classification'), EventClassification, scope=Event, documentation='\n            The classification or level of the event. If the event is a multi-race event, and classification is set per race, use the Classification element of the Race element.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 717, 6)))

Event._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Form'), EventForm, scope=Event, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 724, 6)))

Event._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Organiser'), Organisation, scope=Event, documentation='\n            The organisations that organise the event.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 725, 6)))

Event._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Official'), Role, scope=Event, documentation='\n            The main officials of the event, e.g. course setter and event president.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 732, 6)))

Event._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Class'), Class, scope=Event, documentation='\n            The classes that are available at the event.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 739, 6)))

Event._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Race'), Race, scope=Event, documentation='\n            An event consists of a number of races. The number is equal to the number of times a competitor should start. Most events contain a single race, and this elemend could then be omitted.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 746, 6)))

Event._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EntryReceiver'), EntryReceiver, scope=Event, documentation='\n            Address and contact information to the person or organisation which registers the entries for the event.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 753, 6)))

Event._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Service'), Service, scope=Event, documentation='\n            The services available for the event, e.g. accomodation and transport.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 760, 6)))

Event._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Account'), Account, scope=Event, documentation='\n            The bank account for the event.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 767, 6)))

Event._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'URL'), EventURL, scope=Event, documentation='\n            URLs to various types of additional information regarding the event, e.g. event website or result list.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 774, 6)))

Event._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Information'), InformationItem, scope=Event, documentation='\n            Presents arbitrary data about the event, e.g. "Accommodation", "Local Attractions", and so on. Information present here should be defined well in advance of the event, in contrast to the \'News\' element.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 781, 6)))

Event._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Schedule'), Schedule, scope=Event, documentation='\n            Defines the schedule of events that comprise the entire orienteering event, e.g. entry deadlines, banquet and social events, and awards ceremonies.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 788, 6)))

Event._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'News'), InformationItem, scope=Event, documentation='\n            Presents "last minute information" about the event.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 795, 6)))

Event._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=Event, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 802, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 694, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 696, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 703, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 710, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 717, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 724, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 725, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 732, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 739, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 746, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 753, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 760, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 767, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 774, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 781, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 788, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 795, 6))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 802, 6))
    counters.add(cc_17)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Event._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 694, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Event._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 695, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Event._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartTime')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 696, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Event._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndTime')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 703, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Event._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Status')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 710, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Event._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Classification')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 717, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Event._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Form')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 724, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Event._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Organiser')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 725, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Event._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Official')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 732, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Event._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Class')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 739, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Event._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Race')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 746, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Event._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EntryReceiver')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 753, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(Event._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Service')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 760, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(Event._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Account')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 767, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(Event._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'URL')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 774, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(Event._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Information')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 781, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(Event._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Schedule')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 788, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(Event._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'News')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 795, 6))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(Event._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 802, 6))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, True) ]))
    st_18._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Event._Automaton = _BuildAutomaton_3()




EntryReceiver._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Address'), Address, scope=EntryReceiver, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 815, 6)))

EntryReceiver._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Contact'), Contact, scope=EntryReceiver, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 816, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 815, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 816, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(EntryReceiver._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Address')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 815, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(EntryReceiver._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Contact')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 816, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
EntryReceiver._Automaton = _BuildAutomaton_4()




Race._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RaceNumber'), pyxb.binding.datatypes.integer, scope=Race, documentation='\n            The ordinal number of the race in the multi-race event, starting at 1.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 882, 6)))

Race._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), pyxb.binding.datatypes.string, scope=Race, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 889, 6)))

Race._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartTime'), DateAndOptionalTime, scope=Race, documentation='\n            The start time for the first starting competitor of the race.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 890, 6)))

Race._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndTime'), DateAndOptionalTime, scope=Race, documentation='\n            The time when the finish closes.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 897, 6)))

Race._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Status'), EventStatus, scope=Race, documentation='\n            The status of the race. This element overrides the Status element of the parent Event element.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 904, 6)))

Race._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Classification'), EventClassification, scope=Race, documentation='\n            The classification or level of the race. This element overrides the Classification element of the parent Event element.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 911, 6)))

Race._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Position'), GeoPosition, scope=Race, documentation='\n            The geographical location of the arena.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 918, 6)))

Race._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Discipline'), RaceDiscipline, scope=Race, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 925, 6)))

Race._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Organiser'), Organisation, scope=Race, documentation='\n            The organisations that organise the event.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 926, 6)))

Race._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Official'), Role, scope=Race, documentation='\n            The main officials of the event, e.g. course setter and event president.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 933, 6)))

Race._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Service'), Service, scope=Race, documentation='\n            The services available for the race, e.g. accomodation and transport.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 940, 6)))

Race._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'URL'), EventURL, scope=Race, documentation='\n            URLs to various types of additional information regarding the event, e.g. event website or result list.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 947, 6)))

Race._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=Race, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 954, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 890, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 897, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 904, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 911, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 918, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 925, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 926, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 933, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 940, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 947, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 954, 6))
    counters.add(cc_10)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Race._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RaceNumber')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 882, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Race._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 889, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Race._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartTime')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 890, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Race._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndTime')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 897, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Race._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Status')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 904, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Race._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Classification')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 911, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Race._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Position')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 918, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Race._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Discipline')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 925, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Race._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Organiser')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 926, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Race._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Official')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 933, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Race._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Service')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 940, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Race._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'URL')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 947, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Race._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 954, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Race._Automaton = _BuildAutomaton_5()




Schedule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartTime'), pyxb.binding.datatypes.dateTime, scope=Schedule, documentation='\n            The start time of the sub-event.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1009, 6)))

Schedule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndTime'), pyxb.binding.datatypes.dateTime, scope=Schedule, documentation='\n            The end time of the sub-event.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1016, 6)))

Schedule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), pyxb.binding.datatypes.string, scope=Schedule, documentation='\n            The name or title of the sub-event.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1023, 6)))

Schedule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Venue'), pyxb.binding.datatypes.string, scope=Schedule, documentation='\n            The name of the place where the sub-event occurs.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1030, 6)))

Schedule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Position'), GeoPosition, scope=Schedule, documentation='\n            The geographical position of the sub-event.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1037, 6)))

Schedule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Details'), pyxb.binding.datatypes.string, scope=Schedule, documentation='\n            Any extra information about the sub-event.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1044, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1016, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1030, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1037, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1044, 6))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Schedule._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartTime')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1009, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Schedule._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndTime')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1016, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Schedule._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1023, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Schedule._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Venue')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1030, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Schedule._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Position')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1037, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Schedule._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Details')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1044, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Schedule._Automaton = _BuildAutomaton_6()




InformationItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Title'), pyxb.binding.datatypes.string, scope=InformationItem, documentation='\n            A short summary of the information.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1062, 6)))

InformationItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Content'), pyxb.binding.datatypes.string, scope=InformationItem, documentation='\n            The information in detailed form.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1069, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InformationItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Title')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1062, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InformationItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Content')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1069, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InformationItem._Automaton = _BuildAutomaton_7()




ClassType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Id, scope=ClassType, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1273, 6)))

ClassType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), pyxb.binding.datatypes.string, scope=ClassType, documentation='\n            The name of the class type.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1274, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1273, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ClassType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1273, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ClassType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1274, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ClassType._Automaton = _BuildAutomaton_8()




RaceClass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PunchingSystem'), pyxb.binding.datatypes.string, scope=RaceClass, documentation='\n            The punching system used for the class at the race. Multiple punching systems can be specified, e.g. one for punch checking and another for timing.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1389, 6)))

RaceClass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TeamFee'), Fee, scope=RaceClass, documentation='\n            The entry fees for a team as a whole taking part in this class. Use the Fee element to specify a fee for an individual competitor in the team. Use the TeamFee subelement of the Class element to specify a fee on event level.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1396, 6)))

RaceClass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Fee'), Fee, scope=RaceClass, documentation='\n            The entry fees for an individual competitor taking part in the race class. Use the TeamFee element to specify a fee for the team as a whole. Use the Fee subelement of the Class element to specify a fee on event level.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1403, 6)))

RaceClass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FirstStart'), pyxb.binding.datatypes.dateTime, scope=RaceClass, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1410, 6)))

RaceClass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Status'), RaceClassStatus, scope=RaceClass, documentation='\n            The status of the race, e.g. if results should be considered invalid due to misplaced constrols.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1411, 6)))

RaceClass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Course'), SimpleCourse, scope=RaceClass, documentation='\n            The courses assigned to this class. For a mass-start event or a relay event, there are usually multiple courses per class due to the usage of spreading methods.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1418, 6)))

RaceClass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OnlineControl'), Control, scope=RaceClass, documentation='\n            The controls that are online controls for this class.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1425, 6)))

RaceClass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=RaceClass, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1432, 6)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1389, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1396, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1403, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1410, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1411, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1418, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1425, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1432, 6))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RaceClass._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PunchingSystem')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1389, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RaceClass._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TeamFee')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1396, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RaceClass._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Fee')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1403, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(RaceClass._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FirstStart')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1410, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(RaceClass._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Status')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1411, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(RaceClass._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Course')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1418, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(RaceClass._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OnlineControl')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1425, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(RaceClass._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1432, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RaceClass._Automaton = _BuildAutomaton_9()




AssignedFee._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Fee'), Fee, scope=AssignedFee, documentation='\n            The fee that has been assigned to the competitor or the team.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1571, 6)))

AssignedFee._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PaidAmount'), Amount, scope=AssignedFee, documentation='\n            The amount that has been paid, optionally including currency code.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1578, 6)))

AssignedFee._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=AssignedFee, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1585, 6)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1578, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1585, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AssignedFee._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Fee')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1571, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AssignedFee._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PaidAmount')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1578, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AssignedFee._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1585, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AssignedFee._Automaton = _BuildAutomaton_10()




PersonEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Id, scope=PersonEntry, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1616, 6)))

PersonEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Person'), Person, scope=PersonEntry, documentation='\n            The person that is entered.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1617, 6)))

PersonEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), Organisation, scope=PersonEntry, documentation='\n            The organisation that the person represents at the event.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1624, 6)))

PersonEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlCard'), ControlCard, scope=PersonEntry, documentation='\n            Information about the control cards (punching cards) that the person uses at the event. Multiple control cards can be specified, e.g. one for punch checking and another for timing.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1631, 6)))

PersonEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Score'), Score, scope=PersonEntry, documentation='\n            Any score that is submitted together with the entry, e.g. World Ranking points.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1638, 6)))

PersonEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Class'), Class, scope=PersonEntry, documentation='\n            The class(es) the person wants to take part in. Multiple classes may be provided in order of preference in scenarios where the number of competitors are limited in some classes.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1645, 6)))

PersonEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RaceNumber'), pyxb.binding.datatypes.integer, scope=PersonEntry, documentation='\n            The ordinal numbers of the races that the person is taking part in, starting at 1. If not specified, the person takes part in all races.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1652, 6)))

PersonEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee'), AssignedFee, scope=PersonEntry, documentation='\n            The fees that the person has to pay when entering the event. In a multi-race event, there is usually one element for each race.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1659, 6)))

PersonEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest'), ServiceRequest, scope=PersonEntry, documentation='\n            Defines the services requested by the person.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1666, 6)))

PersonEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartTimeAllocationRequest'), StartTimeAllocationRequest, scope=PersonEntry, documentation='\n            Any special preferences regarding start time that has to be taken into consideration when making the start list draw.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1673, 6)))

PersonEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EntryTime'), pyxb.binding.datatypes.dateTime, scope=PersonEntry, documentation='\n            The time when the entry was first submitted.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1680, 6)))

PersonEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=PersonEntry, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1687, 6)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1616, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1624, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1631, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1638, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1645, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1652, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1659, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1666, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1673, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1680, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1687, 6))
    counters.add(cc_10)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PersonEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1616, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PersonEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Person')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1617, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PersonEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Organisation')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1624, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(PersonEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ControlCard')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1631, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(PersonEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Score')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1638, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(PersonEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Class')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1645, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(PersonEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RaceNumber')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1652, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(PersonEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1659, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(PersonEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1666, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(PersonEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartTimeAllocationRequest')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1673, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(PersonEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EntryTime')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1680, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(PersonEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1687, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PersonEntry._Automaton = _BuildAutomaton_11()




TeamEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Id, scope=TeamEntry, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1705, 6)))

TeamEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), pyxb.binding.datatypes.string, scope=TeamEntry, documentation='\n            The name of the team. If a relay, this is probably the name of the club optionally followed by a sequence number to distinguish teams from the same club in a class.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1706, 6)))

TeamEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), Organisation, scope=TeamEntry, documentation='\n            The organisation(s) that the team represents.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1713, 6)))

TeamEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TeamEntryPerson'), TeamEntryPerson, scope=TeamEntry, documentation='\n            The persons that make up the team.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1720, 6)))

TeamEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Class'), Class, scope=TeamEntry, documentation='\n            The class(es) the team wants to take part in. Multiple classes may be provided in order of preference in scenarios where the number of competitors are limited in some classes.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1727, 6)))

TeamEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Race'), pyxb.binding.datatypes.integer, scope=TeamEntry, documentation='\n            The numbers of the races that the team is taking part in. If not specified, team person takes part in all races.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1734, 6)))

TeamEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee'), AssignedFee, scope=TeamEntry, documentation='\n            The fees that the team as a whole has to pay when entering the event. In a multi-race event, there is usually one element for each race. If there are differentated fees for the team members, specify them in the TeamEntryPerson elements.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1741, 6)))

TeamEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest'), ServiceRequest, scope=TeamEntry, documentation='\n            Defines the services requested by the team.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1748, 6)))

TeamEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartTimeAllocationRequest'), StartTimeAllocationRequest, scope=TeamEntry, documentation='\n            Any special preferences regarding start time that has to be taken into consideration when making the start list draw.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1755, 6)))

TeamEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContactInformation'), pyxb.binding.datatypes.string, scope=TeamEntry, documentation='\n            Contact information (name and e.g. mobile phone number) to a team leader or coach, expressed as plain text.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1762, 6)))

TeamEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EntryTime'), pyxb.binding.datatypes.dateTime, scope=TeamEntry, documentation='\n            The time when the entry was first submitted.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1769, 6)))

TeamEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=TeamEntry, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1776, 6)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1705, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1713, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1720, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1727, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1734, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1741, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1748, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1755, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1762, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1769, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1776, 6))
    counters.add(cc_10)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TeamEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1705, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TeamEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1706, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TeamEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Organisation')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1713, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TeamEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TeamEntryPerson')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1720, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TeamEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Class')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1727, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TeamEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Race')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1734, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(TeamEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1741, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(TeamEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1748, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(TeamEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartTimeAllocationRequest')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1755, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(TeamEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ContactInformation')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1762, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(TeamEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EntryTime')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1769, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(TeamEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1776, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TeamEntry._Automaton = _BuildAutomaton_12()




TeamEntryPerson._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Person'), Person, scope=TeamEntryPerson, documentation='\n            The person. Omit if the person is not known at the moment, but for example the control card is known.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1794, 6)))

TeamEntryPerson._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), Organisation, scope=TeamEntryPerson, documentation='\n            The organisation that the person represent. Omit if this is the same as the organsiation given in the TeamEntry element.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1801, 6)))

TeamEntryPerson._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Leg'), pyxb.binding.datatypes.integer, scope=TeamEntryPerson, documentation='\n            For relay entries, the number of the leg that this person is taking part in.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1808, 6)))

TeamEntryPerson._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LegOrder'), pyxb.binding.datatypes.integer, scope=TeamEntryPerson, documentation="\n            Defines the person's starting order within a team at a parallel relay leg.\n          ", location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1815, 6)))

TeamEntryPerson._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlCard'), ControlCard, scope=TeamEntryPerson, documentation='\n            Information about the control cards (punching cards) that the person uses at the event. Multiple control cards can be specified, e.g. one for punch checking and another for timing.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1822, 6)))

TeamEntryPerson._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Score'), Score, scope=TeamEntryPerson, documentation='\n            Any score that is submitted together with the entry, e.g. World Ranking points.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1829, 6)))

TeamEntryPerson._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee'), AssignedFee, scope=TeamEntryPerson, documentation='\n            The fees that this particular person has to pay when entering the event. In a multi-race event, there is usually one element for each race. Fees assigned to the team as a whole should be defined in the TeamEntry element.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1836, 6)))

TeamEntryPerson._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=TeamEntryPerson, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1843, 6)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1794, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1801, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1808, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1815, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1822, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1829, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1836, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1843, 6))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TeamEntryPerson._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Person')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1794, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TeamEntryPerson._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Organisation')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1801, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TeamEntryPerson._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Leg')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1808, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TeamEntryPerson._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LegOrder')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1815, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TeamEntryPerson._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ControlCard')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1822, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(TeamEntryPerson._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Score')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1829, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(TeamEntryPerson._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1836, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(TeamEntryPerson._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1843, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TeamEntryPerson._Automaton = _BuildAutomaton_13()




ClassStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Class'), Class, scope=ClassStart, documentation='\n            The class that the start list belongs to.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1930, 6)))

ClassStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Course'), SimpleRaceCourse, scope=ClassStart, documentation='\n            Defines the course assigned to the class. If courses are unique per competitor, use PersonStart/Course or TeamStart/TeamMemberStart/Course instead. One element per race.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1937, 6)))

ClassStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartName'), StartName, scope=ClassStart, documentation='\n            Defines the name of the start place (e.g. Start 1), if the race has multiple start places. One element per race.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1944, 6)))

ClassStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PersonStart'), PersonStart, scope=ClassStart, documentation='\n            Start times for individual competitors in the class.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1951, 6)))

ClassStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TeamStart'), TeamStart, scope=ClassStart, documentation='\n            Start times for teams in the class.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1958, 6)))

ClassStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=ClassStart, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1965, 6)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1937, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1944, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1951, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1958, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1965, 6))
    counters.add(cc_4)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ClassStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Class')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1930, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ClassStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Course')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1937, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ClassStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartName')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1944, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ClassStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PersonStart')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1951, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ClassStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TeamStart')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1958, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ClassStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1965, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ClassStart._Automaton = _BuildAutomaton_14()




PersonStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EntryId'), Id, scope=PersonStart, documentation="\n            The id corresponding to this person's entry in an EntryList.\n          ", location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2009, 6)))

PersonStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Person'), Person, scope=PersonStart, documentation='\n            The person that the start time belongs to. Omit if there is no person assigned to the start time, e.g. a vacant person.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2016, 6)))

PersonStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), Organisation, scope=PersonStart, documentation='\n            The organisation that the person is representing at the event.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2023, 6)))

PersonStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Start'), PersonRaceStart, scope=PersonStart, documentation='\n            The core start information for the person; one element per race in the event.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2030, 6)))

PersonStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=PersonStart, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2037, 6)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2009, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2016, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2023, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2037, 6))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PersonStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EntryId')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2009, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PersonStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Person')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2016, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PersonStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Organisation')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2023, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PersonStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Start')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2030, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(PersonStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2037, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PersonStart._Automaton = _BuildAutomaton_15()




PersonRaceStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BibNumber'), pyxb.binding.datatypes.string, scope=PersonRaceStart, documentation='\n            The bib number that the person is wearing.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2055, 6)))

PersonRaceStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartTime'), pyxb.binding.datatypes.dateTime, scope=PersonRaceStart, documentation='\n            The time when the person starts.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2062, 6)))

PersonRaceStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Course'), SimpleCourse, scope=PersonRaceStart, documentation='\n            Defines the course assigned to the person.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2069, 6)))

PersonRaceStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlCard'), ControlCard, scope=PersonRaceStart, documentation='\n            Defines the control cards assigned to the person. Multiple control cards can be specified, e.g. one for punch checking and another for timing.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2076, 6)))

PersonRaceStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee'), AssignedFee, scope=PersonRaceStart, documentation='\n            Defines the fees that the person has been assigned.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2083, 6)))

PersonRaceStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest'), ServiceRequest, scope=PersonRaceStart, documentation='\n            Defines the services requested by the person.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2090, 6)))

PersonRaceStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=PersonRaceStart, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2097, 6)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2055, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2062, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2069, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2076, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2083, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2090, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2097, 6))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PersonRaceStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BibNumber')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2055, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PersonRaceStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartTime')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2062, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(PersonRaceStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Course')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2069, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(PersonRaceStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ControlCard')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2076, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(PersonRaceStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2083, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(PersonRaceStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2090, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(PersonRaceStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2097, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PersonRaceStart._Automaton = _BuildAutomaton_16()




TeamStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EntryId'), Id, scope=TeamStart, documentation="\n            The id corresponding to this team's entry in an EntryList.\n          ", location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2121, 6)))

TeamStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), pyxb.binding.datatypes.string, scope=TeamStart, documentation='\n            The name of the team, e.g. organisation name and team number for a relay team. Omit if the team name is not know, e.g. a vacant team.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2128, 6)))

TeamStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), Organisation, scope=TeamStart, documentation='\n            The organisation(s) the team is representing.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2135, 6)))

TeamStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BibNumber'), pyxb.binding.datatypes.string, scope=TeamStart, documentation='\n            The bib number that the members of the team are wearing. If each team member has a unique bib number, use the BibNumber of the TeamMemberStart element.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2142, 6)))

TeamStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TeamMemberStart'), TeamMemberStart, scope=TeamStart, documentation='\n            Information about the start times for the team members. One element per relay leg must be included, even if the team has not assigned any team member to the leg.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2149, 6)))

TeamStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee'), AssignedFee, scope=TeamStart, documentation='\n            Defines the fees that the team has been assigned.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2156, 6)))

TeamStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest'), ServiceRequest, scope=TeamStart, documentation='\n            Defines the services requested by the team.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2163, 6)))

TeamStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=TeamStart, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2170, 6)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2121, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2128, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2135, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2142, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2149, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2156, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2163, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2170, 6))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TeamStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EntryId')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2121, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TeamStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2128, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TeamStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Organisation')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2135, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TeamStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BibNumber')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2142, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TeamStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TeamMemberStart')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2149, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(TeamStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2156, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(TeamStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2163, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(TeamStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2170, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TeamStart._Automaton = _BuildAutomaton_17()




TeamMemberStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EntryId'), Id, scope=TeamMemberStart, documentation="\n            The id corresponding to this team member's entry in an EntryList.\n          ", location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2188, 6)))

TeamMemberStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Person'), Person, scope=TeamMemberStart, documentation='\n            The team member that the start time belongs to.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2195, 6)))

TeamMemberStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), Organisation, scope=TeamMemberStart, documentation='\n            The organisation that the team member is representing at the event.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2202, 6)))

TeamMemberStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Start'), TeamMemberRaceStart, scope=TeamMemberStart, documentation='\n            The core start information for the team member; one element per race in the event.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2209, 6)))

TeamMemberStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=TeamMemberStart, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2216, 6)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2188, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2195, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2202, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2216, 6))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TeamMemberStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EntryId')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2188, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TeamMemberStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Person')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2195, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TeamMemberStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Organisation')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2202, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TeamMemberStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Start')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2209, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2216, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TeamMemberStart._Automaton = _BuildAutomaton_18()




TeamMemberRaceStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Leg'), pyxb.binding.datatypes.integer, scope=TeamMemberRaceStart, documentation='\n            In case of a relay, this is the number of the leg that the team member takes part in.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2234, 6)))

TeamMemberRaceStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LegOrder'), pyxb.binding.datatypes.integer, scope=TeamMemberRaceStart, documentation="\n            In case of a relay with parallel legs, this defines the team member's starting order of the leg within the team.\n          ", location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2241, 6)))

TeamMemberRaceStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BibNumber'), pyxb.binding.datatypes.string, scope=TeamMemberRaceStart, documentation='\n            The bib number that the team member is wearing.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2248, 6)))

TeamMemberRaceStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartTime'), pyxb.binding.datatypes.dateTime, scope=TeamMemberRaceStart, documentation='\n            The time when the team member starts.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2255, 6)))

TeamMemberRaceStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Course'), SimpleCourse, scope=TeamMemberRaceStart, documentation='\n            Defines the course assigned to the team member.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2262, 6)))

TeamMemberRaceStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlCard'), ControlCard, scope=TeamMemberRaceStart, documentation='\n            Defines the control card assigned to the team member. Multiple control cards can be specified, e.g. one for punch checking and another for timing.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2269, 6)))

TeamMemberRaceStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee'), AssignedFee, scope=TeamMemberRaceStart, documentation='\n            Defines the fees that the team member has been assigned.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2276, 6)))

TeamMemberRaceStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest'), ServiceRequest, scope=TeamMemberRaceStart, documentation='\n            Defines the services requested by the team member.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2283, 6)))

TeamMemberRaceStart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=TeamMemberRaceStart, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2290, 6)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2234, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2241, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2248, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2255, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2262, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2269, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2276, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2283, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2290, 6))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Leg')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2234, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LegOrder')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2241, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BibNumber')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2248, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartTime')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2255, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Course')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2262, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ControlCard')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2269, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2276, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2283, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceStart._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2290, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TeamMemberRaceStart._Automaton = _BuildAutomaton_19()




ClassResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Class'), Class, scope=ClassResult, documentation='\n            The class that the result list belongs to.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2314, 6)))

ClassResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Course'), SimpleRaceCourse, scope=ClassResult, documentation='\n            Defines the course assigned to the class. If courses are unique per competitor, use PersonResult/Course or TeamResult/TeamMemberResult/Course instead. One element per race.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2321, 6)))

ClassResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PersonResult'), PersonResult, scope=ClassResult, documentation='\n            Results for individual competitors in the class.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2328, 6)))

ClassResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TeamResult'), TeamResult, scope=ClassResult, documentation='\n            Results for teams in the class.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2335, 6)))

ClassResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=ClassResult, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2342, 6)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2321, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2328, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2335, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2342, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ClassResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Class')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2314, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ClassResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Course')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2321, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ClassResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PersonResult')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2328, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ClassResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TeamResult')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2335, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ClassResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2342, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ClassResult._Automaton = _BuildAutomaton_20()




PersonResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EntryId'), Id, scope=PersonResult, documentation="\n            The id corresponding to this person's entry in an EntryList.\n          ", location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2367, 6)))

PersonResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Person'), Person, scope=PersonResult, documentation='\n            The person that the result belongs to.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2374, 6)))

PersonResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), Organisation, scope=PersonResult, documentation='\n            The organisation that the person is representing at the event.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2381, 6)))

PersonResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Result'), PersonRaceResult, scope=PersonResult, documentation='\n            The core result information for the person; one element per race in the event.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2388, 6)))

PersonResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=PersonResult, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2395, 6)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2367, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2381, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2388, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2395, 6))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PersonResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EntryId')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2367, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PersonResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Person')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2374, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PersonResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Organisation')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2381, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(PersonResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Result')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2388, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(PersonResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2395, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PersonResult._Automaton = _BuildAutomaton_21()




PersonRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BibNumber'), pyxb.binding.datatypes.string, scope=PersonRaceResult, documentation='\n            The bib number that the person that the result belongs to is wearing.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2413, 6)))

PersonRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartTime'), pyxb.binding.datatypes.dateTime, scope=PersonRaceResult, documentation='\n            The time when the person that the result belongs to started, expressed in ISO 8601 format.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2420, 6)))

PersonRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FinishTime'), pyxb.binding.datatypes.dateTime, scope=PersonRaceResult, documentation='\n            The time when the person that the result belongs to finished, expressed in ISO 8601 format.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2427, 6)))

PersonRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Time'), pyxb.binding.datatypes.double, scope=PersonRaceResult, documentation='\n            The time, in seconds, that is shown in the result list. Fractions of seconds (e.g. 258.7) may be used if the time resolution is higher than one second.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2434, 6)))

PersonRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TimeBehind'), pyxb.binding.datatypes.double, scope=PersonRaceResult, documentation='\n            The time, in seconds, that the the person is behind the winner. Fractions of seconds (e.g. 258.7) may be used if the time resolution is higher than one second.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2441, 6)))

PersonRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Position'), pyxb.binding.datatypes.integer, scope=PersonRaceResult, documentation='\n            The position in the result list for the person that the result belongs to. This element should only be present when the Status element is set to OK.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2448, 6)))

PersonRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Status'), ResultStatus, scope=PersonRaceResult, documentation='\n            The status of the result.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2455, 6)))

PersonRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Score'), Score, scope=PersonRaceResult, documentation='\n            Any scores that are attached to the result, e.g. World Ranking points.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2462, 6)))

PersonRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OverallResult'), OverallResult, scope=PersonRaceResult, documentation='\n            Holds the overall result for the person after the current race for a multi-race event.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2469, 6)))

PersonRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Course'), SimpleCourse, scope=PersonRaceResult, documentation='\n            Defines the course assigned to the person.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2476, 6)))

PersonRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SplitTime'), SplitTime, scope=PersonRaceResult, documentation="\n            Contains the times at each control of the course. Each control of the competitor's course (if known) has to be defined in a SplitTime element, even if the control has not been punched or if the competitor has not started. Start and finish times must not be present as SplitTime elements.\n          ", location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2483, 6)))

PersonRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlAnswer'), ControlAnswer, scope=PersonRaceResult, documentation='\n            Defines the answer for a trail-O control.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2490, 6)))

PersonRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Route'), Route, scope=PersonRaceResult, documentation="\n            Defines the person's route recorded by a tracking device.\n          ", location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2497, 6)))

PersonRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlCard'), ControlCard, scope=PersonRaceResult, documentation='\n            Defines the control card assigned to the person. Multiple control cards can be specified, e.g. one for punch checking and another for timing.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2504, 6)))

PersonRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee'), AssignedFee, scope=PersonRaceResult, documentation='\n            Defines the fees that the person has been assigned.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2511, 6)))

PersonRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest'), ServiceRequest, scope=PersonRaceResult, documentation='\n            Defines the services requested by the person.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2518, 6)))

PersonRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=PersonRaceResult, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2525, 6)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2413, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2420, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2427, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2434, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2441, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2448, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2462, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2469, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2476, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2483, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2490, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2497, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2504, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2511, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2518, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2525, 6))
    counters.add(cc_15)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PersonRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BibNumber')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2413, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PersonRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartTime')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2420, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PersonRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FinishTime')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2427, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PersonRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Time')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2434, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PersonRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TimeBehind')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2441, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PersonRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Position')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2448, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PersonRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Status')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2455, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(PersonRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Score')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2462, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(PersonRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OverallResult')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2469, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(PersonRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Course')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2476, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(PersonRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SplitTime')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2483, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(PersonRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ControlAnswer')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2490, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(PersonRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Route')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2497, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(PersonRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ControlCard')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2504, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(PersonRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2511, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(PersonRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2518, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(PersonRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2525, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True) ]))
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PersonRaceResult._Automaton = _BuildAutomaton_22()




TeamResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EntryId'), Id, scope=TeamResult, documentation="\n            The id corresponding to this team's entry in an EntryList.\n          ", location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2549, 6)))

TeamResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), pyxb.binding.datatypes.string, scope=TeamResult, documentation='\n            The name of the team, e.g. organisation name and team number for a relay team.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2556, 6)))

TeamResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), Organisation, scope=TeamResult, documentation='\n            The organisation(s) the team is representing.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2563, 6)))

TeamResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BibNumber'), pyxb.binding.datatypes.string, scope=TeamResult, documentation='\n            The bib number that the members of the team are wearing. If each team member has a unique bib number, use the BibNumber of the TeamMemberStart element.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2570, 6)))

TeamResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TeamMemberResult'), TeamMemberResult, scope=TeamResult, documentation='\n            Defines the result information for each team member. One element per relay leg must be included, even if the team has not assigned any team member to the leg, with exception for delta results.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2577, 6)))

TeamResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee'), AssignedFee, scope=TeamResult, documentation='\n            Defines the fees that the team has been assigned.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2584, 6)))

TeamResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest'), ServiceRequest, scope=TeamResult, documentation='\n            Defines the services requested by the team.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2591, 6)))

TeamResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=TeamResult, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2598, 6)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2549, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2563, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2570, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2577, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2584, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2591, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2598, 6))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TeamResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EntryId')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2549, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TeamResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2556, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TeamResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Organisation')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2563, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TeamResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BibNumber')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2570, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TeamResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TeamMemberResult')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2577, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TeamResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2584, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(TeamResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2591, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(TeamResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2598, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TeamResult._Automaton = _BuildAutomaton_23()




TeamMemberResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EntryId'), Id, scope=TeamMemberResult, documentation="\n            The id corresponding to this team member's entry in an EntryList.\n          ", location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2615, 6)))

TeamMemberResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Person'), Person, scope=TeamMemberResult, documentation='\n            The team member that the result belongs to. If a relay team is missing a team member, omit this element.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2622, 6)))

TeamMemberResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), Organisation, scope=TeamMemberResult, documentation='\n            The organisation that the team member is representing at the event.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2629, 6)))

TeamMemberResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Result'), TeamMemberRaceResult, scope=TeamMemberResult, documentation='\n            The core result information for the person; one element per race in the event.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2636, 6)))

TeamMemberResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=TeamMemberResult, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2643, 6)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2615, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2622, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2629, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2636, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2643, 6))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EntryId')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2615, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Person')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2622, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Organisation')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2629, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Result')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2636, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2643, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TeamMemberResult._Automaton = _BuildAutomaton_24()




TeamMemberRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Leg'), pyxb.binding.datatypes.integer, scope=TeamMemberRaceResult, documentation='\n            In case of a relay, this is the number of the leg that the team member takes part in.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2661, 6)))

TeamMemberRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LegOrder'), pyxb.binding.datatypes.integer, scope=TeamMemberRaceResult, documentation="\n            In case of a relay with parallel legs, this defines the team member's starting order of the leg within the team.\n          ", location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2668, 6)))

TeamMemberRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BibNumber'), pyxb.binding.datatypes.string, scope=TeamMemberRaceResult, documentation='\n            The bib number that the team member that the result belongs to is wearing.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2675, 6)))

TeamMemberRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartTime'), pyxb.binding.datatypes.dateTime, scope=TeamMemberRaceResult, documentation='\n            The time when the team member that the result belongs to started, expressed in ISO 8601 format.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2682, 6)))

TeamMemberRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FinishTime'), pyxb.binding.datatypes.dateTime, scope=TeamMemberRaceResult, documentation='\n            The time when the team member that the result belongs to finished, expressed in ISO 8601 format.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2689, 6)))

TeamMemberRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Time'), pyxb.binding.datatypes.double, scope=TeamMemberRaceResult, documentation='\n            The time, in seconds, that is shown in the result list. Fractions of seconds (e.g. 258.7) may be used if the time resolution is higher than one second.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2696, 6)))

TeamMemberRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TimeBehind'), CTD_ANON_10, scope=TeamMemberRaceResult, documentation='\n            The time, in seconds, that the the team member is behind the winner. Fractions of seconds (e.g. 258.7) may be used if the time resolution is higher than one second.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2703, 6)))

TeamMemberRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Position'), CTD_ANON_11, scope=TeamMemberRaceResult, documentation='\n            The position in the result list for the person that the result belongs to. This element should only be present when the Status element is set to OK.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2736, 6)))

TeamMemberRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Status'), ResultStatus, scope=TeamMemberRaceResult, documentation='\n            The status of the result.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2769, 6)))

TeamMemberRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Score'), Score, scope=TeamMemberRaceResult, documentation='\n            Any scores that are attached to the result, e.g. World Ranking points.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2776, 6)))

TeamMemberRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OverallResult'), OverallResult, scope=TeamMemberRaceResult, documentation='\n            Holds the result after the current leg for the team.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2783, 6)))

TeamMemberRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Course'), SimpleCourse, scope=TeamMemberRaceResult, documentation='\n            Defines the course assigned to the person.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2790, 6)))

TeamMemberRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SplitTime'), SplitTime, scope=TeamMemberRaceResult, documentation="\n            Contains the times at each control of the course. Each control of the team member's course has to be defined in a SplitTime element, even if the control has not been punched. Start and finish times must not be present as SplitTime elements.\n          ", location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2797, 6)))

TeamMemberRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlAnswer'), ControlAnswer, scope=TeamMemberRaceResult, documentation='\n            Defines the answer for a trail-O control.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2804, 6)))

TeamMemberRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Route'), Route, scope=TeamMemberRaceResult, documentation="\n            Defines the person's route recorded by a tracking device.\n          ", location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2811, 6)))

TeamMemberRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlCard'), ControlCard, scope=TeamMemberRaceResult, documentation='\n            Defines the control card assigned to the person. Multiple control cards can be specified, e.g. one for punch checking and another for timing.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2818, 6)))

TeamMemberRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee'), AssignedFee, scope=TeamMemberRaceResult, documentation='\n            Defines the fees that the team member has been assigned.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2825, 6)))

TeamMemberRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest'), ServiceRequest, scope=TeamMemberRaceResult, documentation='\n            Defines the services requested by the team member.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2832, 6)))

TeamMemberRaceResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=TeamMemberRaceResult, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2839, 6)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2661, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2668, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2675, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2682, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2689, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2696, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2703, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2736, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2776, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2783, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2790, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2797, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2804, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2811, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2818, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2825, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2832, 6))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2839, 6))
    counters.add(cc_17)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Leg')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2661, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LegOrder')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2668, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BibNumber')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2675, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartTime')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2682, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FinishTime')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2689, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Time')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2696, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TimeBehind')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2703, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Position')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2736, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Status')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2769, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Score')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2776, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OverallResult')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2783, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Course')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2790, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SplitTime')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2797, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ControlAnswer')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2804, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Route')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2811, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ControlCard')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2818, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2825, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2832, 6))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberRaceResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2839, 6))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, True) ]))
    st_18._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TeamMemberRaceResult._Automaton = _BuildAutomaton_25()




OverallResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Time'), pyxb.binding.datatypes.double, scope=OverallResult, documentation='\n            The time, in seconds, that is shown in the result list. Fractions of seconds (e.g. 258.7) may be used if the time resolution is higher than one second.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2858, 6)))

OverallResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TimeBehind'), pyxb.binding.datatypes.double, scope=OverallResult, documentation='\n            The time, in seconds, that the the person or team is behind the leader or winner. Fractions of seconds (e.g. 258.7) may be used if the time resolution is higher than one second.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2865, 6)))

OverallResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Position'), pyxb.binding.datatypes.integer, scope=OverallResult, documentation='\n            The position in the result list for the person or team that the result belongs to. This element should only be present when the Status element is set to OK.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2872, 6)))

OverallResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Status'), ResultStatus, scope=OverallResult, documentation='\n            The status of the result.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2879, 6)))

OverallResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Score'), Score, scope=OverallResult, documentation='\n            Any scores that are attached to the result, e.g. World Ranking points.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2886, 6)))

OverallResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=OverallResult, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2893, 6)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2858, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2865, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2872, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2886, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2893, 6))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OverallResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Time')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2858, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OverallResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TimeBehind')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2865, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OverallResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Position')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2872, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OverallResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Status')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2879, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(OverallResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Score')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2886, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(OverallResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 2893, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OverallResult._Automaton = _BuildAutomaton_26()




ControlAnswer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Answer'), pyxb.binding.datatypes.string, scope=ControlAnswer, documentation='\n            The answer that the competitor selected. If the competitor did not give any answer, use an empty string.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3025, 6)))

ControlAnswer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CorrectAnswer'), pyxb.binding.datatypes.string, scope=ControlAnswer, documentation='\n            The correct answer. If no answer is correct, use an empty string.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3032, 6)))

ControlAnswer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Time'), pyxb.binding.datatypes.double, scope=ControlAnswer, documentation='\n            The time in seconds used to give the answer, in case of a timed control. Fractions of seconds (e.g. 258.7) may be used if the time resolution is higher than one second.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3039, 6)))

ControlAnswer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=ControlAnswer, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3046, 6)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3039, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3046, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ControlAnswer._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Answer')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3025, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ControlAnswer._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CorrectAnswer')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3032, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ControlAnswer._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Time')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3039, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ControlAnswer._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3046, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ControlAnswer._Automaton = _BuildAutomaton_27()




Leg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), pyxb.binding.datatypes.string, scope=Leg, documentation='\n            The name of the leg, if not sequentially named.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3212, 6)))

Leg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=Leg, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3219, 6)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3212, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3219, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Leg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3212, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Leg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3219, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Leg._Automaton = _BuildAutomaton_28()




Map._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Id, scope=Map, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3339, 6)))

Map._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Image'), Image, scope=Map, documentation='\n            The map image.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3340, 6)))

Map._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Scale'), pyxb.binding.datatypes.double, scope=Map, documentation='\n            The denominator of the scale of the map. 1:15000 should be represented as 15000.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3347, 6)))

Map._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MapPositionTopLeft'), MapPosition, scope=Map, documentation="\n            The position of the map's top left corner given in the map's coordinate system, usually (0, 0).\n          ", location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3354, 6)))

Map._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MapPositionBottomRight'), MapPosition, scope=Map, documentation="\n            The position of the map's bottom right corner given in the map's coordinate system.\n          ", location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3361, 6)))

Map._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=Map, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3368, 6)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3339, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3340, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3368, 6))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Map._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3339, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Map._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Image')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3340, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Map._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Scale')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3347, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Map._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MapPositionTopLeft')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3354, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Map._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MapPositionBottomRight')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3361, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Map._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3368, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Map._Automaton = _BuildAutomaton_29()




RaceCourseData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Map'), Map, scope=RaceCourseData, documentation='\n            The map(s) used in this race. Usually just one map, but different courses may use different scales and/or areas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3479, 6)))

RaceCourseData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Control'), Control, scope=RaceCourseData, documentation='\n            All controls of the race.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3486, 6)))

RaceCourseData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Course'), Course, scope=RaceCourseData, documentation='\n            All courses of the race.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3493, 6)))

RaceCourseData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClassCourseAssignment'), ClassCourseAssignment, scope=RaceCourseData, documentation='\n            The assignment of courses to classes.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3500, 6)))

RaceCourseData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PersonCourseAssignment'), PersonCourseAssignment, scope=RaceCourseData, documentation='\n            The assignment of courses to individual competitors.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3507, 6)))

RaceCourseData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TeamCourseAssignment'), TeamCourseAssignment, scope=RaceCourseData, documentation='\n            The assignment of courses to relay team members teams.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3514, 6)))

RaceCourseData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=RaceCourseData, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3521, 6)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3479, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3486, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3493, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3500, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3507, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3514, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3521, 6))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RaceCourseData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Map')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3479, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RaceCourseData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Control')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3486, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RaceCourseData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Course')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3493, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(RaceCourseData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ClassCourseAssignment')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3500, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(RaceCourseData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PersonCourseAssignment')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3507, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(RaceCourseData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TeamCourseAssignment')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3514, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(RaceCourseData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3521, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RaceCourseData._Automaton = _BuildAutomaton_30()




ClassCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClassId'), Id, scope=ClassCourseAssignment, documentation='\n            The id of the class.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3545, 6)))

ClassCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClassName'), pyxb.binding.datatypes.string, scope=ClassCourseAssignment, documentation='\n            The name of the class.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3552, 6)))

ClassCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AllowedOnLeg'), pyxb.binding.datatypes.integer, scope=ClassCourseAssignment, documentation='\n            The legs that the course can be assigned to in a relay class. This element can be omitted for individual classes.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3559, 6)))

ClassCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CourseName'), pyxb.binding.datatypes.string, scope=ClassCourseAssignment, documentation='\n            The name of the course.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3566, 6)))

ClassCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CourseFamily'), pyxb.binding.datatypes.string, scope=ClassCourseAssignment, documentation='\n            The family or group of forked courses that the course is part of.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3573, 6)))

ClassCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=ClassCourseAssignment, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3580, 6)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3545, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3559, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3566, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3573, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3580, 6))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ClassCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ClassId')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3545, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ClassCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ClassName')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3552, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ClassCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AllowedOnLeg')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3559, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ClassCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CourseName')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3566, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ClassCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CourseFamily')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3573, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ClassCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3580, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ClassCourseAssignment._Automaton = _BuildAutomaton_31()




PersonCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EntryId'), Id, scope=PersonCourseAssignment, documentation="\n            The id corresponding to this person's entry in an EntryList.\n          ", location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3604, 6)))

PersonCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BibNumber'), pyxb.binding.datatypes.string, scope=PersonCourseAssignment, documentation='\n            The bib number of the person.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3611, 6)))

PersonCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PersonName'), pyxb.binding.datatypes.string, scope=PersonCourseAssignment, documentation='\n            The name of the person.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3618, 6)))

PersonCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClassName'), pyxb.binding.datatypes.string, scope=PersonCourseAssignment, documentation='\n            The name of the class that the person belongs to.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3625, 6)))

PersonCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CourseName'), pyxb.binding.datatypes.string, scope=PersonCourseAssignment, documentation='\n            The name of the course.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3632, 6)))

PersonCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CourseFamily'), pyxb.binding.datatypes.string, scope=PersonCourseAssignment, documentation='\n            The family or group of forked courses that the course is part of.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3639, 6)))

PersonCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=PersonCourseAssignment, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3646, 6)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3604, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3611, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3618, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3625, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3632, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3639, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3646, 6))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PersonCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EntryId')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3604, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PersonCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BibNumber')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3611, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(PersonCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PersonName')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3618, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(PersonCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ClassName')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3625, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(PersonCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CourseName')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3632, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(PersonCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CourseFamily')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3639, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(PersonCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3646, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PersonCourseAssignment._Automaton = _BuildAutomaton_32()




TeamCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BibNumber'), pyxb.binding.datatypes.string, scope=TeamCourseAssignment, documentation='\n            The bib number of the team.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3663, 6)))

TeamCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TeamName'), pyxb.binding.datatypes.string, scope=TeamCourseAssignment, documentation='\n            The name of the team.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3670, 6)))

TeamCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClassName'), pyxb.binding.datatypes.string, scope=TeamCourseAssignment, documentation='\n            The name of the class that the team belongs to.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3677, 6)))

TeamCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TeamMemberCourseAssignment'), TeamMemberCourseAssignment, scope=TeamCourseAssignment, documentation='\n            The assignment of courses to team members.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3684, 6)))

TeamCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=TeamCourseAssignment, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3691, 6)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3663, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3670, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3677, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3684, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3691, 6))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TeamCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BibNumber')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3663, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TeamCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TeamName')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3670, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TeamCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ClassName')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3677, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TeamCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TeamMemberCourseAssignment')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3684, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TeamCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3691, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TeamCourseAssignment._Automaton = _BuildAutomaton_33()




TeamMemberCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EntryId'), Id, scope=TeamMemberCourseAssignment, documentation="\n            The id corresponding to this person's entry in an EntryList.\n          ", location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3708, 6)))

TeamMemberCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BibNumber'), pyxb.binding.datatypes.string, scope=TeamMemberCourseAssignment, documentation='\n            The bib number of the person or the team that the person belongs to. Omit if the bib number is specified in the TeamCourseAssignment element.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3715, 6)))

TeamMemberCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Leg'), pyxb.binding.datatypes.integer, scope=TeamMemberCourseAssignment, documentation='\n            For relay entries, the number of the leg that the person is taking part in.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3722, 6)))

TeamMemberCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LegOrder'), pyxb.binding.datatypes.integer, scope=TeamMemberCourseAssignment, documentation="\n            Defines the person's starting order within a team at a parallel relay leg.\n          ", location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3729, 6)))

TeamMemberCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TeamMemberName'), pyxb.binding.datatypes.string, scope=TeamMemberCourseAssignment, documentation='\n            The name of the person.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3736, 6)))

TeamMemberCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CourseName'), pyxb.binding.datatypes.string, scope=TeamMemberCourseAssignment, documentation='\n            The name of the course.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3743, 6)))

TeamMemberCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CourseFamily'), pyxb.binding.datatypes.string, scope=TeamMemberCourseAssignment, documentation='\n            The family or group of forked courses that the course is part of.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3750, 6)))

TeamMemberCourseAssignment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=TeamMemberCourseAssignment, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3757, 6)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3708, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3715, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3722, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3729, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3736, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3743, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3750, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3757, 6))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EntryId')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3708, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BibNumber')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3715, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Leg')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3722, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LegOrder')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3729, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TeamMemberName')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3736, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CourseName')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3743, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CourseFamily')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3750, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(TeamMemberCourseAssignment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3757, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TeamMemberCourseAssignment._Automaton = _BuildAutomaton_34()




Course._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Id, scope=Course, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3774, 6)))

Course._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), pyxb.binding.datatypes.string, scope=Course, documentation='\n            The name of the course.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3775, 6)))

Course._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CourseFamily'), pyxb.binding.datatypes.string, scope=Course, documentation='\n            The family or group of forked courses that the course is part of.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3782, 6)))

Course._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Length'), pyxb.binding.datatypes.double, scope=Course, documentation='\n            The length of the course, in meters.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3789, 6)))

Course._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Climb'), pyxb.binding.datatypes.double, scope=Course, documentation='\n            The climb of the course, in meters, along the expected best route choice.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3796, 6)))

Course._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CourseControl'), CourseControl, scope=Course, documentation='\n            The controls, including start and finish, that the course is made up of.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3803, 6)))

Course._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MapId'), pyxb.binding.datatypes.integer, scope=Course, documentation='\n            The id of the map used for this course.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3810, 6)))

Course._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=Course, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3817, 6)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3774, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3782, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3789, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3796, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3803, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3810, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3817, 6))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Course._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3774, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Course._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3775, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Course._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CourseFamily')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3782, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Course._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Length')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3789, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Course._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Climb')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3796, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Course._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CourseControl')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3803, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Course._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MapId')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3810, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Course._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3817, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Course._Automaton = _BuildAutomaton_35()




SimpleCourse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Id, scope=SimpleCourse, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3842, 6)))

SimpleCourse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), pyxb.binding.datatypes.string, scope=SimpleCourse, documentation='\n            The name of the course.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3843, 6)))

SimpleCourse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CourseFamily'), pyxb.binding.datatypes.string, scope=SimpleCourse, documentation='\n            The family or group of forked courses that the course is part of.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3850, 6)))

SimpleCourse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Length'), pyxb.binding.datatypes.double, scope=SimpleCourse, documentation='\n            The length of the course, in meters.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3857, 6)))

SimpleCourse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Climb'), pyxb.binding.datatypes.double, scope=SimpleCourse, documentation='\n            The climb of the course, in meters, along the expected best route choice.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3864, 6)))

SimpleCourse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumberOfControls'), pyxb.binding.datatypes.integer, scope=SimpleCourse, documentation='\n            The number of controls in the course, excluding start and finish.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3871, 6)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3842, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3843, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3850, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3857, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3864, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3871, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SimpleCourse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3842, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SimpleCourse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3843, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SimpleCourse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CourseFamily')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3850, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SimpleCourse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Length')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3857, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(SimpleCourse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Climb')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3864, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SimpleCourse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumberOfControls')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3871, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SimpleCourse._Automaton = _BuildAutomaton_36()




Service._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Id, scope=Service, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4012, 6)))

Service._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), LanguageString, scope=Service, documentation='\n            The name of the service.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4013, 6)))

Service._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Fee'), Fee, scope=Service, documentation='\n            The fees attached to this service.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4020, 6)))

Service._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Description'), LanguageString, scope=Service, documentation='\n            A further description of the service than the Name element gives.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4027, 6)))

Service._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MaxNumber'), pyxb.binding.datatypes.double, scope=Service, documentation='\n            The maximum number of instances of this service that are available. Omit this element if there is no such limit.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4034, 6)))

Service._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RequestedNumber'), pyxb.binding.datatypes.double, scope=Service, documentation='\n            The number of instances of this service that has been requested.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4041, 6)))

Service._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=Service, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4048, 6)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4012, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4020, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4027, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4034, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4041, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4048, 6))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Service._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4012, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Service._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4013, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Service._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Fee')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4020, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Service._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Description')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4027, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Service._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MaxNumber')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4034, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Service._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RequestedNumber')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4041, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Service._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4048, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Service._Automaton = _BuildAutomaton_37()




OrganisationServiceRequest._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), Organisation, scope=OrganisationServiceRequest, documentation='\n            The organisation that made the requests.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4073, 6)))

OrganisationServiceRequest._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest'), ServiceRequest, scope=OrganisationServiceRequest, documentation='\n            The service requests that the organisation made.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4080, 6)))

OrganisationServiceRequest._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PersonServiceRequest'), PersonServiceRequest, scope=OrganisationServiceRequest, documentation='\n            The service requests made by persons representing the organisation.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4087, 6)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4080, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4087, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OrganisationServiceRequest._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Organisation')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4073, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OrganisationServiceRequest._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4080, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(OrganisationServiceRequest._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PersonServiceRequest')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4087, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OrganisationServiceRequest._Automaton = _BuildAutomaton_38()




PersonServiceRequest._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Person'), Person, scope=PersonServiceRequest, documentation='\n            The person that made the requests.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4104, 6)))

PersonServiceRequest._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest'), ServiceRequest, scope=PersonServiceRequest, documentation='\n            The service requests.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4111, 6)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PersonServiceRequest._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Person')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4104, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PersonServiceRequest._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceRequest')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4111, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PersonServiceRequest._Automaton = _BuildAutomaton_39()




ServiceRequest._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Id, scope=ServiceRequest, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4123, 6)))

ServiceRequest._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Service'), Service, scope=ServiceRequest, documentation='\n            The service that is requested.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4124, 6)))

ServiceRequest._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RequestedQuantity'), pyxb.binding.datatypes.double, scope=ServiceRequest, documentation='\n            The quantity (number of instances) of the service that is requested.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4131, 6)))

ServiceRequest._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DeliveredQuantity'), pyxb.binding.datatypes.double, scope=ServiceRequest, documentation='\n            The quantity (number of instances) of the service that has been delivered. Can differ from RequestedQuantity when the available number of instances of a service is limited.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4138, 6)))

ServiceRequest._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Comment'), pyxb.binding.datatypes.string, scope=ServiceRequest, documentation='\n            Any extra information or comment attached to the service request.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4145, 6)))

ServiceRequest._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee'), AssignedFee, scope=ServiceRequest, documentation='\n            The fees related to this service request.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4152, 6)))

ServiceRequest._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=ServiceRequest, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4159, 6)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4123, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4138, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4145, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4152, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4159, 6))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ServiceRequest._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4123, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ServiceRequest._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Service')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4124, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ServiceRequest._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RequestedQuantity')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4131, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ServiceRequest._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DeliveredQuantity')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4138, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ServiceRequest._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Comment')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4145, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ServiceRequest._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AssignedFee')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4152, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ServiceRequest._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4159, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ServiceRequest._Automaton = _BuildAutomaton_40()




Address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CareOf'), pyxb.binding.datatypes.string, scope=Address, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4196, 6)))

Address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Street'), pyxb.binding.datatypes.string, scope=Address, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4197, 6)))

Address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ZipCode'), pyxb.binding.datatypes.string, scope=Address, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4198, 6)))

Address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'City'), pyxb.binding.datatypes.string, scope=Address, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4199, 6)))

Address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'State'), pyxb.binding.datatypes.string, scope=Address, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4200, 6)))

Address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Country'), Country, scope=Address, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4201, 6)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4196, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4197, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4198, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4199, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4200, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4201, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CareOf')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4196, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Street')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4197, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ZipCode')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4198, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'City')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4199, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'State')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4200, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Country')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4201, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Address._Automaton = _BuildAutomaton_41()




DateAndOptionalTime._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Date'), pyxb.binding.datatypes.date, scope=DateAndOptionalTime, documentation='\n            The date part, expressed in ISO 8601 format.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4264, 6)))

DateAndOptionalTime._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Time'), pyxb.binding.datatypes.time, scope=DateAndOptionalTime, documentation='\n            The time part, expressed in ISO 8601 format.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4271, 6)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4271, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DateAndOptionalTime._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Date')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4264, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DateAndOptionalTime._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Time')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4271, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DateAndOptionalTime._Automaton = _BuildAutomaton_42()




def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4307, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.orienteering.org/datastandard/3.0')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 4307, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Extensions._Automaton = _BuildAutomaton_43()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Competitor'), Competitor, scope=CTD_ANON, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 75, 12)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=CTD_ANON, documentation='\n                  Container element for custom elements from other schemas.\n                ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 76, 12)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 75, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 76, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Competitor')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 75, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 76, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_44()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), Organisation, scope=CTD_ANON_, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 99, 12)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=CTD_ANON_, documentation='\n                  Container element for custom elements from other schemas.\n                ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 100, 12)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 99, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 100, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Organisation')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 99, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 100, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_45()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Event'), Event, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 123, 12)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=CTD_ANON_2, documentation='\n                  Container element for custom elements from other schemas.\n                ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 124, 12)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 123, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 124, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Event')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 123, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 124, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_46()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Class'), Class, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 147, 12)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=CTD_ANON_3, documentation='\n                  Container element for custom elements from other schemas.\n                ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 148, 12)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 147, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 148, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Class')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 147, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 148, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_47()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Event'), Event, scope=CTD_ANON_4, documentation='\n                  The event that the entry list belongs to.\n                ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 171, 12)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TeamEntry'), TeamEntry, scope=CTD_ANON_4, documentation='\n                  The teams registered for the event.\n                ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 178, 12)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PersonEntry'), PersonEntry, scope=CTD_ANON_4, documentation='\n                  The individual competitors registered for the event.\n                ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 185, 12)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=CTD_ANON_4, documentation='\n                  Container element for custom elements from other schemas.\n                ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 192, 12)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 178, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 185, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 192, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Event')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 171, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TeamEntry')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 178, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PersonEntry')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 185, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 192, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_48()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Event'), Event, scope=CTD_ANON_5, documentation='\n                  The event that the course data belongs to.\n                ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 215, 12)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RaceCourseData'), RaceCourseData, scope=CTD_ANON_5, documentation='\n                  The course data for each race; one element per race in the event.\n                ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 222, 12)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=CTD_ANON_5, documentation='\n                  Container element for custom elements from other schemas.\n                ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 229, 12)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 229, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Event')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 215, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RaceCourseData')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 222, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 229, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_49()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Event'), Event, scope=CTD_ANON_6, documentation='\n                  The event that the start lists belong to.\n                ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 252, 12)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClassStart'), ClassStart, scope=CTD_ANON_6, documentation='\n                  Start lists for the classes in the event.\n                ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 259, 12)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=CTD_ANON_6, documentation='\n                  Container element for custom elements from other schemas.\n                ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 266, 12)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 259, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 266, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Event')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 252, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ClassStart')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 259, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 266, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_50()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Event'), Event, scope=CTD_ANON_7, documentation='\n                  The event that the result lists belong to.\n                ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 289, 12)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClassResult'), ClassResult, scope=CTD_ANON_7, documentation='\n                  Result lists for the classes in the event.\n                ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 296, 12)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=CTD_ANON_7, documentation='\n                  Container element for custom elements from other schemas.\n                ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 303, 12)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 296, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 303, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Event')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 289, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ClassResult')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 296, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 303, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_51()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Event'), Event, scope=CTD_ANON_8, documentation='\n                  The event that the service requests are valid for.\n                ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 358, 12)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OrganisationServiceRequest'), OrganisationServiceRequest, scope=CTD_ANON_8, documentation='\n                  Service requests made by organisations.\n                ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 365, 12)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PersonServiceRequest'), PersonServiceRequest, scope=CTD_ANON_8, documentation='\n                  Service requests made by persons.\n                ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 372, 12)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=CTD_ANON_8, documentation='\n                  Container element for custom elements from other schemas.\n                ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 379, 12)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 365, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 372, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 379, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Event')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 358, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OrganisationServiceRequest')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 365, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PersonServiceRequest')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 372, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 379, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_52()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Owner'), pyxb.binding.datatypes.string, scope=CTD_ANON_9, documentation='\n                  The owner of the control cards.\n                ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 402, 12)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlCard'), ControlCard, scope=CTD_ANON_9, documentation='\n                  The control cards.\n                ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 409, 12)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=CTD_ANON_9, documentation='\n                  Container element for custom elements from other schemas.\n                ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 416, 12)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 402, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 416, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Owner')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 402, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ControlCard')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 409, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 416, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_53()




Person._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Id, scope=Person, documentation='\n            The identifier of the person. Multiple identifiers can be included, e.g. when there is both a World Ranking Event identifier and a national database identifier for the person.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 458, 6)))

Person._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), PersonName, scope=Person, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 465, 6)))

Person._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BirthDate'), pyxb.binding.datatypes.date, scope=Person, documentation='\n            The date when the person was born, expressed in ISO 8601 format.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 466, 6)))

Person._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nationality'), Country, scope=Person, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 473, 6)))

Person._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Address'), Address, scope=Person, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 474, 6)))

Person._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Contact'), Contact, scope=Person, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 475, 6)))

Person._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=Person, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 476, 6)))

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 458, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 466, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 473, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 474, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 475, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 476, 6))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Person._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 458, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Person._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 465, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Person._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BirthDate')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 466, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Person._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nationality')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 473, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Person._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Address')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 474, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Person._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Contact')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 475, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Person._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 476, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Person._Automaton = _BuildAutomaton_54()




Organisation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Id, scope=Organisation, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 589, 6)))

Organisation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), pyxb.binding.datatypes.string, scope=Organisation, documentation='\n            The full name of the organisation.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 590, 6)))

Organisation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ShortName'), pyxb.binding.datatypes.string, scope=Organisation, documentation='\n            The short (abbreviated) name of the organisation.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 597, 6)))

Organisation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MediaName'), pyxb.binding.datatypes.string, scope=Organisation, documentation='\n            The name of the organisation as appearing in result lists targeted to media.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 604, 6)))

Organisation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ParentOrganisationId'), pyxb.binding.datatypes.integer, scope=Organisation, documentation='\n            The id of the parent of this organisation, e.g. a regional organisation for a club.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 611, 6)))

Organisation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Country'), Country, scope=Organisation, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 618, 6)))

Organisation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Address'), Address, scope=Organisation, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 619, 6)))

Organisation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Contact'), Contact, scope=Organisation, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 620, 6)))

Organisation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Position'), GeoPosition, scope=Organisation, documentation='\n            The geographical location of the organisation, e.g. a city center, an office or a club house.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 621, 6)))

Organisation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Account'), Account, scope=Organisation, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 628, 6)))

Organisation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Role'), Role, scope=Organisation, documentation='\n            Persons having certain roles within the organisation, e.g. chairman, secretary, and treasurer.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 629, 6)))

Organisation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Logotype'), Image, scope=Organisation, documentation='\n            The logotype for the organisation. Multiple logotypes may be included; in this case, make sure to include width and height attributes.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 636, 6)))

Organisation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=Organisation, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 643, 6)))

def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 589, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 597, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 604, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 611, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 618, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 619, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 620, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 621, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 628, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 629, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 636, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 643, 6))
    counters.add(cc_11)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Organisation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 589, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Organisation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 590, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Organisation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ShortName')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 597, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Organisation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MediaName')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 604, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Organisation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ParentOrganisationId')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 611, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Organisation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Country')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 618, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Organisation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Address')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 619, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Organisation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Contact')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 620, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Organisation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Position')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 621, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Organisation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Account')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 628, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Organisation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Role')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 629, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Organisation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Logotype')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 636, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(Organisation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 643, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Organisation._Automaton = _BuildAutomaton_55()




Class._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Id, scope=Class, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1087, 6)))

Class._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), pyxb.binding.datatypes.string, scope=Class, documentation='\n            The name of the class.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1088, 6)))

Class._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ShortName'), pyxb.binding.datatypes.string, scope=Class, documentation='\n            The abbreviated name of a class, used when space is limited.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1095, 6)))

Class._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClassType'), ClassType, scope=Class, documentation='\n            The class type(s) for the class.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1102, 6)))

Class._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Leg'), Leg, scope=Class, documentation='\n            Information about the legs, if the class is a relay class. One Leg element per leg must be present.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1109, 6)))

Class._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TeamFee'), Fee, scope=Class, documentation='\n            The entry fees for a team as a whole taking part in this class. Use the Fee element to specify a fee for an individual competitor in the team. Use the TeamFee subelement of the RaceClass element to specify a fee on race level.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1116, 6)))

Class._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Fee'), Fee, scope=Class, documentation='\n            The entry fees for an individual competitor taking part in the class. Use the TeamFee element to specify a fee for the team as a whole. Use the Fee subelement of the RaceClass element to specify a fee on race level.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1123, 6)))

Class._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Status'), EventClassStatus, scope=Class, documentation='\n            The overall status of the class, e.g. if overall results should be considered invalid due to misplaced controls.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1130, 6), unicode_default='Normal'))

Class._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RaceClass'), RaceClass, scope=Class, documentation='\n            Race-specific information for the class, e.g. course(s) assigned to the class.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1137, 6)))

Class._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TooFewEntriesSubstituteClass'), Class, scope=Class, documentation='\n            The class that competitors in this class should be transferred to if there are too few entries in this class.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1144, 6)))

Class._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TooManyEntriesSubstituteClass'), Class, scope=Class, documentation='\n            The class that competitors that are not qualified (e.g. due to too low ranking) should be transferred to if there are too many entries in this class.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1151, 6)))

Class._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=Class, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1158, 6)))

def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1087, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1095, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1102, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1109, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1116, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1123, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1130, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1137, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1144, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1151, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1158, 6))
    counters.add(cc_10)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Class._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1087, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Class._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1088, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Class._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ShortName')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1095, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Class._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ClassType')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1102, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Class._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Leg')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1109, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Class._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TeamFee')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1116, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Class._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Fee')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1123, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Class._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Status')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1130, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Class._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RaceClass')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1137, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Class._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TooFewEntriesSubstituteClass')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1144, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Class._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TooManyEntriesSubstituteClass')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1151, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Class._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1158, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Class._Automaton = _BuildAutomaton_56()




Fee._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Id, scope=Fee, location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1464, 6)))

Fee._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), LanguageString, scope=Fee, documentation="\n            A describing name of the fee, e.g. 'Late entry fee'.\n          ", location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1465, 6)))

Fee._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Amount'), Amount, scope=Fee, documentation='\n            The fee amount, optionally including currency code. This element must not be present if a Percentage element exists.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1472, 6)))

Fee._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TaxableAmount'), Amount, scope=Fee, documentation='\n            The fee amount that is taxable, i.e. considered when calculating taxes for an event. This element must not be present if a Percentage element exists, or if an Amount element does not exist.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1479, 6)))

Fee._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Percentage'), pyxb.binding.datatypes.double, scope=Fee, documentation='\n            The percentage to increase or decrease already existing fees in a fee list with. This element must not be present if an Amount element exists.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1486, 6)))

Fee._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TaxablePercentage'), pyxb.binding.datatypes.double, scope=Fee, documentation='\n            The percentage to increase or decrease already existing taxable fees in a fee list with. This element must not be present if an Amount element exists, or if a Percentage element does not exist.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1493, 6)))

Fee._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValidFromTime'), pyxb.binding.datatypes.dateTime, scope=Fee, documentation='\n            The time when the fee takes effect.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1500, 6)))

Fee._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValidToTime'), pyxb.binding.datatypes.dateTime, scope=Fee, documentation='\n            The time when the fee expires.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1507, 6)))

Fee._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FromDateOfBirth'), pyxb.binding.datatypes.date, scope=Fee, documentation='\n            The start of the birth date interval that the fee should be applied to. Omit if no lower birth date restriction.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1514, 6)))

Fee._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ToDateOfBirth'), pyxb.binding.datatypes.date, scope=Fee, documentation='\n            The end of the birth date interval that the fee should be applied to. Omit if no upper birth date restriction.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1521, 6)))

Fee._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=Fee, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1528, 6)))

def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1464, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1472, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1479, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1486, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1493, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1500, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1507, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1514, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1521, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1528, 6))
    counters.add(cc_9)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Fee._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1464, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Fee._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1465, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Fee._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Amount')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1472, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Fee._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TaxableAmount')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1479, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Fee._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Percentage')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1486, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Fee._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TaxablePercentage')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1493, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Fee._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValidFromTime')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1500, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Fee._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValidToTime')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1507, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Fee._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FromDateOfBirth')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1514, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Fee._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ToDateOfBirth')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1521, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Fee._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1528, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Fee._Automaton = _BuildAutomaton_57()




StartTimeAllocationRequest._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), Organisation, scope=StartTimeAllocationRequest, documentation='\n            The reference organisation for the start time allocation request.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1860, 6)))

StartTimeAllocationRequest._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Person'), Person, scope=StartTimeAllocationRequest, documentation='\n            The reference person for the start time allocation request.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1867, 6)))

def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1860, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1867, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(StartTimeAllocationRequest._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Organisation')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1860, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(StartTimeAllocationRequest._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Person')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 1867, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
StartTimeAllocationRequest._Automaton = _BuildAutomaton_58()




SplitTime._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlCode'), pyxb.binding.datatypes.string, scope=SplitTime, documentation='\n            The code of the control.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3063, 6)))

SplitTime._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Time'), pyxb.binding.datatypes.double, scope=SplitTime, documentation='\n            The time, in seconds, elapsed from start to punching the control. Fractions of seconds (e.g. 258.7) may be used if the time resolution is higher than one second.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3070, 6)))

SplitTime._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=SplitTime, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3077, 6)))

def _BuildAutomaton_59 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3070, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3077, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SplitTime._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ControlCode')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3063, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SplitTime._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Time')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3070, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SplitTime._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3077, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SplitTime._Automaton = _BuildAutomaton_59()




Control._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Id, scope=Control, documentation='\n            The code of the control.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3250, 6)))

Control._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PunchingUnitId'), Id, scope=Control, documentation='\n            If the control has multiple punching units with separate codes, specify all these codes using elements of this kind. Omit this element if there is a single punching unit whose code is the same as the control code.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3257, 6)))

Control._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), LanguageString, scope=Control, documentation="\n            The name of the control, used for e.g. online controls ('spectator control', 'prewarning').\n          ", location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3264, 6)))

Control._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Position'), GeoPosition, scope=Control, documentation='\n            The geographical position of the control.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3271, 6)))

Control._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MapPosition'), MapPosition, scope=Control, documentation="\n            The position of the control according to tha map's coordinate system.\n          ", location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3278, 6)))

Control._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=Control, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3285, 6)))

def _BuildAutomaton_60 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3250, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3257, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3264, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3271, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3278, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3285, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Control._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3250, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Control._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PunchingUnitId')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3257, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Control._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3264, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Control._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Position')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3271, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Control._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MapPosition')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3278, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Control._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3285, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Control._Automaton = _BuildAutomaton_60()




def _BuildAutomaton_61 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3842, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3843, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3850, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3857, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3864, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3871, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SimpleRaceCourse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3842, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SimpleRaceCourse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3843, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SimpleRaceCourse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CourseFamily')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3850, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SimpleRaceCourse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Length')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3857, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(SimpleRaceCourse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Climb')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3864, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SimpleRaceCourse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumberOfControls')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3871, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SimpleRaceCourse._Automaton = _BuildAutomaton_61()




CourseControl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Control'), pyxb.binding.datatypes.string, scope=CourseControl, documentation='\n            The code(s) of the control(s), without course-specific information. Specifying multiple control codes means that the competitor is required to punch one of the controls, but not all of them.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3907, 6)))

CourseControl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MapText'), pyxb.binding.datatypes.string, scope=CourseControl, documentation='\n            Indicates the text shown next to the control circle, i.e. the control number.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3914, 6)))

CourseControl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MapTextPosition'), MapPosition, scope=CourseControl, documentation='\n            Indicates the position of the center of the text relative to the center of the control circle.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3921, 6)))

CourseControl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LegLength'), pyxb.binding.datatypes.double, scope=CourseControl, documentation='\n            The length in meters from the previous control on the course. For starts, this length may refer to the distance from the time start to the start flag.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3928, 6)))

CourseControl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Score'), pyxb.binding.datatypes.double, scope=CourseControl, documentation='\n            The score of the control in score-O events.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3935, 6)))

CourseControl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), Extensions, scope=CourseControl, documentation='\n            Container element for custom elements from other schemas.\n          ', location=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3942, 6)))

def _BuildAutomaton_62 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3914, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3921, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3928, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3935, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3942, 6))
    counters.add(cc_4)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CourseControl._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Control')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3907, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CourseControl._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MapText')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3914, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CourseControl._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MapTextPosition')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3921, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CourseControl._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LegLength')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3928, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CourseControl._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Score')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3935, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CourseControl._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('C:\\Users\\ASUS-Rok\\workspace\\oevent2xml\\IOF.xsd', 3942, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CourseControl._Automaton = _BuildAutomaton_62()

