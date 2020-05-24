
import base64
import binascii
from zlib import decompress
from xml.dom import minidom 


class PaReqUtils:
  def extract_xml(self,pareq_encode):
    try:
        xml_data = decompress(self._decode_pareq(pareq_encode))
        xml = minidom.parseString(xml_data)
        return xml.toprettyxml()

    except xml.parsers.expat.ExpatError as e:
        # You will get a xml.parsers.expat.ExpatError if the XML is invalid.
        print(e)
    
  def _decode_pareq(self, pareq):
    try:
        return base64.b64decode(pareq)
    except binascii.Error as e:
        # A binascii.Error exception is raised if s is incorrectly padded.
        print(e)
    

    


