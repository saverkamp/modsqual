#!/usr/bin/python

from lxml import etree, objectify
from collections import Counter, defaultdict
import xmltodict

sample1 = u'<?xml version="1.0" encoding="UTF-8"?> <mods xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.loc.gov/mods/v3" version="3.4" xsi:schemaLocation="http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-4.xsd"> <titleInfo usage="primary"> <title>Bal de Sceaux</title> </titleInfo> <typeOfResource usage="primary">still image</typeOfResource> <genre authority="lctgm" valueURI="http://id.loc.gov/vocabulary/graphicMaterials/tgm008237">Prints</genre> <genre authority="tgm" usage="primary" valueURI="http://id.loc.gov/vocabulary/graphicMaterials/tgm001698">Caricatures</genre> <genre authority="aat" valueURI="">lithographs</genre> <genre authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh99001244">Caricatures and cartoons</genre> <identifier type="oclc">792748710</identifier> <identifier type="local_bnumber" displayLabel="NYPL catalog ID (B-number)">b19608357</identifier> <location> <physicalLocation authority="marcorg" type="repository">nn</physicalLocation> <physicalLocation type="division">Jerome Robbins Dance Division</physicalLocation> <physicalLocation type="division_short_name">Jerome Robbins Dance Division</physicalLocation> <physicalLocation type="code">DAN</physicalLocation> </location> <location> <shelfLocator>*MGZFD Del F Bal 1</shelfLocator> <physicalLocation type="division">Jerome Robbins Dance Division</physicalLocation> <physicalLocation type="division_short_name">Jerome Robbins Dance Division</physicalLocation> <physicalLocation type="code">DAN</physicalLocation> </location> <name type="personal" usage="primary" authority="naf" valueURI="http://id.loc.gov/authorities/names/n97874402"> <role> <roleTerm authority="marcrelator" type="code">ltg</roleTerm> <roleTerm authority="marcrelator" valueURI="http://id.loc.gov/vocabulary/relators/ltg" type="text">Lithographer</roleTerm> </role> <namePart>Delpech, François Séraphin, 1778-1825</namePart> </name> <name type="personal" authority="naf" valueURI="http://id.loc.gov/authorities/names/n97861896"> <role> <roleTerm authority="marcrelator" type="code">att </roleTerm> </role> <namePart>Lecomte, Hippolyte, 1781-1857</namePart> </name> <originInfo> <place> <placeTerm type="text">Paris?</placeTerm> </place> <publisher>Chez Martinet?</publisher> <dateIssued>183-?</dateIssued> </originInfo> <originInfo><dateCreated>1835</dateCreated> </originInfo> <physicalDescription> <extent>1 print : lithograph, hand-colored ; 24 x 32 cm.</extent> </physicalDescription> <abstract type="Summary">Depiction of a ball under a tent or awning, with trees in the background. Four women and three men, with oversized heads and exaggerated facial features and bodies, are engaged in various interactions: at left, a man invites a young woman to dance, while her mother or chaperon looks on; at center, a couple is dancing, flanked by a man and a woman. Two male musicians play on an elevated stand. The back views of a bonneted woman and a man are visible in the distance.</abstract> <note type="statement of responsibility" altRepGroup="00">Lecomte ; y. lithog. de F. Delpech.</note> <note>Caption title.</note> <note>At upper right: No. 2.</note> <note>Although the image is signed on stone, the artist\'s first initial is difficult to read. His last name, Lecomte, may indicate that he was Hippolyte Lecomte, with whom the lithographer François Séraphin Delpech is known to have collaborated.</note> <note type="acquisition">Gift; Lincoln Kirstein.</note> <note type="biographical/historical">François Séraphin Delpech was a French lithographer and publisher.</note> <note type="biographical/historical">It is uncertain whether this print bears any relationship to Honoré de Balzac\'s novel Le bal de Sceaux, first published in 1830.</note> <subject authority="lcsh"> <topic authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh85011339">Ballroom dancing</topic> <geographic authority="naf" valueURI="http://id.loc.gov/authorities/names/n79006404">France</geographic> <temporal authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh2002012475">19th century</temporal> </subject> <subject authority="lcsh"> <topic authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh85011339">Ballroom dancing</topic> </subject> <subject authority="lcsh"> <topic authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh85035659">Dance</topic> </subject> <recordInfo> <descriptionStandard>gihc</descriptionStandard> <recordContentSource authority="marcorg">NYP</recordContentSource> <recordIdentifier>792748710</recordIdentifier> <recordOrigin>Converted from MARCXML to MODS version 3.5 using MARC21slim2MODS3-5.xsl (Revision 1.102 2014/08/12)</recordOrigin> </recordInfo> <identifier type="uuid">74c80cf0-0baf-0133-ce9e-58d385a7bbd0</identifier> <relatedItem type="host"> <titleInfo> <title>Subjects</title> </titleInfo> <identifier type="uuid">cca17700-c6f4-012f-328a-58d385a7bc34</identifier> <identifier type="local_hades">855699 </identifier> <relatedItem type="host"> <titleInfo> <title>Prints depicting dance</title> </titleInfo> <identifier type="uuid">bb5c4380-c6f4-012f-df87-58d385a7bc34</identifier> <identifier type="local_hades">855695 </identifier> </relatedItem> </relatedItem> </mods>'
sample2 = u'<?xml version="1.0" encoding="UTF-8"?><mods xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.loc.gov/mods/v3" version="3.4" xsi:schemaLocation="http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-4.xsd">  <titleInfo usage="primary" supplied="no">    <title>Scene in front of the "wickedest man\'s" dance-house.</title>  </titleInfo>  <typeOfResource>still image</typeOfResource>  <identifier type="local_hades_collection" displayLabel="Hades Collection Guide ID (legacy)">482</identifier>  <identifier type="local_other" displayLabel="Dynix">1616195</identifier>  <identifier type="local_bnumber" displayLabel="NYPL catalog ID (B-number)">b17539114</identifier>  <identifier type="local_hades" displayLabel="Hades struc ID (legacy)">693446</identifier>  <identifier type="local_barcode" displayLabel="Barcode">33333159165923</identifier>  <location>    <physicalLocation authority="marcorg" type="repository">nn</physicalLocation>    <physicalLocation type="division">Art and Picture Collection</physicalLocation>    <physicalLocation type="division_short_name">Art and Picture Collection</physicalLocation>    <physicalLocation type="code">MMPC</physicalLocation>  </location>  <location>    <shelfLocator>PC NEW YC-Lif-18</shelfLocator>  </location>  <location>    <physicalLocation type="division">Art and Picture Collection</physicalLocation>    <physicalLocation type="division_short_name">Art and Picture Collection</physicalLocation>    <physicalLocation type="code">MMPC</physicalLocation>  </location>  <physicalDescription>    <extent>1 print : b ; 10 x 13 cm. (4 x 4 3/4 in.)</extent>  </physicalDescription>  <name type="personal" authority="" valueURI="" usage="primary">    <namePart>Fox, Stanley</namePart>    <role>      <roleTerm valueURI="http://id.loc.gov/vocabulary/relators/art" authority="marcrelator" type="code">art</roleTerm>      <roleTerm valueURI="http://id.loc.gov/vocabulary/relators/art" authority="marcrelator" type="text">Artist</roleTerm>    </role>  </name>  <originInfo>    <dateIssued encoding="w3cdtf" keyDate="yes">1868</dateIssued>  </originInfo> <originInfo>    <dateCreated encoding="w3cdtf" keyDate="yes" point="start">1860</dateCreated> <dateCreated encoding="w3cdtf" keyDate="yes">1870</dateCreated>  </originInfo> <note type="content">Written on border: "8. 19. 1868."</note>  <subject>    <topic authority="tgm" valueURI="http://id.loc.gov/vocabulary/graphicMaterials/tgm006241">Manners &amp; customs</topic>    <geographic authority="naf" valueURI="http://id.loc.gov/authorities/names/n80126293">New York (State)</geographic>    <geographic>New York</geographic>    <temporal>1800-1899</temporal>  </subject>  <subject>    <topic authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh85034333">Crowds</topic>    <geographic authority="naf" valueURI="http://id.loc.gov/authorities/names/n80126293">New York (State)</geographic>    <geographic>New York</geographic>    <temporal>1800-1899</temporal>  </subject>  <subject>    <topic authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh2003000157">Dance halls</topic>    <geographic authority="naf" valueURI="http://id.loc.gov/authorities/names/n80126293">New York (State)</geographic>    <geographic>New York</geographic>    <temporal>1800-1899</temporal>  </subject>  <identifier type="uuid">9ed4e210-c55e-012f-b4eb-58d385a7bc34</identifier>  <relatedItem type="host">    <titleInfo>      <title>New York City -- Life -- 1800s</title>    </titleInfo>    <identifier type="uuid">710a4430-c55e-012f-bdb0-58d385a7bc34</identifier>    <identifier type="local_hades">693421 local_other</identifier>    <relatedItem type="host">      <titleInfo>        <title>Mid-Manhattan Picture Collection</title>      </titleInfo>      <identifier type="uuid">79d4a650-c52e-012f-67ad-58d385a7bc34</identifier>      <identifier type="local_hades">569241 local_hades_collection</identifier>    </relatedItem>  </relatedItem></mods>'

#replace with your mods namespace if you're not using this one
modsns = 'http://www.loc.gov/mods/v3'

modstoplevels = ['titleInfo', 'name', 'typeOfResource', 'genre', 'originInfo', 'language',
                  'physicalDescription', 'abstract', 'tableOfContents', 'targetAudience', 
                  'note', 'subject', 'classification', 'relatedItem', 'identifier', 'location',
                  'accessCondition', 'part', 'extension', 'recordInfo']

def ln(tag):
    localname = etree.QName(tag).localname
    return localname

def count(mods, element):
    try:
        return len(mods.findall(element))
    except IndexError:
        return 0
    
def existence(mods, element):
    """Check if an element exists, returns true or false."""
    if len(mods.findall(element)) > 0:
        return True
    else:
        return False
    
def todict(mods):
    """Returns a list of dicts, one per element instance."""
    ixml = [(etree.tostring(i), ln(i)) for i in mods]
    idict = [xmltodict.parse(x[0], process_namespaces=False) for x in ixml]
    return idict
        
def byattr(elem, attr, subels=[]):
    """Returns a dictionary of text values by specified attribute."""
    att = '@' + attr
    byatts = []
    tag = elem.tag
    for d in elem.dict:
        if att in d[tag].keys():
            if len(subels) > 0:
                texts = {s : d[tag][s] for s in subels if s in d[tag].keys()}
            else:
                texts = d[tag]['#text']
            byatts.append((d[tag][att], texts))    
    dictbyatts = defaultdict(list)
    for a, v in byatts:
        dictbyatts[a].append(v)
    return dictbyatts

def text(elem):
    """Returns a list of texts for all text instances within an element or its children."""
    if elem.exists:
        texts = []
        for i in elem.mods:
            if i.text:
                texts.append(i.text)
            else:
                childtexts = [c for c in i.itertext()]
                texts.append(childtexts)
    else:
        texts = None
    return texts

class Element(object):
    def __init__(self, mods, modselement):
        #self.mods = mods.findall(modselement)
        #self.modsvalue = modsvalue(mods, self.modselement)
        self.name = modselement.replace('{*}', '')
        self.exists = existence(mods, modselement)
        self.count = count(mods, modselement)
        if self.exists:
            self.mods = getattr(mods, self.name)
            self.tag = ln(self.mods)
            self.dict = todict(self.mods)
        else:
            self.mods = None
            self.tag = modselement.replace('{*}', '')
            self.dict = []

    def text(self):
        texts = text(self)
        return texts
    
    def match(self, attr=[], regex='', xpath='', flag=''):
        """
        Wrapper around lxml.objectify to match element values through regex, attribute value, or xpath.     
        Returns a list of lxml.objectify xpath results.
        Arguments:
        attr: Given a list of attribute values of the element, returns matching instances of that element, To match by attribute,
        specify as attribute="attr value" in a comma-delimited list, ex. ['@authority="lcnaf"'].
        regex: Given a regular expression, returns instances of that element where the regex matches the text value. More info 
        on regex at http://exslt.org/regexp/index.html
        xpath: Given a valid xpath expression, returns instances of matching elements. Xpaths should treat parent MODS as root and
        include the element tag. (ex. './m:subject[*[@authority="lcsh"]]') Prepend any element tags with namespace 'm:'
        flag: flags for refining regex: 
              g: global match - the submatches from all the matches in the string are returned. 
                 If this character is not present, then only the submatches from the first match in the string are returned.
              i: case insensitive - the regular expression is treated as case insensitive. If this character is not present,
                 then the regular expression is case sensitive.
        """
        if self.exists:
            selftag = 'm:' + ln(self.mods.tag)
            regexpNS = "http://exslt.org/regular-expressions"
            if regex != '':            
                if flag != '':
                    flag = ', "' + flag + '"'
                path = './{0}[text()[re:test(., "{1}"{2})]]'.format(selftag,regex,flag)
            elif len(attr) >= 1:
                attrs = ['['+ a + ']' for a in attr]
                attrs = ''.join(attrs)
                path = './{0}{1}'.format(selftag,attrs)
            elif xpath != '':
                path = xpath
            find = etree.XPath(path, namespaces={'re':regexpNS, 'm':modsns})
            xxpath = find(self.mods.getparent())
            thematch = xxpath
            return thematch
        else:
            thematch = None
        return None
    
    def xml(self):
        '''Returns a list of xml representations for all instances of an element in a document.'''
        if self.exists:
            xml = []
            for s in self.mods:
                x = etree.tostring(s, pretty_print=True)
                xml.append(x)
        else:
            xml = None
        return xml
    
class Abstract(Element):
    def __init__(self, mods, modselement='{*}abstract'):
        Element.__init__(self, mods, modselement)  
        
class AccessCondition(Element):
    def __init__(self, mods, modselement='{*}accessCondition'):
        Element.__init__(self, mods, modselement)         
                
class Classification(Element):
    def __init__(self, mods, modselement='{*}classification'):
        Element.__init__(self, mods, modselement)   
        
class Extension(Element):
    def __init__(self, mods, modselement='{*}extension'):
        Element.__init__(self, mods, modselement)    
                
class Genre(Element):
    def __init__(self, mods, modselement='{*}genre'):
        Element.__init__(self, mods, modselement) 
        
class Identifier(Element):
    def __init__(self, mods, modselement='{*}identifier'):
        Element.__init__(self, mods, modselement)  
        
class Language(Element):
    def __init__(self, mods, modselement='{*}language'):
        Element.__init__(self, mods, modselement)  
        
class Location(Element):
    def __init__(self, mods, modselement='{*}location'):
        Element.__init__(self, mods, modselement)
        
class Name(Element):
    def __init__(self, mods, modselement='{*}name'):
        Element.__init__(self, mods, modselement)  
        
class Note(Element):
    def __init__(self, mods, modselement='{*}note'):
        Element.__init__(self, mods, modselement)  
        
class OriginInfo(Element):
    def __init__(self, mods, modselement='{*}originInfo'):
        Element.__init__(self, mods, modselement)    
        
class Part(Element):
    def __init__(self, mods, modselement='{*}part'):
        Element.__init__(self, mods, modselement)     
        
class PhysicalDescription(Element):
    def __init__(self, mods, modselement='{*}physicalDescription'):
        Element.__init__(self, mods, modselement)   
        
class RecordInfo(Element):
    def __init__(self, mods, modselement='{*}recordInfo'):
        Element.__init__(self, mods, modselement)  
        
class RelatedItem(Element):
    def __init__(self, mods, modselement='{*}relatedItem'):
        Element.__init__(self, mods, modselement)  
        
class Subject(Element):
    def __init__(self, mods, modselement='{*}subject'):
        Element.__init__(self, mods, modselement)
        counts = Counter()
        if self.exists == 'true':
            for c in self.mods.getchildren():
                counts[ln(c.tag)] += 1
            self.counts = dict(counts)
        else:
            self.counts = None
        self.subels = ['topical', 'geographic', 'temporal', 'genre', 'name', 'titleInfo', 'hierarchicalGeographic',
                       'geographicCode', 'cartographics', 'occupation']
        
    def text(self):
        texts = (text(self))
        if texts is not None:
            formattedtexts = []
            for t in texts:
                formattedtexts.append(' -- '.join(t))
        else:
            formattedtexts = None
        return formattedtexts 
        
class TableOfContents(Element):
    def __init__(self, mods, modselement='{*}tableOfContents'):
        Element.__init__(self, mods, modselement)  

class TargetAudience(Element):
    def __init__(self, mods, modselement='{*}targetAudience'):
        Element.__init__(self, mods, modselement)  
        
class TitleInfo(Element):
    def __init__(self, mods, modselement='{*}titleInfo'):
        Element.__init__(self, mods, modselement)  
        counts = Counter()
        if self.exists == 'true':
            for c in self.mods.getchildren():
                counts[ln(c.tag)] += 1
            self.counts = dict(counts)
        else:
            self.counts = None
        self.subels = ['nonSort', 'title', 'subTitle', 'partName', 'partNumber']
        
    def byattr(self, attr):
        return byattr(self, attr, subels=self.subels)
        
class TypeOfResource(Element):
    def __init__(self, mods, modselement='{*}typeOfResource'):
        Element.__init__(self, mods, modselement)        
        
class Mods(object):
    def __init__(self, record, allelements=True):
        """Takes a MODS XML string and creates a MODS object. Set allelements to False if you do not 
        want to create subobjects for top-level elements."""
        try:
            mods = record.replace('<?xml version="1.0" encoding="UTF-8"?>', '')
            #parser = etree.XMLParser(remove_blank_text=True)
            self.mods = objectify.fromstring(mods)          
            #if this works, the record is well-formed
            self.wf = True
            #get counts of all top-level elements
            counts = Counter()
            for c in self.mods.getchildren():
                counts[ln(c.tag)] += 1
            self.counts = dict(counts)
            #a list of the top level elements present in the document
            self.toplevels = [k for k in self.counts.keys()]
            
        except:
            #if unable to parse, the record is likely malformed
            self.wf = False
        
        if self.wf:
            if allelements:
                self.getAbstract()
                self.getAccessCondition()
                self.getClassification()
                self.getExtension()
                self.getGenre()
                self.getIdentifier()
                self.getLanguage()
                self.getLocation()
                self.getName()
                self.getNote()
                self.getOriginInfo()
                self.getPart()
                self.getPhysicalDescription()
                self.getRecordInfo()
                self.getRelatedItem()
                self.getSubject()
                self.getTableOfContents()
                self.getTargetAudience()
                self.getTitleInfo()
                self.getTypeOfResource()

                    
    def getAbstract(self):
        self.abstract = Abstract(self.mods)

    def getAccessCondition(self):
        self.accessCondition = AccessCondition(self.mods)
        
    def getClassification(self):
        self.classification = Classification(self.mods)
        
    def getExtension(self):
        self.extension = Extension(self.mods)

    def getGenre(self):
        self.genre = Genre(self.mods)
        
    def getIdentifier(self):
        self.identifier = Identifier(self.mods)
        
    def getLanguage(self):
        self.language = Language(self.mods)
        
    def getLocation(self):
        self.location = Location(self.mods)
              
    def getName(self):
        self.name = Name(self.mods)
        
    def getNote(self):
        self.note = Note(self.mods)

    def getOriginInfo(self):
        self.originInfo = OriginInfo(self.mods)
        
    def getPart(self):
        self.part = Part(self.mods)
        
    def getPhysicalDescription(self):
        self.physicalDescription = PhysicalDescription(self.mods)

    def getRecordInfo(self):
        self.recordInfo = RecordInfo(self.mods)
        
    def getRelatedItem(self):
        self.relatedItem = RelatedItem(self.mods)
       
    def getSubject(self):
        self.subject = Subject(self.mods)
        
    def getTableOfContents(self):
        self.tableOfContents = TableOfContents(self.mods)
        
    def getTargetAudience(self):
        self.targetAudience = TargetAudience(self.mods)
        
    def getTitleInfo(self):
        self.titleInfo = TitleInfo(self.mods)
        
    def getTypeOfResource(self):
        self.typeOfResource = TypeOfResource(self.mods)

    def match(self, attr=[], regex='', xpath='', flag=''):
        """
        Wrapper around lxml.objectify to match element values through regex, attribute value, or xpath.     
        Returns a list of lxml.objectify xpath results.
        Arguments:
        attr: Given a list of attribute values of the element, returns matching instances of that element, To match by attribute,
        specify as attribute="attr value" in a comma-delimited list, ex. ['@authority="lcnaf"'].
        regex: Given a regular expression, returns instances of that element where the regex matches the text value. More info 
        on regex at http://exslt.org/regexp/index.html
        xpath: Given a valid xpath expression, returns instances of matching elements. Prepend any element tags with namespace 'm:'
        flag: flags for refining regex: 
              g: global match - the submatches from all the matches in the string are returned. 
                 If this character is not present, then only the submatches from the first match in the string are returned.
              i: case insensitive - the regular expression is treated as case insensitive. If this character is not present,
                 then the regular expression is case sensitive.
        """
        selftag = 'm:' + ln(self.mods.tag)
        regexpNS = "http://exslt.org/regular-expressions"
        if regex != '':            
            if flag != '':
                flag = ', "' + flag + '"'
            path = './*[text()[re:test(., "{0}"{1})]]'.format(regex,flag)
        elif len(attr) >= 1:
            attrs = ['['+ a + ']' for a in attr]
            attrs = ''.join(attrs)
            path = './*{0}'.format(attrs)
        elif regex != '':
            path = regex
        find = etree.XPath(path, namespaces={'re':regexpNS, 'm':modsns})
        xpath = find(self.mods)
        return xpath
    
    def xml(self):
        """Returns an XML representation of the MODS document."""
        xml = etree.tostring(self.mods, pretty_print=True)
        return xml
    
if __name__ == '__main__':
    mods1 = Mods(sample1)
    print mods1.wf
    if mods1.wf:
        print mods1.counts
        for a in modstoplevels:
            element = getattr(mods1, a)
            print element.name + ': ' + str(element.exists)
        for t in mods1.toplevels:
            element = getattr(mods1, t)
            print 'NAME: ' + element.name
            print 'COUNT: ' + str(element.count)
            print 'TAG: ' + element.tag
            print 'XML:'
            print element.xml()
            print 'DICT:'
            print element.dict
            print 'TEXT:'
            print element.text()