from construct import Select

from .level import GenericLevelMessage
from .light.ctl import LightCTLMessage, LightCTLSetupMessage
from .light.lightness import LightLightnessMessage, LightLightnessSetupMessage
from .light.hsl import LightHSLMessage, LightHSLSetupMessage
from .onoff import GenericOnOffMessage

GenericMessage = Select(
    GenericOnOffMessage,
    GenericLevelMessage,
    LightCTLMessage,
    LightCTLSetupMessage,
    LightLightnessMessage,
    LightLightnessSetupMessage,
    LightHSLMessage,
    LightHSLSetupMessage,
)
