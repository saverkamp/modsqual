#modsqual

(This is still very much in progress, so use at your own risk! Constructive feedback and pull requests welcome.)

modsqual is a Python library to help you evaluate the quality of your MODS metadata. First and foremost, modsqual aims to make the work of parsing XML easier, so you can spend more time working with your metadata content. modsqual provides a wrapper around the popular lxml Python library, to simplify common quality control tasks, like testing for the existing of an element, counting instances of an element, and searching elements by attribute value, text match, or regular expression.   

modsqual also provides multiple representations of MODS elements to best suit the tools and skills you have at hand. modsqual can return elements in XML, Python ordered dictionaries, or just the text values of an top-level element.   

##Usage

(requires [lxml](http://lxml.de/) and [xmltodict](https://github.com/martinblech/xmltodict))  


To create a MODS object, pass a MODS XML document to the Mods class:  

```python
import modsqual

f = open('sample1.xml', 'rb')
modsdoc = read(f)
record = modsqual.Mods(modsdoc)
```

###Well-formed XML and element existence

Check that the document is wellformed:  

```python
>>> print record.wf  

True
```

Each top-level MODS element is represented as an attribute of the Mods object. Check if the name element exists in the MODS document:

```python
>>> print record.name.exists  

True  
```

###Element counts

View the counts of top-level elements present in your MODS object:

```python
>>> print record.counts  

{u'genre': 1,

 u'identifier': 6,
 u'location': 1,
 u'name': 2,
 u'originInfo': 1,
 u'physicalDescription': 1,
 u'relatedItem': 1,
 u'subject': 3,
 u'titleInfo': 1,
 u'typeOfResource': 1}
 ```

Return the count of a top-level element in the MODS document:

```python
>>> print record.subject.count  

3  
```


###Matching elements and values

The match() function allows you to return matching elements by attribute value, regular expression, or xpath:

Given a list of attribute values of the element, returns matching instances of that element, To match by attribute, specify as attribute="attr value" in a comma-delimited list, ex. `['@authority="lcnaf"']`:

```python
>>> print record.name.match(attr=['@authority="naf"'])  

[OrderedDict([(u'name', OrderedDict([(u'@xmlns', u'http://www.loc.gov/mods/v3'), (u'@xmlns:xsi', u'http://www.w3.org/2001/XMLSchema-instance'), (u'@type', u'personal'), (u'@authority', u'naf'), (u'@valueURI', u''), (u'@usage', u'primary'), (u'namePart', u'Lotter, Matth\xe4us Albrecht (1741-1810 )'), (u'role', OrderedDict([(u'roleTerm', [OrderedDict([(u'@valueURI', u'http://id.loc.gov/vocabulary/relators/ctg'), (u'@authority', u'marcrelator'), (u'@type', u'code'), ('#text', u'ctg')]), OrderedDict([(u'@valueURI', u'http://id.loc.gov/vocabulary/relators/ctg'), (u'@authority', u'marcrelator'), (u'@type', u'text'), ('#text', u'Cartographer')])])]))]))]), OrderedDict([(u'name', OrderedDict([(u'@xmlns', u'http://www.loc.gov/mods/v3'), (u'@xmlns:xsi', u'http://www.w3.org/2001/XMLSchema-instance'), (u'@type', u'personal'), (u'@authority', u'naf'), (u'@valueURI', u''), (u'namePart', u'Lotter, Tobias Conrad (1717-1777 )'), (u'role', OrderedDict([(u'roleTerm', [OrderedDict([(u'@valueURI', u'http://id.loc.gov/vocabulary/relators/pbl'), (u'@authority', u'marcrelator'), (u'@type', u'code'), ('#text', u'pbl')]), OrderedDict([(u'@valueURI', u'http://id.loc.gov/vocabulary/relators/pbl'), (u'@authority', u'marcrelator'), (u'@type', u'text'), ('#text', u'Publisher')])])]))]))])]  
```



Use any regular expression to match text values in the top-level element or its children:

```python
#returns all <identifier> values starting with 4 or more numbers
>>> print record.identifier.match(regex='^[0-9]{4,}')  

[OrderedDict([(u'identifier', OrderedDict([(u'@xmlns', u'http://www.loc.gov/mods/v3'), (u'@xmlns:xsi', u'http://www.w3.org/2001/XMLSchema-instance'), (u'@type', u'local_hades'), (u'@displayLabel', u'Hades struc ID (legacy)'), ('#text', u'300826')]))]), OrderedDict([(u'identifier', OrderedDict([(u'@xmlns', u'http://www.loc.gov/mods/v3'), (u'@xmlns:xsi', u'http://www.w3.org/2001/XMLSchema-instance'), (u'@type', u'local_other'), (u'@displayLabel', u'RLIN/OCLC'), ('#text', u'5416579')]))]), OrderedDict([(u'identifier', OrderedDict([(u'@xmlns', u'http://www.loc.gov/mods/v3'), (u'@xmlns:xsi', u'http://www.w3.org/2001/XMLSchema-instance'), (u'@type', u'uuid'), ('#text', u'900112c0-c52a-012f-640c-3c075448cc4b')]))])]
```

Use the `g` or `i` flags for refining regex:  
 `g` = global match - the submatches from all the matches in the string are returned. If this character is not present, then only the submatches from the first match in the string are returned.  
`i` = case insensitive - the regular expression is treated as case insensitive. If this character is not present, then the regular expression is case sensitive.

You can also use xpath to find elements or values within the Mods object or any top-level element. (Doesn't work yet for returning text results, but I'm working on it.) Xpaths should treat parent MODS as root and include the top-level element's tag. (ex. `./m:subject[*[@authority="lcsh"]]`) Prepend any element tags with namespace `m:`  

```python
>>> print record.location.match(xpath='./m:location[m:physicalLocation[@type="division"]]')  

[OrderedDict([(u'location', OrderedDict([(u'@xmlns', u'http://www.loc.gov/mods/v3'), (u'@xmlns:xsi', u'http://www.w3.org/2001/XMLSchema-instance'), (u'physicalLocation', [OrderedDict([(u'@type', u'division'), ('#text', u'Lionel Pincus and Princess Firyal Map Division')]), OrderedDict([(u'@type', u'division_short_name'), ('#text', u'Map Division')]), OrderedDict([(u'@type', u'code'), ('#text', u'MAP')])]), (u'shelfLocator', u'Map Div. 01-5200')]))])]
```

###Data structures

For each top-level element, you can output data as a list of XML fragments:  

```python
>>> print record.subject.xml()  

['<subject xmlns="http://www.loc.gov/mods/v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" authority="lcsh">\n  <geographic authority="naf" valueURI="http://id.loc.gov/authorities/names/n78095330">United States</geographic>\n</subject>\n', '<subject xmlns="http://www.loc.gov/mods/v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh85056660">\n  <geographic authority="naf" valueURI="http://id.loc.gov/authorities/names/n79023147">Great Britain</geographic>\n  <topic authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh99005254">Colonies</topic>\n  <geographic authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh85004220">America</geographic>\n</subject>\n', '<subject xmlns="http://www.loc.gov/mods/v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh85092455">\n  <geographic authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh85092455">North America</geographic>\n</subject>\n']
```

an Ordered Dict:
```python
>>> print record.subject.dict  

[OrderedDict([(u'subject', OrderedDict([(u'@xmlns', u'http://www.loc.gov/mods/v3'), (u'@xmlns:xsi', u'http://www.w3.org/2001/XMLSchema-instance'), (u'@authority', u'lcsh'), (u'geographic', OrderedDict([(u'@authority', u'naf'), (u'@valueURI', u'http://id.loc.gov/authorities/names/n78095330'), ('#text', u'United States')]))]))]), OrderedDict([(u'subject', OrderedDict([(u'@xmlns', u'http://www.loc.gov/mods/v3'), (u'@xmlns:xsi', u'http://www.w3.org/2001/XMLSchema-instance'), (u'@authority', u'lcsh'), (u'@valueURI', u'http://id.loc.gov/authorities/subjects/sh85056660'), (u'geographic', [OrderedDict([(u'@authority', u'naf'), (u'@valueURI', u'http://id.loc.gov/authorities/names/n79023147'), ('#text', u'Great Britain')]), OrderedDict([(u'@authority', u'lcsh'), (u'@valueURI', u'http://id.loc.gov/authorities/subjects/sh85004220'), ('#text', u'America')])]), (u'topic', OrderedDict([(u'@authority', u'lcsh'), (u'@valueURI', u'http://id.loc.gov/authorities/subjects/sh99005254'), ('#text', u'Colonies')]))]))]), OrderedDict([(u'subject', OrderedDict([(u'@xmlns', u'http://www.loc.gov/mods/v3'), (u'@xmlns:xsi', u'http://www.w3.org/2001/XMLSchema-instance'), (u'@authority', u'lcsh'), (u'@valueURI', u'http://id.loc.gov/authorities/subjects/sh85092455'), (u'geographic', OrderedDict([(u'@authority', u'lcsh'), (u'@valueURI', u'http://id.loc.gov/authorities/subjects/sh85092455'), ('#text', u'North America')]))]))])]
```

or a list of text values:

```python
# complex subjects are delimited by '--' by default
>>> print record.subject.text()  

['United States', 'Great Britain -- Colonies -- America', 'North America']
```

###lxml

If you're familiar with [lxml objecify](http://lxml.de/objectify.html), you can treat any top-level element as an lxml object by calling the mods attribute:

```python
>>> print record.titleInfo.mods  

<Element {http://www.loc.gov/mods/v3}subject at 0x4146a88>
```



