## Copyright (c) 2005-2006, Gillmer J. Derge.

## This file is part of Civilization IV Alerts mod.
##
## Civilization IV Alerts mod is free software; you can redistribute
## it and/or modify it under the terms of the GNU General Public
## License as published by the Free Software Foundation; either
## version 2 of the License, or (at your option) any later version.
##
## Civilization IV Alerts mod is distributed in the hope that it will
## be useful, but WITHOUT ANY WARRANTY; without even the implied
## warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
## See the GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Civilization IV Alerts mod; if not, write to the Free
## Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
## 02110-1301 USA

import CvEventManager
import CvMercEventManager
import CvRFCEventHandler
import RiseAndFall
import Religions
import RFCCWAIWars

class CvCustomEventManager(CvEventManager.CvEventManager, object):

	"""Extends the standard event manager by adding support for multiple
	handlers for each event.
	
	Methods exist for both adding and removing event handlers.  A set method 
	also exists to override the default handlers.  Clients should not depend 
	on event handlers being called in a particular order.
	
	This approach works best with mods that have implemented the design
	pattern suggested on Apolyton by dsplaisted.
	
	http://apolyton.net/foDacias/showthread.php?s=658a68df728b2719e9ebfe842d784002&threadid=142916
	
	The example given in the 8th post in the thread would be handled by adding
	the following lines to the CvCustomEventManager constructor.  The RealFort,
	TechConquest, and CulturalDecay classes can remain unmodified.
	
		self.addEventHandler("unitMove", rf.onUnitMove)
		self.addEventHandler("improvementBuilt", rf.onImprovementBuilt)
		self.addEventHandler("techAcquired", rf.onTechAcquired)
		self.addEventHandler("cityAcquired", tc.onCityAcquired)
		self.addEventHandler("EndGameTurn", cd.onEndGameTurn)
		
	Note that the naming conventions for the event type strings vary from event
	to event.  Some use initial capitalization, some do not; some eliminate the
	"on..." prefix used in the event handler function name, some do not.  Look
	at the unmodified CvEventManager.py source code to determine the correct
	name for a particular event.
	
	Take care with event handlers that also extend CvEventManager.  Since
	this event manager handles invocation of the base class handler function,
	additional handlers should not also call the base class function themselves.
	
	"""

	def __init__(self, *args, **kwargs):
		super(CvCustomEventManager, self).__init__(*args, **kwargs)
		# map the initial EventHandlerMap values into the new data structure
		for eventType, eventHandler in self.EventHandlerMap.iteritems():
			self.setEventHandler(eventType, eventHandler)
			
		self.CustomEvents = {
			7614 : ('RiseAndFallPopupEvent', self.rnfEventApply7614, self.rnfEventBegin7614),
			7615 : ('FlipPopupEvent', self.rnfEventApply7615, self.rnfEventBegin7615),
			7616 : ('PirateBribeAndHirePopupEvent', self.rfccwaiwEventApply7616, self.rfccwaiwEventBegin7616),
			7617 : ('PirateBribeOnlyPopupEvent', self.rfccwaiwEventApply7617, self.rfccwaiwEventBegin7617),
			7622 : ('ResurrectionEvent', self.rnfEventApply7622, self.rnfEventBegin7622),
			7624 : ('HolyWarEvent', self.relEventApply7624, self.relEventBegin7624),
			7625 : ('HolyWarCall', self.relEventApply7625, self.relEventBegin7625),
			7626 : ('Persecution', self.relEventApply7626, self.relEventBegin7626),
			7627 : ('RomanUHVChoice', self.rnfEventApply7627, self.rnfEventBegin7627),
			7628 : ('RomanCivilWarEnd', self.rnfEventApply7628, self.rnfEventBegin7628),
			7629 : ('ThreeKingdomsChoice', self.rnfEventApply7629, self.rnfEventBegin7629),
			7630 : ('SecretDiplomacyVassalize', self.rfccwaiwEventApply7630, self.rfccwaiwEventBegin7630),
			7631 : ('SecretDiplomacySurrender', self.rfccwaiwEventApply7631, self.rfccwaiwEventBegin7631),
		}

		# --> INSERT EVENT HANDLER INITIALIZATION HERE <--
		CvMercEventManager.CvMercEventManager(self)
		CvRFCEventHandler.CvRFCEventHandler(self)
		self.rnf = RiseAndFall.RiseAndFall()
		self.rel = Religions.Religions()
		self.rfccwaiw = RFCCWAIWars.RFCCWAIWars()

	def addEventHandler(self, eventType, eventHandler):
		"""Adds a handler for the given event type.
		
		A list of supported event types can be found in the initialization 
		of EventHandlerMap in the CvEventManager class.
		
		Throws LookupError if the eventType is not valid.

		"""
		if eventType not in self.EventHandlerMap:
			raise LookupError(eventType)
		self.EventHandlerMap[eventType].append(eventHandler)

	def removeEventHandler(self, eventType, eventHandler):
		"""Removes a handler for the given event type.
		
		A list of supported event types can be found in the initialization 
		of EventHandlerMap in the CvEventManager class.  It is an error if 
		the given handler is not found in the list of installed handlers.
		
		Throws LookupError if the eventType is not valid.

		"""
		if eventType not in self.EventHandlerMap:
			raise LookupError(eventType)
		self.EventHandlerMap[eventType].remove(eventHandler)
	
	def setEventHandler(self, eventType, eventHandler):
		"""Removes all previously installed event handlers for the given 
		event type and installs a new handler.
		
		A list of supported event types can be found in the initialization 
		of EventHandlerMap in the CvEventManager class.  This method is 
		primarily useful for overriding, rather than extending, the default 
		event handler functionality.
		
		Throws LookupError if the eventType is not valid.

		"""
		if eventType not in self.EventHandlerMap:
			raise LookupError(eventType)
		self.EventHandlerMap[eventType] = [eventHandler]
	
	def setPopupHandler(self, eventType, popupHandler):
		"""Removes all previously installed popup handlers for the given 
		event type and installs a new handler.
		
		The eventType should be an integer.  It must be unique with respect
		to the integers assigned to built in events.  The popupHandler should
		be a list made up of (name, beginFunction, applyFunction).  The name
		is used in debugging output.  The begin and apply functions are invoked
		by beginEvent and applyEvent, respectively, to manage a popup dialog
		in response to the event.

		"""
		self.Events[eventType] = popupHandler

	def handleEvent(self, argsList):
		"""Handles events by calling all installed handlers."""
		self.origArgsList = argsList
		flagsIndex = len(argsList) - 6
		self.bDbg, self.bMultiPlayer, self.bAlt, self.bCtrl, self.bShift, self.bAllowCheats = argsList[flagsIndex:]
		eventType = argsList[0]
		return {
			"kbdEvent": self._handleConsumableEvent,
			"mouseEvent": self._handleConsumableEvent,
			"OnSave": self._handleOnSaveEvent,
			"OnLoad": self._handleOnLoadEvent
		}.get(eventType, self._handleDefaultEvent)(eventType, argsList[1:])

	def _handleDefaultEvent(self, eventType, argsList):
		if self.EventHandlerMap.has_key(eventType):
			for eventHandler in self.EventHandlerMap[eventType]:
				# the last 6 arguments are for internal use by handleEvent
				eventHandler(argsList[:len(argsList) - 6])

	def _handleConsumableEvent(self, eventType, argsList):
		"""Handles events that can be consumed by the handlers, such as
		keyboard or mouse events.
		
		If a handler returns non-zero, processing is terminated, and no 
		subsequent handlers are invoked.

		"""
		if self.EventHandlerMap.has_key(eventType):
			for eventHandler in self.EventHandlerMap[eventType]:
				# the last 6 arguments are for internal use by handleEvent
				result = eventHandler(argsList[:len(argsList) - 6])
				if (result > 0):
					return result
		return 0

	# TODO: this probably needs to be more complex
	def _handleOnSaveEvent(self, eventType, argsList):
		"""Handles OnSave events by concatenating the results obtained
		from each handler to form an overall consolidated save string.

		"""
		result = ""
		if self.EventHandlerMap.has_key(eventType):
			for eventHandler in self.EventHandlerMap[eventType]:
				# the last 6 arguments are for internal use by handleEvent
				result = result + eventHandler(argsList[:len(argsList) - 6])
		return result

	# TODO: this probably needs to be more complex
	def _handleOnLoadEvent(self, eventType, argsList):
		"""Handles OnLoad events."""
		return self._handleDefaultEvent(eventType, argsList)

	# RFC

	# popup event handlers
	def beginEvent( self, context, argsList=-1 ):
		"""Begin Event"""
		
		if self.CustomEvents.has_key(context):
			return self.CustomEvents[context][2](argsList)
		else:
			super(CvCustomEventManager, self).beginEvent(context, argsList)
		
	def applyEvent( self, argsList ):
		"""Apply the effects of an event"""
		context, playerID, netUserData, popupReturn = argsList
		
		if self.CustomEvents.has_key(context):
			entry = self.CustomEvents[context]
			# the apply function
			return entry[1]( playerID, netUserData, popupReturn )   
		else:
			return super(CvCustomEventManager, self).applyEvent(argsList)

	# popup events
	def rnfEventBegin7614(self):
		pass
  
	def rnfEventApply7614(self, playerID, netUserData, popupReturn):
		self.rnf.eventApply7614(popupReturn)

	def rnfEventBegin7615(self):
		pass
   
	def rnfEventApply7615(self, playerID, netUserData, popupReturn):
		self.rnf.eventApply7615(popupReturn)
		
	def rfccwaiwEventBegin7616(self):
		pass
   
	def rfccwaiwEventApply7616(self, playerID, netUserData, popupReturn):
		self.rfccwaiw.eventApply7616(popupReturn)
		
	def rfccwaiwEventBegin7617(self):
		pass
   
	def rfccwaiwEventApply7617(self, playerID, netUserData, popupReturn):
		self.rfccwaiw.eventApply7617(popupReturn)

	def rnfEventBegin7622(self):
		pass
       
	def rnfEventApply7622(self, playerID, netUserData, popupReturn):
		self.rnf.eventApply7622(popupReturn)

	def relEventBegin7624(self):
		pass

	def relEventApply7624(self, playerID, netUserData, popupReturn):
		self.rel.eventApply7624(popupReturn)

	def relEventApply7625(self, playerID, netUserData, popupReturn):
		self.rel.eventApply7625(popupReturn)

	def relEventBegin7625(self):
		pass

	def relEventBegin7626(self):
		pass

	def relEventApply7626(self, playerID, netUserData, popupReturn):
		self.rel.eventApply7626(popupReturn)
		
	def rnfEventBegin7627(self):
		pass
   
	def rnfEventApply7627(self, playerID, netUserData, popupReturn):
		self.rnf.eventApply7627(popupReturn)
		
	def rnfEventBegin7628(self):
		pass
   
	def rnfEventApply7628(self, playerID, netUserData, popupReturn):
		self.rnf.eventApply7628(popupReturn)
		
	def rnfEventBegin7629(self):
		pass
   
	def rnfEventApply7629(self, playerID, netUserData, popupReturn):
		self.rnf.eventApply7629(popupReturn)
		
	def rfccwaiwEventBegin7630(self):
		pass
   
	def rfccwaiwEventApply7630(self, playerID, netUserData, popupReturn):
		self.rfccwaiw.eventApply7630(popupReturn)
		
	def rfccwaiwEventBegin7631(self):
		pass
   
	def rfccwaiwEventApply7631(self, playerID, netUserData, popupReturn):
		self.rfccwaiw.eventApply7631(popupReturn)
