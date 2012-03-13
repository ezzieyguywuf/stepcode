# This file was generated by fedex_python.  You probably don't want to edit
# it since your modifications will be lost if fedex_plus is used to
# regenerate it.
import sys

from SCL.SCLBase import *
from SCL.SimpleDataTypes import *
from SCL.ConstructedDataTypes import *
from SCL.AggregationDataTypes import *
from SCL.TypeChecker import check_type
from SCL.Builtin import *
from SCL.Rules import *
from SCL.Algorithms import *

schema_name = 'test_multiple_inheritance'

schema_scope = sys.modules[__name__]

# SELECT TYPE classification_item
classification_item = SELECT(
	'person_and_organization_address',
	'address',
	scope = schema_scope)
# Defined datatype text
class text(STRING):
	pass
# Defined datatype identifier
class identifier(STRING):
	pass
# Defined datatype label
class label(STRING):
	pass

####################
 # ENTITY address #
####################
class address(BaseEntityClass):
	'''Entity address definition.

	:param internal_location
	:type internal_location:label

	:param street_number
	:type street_number:label

	:param street
	:type street:label

	:param postal_box
	:type postal_box:label

	:param town
	:type town:label

	:param region
	:type region:label

	:param postal_code
	:type postal_code:label

	:param country
	:type country:label

	:param facsimile_number
	:type facsimile_number:label

	:param telephone_number
	:type telephone_number:label

	:param electronic_mail_address
	:type electronic_mail_address:label

	:param telex_number
	:type telex_number:label
	'''
	def __init__( self , internal_location,street_number,street,postal_box,town,region,postal_code,country,facsimile_number,telephone_number,electronic_mail_address,telex_number, ):
		self.internal_location = internal_location
		self.street_number = street_number
		self.street = street
		self.postal_box = postal_box
		self.town = town
		self.region = region
		self.postal_code = postal_code
		self.country = country
		self.facsimile_number = facsimile_number
		self.telephone_number = telephone_number
		self.electronic_mail_address = electronic_mail_address
		self.telex_number = telex_number

	@apply
	def internal_location():
		def fget( self ):
			return self._internal_location
		def fset( self, value ):
			if value != None: # OPTIONAL attribute
				if not check_type(value,label):
					self._internal_location = label(value)
			else:
				self._internal_location = value
		return property(**locals())

	@apply
	def street_number():
		def fget( self ):
			return self._street_number
		def fset( self, value ):
			if value != None: # OPTIONAL attribute
				if not check_type(value,label):
					self._street_number = label(value)
			else:
				self._street_number = value
		return property(**locals())

	@apply
	def street():
		def fget( self ):
			return self._street
		def fset( self, value ):
			if value != None: # OPTIONAL attribute
				if not check_type(value,label):
					self._street = label(value)
			else:
				self._street = value
		return property(**locals())

	@apply
	def postal_box():
		def fget( self ):
			return self._postal_box
		def fset( self, value ):
			if value != None: # OPTIONAL attribute
				if not check_type(value,label):
					self._postal_box = label(value)
			else:
				self._postal_box = value
		return property(**locals())

	@apply
	def town():
		def fget( self ):
			return self._town
		def fset( self, value ):
			if value != None: # OPTIONAL attribute
				if not check_type(value,label):
					self._town = label(value)
			else:
				self._town = value
		return property(**locals())

	@apply
	def region():
		def fget( self ):
			return self._region
		def fset( self, value ):
			if value != None: # OPTIONAL attribute
				if not check_type(value,label):
					self._region = label(value)
			else:
				self._region = value
		return property(**locals())

	@apply
	def postal_code():
		def fget( self ):
			return self._postal_code
		def fset( self, value ):
			if value != None: # OPTIONAL attribute
				if not check_type(value,label):
					self._postal_code = label(value)
			else:
				self._postal_code = value
		return property(**locals())

	@apply
	def country():
		def fget( self ):
			return self._country
		def fset( self, value ):
			if value != None: # OPTIONAL attribute
				if not check_type(value,label):
					self._country = label(value)
			else:
				self._country = value
		return property(**locals())

	@apply
	def facsimile_number():
		def fget( self ):
			return self._facsimile_number
		def fset( self, value ):
			if value != None: # OPTIONAL attribute
				if not check_type(value,label):
					self._facsimile_number = label(value)
			else:
				self._facsimile_number = value
		return property(**locals())

	@apply
	def telephone_number():
		def fget( self ):
			return self._telephone_number
		def fset( self, value ):
			if value != None: # OPTIONAL attribute
				if not check_type(value,label):
					self._telephone_number = label(value)
			else:
				self._telephone_number = value
		return property(**locals())

	@apply
	def electronic_mail_address():
		def fget( self ):
			return self._electronic_mail_address
		def fset( self, value ):
			if value != None: # OPTIONAL attribute
				if not check_type(value,label):
					self._electronic_mail_address = label(value)
			else:
				self._electronic_mail_address = value
		return property(**locals())

	@apply
	def telex_number():
		def fget( self ):
			return self._telex_number
		def fset( self, value ):
			if value != None: # OPTIONAL attribute
				if not check_type(value,label):
					self._telex_number = label(value)
			else:
				self._telex_number = value
		return property(**locals())

####################
 # ENTITY personal_address #
####################
class personal_address(address):
	'''Entity personal_address definition.

	:param people
	:type people:SET(1,None,'person', scope = schema_scope)

	:param description
	:type description:text
	'''
	def __init__( self , inherited0__internal_location , inherited1__street_number , inherited2__street , inherited3__postal_box , inherited4__town , inherited5__region , inherited6__postal_code , inherited7__country , inherited8__facsimile_number , inherited9__telephone_number , inherited10__electronic_mail_address , inherited11__telex_number , people,description, ):
		address.__init__(self , inherited0__internal_location , inherited1__street_number , inherited2__street , inherited3__postal_box , inherited4__town , inherited5__region , inherited6__postal_code , inherited7__country , inherited8__facsimile_number , inherited9__telephone_number , inherited10__electronic_mail_address , inherited11__telex_number , )
		self.people = people
		self.description = description

	@apply
	def people():
		def fget( self ):
			return self._people
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument people is mantatory and can not be set to None')
			if not check_type(value,SET(1,None,'person', scope = schema_scope)):
				self._people = SET(value)
			else:
				self._people = value
		return property(**locals())

	@apply
	def description():
		def fget( self ):
			return self._description
		def fset( self, value ):
			if value != None: # OPTIONAL attribute
				if not check_type(value,text):
					self._description = text(value)
			else:
				self._description = value
		return property(**locals())

####################
 # ENTITY organizational_address #
####################
class organizational_address(address):
	'''Entity organizational_address definition.

	:param organizations
	:type organizations:SET(1,None,'organization', scope = schema_scope)

	:param description
	:type description:text
	'''
	def __init__( self , inherited0__internal_location , inherited1__street_number , inherited2__street , inherited3__postal_box , inherited4__town , inherited5__region , inherited6__postal_code , inherited7__country , inherited8__facsimile_number , inherited9__telephone_number , inherited10__electronic_mail_address , inherited11__telex_number , organizations,description, ):
		address.__init__(self , inherited0__internal_location , inherited1__street_number , inherited2__street , inherited3__postal_box , inherited4__town , inherited5__region , inherited6__postal_code , inherited7__country , inherited8__facsimile_number , inherited9__telephone_number , inherited10__electronic_mail_address , inherited11__telex_number , )
		self.organizations = organizations
		self.description = description

	@apply
	def organizations():
		def fget( self ):
			return self._organizations
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument organizations is mantatory and can not be set to None')
			if not check_type(value,SET(1,None,'organization', scope = schema_scope)):
				self._organizations = SET(value)
			else:
				self._organizations = value
		return property(**locals())

	@apply
	def description():
		def fget( self ):
			return self._description
		def fset( self, value ):
			if value != None: # OPTIONAL attribute
				if not check_type(value,text):
					self._description = text(value)
			else:
				self._description = value
		return property(**locals())

####################
 # ENTITY person #
####################
class person(BaseEntityClass):
	'''Entity person definition.

	:param id
	:type id:identifier

	:param last_name
	:type last_name:label

	:param first_name
	:type first_name:label

	:param middle_names
	:type middle_names:LIST(1,None,'STRING', scope = schema_scope)

	:param prefix_titles
	:type prefix_titles:LIST(1,None,'STRING', scope = schema_scope)

	:param suffix_titles
	:type suffix_titles:LIST(1,None,'STRING', scope = schema_scope)
	'''
	def __init__( self , id,last_name,first_name,middle_names,prefix_titles,suffix_titles, ):
		self.id = id
		self.last_name = last_name
		self.first_name = first_name
		self.middle_names = middle_names
		self.prefix_titles = prefix_titles
		self.suffix_titles = suffix_titles

	@apply
	def id():
		def fget( self ):
			return self._id
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument id is mantatory and can not be set to None')
			if not check_type(value,identifier):
				self._id = identifier(value)
			else:
				self._id = value
		return property(**locals())

	@apply
	def last_name():
		def fget( self ):
			return self._last_name
		def fset( self, value ):
			if value != None: # OPTIONAL attribute
				if not check_type(value,label):
					self._last_name = label(value)
			else:
				self._last_name = value
		return property(**locals())

	@apply
	def first_name():
		def fget( self ):
			return self._first_name
		def fset( self, value ):
			if value != None: # OPTIONAL attribute
				if not check_type(value,label):
					self._first_name = label(value)
			else:
				self._first_name = value
		return property(**locals())

	@apply
	def middle_names():
		def fget( self ):
			return self._middle_names
		def fset( self, value ):
			if value != None: # OPTIONAL attribute
				if not check_type(value,LIST(1,None,'STRING', scope = schema_scope)):
					self._middle_names = LIST(value)
			else:
				self._middle_names = value
		return property(**locals())

	@apply
	def prefix_titles():
		def fget( self ):
			return self._prefix_titles
		def fset( self, value ):
			if value != None: # OPTIONAL attribute
				if not check_type(value,LIST(1,None,'STRING', scope = schema_scope)):
					self._prefix_titles = LIST(value)
			else:
				self._prefix_titles = value
		return property(**locals())

	@apply
	def suffix_titles():
		def fget( self ):
			return self._suffix_titles
		def fset( self, value ):
			if value != None: # OPTIONAL attribute
				if not check_type(value,LIST(1,None,'STRING', scope = schema_scope)):
					self._suffix_titles = LIST(value)
			else:
				self._suffix_titles = value
		return property(**locals())

####################
 # ENTITY organization #
####################
class organization(BaseEntityClass):
	'''Entity organization definition.

	:param id
	:type id:identifier

	:param name
	:type name:label

	:param description
	:type description:text
	'''
	def __init__( self , id,name,description, ):
		self.id = id
		self.name = name
		self.description = description

	@apply
	def id():
		def fget( self ):
			return self._id
		def fset( self, value ):
			if value != None: # OPTIONAL attribute
				if not check_type(value,identifier):
					self._id = identifier(value)
			else:
				self._id = value
		return property(**locals())

	@apply
	def name():
		def fget( self ):
			return self._name
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument name is mantatory and can not be set to None')
			if not check_type(value,label):
				self._name = label(value)
			else:
				self._name = value
		return property(**locals())

	@apply
	def description():
		def fget( self ):
			return self._description
		def fset( self, value ):
			if value != None: # OPTIONAL attribute
				if not check_type(value,text):
					self._description = text(value)
			else:
				self._description = value
		return property(**locals())

####################
 # ENTITY person_and_organization_address #
####################
class person_and_organization_address(organizational_address,personal_address):
	'''Entity person_and_organization_address definition.

	:param organizational_address_organizations
	:type organizational_address_organizations:SET(1,1,'organization', scope = schema_scope)

	:param personal_address_people
	:type personal_address_people:SET(1,1,'person', scope = schema_scope)
	'''
	def __init__( self , inherited0__internal_location , inherited1__street_number , inherited2__street , inherited3__postal_box , inherited4__town , inherited5__region , inherited6__postal_code , inherited7__country , inherited8__facsimile_number , inherited9__telephone_number , inherited10__electronic_mail_address , inherited11__telex_number , inherited12__organizations , inherited13__description , inherited14__internal_location , inherited15__street_number , inherited16__street , inherited17__postal_box , inherited18__town , inherited19__region , inherited20__postal_code , inherited21__country , inherited22__facsimile_number , inherited23__telephone_number , inherited24__electronic_mail_address , inherited25__telex_number , inherited26__people , inherited27__description , organizational_address_organizations,personal_address_people, ):
		organizational_address.__init__(self , inherited0__internal_location , inherited1__street_number , inherited2__street , inherited3__postal_box , inherited4__town , inherited5__region , inherited6__postal_code , inherited7__country , inherited8__facsimile_number , inherited9__telephone_number , inherited10__electronic_mail_address , inherited11__telex_number , inherited12__organizations , inherited13__description , )
		personal_address.__init__(self , inherited14__internal_location , inherited15__street_number , inherited16__street , inherited17__postal_box , inherited18__town , inherited19__region , inherited20__postal_code , inherited21__country , inherited22__facsimile_number , inherited23__telephone_number , inherited24__electronic_mail_address , inherited25__telex_number , inherited26__people , inherited27__description , )
		self.organizational_address_organizations = organizational_address_organizations
		self.personal_address_people = personal_address_people

	@apply
	def organizational_address_organizations():
		def fget( self ):
			return self._organizational_address_organizations
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument organizational_address_organizations is mantatory and can not be set to None')
			if not check_type(value,SET(1,1,'organization', scope = schema_scope)):
				self._organizational_address_organizations = SET(value)
			else:
				self._organizational_address_organizations = value
		return property(**locals())

	@apply
	def personal_address_people():
		def fget( self ):
			return self._personal_address_people
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument personal_address_people is mantatory and can not be set to None')
			if not check_type(value,SET(1,1,'person', scope = schema_scope)):
				self._personal_address_people = SET(value)
			else:
				self._personal_address_people = value
		return property(**locals())
